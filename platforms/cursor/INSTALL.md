# Cursor — Install Guide

## Quick Install

```bash
bash scripts/install.sh cursor
```

## MCP Setup (Optional)

Add to `.vscode/settings.json`:

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/mathiaschu/google-ads-mcp.git", "google-ads-mcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "${env:GOOGLE_APPLICATION_CREDENTIALS}",
        "GOOGLE_ADS_DEVELOPER_TOKEN": "${env:GOOGLE_ADS_DEVELOPER_TOKEN}",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "${env:GOOGLE_ADS_LOGIN_CUSTOMER_ID}"
      }
    }
  }
}
```

Run `cd scripts && python3 setup.py` first.
