# Google Ads Analyzer — Multi-Platform AI Skill

Expert-level Google Ads campaign analysis, diagnosis, and management skill for AI coding platforms. Includes GAQL query templates, Quality Score diagnostics, Smart Bidding evaluation, Performance Max deep dives, campaign write tools, and 12 reference documents.

## Supported Platforms

| Platform | Install Command | Type |
|:---------|:---------------|:-----|
| **Hermes Agent** | `bash scripts/install.sh hermes` | Skill |
| **Claude Code** | `bash scripts/install.sh claude-code` | Skill |
| **Cursor** | `bash scripts/install.sh cursor` | Rules |
| **GitHub Copilot** | `bash scripts/install.sh copilot` | Instructions |
| **OpenCode** | `bash scripts/install.sh opencode` | Skill |
| **Windsurf** | `bash scripts/install.sh windsurf` | Rules |
| **Aider** | `bash scripts/install.sh aider` | Rules |

Install all at once: `bash scripts/install.sh all`

## What It Does

When installed on any supported platform, the AI can:

**Read & Analyze:**
- Query your Google Ads accounts directly using GAQL (Google Ads Query Language)
- Analyze campaign, ad group, keyword, and search term performance
- Diagnose Quality Score issues at the component level (expected CTR, ad relevance, landing page)
- Evaluate Impression Share to identify budget vs rank opportunities
- Assess Smart Bidding performance and learning status
- Deep dive Performance Max campaigns (asset groups, ad strength, cannibalization)
- Review search term reports and identify negative keyword gaps
- Generate structured analysis reports with prioritized recommendations

**Write & Manage:**
- Add negative keywords to campaigns (Broad, Phrase, or Exact match)
- Pause or enable campaigns, ad groups, and individual ads
- Update daily budgets
- Change bidding strategies (Target CPA, Target ROAS, Maximize Conversions, Maximize Conversion Value)

## Quick Start

### 1. Install for your platform

```bash
# Clone the repo
git clone https://github.com/jfiscman/google-ads-analyzer.git
cd google-ads-analyzer

# Install
bash scripts/install.sh hermes        # or: claude-code, cursor, copilot, etc.
```

> **Note on install location:** `hermes` and `opencode` install into your home
> directory (`~/.hermes`, `~/.opencode`) and work from anywhere. The
> project-scoped platforms (`claude-code`, `cursor`, `copilot`, `windsurf`,
> `aider`) install into the **current working directory** — run their install
> command from the root of the project you want the skill available in, not
> from inside this cloned repo.

### 2. Set up MCP (optional, for live API data)

```bash
cd scripts/

# Place your OAuth client JSON in this folder
# (download from Google Cloud Console → APIs & Services → Credentials)

python3 setup.py
```

The script will guide you through OAuth authentication, Developer Token setup, and connection testing.

### 3. Start analyzing

Ask your AI assistant:

**Analysis:**
- "Analyze my Google Ads campaigns from the last 30 days"
- "What's my Quality Score distribution across keywords?"
- "Show me Impression Share breakdown — am I losing to budget or rank?"
- "Review my search terms and suggest negative keywords"
- "Is my Smart Bidding strategy performing within target?"
- "Deep dive into my Performance Max campaign"
- "Compare this month vs last month across all campaigns"
- "Which campaigns have the highest wasted spend?"

**Management:**
- "Pause campaign X"
- "Add these negative keywords to my Search campaign: [list]"
- "Increase the daily budget on campaign Y to $100"
- "Switch campaign Z to Target ROAS at 4x"

## Repository Structure

```
google-ads-analyzer/
├── SKILL.md                    ← Platform-agnostic skill definition
├── references/                 ← 12 domain knowledge docs (shared by all platforms)
│   ├── core_concepts.md        ← Hub: Ad Rank, QS, Smart Bidding, PMax, GAQL
│   ├── gaql_queries.md         ← Ready-to-use GAQL queries
│   ├── quality_score.md        ← 3 QS components, diagnosis
│   ├── impression_share.md     ← IS, lost by budget vs rank
│   ├── smart_bidding.md        ← tCPA, tROAS, learning period
│   ├── performance_max.md      ← Asset groups, signals, cannibalization
│   ├── conversion_tracking.md  ← Types, DDA, conversion lag
│   ├── account_structure.md    ← MCC hierarchy, naming
│   ├── search_terms_negatives.md
│   ├── ad_copy_rsa.md          ← RSA, headlines, ad strength
│   ├── segmentation.md         ← GAQL segments: device, geo, day_of_week
│   └── performance_fluctuations.md
├── platforms/                  ← Platform-specific adapters
│   ├── hermes/                 ← Hermes Agent skill
│   ├── claude-code/            ← Claude Code skill
│   ├── cursor/                 ← Cursor rules
│   ├── copilot/                ← GitHub Copilot instructions
│   ├── opencode/               ← OpenCode skill
│   ├── windsurf/               ← Windsurf rules
│   └── aider/                  ← Aider rules
├── mcp/                        ← MCP server config (multi-platform)
├── scripts/                    ← Setup & install scripts
│   ├── install.sh              ← Universal installer
│   └── setup.py                ← Google OAuth setup
└── README.md
```

## Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- A Google Ads account (with a Developer Token)
- A Google Cloud project with the Google Ads API enabled
- OAuth 2.0 Desktop Client credentials

## What's in the Reference Docs

| # | Document | Covers |
|---|----------|--------|
| 1 | `core_concepts.md` | Ad Rank, Quality Score, Smart Bidding, PMax, GAQL overview |
| 2 | `gaql_queries.md` | Ready-to-use GAQL queries for each analysis step |
| 3 | `quality_score.md` | 3 components, diagnosis by component, prioritization |
| 4 | `impression_share.md` | IS lost by budget vs rank, auction insights |
| 5 | `smart_bidding.md` | tCPA, tROAS, learning period, when to intervene |
| 6 | `performance_max.md` | Asset groups, signals, feed quality, cannibalization |
| 7 | `conversion_tracking.md` | Types, DDA, conversion lag, primary vs secondary |
| 8 | `account_structure.md` | MCC hierarchy, naming, brand vs non-brand |
| 9 | `search_terms_negatives.md` | Search term report, match types, negative keywords |
| 10 | `ad_copy_rsa.md` | RSA headlines, descriptions, ad strength, asset labels |
| 11 | `segmentation.md` | GAQL segments: device, geo, day_of_week, audiences |
| 12 | `performance_fluctuations.md` | Normal vs concerning changes, conversion lag trap |

## Write Tools

| Tool | What it does |
|:---|:---|
| `add_negative_keywords` | Adds negative keywords (BROAD, PHRASE, EXACT) |
| `update_campaign_status` | Pauses or enables a campaign |
| `update_campaign_budget` | Changes daily budget |
| `update_bidding_strategy` | Changes bid strategy (TARGET_CPA, TARGET_ROAS, etc.) |
| `update_ad_group_status` | Pauses or enables an ad group |
| `update_ad_status` | Pauses or enables an ad |

## Troubleshooting

| Error | Cause | Fix |
|:---|:---|:---|
| `UNAUTHENTICATED` | Refresh token revoked or expired | Run `python3 scripts/setup.py` again |
| `PERMISSION_DENIED` | Developer token not approved | Check token status in API Center |
| `DEVELOPER_TOKEN_NOT_APPROVED` | Token still in test mode | Apply for Basic Access |
| `INVALID_CUSTOMER_ID` | Wrong customer ID format | Use 10-digit ID without dashes |
| MCP not connecting | Config or credentials issue | Verify paths; restart your AI platform |
| No data returned | Wrong date range or no active campaigns | Check `campaign.status = 'ENABLED'` |

## License

MIT — Copyright (c) 2026 Mathias Chu
