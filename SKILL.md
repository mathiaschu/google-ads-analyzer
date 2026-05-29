---
name: google-ads-analyzer
description: "Expert-level analysis, diagnosis, and management for Google Ads campaigns. Interprets performance data via GAQL, diagnoses Quality Score and Impression Share issues, evaluates Smart Bidding and Performance Max campaigns. Includes write tools for campaign management (pause/enable, budget, bidding, negative keywords)."
version: 2.0.0
author: Mathias Chu
license: MIT
platforms:
  - hermes
  - claude-code
  - cursor
  - copilot
  - opencode
  - windsurf
  - aider
tags:
  - google-ads
  - gaql
  - quality-score
  - impression-share
  - smart-bidding
  - performance-max
  - campaign-management
  - search-terms
  - negative-keywords
  - mcp
prerequisites:
  commands:
    - python (3.8+)
    - uv
metadata:
  hermes:
    skill_type: analysis
    mcp_required: false
    mcp_optional: true
---

# Google Ads Analysis & Diagnosis Skill

Multi-platform skill for analyzing, diagnosing, and managing Google Ads campaigns. Works across Hermes, Claude Code, Cursor, GitHub Copilot, OpenCode, Windsurf, and Aider.

## When to Use

Use this skill when you need to **analyze, diagnose, and manage Google Ads campaigns**, including:
- Interpreting campaign, ad group, or keyword-level performance data
- Running GAQL queries to pull metrics from the Google Ads API
- Diagnosing Quality Score, Impression Share, and Smart Bidding issues
- Evaluating Performance Max campaigns (asset groups, signals, feed quality)
- Analyzing search term reports and negative keyword coverage
- Generating structured analysis reports with actionable recommendations
- Managing campaigns: pause/enable, budgets, bidding strategies, negative keywords

## Domain Knowledge (Mandatory Reading)

Load these reference documents in order for complete domain understanding:

| # | Document | Covers |
|---|----------|--------|
| 1 | `references/core_concepts.md` | Hub: Ad Rank, Quality Score, Smart Bidding, PMax, GAQL |
| 2 | `references/gaql_queries.md` | Ready-to-use GAQL queries for each workflow step |
| 3 | `references/quality_score.md` | 3 components, diagnosis by component, prioritization |
| 4 | `references/impression_share.md` | IS lost by budget vs rank, auction insights |
| 5 | `references/smart_bidding.md` | tCPA, tROAS, learning period, when to intervene |
| 6 | `references/performance_max.md` | Asset groups, signals, feed quality, cannibalization |
| 7 | `references/conversion_tracking.md` | Types, DDA, conversion lag, primary vs secondary |
| 8 | `references/account_structure.md` | MCC hierarchy, naming, brand vs non-brand |
| 9 | `references/search_terms_negatives.md` | Search term report, match types, negative keywords |
| 10 | `references/ad_copy_rsa.md` | RSA headlines, descriptions, ad strength, asset labels |
| 11 | `references/segmentation.md` | GAQL segments: device, geo, day_of_week, audiences |
| 12 | `references/performance_fluctuations.md` | Normal vs concerning changes, conversion lag trap |

## Core Principles

- **Structure First:** Understand the account hierarchy (MCC → accounts → campaigns → ad groups → keywords) before drilling into metrics. Context determines what "good" looks like.
- **Signal over Noise:** Google Ads data is noisy day-to-day. Analyze trends over 14-30 day windows. Single-day spikes are rarely actionable.
- **System Awareness:** Smart Bidding, Broad Match, and Performance Max are ML-driven systems. Respect learning periods, avoid micro-managing, and diagnose the system's constraints rather than overriding its decisions.

## Result Recommendations (MANDATORY for Final Reports)

> **IMPORTANT:** These rules are **MANDATORY** and **MUST be strictly followed** when writing the final analysis report.

- **ALWAYS divide `cost_micros` by 1,000,000** to get the actual cost. Google Ads API returns all monetary values in micros.
- **ALWAYS identify `customer.currency_code`** before interpreting any cost values. Never assume USD.
- **ALWAYS compare vs. prior period** (month-over-month at minimum). Never present metrics in isolation without temporal context.
- **ALWAYS discount the last 7 days** when evaluating conversion-based metrics. Conversion lag means recent data underreports actual performance.
- **ALWAYS discover account via MCC first.** Use `list_accessible_customers` to find accounts, then query with `login-customer-id` header.
- **NEVER judge Performance Max** without reviewing asset group performance, ad strength, and feed quality (if Shopping). PMax is a black box — surface-level metrics are misleading.
- **NEVER recommend increasing budget** if Impression Share lost by Ad Rank exceeds 50%. Fix Quality Score and bids first.
- **EVERY insight must include data evidence and explanation.** Every recommendation must be actionable and verifiable.
- **Disambiguate conversion types.** Always clarify `conversions` (primary only) vs `all_conversions` (primary + secondary).

## Metric Naming Guidelines

**IMPORTANT:** Always rename API metric names to standardized display names in all responses:

| API Metric | Standardized Display Name |
|:---|:---|
| `metrics.cost_micros` | Cost |
| `metrics.impressions` | Impressions |
| `metrics.clicks` | Clicks |
| `metrics.ctr` | CTR |
| `metrics.average_cpc` | Avg. CPC |
| `metrics.conversions` | Conversions (Primary) |
| `metrics.all_conversions` | Conversions (All) |
| `metrics.conversions_value` | Conversion Value |
| `metrics.cost_per_conversion` | Cost / Conversion |
| `metrics.search_impression_share` | Search IS |
| `metrics.search_budget_lost_impression_share` | Search IS Lost (Budget) |
| `metrics.search_rank_lost_impression_share` | Search IS Lost (Rank) |
| `metrics.interaction_rate` | Interaction Rate |
| `metrics.average_cost` | Avg. Cost |
| `ad_group_criterion.quality_info.quality_score` | Quality Score |

**Monetary values:** Always divide `cost_micros` by 1,000,000 and format with the account's currency symbol.

## Google Ads Domain Knowledge

### Micros
All monetary values from the API are in **micros** (1 currency unit = 1,000,000 micros). Always divide by 1,000,000 before displaying.

### Account Hierarchy
- **MCC (Manager Account):** Top-level account managing multiple client accounts
- **Customer Account:** Individual ad account with campaigns
- **`login-customer-id`:** Required header when querying via MCC access. Set to the MCC ID.

### GAQL (Google Ads Query Language)
The API uses GAQL, a SQL-like language for querying resources. Key differences from SQL:
- No `JOIN` — each resource has pre-defined accessible fields
- Use `segments.*` for breakdowns (device, date, day_of_week, etc.)
- Filtering uses `WHERE` with specific operators per field type
- Date ranges via `segments.date BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'`

### Campaign Types
| Type | Key Characteristics |
|:---|:---|
| **Search** | Keyword-targeted text ads on Search results |
| **Performance Max** | All-channel automated campaign (Search, Display, YouTube, Gmail, Maps, Discover) |
| **Shopping** | Product feed-based ads on Shopping tab and Search |
| **Display** | Banner/image ads across Google Display Network |
| **Video** | YouTube ads (in-stream, bumper, discovery) |
| **Demand Gen** | Visual ads across YouTube, Gmail, Discover |

## Analysis Workflow

### Step 1: Discovery
Identify the account structure before any analysis:
1. Call `list_accessible_customers` to find available accounts
2. Query `customer` resource for account name, currency, timezone
3. Query `campaign` resource for active campaigns, types, and bidding strategies
4. Note which campaigns are PMax (separate analysis path)

### Step 2: Pull Metrics + Temporal Comparison
Pull performance data with always two periods for comparison:
| Period | Purpose |
|:---|:---|
| Current month (excluding last 7 days) | Primary analysis window |
| Previous month (same day count) | Comparison baseline |

Use queries from `gaql_queries.md`. Always pull daily granularity for trend analysis.

### Step 3: Diagnose
Run diagnostic checks in this order:
1. **Quality Score** — Pull keyword-level QS with components. Flag keywords with QS < 5
2. **Impression Share** — Check IS lost by budget vs rank. Budget-limited = opportunity. Rank-limited = fix QS/bids
3. **Smart Bidding** — Check bidding strategy status, learning state, target vs actual CPA/ROAS
4. **Conversions** — Verify tracking setup, conversion lag impact, primary vs secondary actions
5. **Search Terms** — Review search term report for wasted spend, irrelevant queries, missing negatives

### Step 4: Deep Dive Performance Max (if applicable)
PMax requires a separate analysis path:
1. Pull asset group performance (impressions, conversions, cost)
2. Check ad strength per asset group (Excellent, Good, Average, Poor)
3. Review listing group filters (if Shopping feed)
4. Check for cannibalization with branded Search campaigns
5. Evaluate audience signals vs actual reach

### Step 5: Generate Report
Structure every analysis report as:
1. **Executive Summary** — 2-3 key findings with business impact
2. **Account Overview** — Structure, campaign types, bidding strategies, budget allocation
3. **Performance Analysis** — Metrics with period comparison and trends
4. **Quality Score & Impression Share Diagnosis** — Component-level QS, IS breakdown
5. **Conversion & Bidding Analysis** — Tracking health, Smart Bidding status, lag impact
6. **Search Terms & Negatives** — Wasted spend, opportunities, negative keyword gaps
7. **Recommendations** — Prioritized, actionable, with expected impact and effort level

## Write Tools (Campaign Management)

The MCP server includes 6 write tools for acting on analysis findings:

| Tool | What it does |
|:---|:---|
| `add_negative_keywords` | Adds negative keywords to a campaign (BROAD, PHRASE, or EXACT match) |
| `update_campaign_status` | Pauses or enables a campaign |
| `update_campaign_budget` | Changes the daily budget (in account currency, e.g. 50.00 for $50) |
| `update_bidding_strategy` | Changes bid strategy: TARGET_CPA, TARGET_ROAS, MAXIMIZE_CONVERSIONS, MAXIMIZE_CONVERSION_VALUE |
| `update_ad_group_status` | Pauses or enables an ad group |
| `update_ad_status` | Pauses or enables an ad |

**Important:** Always confirm with the user before executing write operations.

## MCP Server (Optional — Live API Data)

An MCP server (`google-ads-mcp` via `uvx`) connects directly to the Google Ads API for querying and managing campaigns. See `mcp/` for configuration templates.

**Prerequisites:** Google Cloud project with Google Ads API enabled, OAuth 2.0 credentials, Developer Token.
