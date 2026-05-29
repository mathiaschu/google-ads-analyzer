# Quality Score

## What It Is

Quality Score is a **diagnostic metric** (1-10) that estimates the quality of your ads, keywords, and landing pages relative to other advertisers. It is NOT a direct auction input — the real-time auction uses more granular, query-specific signals.

**Why it matters:** Keywords with low Quality Score consistently pay more per click and appear in lower positions. Improving QS components directly reduces costs.

## Three Components

| Component | Rating Scale | What It Measures |
| :--- | :--- | :--- |
| **Expected CTR** | Above Average / Average / Below Average | How likely users are to click your ad for this keyword |
| **Ad Relevance** | Above Average / Average / Below Average | How closely your ad matches the user's search intent |
| **Landing Page Experience** | Above Average / Average / Below Average | How useful and relevant the landing page is after clicking |

## Diagnosis by Component

| Weak Component | Root Cause | Fix |
| :--- | :--- | :--- |
| Expected CTR | Ad copy not compelling, weak CTA | Test new headlines with keyword insertion, add CTAs, use RSA |
| Ad Relevance | Keyword-ad mismatch, too broad ad groups | Tighter ad groups (SKAG or STAG), align headlines to keywords |
| Landing Page | Slow page, irrelevant content, poor UX | Improve page speed, match content to ad promise, mobile optimize |

## Key Insight

Quality Score is reported at **keyword level** and reflects **historical performance**. A keyword can have QS = 7 but still lose auctions if the competition is strong. Conversely, QS = 4 keywords can still convert profitably — QS measures ad quality, not conversion quality.

## Analysis Implications

- Pull QS data with component breakdown using the `keyword_view` resource
- Prioritize fixing low-QS keywords that have high spend (high cost + low QS = biggest waste)
- QS improvements take days to weeks to reflect — don't expect instant changes
- If all three components are "Below Average," the keyword-ad-landing page chain is fundamentally misaligned. Consider restructuring the ad group
- QS is only available for Search campaigns — PMax, Display, and Video don't have keyword-level QS
