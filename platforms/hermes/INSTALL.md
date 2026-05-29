# Hermes Agent — Install Guide

## Quick Install

```bash
bash scripts/install.sh hermes
```

Or manually:

```bash
mkdir -p ~/.hermes/skills/google-ads-analyzer
cp platforms/hermes/SKILL.md ~/.hermes/skills/google-ads-analyzer/
cp -r references/ ~/.hermes/skills/google-ads-analyzer/references/
```

## MCP Setup (Optional — Live API Data)

1. Set up Google OAuth credentials:

```bash
cd scripts/
# Place your OAuth client JSON in this folder
python3 setup.py
```

2. Add the MCP server to your Hermes `config.yaml`:

```yaml
mcp_servers:
  google-ads:
    command: uvx
    args:
      - "--from"
      - "git+https://github.com/mathiaschu/google-ads-mcp.git"
      - "google-ads-mcp"
    env:
      GOOGLE_APPLICATION_CREDENTIALS: "/path/to/scripts/credentials.json"
      GOOGLE_ADS_DEVELOPER_TOKEN: "YOUR_TOKEN"
      GOOGLE_ADS_LOGIN_CUSTOMER_ID: "YOUR_MCC_ID"
```

3. Restart Hermes.

## Usage

- "Analizá mis campañas de Google Ads de los últimos 30 días"
- "¿Cuál es la distribución de Quality Score de mis keywords?"
- "Mostrame el breakdown de Impression Share"
- "Revisá mis search terms y sugerí negative keywords"
- "Hacé un deep dive de mi campaña Performance Max"
- "Pausá la campaña X"
- "Agregá estas negative keywords: [lista]"
