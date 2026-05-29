# Performance Fluctuations

Ad performance naturally fluctuates. Understanding causes helps distinguish normal variation from actual problems.

## Common Causes

| Cause | Description | Action |
| :--- | :--- | :--- |
| **Conversion lag** | Recent data underreports conversions | Wait 7-14 days before reacting to recent drops |
| **Smart Bidding learning** | Strategy adjusting after changes | Wait ~2 weeks, avoid additional edits |
| **Seasonality** | Demand patterns by time of year | Compare to same period last year, not just last month |
| **Competition changes** | New advertisers or bid increases | Check Impression Share and auction insights |
| **Quality Score shifts** | QS components degraded | Pull QS history, check component breakdown |
| **Budget constraints** | Budget can't cover demand | Check IS Lost (Budget) trends |
| **Ad fatigue** | RSA combinations exhausted | Add new headlines/descriptions, refresh creative |
| **External factors** | News, economy, platform updates | Account for context before diagnosing |

## Normal vs Concerning

**Normal:**
- Day-to-day CPA variation within 20-30%
- Weekend vs weekday differences (especially B2B)
- Gradual cost increases in competitive verticals
- Lower conversions on recent days (conversion lag)
- Fluctuations during Smart Bidding learning period

**Concerning:**
- Sustained CPA increase >40% for 2+ weeks (after accounting for lag)
- Impression Share dropping with stable budgets
- CTR declining while impressions grow (relevance problem)
- Conversions dropping while clicks remain stable (tracking or landing page issue)
- Sudden delivery drop to near zero (policy issue, payment failure, bid floor)

## The Conversion Lag Trap

The #1 most common misdiagnosis: "conversions dropped this week."

**Reality:** Most conversions in the last 7 days haven't been attributed yet. A campaign showing 5 conversions this week might show 15 when checked next week for the same period.

**Rule:** Never compare the last 7 days to any prior period without explicitly disclaiming conversion lag. For actionable comparisons, use data that's at least 7-14 days old.

## Diagnosis Checklist

When performance changes, check in this order:

1. **Conversion lag** — Is the "drop" just incomplete data?
2. **Tracking** — Did conversion tags fire correctly? Check Google Tag status.
3. **Smart Bidding** — Was there a recent strategy or target change? Is it in learning?
4. **Budget** — Is IS Lost (Budget) increasing?
5. **Quality Score** — Did QS components change?
6. **Competition** — Is IS Lost (Rank) increasing?
7. **Landing page** — Did anything change on the site (speed, content, checkout flow)?
8. **Seasonality** — Compare to same period last year, not just last month
9. **External** — Industry news, economic shifts, platform algorithm changes

## Key Insight

Most "performance problems" reported within 7 days of occurrence are conversion lag. Always check lag first. The second most common false alarm is Smart Bidding learning — give it at least 2 weeks before diagnosing.

## Analysis Implications

- When a client says "performance dropped this week" — first response is always to check conversion lag
- Use 14-30 day windows for reliable trend analysis
- Compare same day counts (e.g., first 20 days of this month vs first 20 days of last month)
- If both conversion lag and Smart Bidding learning are ruled out, then investigate structural causes
- Document the diagnosis path: what you checked, what you ruled out, what remains
