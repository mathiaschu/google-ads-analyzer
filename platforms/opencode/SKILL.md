---
name: google-ads-analyzer
description: "Expert Google Ads campaign analysis, diagnosis, and management. Use when analyzing campaign performance, diagnosing Quality Score and Impression Share issues, evaluating Smart Bidding and Performance Max campaigns."
---

<!--
  OPENCODE SKILL
  Install: cp -r platforms/opencode/ ~/.opencode/skills/google-ads-analyzer/
  Then copy references/ into ~/.opencode/skills/google-ads-analyzer/references/
-->

# Google Ads Analysis & Diagnosis Skill

## When to Use This Skill

Use this skill when you need to **analyze, diagnose, and manage Google Ads campaigns**, including:
- Interpreting campaign, ad group, or keyword-level performance data
- Running GAQL queries to pull metrics from the Google Ads API
- Diagnosing Quality Score, Impression Share, and Smart Bidding issues
- Evaluating Performance Max campaigns (asset groups, signals, feed quality)
- Analyzing search term reports and negative keyword coverage
- Generating structured analysis reports with actionable recommendations
- Managing campaigns: pause/enable, budgets, bidding strategies, negative keywords

## Reference Documents

Load these reference documents (in `references/`) before performing any analysis:

1. `references/core_concepts.md` — Hub: Ad Rank, Quality Score, Smart Bidding, PMax, GAQL
2. `references/gaql_queries.md` — Ready-to-use GAQL queries for each workflow step
3. `references/quality_score.md` — 3 components, diagnosis by component
4. `references/impression_share.md` — IS, lost by budget vs rank, auction insights
5. `references/smart_bidding.md` — tCPA, tROAS, learning period, when to intervene
6. `references/performance_max.md` — Asset groups, signals, feed quality, cannibalization
7. `references/conversion_tracking.md` — Types, DDA, conversion lag, primary vs secondary
8. `references/account_structure.md` — MCC hierarchy, naming, brand vs non-brand
9. `references/search_terms_negatives.md` — Search term report, match types, negative keywords
10. `references/ad_copy_rsa.md` — RSA, headlines, descriptions, ad strength, asset labels
11. `references/segmentation.md` — GAQL segments: device, geo, day_of_week, audiences
12. `references/performance_fluctuations.md` — Normal vs concerning, conversion lag trap

## Result Recommendations (MANDATORY for Final Reports)

> **IMPORTANT:** These rules are **MANDATORY** and **MUST be strictly followed**.

- **ALWAYS divide `cost_micros` by 1,000,000** to get the actual cost.
- **ALWAYS identify `customer.currency_code`** before interpreting any cost values. Never assume USD.
- **ALWAYS compare vs. prior period** (month-over-month at minimum).
- **ALWAYS discount the last 7 days** when evaluating conversion-based metrics.
- **ALWAYS discover account via MCC first.** Use `list_accessible_customers`.
- **NEVER judge Performance Max** without reviewing asset group performance, ad strength, and feed quality.
- **NEVER recommend increasing budget** if Impression Share lost by Ad Rank exceeds 50%.
- **EVERY insight must include data evidence and explanation.**
- **Disambiguate conversion types.** Always clarify `conversions` (primary) vs `all_conversions` (all).

## Metric Naming Guidelines

**IMPORTANT:** Always rename API metric names to standardized display names:

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
| `metrics.average_cost` | Avg. Cost |
| `ad_group_criterion.quality_info.quality_score` | Quality Score |

**Monetary values:** Always divide `cost_micros` by 1,000,000 and format with the account's currency symbol.

## Core Principles

- **Structure First:** Understand the account hierarchy (MCC → accounts → campaigns → ad groups → keywords) before drilling into metrics.
- **Signal over Noise:** Google Ads data is noisy day-to-day. Analyze trends over 14-30 day windows.
- **System Awareness:** Smart Bidding, Broad Match, and Performance Max are ML-driven systems. Respect learning periods.

## Google Ads Domain Knowledge

### Micros
All monetary values from the API are in **micros** (1 unit = 1,000,000 micros).

### Account Hierarchy
- **MCC (Manager Account):** Top-level account managing multiple client accounts
- **Customer Account:** Individual ad account with campaigns
- **`login-customer-id`:** Required header when querying via MCC access

### GAQL (Google Ads Query Language)
The API uses GAQL, a SQL-like language for querying resources. Key differences from SQL:
- No `JOIN` — each resource has pre-defined accessible fields
- Use `segments.*` for breakdowns (device, date, day_of_week, etc.)
- Date ranges via `segments.date BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'`

### Campaign Types
| Type | Key Characteristics |
|:---|:---|
| **Search** | Keyword-targeted text ads on Search results |
| **Performance Max** | All-channel automated campaign |
| **Shopping** | Product feed-based ads |
| **Display** | Banner/image ads across GDN |
| **Video** | YouTube ads |
| **Demand Gen** | Visual ads across YouTube, Gmail, Discover |

## Analysis Workflow

### Step 1: Discovery
1. Call `list_accessible_customers` to find available accounts
2. Query `customer` resource for account name, currency, timezone
3. Query `campaign` resource for active campaigns, types, and bidding strategies
4. Note which campaigns are PMax (separate analysis path)

### Step 2: Pull Metrics + Temporal Comparison
| Period | Purpose |
|:---|:---|
| Current month (excluding last 7 days) | Primary analysis window |
| Previous month (same day count) | Comparison baseline |

### Step 3: Diagnose
1. **Quality Score** — Pull keyword-level QS with components. Flag QS < 5
2. **Impression Share** — Check IS lost by budget vs rank
3. **Smart Bidding** — Check bidding strategy status, learning state
4. **Conversions** — Verify tracking setup, conversion lag impact
5. **Search Terms** — Review search term report for wasted spend

### Step 4: Deep Dive Performance Max (if applicable)
1. Pull asset group performance
2. Check ad strength per asset group
3. Review listing group filters (if Shopping feed)
4. Check for cannibalization with branded Search campaigns
5. Evaluate audience signals vs actual reach

### Step 5: Generate Report
1. **Executive Summary** — 2-3 key findings with business impact
2. **Account Overview** — Structure, campaign types, bidding strategies, budget allocation
3. **Performance Analysis** — Metrics with period comparison and trends
4. **Quality Score & Impression Share Diagnosis**
5. **Conversion & Bidding Analysis**
6. **Search Terms & Negatives**
7. **Recommendations** — Prioritized, actionable, with expected impact

## Write Tools (Campaign Management)

| Tool | What it does |
|:---|:---|
| `add_negative_keywords` | Adds negative keywords (BROAD, PHRASE, or EXACT match) |
| `update_campaign_status` | Pauses or enables a campaign |
| `update_campaign_budget` | Changes the daily budget |
| `update_bidding_strategy` | Changes bid strategy |
| `update_ad_group_status` | Pauses or enables an ad group |
| `update_ad_status` | Pauses or enables an ad |

**Important:** Always confirm with the user before executing write operations.
