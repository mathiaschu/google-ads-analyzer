# Google Ads Core Concepts

## Ad Rank

Every search triggers an auction. Ad position is determined by **Ad Rank**:

> *Ad Rank = Max CPC Bid x Quality Score + Ad Extensions Impact*

In Smart Bidding, the system sets bids automatically using:
- Contextual signals (device, location, time, audience, query)
- Historical conversion data
- Predicted conversion probability

**Key:** Ad Rank determines both position and CPC. Higher Quality Score = lower CPC for same position.

## Quality Score

Diagnostic metric (1-10) based on three components:

| Component | What It Measures |
| :--- | :--- |
| Expected CTR | Likelihood of click vs. competitors |
| Ad Relevance | How well the ad matches search intent |
| Landing Page Experience | Usefulness, relevance, and speed of landing page |

**Key:** Quality Score is NOT an auction input — it's a diagnostic tool. The actual auction uses real-time, query-specific signals. But low QS reliably indicates fixable problems.

See `quality_score.md` for deep dive.

## Smart Bidding

ML-powered bid strategies that optimize for conversions or conversion value:
- **Target CPA** — Maximize conversions at target cost per acquisition
- **Target ROAS** — Maximize conversion value at target return on ad spend
- **Maximize Conversions** — Get the most conversions within budget
- **Maximize Conversion Value** — Get the most conversion value within budget

Learning period: ~2 weeks after significant changes. Avoid micro-managing during this phase.

See `smart_bidding.md` for deep dive.

## Performance Max

All-channel campaign type that runs across Search, Display, YouTube, Gmail, Maps, and Discover simultaneously. Uses Google's ML to allocate budget and optimize creative across channels.

**Key:** PMax is a black box. Surface metrics (like overall CPA) can be misleading because they blend branded search traffic with prospecting. Always check asset group level and watch for branded search cannibalization.

See `performance_max.md` for deep dive.

## GAQL (Google Ads Query Language)

SQL-like language for querying the Google Ads API. Key concepts:

- **Resources:** `campaign`, `ad_group`, `ad_group_criterion`, `search_term_view`, etc.
- **Segments:** Breakdowns like `segments.date`, `segments.device`, `segments.ad_network_type`
- **Metrics:** Performance data like `metrics.cost_micros`, `metrics.clicks`, `metrics.conversions`
- **No JOINs:** Each resource has pre-defined accessible fields and metrics

See `gaql_queries.md` for ready-to-use queries.

## Conversion Lag

Conversions can take days or weeks to be attributed back to a click. Recent data (last 7 days) will almost always underreport conversions. Never compare recent periods to older periods without accounting for this lag.

See `conversion_tracking.md` for deep dive.
