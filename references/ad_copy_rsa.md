# Ad Copy & Responsive Search Ads (RSA)

## What Are RSAs

Responsive Search Ads are the standard Search ad format. You provide multiple headlines and descriptions, and Google's ML tests combinations to find the best performers.

**Structure:**
| Element | Max Length | Min Required | Max Allowed |
| :--- | :--- | :--- | :--- |
| Headlines | 30 chars | 3 | 15 |
| Descriptions | 90 chars | 2 | 4 |

Google shows 2-3 headlines and 1-2 descriptions per impression, testing different combinations dynamically.

## Ad Strength

Diagnostic score for RSAs:

| Rating | Meaning |
| :--- | :--- |
| **Excellent** | Full asset mix, good keyword inclusion, unique messaging |
| **Good** | Adequate variety but room for improvement |
| **Average** | Missing assets or limited variety |
| **Poor** | Insufficient assets, limiting optimization |

**What improves Ad Strength:**
- More unique headlines (aim for 10-15)
- Include keywords in at least 2 headlines
- Variety in messaging (features, benefits, CTAs, urgency)
- At least 3-4 descriptions with different angles
- Use popular keywords from the ad group

## Pinning

Pinning forces a specific headline/description to always appear in a specific position:
- **Position 1:** First headline (most visible)
- **Position 2:** Second headline
- **Position 3:** Third headline (may not always show)

**Key:** Pinning reduces ML's ability to optimize. Only pin when legally required (disclaimers) or for brand consistency. Over-pinning is a common mistake.

## Asset Performance Labels

Google rates individual assets after sufficient impressions:
- **Best** — Top performing
- **Good** — Above average
- **Low** — Below average
- **Learning** — Not enough data yet
- **Pending** — Not yet evaluated

## Key Insight

RSA performance is hard to evaluate at the individual headline level because Google shows different combinations. Focus on overall ad-level metrics (CTR, conversion rate) rather than trying to optimize individual assets. Replace "Low" rated assets, keep "Best" ones, and keep testing new variants.

## Analysis Implications

- Check ad strength per ad group — anything below "Good" needs attention
- Look at asset performance labels to identify underperformers
- Count active RSAs per ad group (Google recommends 1-2 RSAs per ad group)
- If CTR is low but ad relevance QS component is "Above Average," the issue is creative, not targeting
- Pinned ads with low CTR should have pins removed to let ML optimize
- GAQL access: `ad_group_ad.ad.responsive_search_ad.headlines` returns headline assets, but performance labels require the UI
