# Google Ads Analyzer — GitHub Copilot Instructions

<!--
  GITHUB COPILOT INTEGRATION
  Copy this file to: .github/copilot-instructions.md
-->

## Google Ads Campaign Analysis

When analyzing Google Ads campaign data, follow these rules:

### Core Principles
- Understand account hierarchy (MCC → accounts → campaigns → ad groups → keywords) before drilling into metrics
- Analyze trends over 14-30 day windows; single-day spikes are rarely actionable
- Smart Bidding and Performance Max are ML-driven — respect learning periods, diagnose constraints

### Mandatory Rules
1. Always divide `cost_micros` by 1,000,000 for actual cost
2. Always identify `customer.currency_code` — never assume USD
3. Always compare vs. prior period (month-over-month minimum)
4. Always discount last 7 days for conversion-based metrics
5. Always discover via MCC first using `list_accessible_customers`
6. Never judge Performance Max without reviewing asset groups, ad strength, and feed quality
7. Never increase budget if Impression Share lost by Ad Rank > 50%
8. Every insight must include data evidence and explanation
9. Disambiguate conversions: `conversions` (primary) vs `all_conversions` (all)

### Metric Naming
| API Metric | Display Name |
|:-----------|:-------------|
| `metrics.cost_micros` | Cost |
| `metrics.impressions` | Impressions |
| `metrics.clicks` | Clicks |
| `metrics.ctr` | CTR |
| `metrics.average_cpc` | Avg. CPC |
| `metrics.conversions` | Conversions (Primary) |
| `metrics.search_impression_share` | Search IS |
| `ad_group_criterion.quality_info.quality_score` | Quality Score |

### GAQL Reference
- No JOIN — each resource has pre-defined accessible fields
- Use `segments.*` for breakdowns
- Date ranges: `segments.date BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'`
- Micros: divide by 1,000,000 for actual amount

### Analysis Workflow
1. Discovery (list customers, query account info, identify campaign types)
2. Pull metrics (two periods, daily granularity)
3. Diagnose (Quality Score → Impression Share → Smart Bidding → Conversions → Search Terms)
4. PMax deep dive (asset groups, ad strength, feed quality, cannibalization)
5. Report: Executive Summary → Account Overview → Performance → QS & IS → Bidding → Search Terms → Recommendations

### Campaign Management Tools
- `add_negative_keywords` — Add negatives (BROAD, PHRASE, EXACT)
- `update_campaign_status` — Pause/enable campaigns
- `update_campaign_budget` — Change daily budget
- `update_bidding_strategy` — Change bid strategy
- `update_ad_group_status` — Pause/enable ad groups
- `update_ad_status` — Pause/enable ads

Always confirm with user before executing write operations.
