# Smart Bidding

## What It Is

Smart Bidding is Google's ML-powered automated bid strategy that optimizes bids in real-time for each auction using contextual signals (device, location, time, audience, query, browser, OS, and more).

## Strategies

| Strategy | Optimizes For | When to Use |
| :--- | :--- | :--- |
| **Target CPA** | Conversions at target cost | Stable conversion volume, known acceptable CPA |
| **Target ROAS** | Conversion value at target return | Revenue-focused, variable conversion values |
| **Maximize Conversions** | Most conversions within budget | New campaigns, building conversion history |
| **Maximize Conv. Value** | Most conversion value within budget | Revenue-focused, early stage |

**Note:** "Target CPA" and "Target ROAS" are technically "Maximize Conversions" / "Maximize Conv. Value" with a target set. The system prioritizes hitting the target over maximizing volume.

## Learning Period

After significant changes, Smart Bidding enters a learning period of approximately **2 weeks**:

| Change Type | Triggers Learning? |
| :--- | :--- |
| New bidding strategy | Yes |
| Target CPA/ROAS change (>15-20%) | Yes |
| Budget change (>30%) | Usually yes |
| New conversion action added | Yes |
| Creative changes | Minor re-learning |
| Keyword additions | Minor re-learning |

During learning: performance is volatile, CPA may spike, volume may fluctuate. **Do not make additional changes during this period.**

## Signals Used

Smart Bidding considers (among others):
- Device type and OS
- Geographic location (granular)
- Time of day and day of week
- Remarketing lists and audience signals
- Search query (broad match + Smart Bidding work together)
- Browser and app
- Ad creative being shown

## When to Intervene

| Situation | Action |
| :--- | :--- |
| Learning period (< 2 weeks after change) | Wait. Do not adjust. |
| CPA 20-30% above target after learning | Check conversion tracking, landing page, competition |
| CPA 50%+ above target after learning | Consider lowering target gradually (10-15% steps) |
| Volume dropped significantly | Target may be too aggressive. Raise CPA target or switch to Maximize Conversions |
| Strategy performing well | Don't touch it. Small "improvements" can reset learning. |

## Key Insight

Smart Bidding works best with **sufficient conversion data** (30+ conversions/month per campaign recommended) and **accurate conversion tracking**. Insufficient data = the ML model can't learn, and performance will be erratic.

## Analysis Implications

- Check `campaign.bidding_strategy_type` to identify which strategy is in use
- Look at `campaign.target_cpa.target_cpa_micros` or `campaign.target_roas.target_roas` for targets
- Compare target vs. actual CPA/ROAS over 14-30 day windows (not daily)
- If a campaign has < 15 conversions/month, Smart Bidding may not be appropriate
- Broad Match + Smart Bidding is Google's recommended combination — query expansion is intentional
