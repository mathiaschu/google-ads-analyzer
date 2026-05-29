#!/usr/bin/env python3
"""
Google Ads Analyzer — Setup Script
Runs OAuth flow, generates credentials, and configures .mcp.json for Claude Code.

Usage:
    python3 setup.py
"""

import http.server
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
CREDENTIALS_FILE = os.path.join(SCRIPT_DIR, "credentials.json")
ENV_FILE = os.path.join(PROJECT_DIR, ".env.google-ads")
MCP_FILE = os.path.join(PROJECT_DIR, ".mcp.json")

PORT = 8085
SCOPES = "https://www.googleapis.com/auth/adwords"
# Google Ads API version used by the connection test — bump in one place when
# Google sunsets it (https://developers.google.com/google-ads/api/docs/release-notes).
API_VERSION = "v18"


def load_client(path):
    """Load OAuth client config from downloaded JSON."""
    with open(path) as f:
        data = json.load(f)
    # Google Cloud Console exports as {"installed": {...}} or {"web": {...}}
    if "installed" in data:
        return data["installed"]
    elif "web" in data:
        return data["web"]
    else:
        print("ERROR: Unrecognized OAuth client JSON format.")
        sys.exit(1)


def do_oauth_flow(client):
    """Run local OAuth flow: open browser, catch redirect, exchange code for tokens."""
    redirect_uri = f"http://localhost:{PORT}"

    auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={client['client_id']}&"
        f"redirect_uri={urllib.parse.quote(redirect_uri, safe='')}&"
        f"response_type=code&"
        f"scope={urllib.parse.quote(SCOPES, safe='')}&"
        f"access_type=offline&"
        f"prompt=consent"
    )

    code = None

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            nonlocal code
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            if "code" in params:
                code = params["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(
                    "<html><body style='font-family:sans-serif;text-align:center;padding:60px'>"
                    "<h2>Authorized! You can close this window.</h2>"
                    "</body></html>".encode()
                )
            else:
                self.send_response(400)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(
                    b"<html><body><h2>Error: authorization code not received</h2></body></html>"
                )

        def log_message(self, format, *args):
            pass  # Suppress HTTP server logs

    print("\nOpening browser for Google authorization...")
    print(f"(If it doesn't open, copy this URL manually:)\n")
    print(auth_url)
    print()
    webbrowser.open(auth_url)

    server = http.server.HTTPServer(("localhost", PORT), Handler)
    print(f"Waiting for authorization at http://localhost:{PORT}...")
    # Keep serving until the redirect carrying ?code= arrives. Without the loop,
    # a stray request (e.g. the browser fetching /favicon.ico) could consume the
    # single handled request and cause us to miss the real authorization code.
    while code is None:
        server.handle_request()
    server.server_close()

    if not code:
        print("ERROR: Authorization code not received.")
        sys.exit(1)

    print("Code received! Exchanging for tokens...")

    data = urllib.parse.urlencode({
        "code": code,
        "client_id": client["client_id"],
        "client_secret": client["client_secret"],
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }).encode()

    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=data,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    try:
        with urllib.request.urlopen(req) as resp:
            tokens = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"ERROR exchanging code: {e.code}")
        print(error_body)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: could not reach Google's token endpoint: {e.reason}")
        sys.exit(1)

    if "refresh_token" not in tokens:
        print(f"ERROR: No refresh_token received: {json.dumps(tokens, indent=2)}")
        sys.exit(1)

    print("Tokens obtained!\n")
    return tokens


def save_credentials(client, tokens, developer_token, login_customer_id):
    """Save ADC-format credentials and .env file."""
    # ADC-format credentials (for the MCP server)
    adc = {
        "type": "authorized_user",
        "client_id": client["client_id"],
        "client_secret": client["client_secret"],
        "refresh_token": tokens["refresh_token"],
    }
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(adc, f, indent=2)
    # Holds a long-lived refresh_token — restrict to the owner only.
    os.chmod(CREDENTIALS_FILE, 0o600)
    print(f"Credentials saved to: {CREDENTIALS_FILE}")

    # .env.google-ads (reference file)
    env_lines = [
        f"GOOGLE_ADS_CLIENT_ID={client['client_id']}",
        f"GOOGLE_ADS_CLIENT_SECRET={client['client_secret']}",
        f"GOOGLE_ADS_REFRESH_TOKEN={tokens['refresh_token']}",
        f"GOOGLE_ADS_DEVELOPER_TOKEN={developer_token}",
    ]
    if login_customer_id:
        env_lines.append(f"GOOGLE_ADS_LOGIN_CUSTOMER_ID={login_customer_id}")
    with open(ENV_FILE, "w") as f:
        f.write("\n".join(env_lines) + "\n")
    # Contains client_secret + refresh_token — restrict to the owner only.
    os.chmod(ENV_FILE, 0o600)
    print(f"Environment variables saved to: {ENV_FILE}")


def update_mcp_json(developer_token, login_customer_id):
    """Add or update the google-ads MCP server in .mcp.json."""
    if os.path.exists(MCP_FILE):
        with open(MCP_FILE) as f:
            config = json.load(f)
    else:
        config = {"mcpServers": {}}

    env = {
        "GOOGLE_APPLICATION_CREDENTIALS": CREDENTIALS_FILE,
        "GOOGLE_ADS_DEVELOPER_TOKEN": developer_token,
    }
    if login_customer_id:
        env["GOOGLE_ADS_LOGIN_CUSTOMER_ID"] = login_customer_id

    config["mcpServers"]["google-ads"] = {
        "command": "uvx",
        "args": [
            "--from",
            "git+https://github.com/mathiaschu/google-ads-mcp.git",
            "google-ads-mcp",
        ],
        "env": env,
    }

    with open(MCP_FILE, "w") as f:
        json.dump(config, f, indent=2)
    print(f".mcp.json updated with google-ads server")


def test_connection(tokens, developer_token):
    """Quick test: list accessible customer accounts."""
    print("\nTesting connection to Google Ads API...")
    req = urllib.request.Request(
        f"https://googleads.googleapis.com/{API_VERSION}/customers:listAccessibleCustomers",
        headers={
            "Authorization": f"Bearer {tokens['access_token']}",
            "developer-token": developer_token,
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
            customers = data.get("resourceNames", [])
            print(f"Connection OK! Accessible accounts: {len(customers)}")
            for c in customers:
                cid = c.split("/")[-1]
                print(f"  - {cid}")
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"Warning: test failed ({e.code}), but credentials may still be valid.")
        print(f"  Detail: {error_body[:200]}")
        return False
    except urllib.error.URLError as e:
        print(f"Warning: could not reach the Google Ads API ({e.reason}); "
              "credentials were still saved.")
        return False


if __name__ == "__main__":
    print("=" * 50)
    print("  Google Ads Analyzer — Setup")
    print("=" * 50)

    # 1. OAuth client JSON
    default_client = os.path.join(SCRIPT_DIR, "oauth_client.json")
    if os.path.exists(default_client):
        print(f"\nFound OAuth client JSON: {default_client}")
        client_path = default_client
    else:
        client_path = input(
            "\nPath to your OAuth client JSON (downloaded from Google Cloud Console): "
        ).strip().strip("'\"")

    if not os.path.exists(client_path):
        print(f"ERROR: File not found: {client_path}")
        sys.exit(1)

    client = load_client(client_path)
    print(f"Client ID: {client['client_id'][:30]}...")
    print(f"Project: {client.get('project_id', 'N/A')}")

    # 2. Developer Token
    developer_token = input("\nGoogle Ads Developer Token: ").strip()
    if not developer_token:
        print("ERROR: Developer token is required.")
        print("Find it at: Google Ads → Tools & Settings → Setup → API Center")
        sys.exit(1)

    # 3. Login Customer ID (MCC)
    login_customer_id = input(
        "Login Customer ID (MCC ID, no dashes — press Enter to skip): "
    ).strip().replace("-", "")

    # 4. OAuth flow
    tokens = do_oauth_flow(client)

    # 5. Save everything
    save_credentials(client, tokens, developer_token, login_customer_id)
    update_mcp_json(developer_token, login_customer_id)

    # 6. Test
    test_connection(tokens, developer_token)

    print("\n" + "=" * 50)
    print("  Setup complete!")
    print("=" * 50)
    print("\nRestart Claude Code to activate the Google Ads MCP server.")
    print('Then ask: "List my Google Ads accounts"')
