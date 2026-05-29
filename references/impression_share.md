# Impression Share

## What It Is

Impression Share (IS) measures the percentage of eligible impressions your ads actually received. It answers: "Of all the times your ad could have shown, how often did it?"

> IS = Impressions Received / Total Eligible Impressions

## Lost Impression Share

The two reasons you miss impressions:

| Metric | Cause | What It Means |
| :--- | :--- | :--- |
| **IS Lost (Budget)** | Daily budget exhausted before day ends | More budget = more impressions. This is an opportunity signal. |
| **IS Lost (Rank)** | Ad Rank too low to enter auction | Quality Score and/or bids are too low vs competitors. |

**Key diagnostic:**
- High IS Lost (Budget) + low IS Lost (Rank) → Increase budget (you're competitive but underfunded)
- Low IS Lost (Budget) + high IS Lost (Rank) → Fix Quality Score and bids (more budget won't help)
- Both high → Fix rank first, then increase budget

## Position Metrics

| Metric | What It Measures |
| :--- | :--- |
| Search Top IS | % of impressions shown above organic results |
| Search Absolute Top IS | % of impressions shown as the very first ad |
| Search Top IS Lost (Budget) | Top impressions lost due to budget |
| Search Top IS Lost (Rank) | Top impressions lost due to rank |

## Auction Insights

Available via the Auction Insights report (not directly via standard GAQL, but accessible via `auction_insight` resource):

| Metric | What It Shows |
| :--- | :--- |
| Overlap Rate | How often a competitor's ad showed alongside yours |
| Outranking Share | How often your ad ranked higher than a competitor |
| Position Above Rate | How often competitor appeared above you |
| Top of Page Rate | Competitor's top-of-page frequency |

## Key Insight

Impression Share is only meaningful for **Search campaigns**. PMax and Display campaigns have different IS metrics that are less actionable because the eligible impression pool is much larger and less defined.

## Analysis Implications

- IS below 70% on branded terms is a red flag — competitors may be bidding on your brand
- IS below 50% on high-intent non-brand terms = significant missed opportunity
- If IS Lost (Rank) > 50%, do NOT recommend increasing budget — it won't help until rank improves
- Compare IS trends over time — declining IS with stable budgets suggests increasing competition
- Pull IS data at campaign level first, then drill into ad group level for specific diagnoses
