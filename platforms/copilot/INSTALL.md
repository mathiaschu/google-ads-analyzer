# GitHub Copilot — Install Guide

## Quick Install

```bash
bash scripts/install.sh copilot
```

## Optional: VS Code Settings

Add to `.vscode/settings.json`:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/copilot-instructions.md" }
  ]
}
```
