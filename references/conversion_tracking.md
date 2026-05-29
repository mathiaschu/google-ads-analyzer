# Conversion Tracking

## Conversion Types

| Type | Source | Common Use |
| :--- | :--- | :--- |
| **Website** | Google tag / GTM on site | Purchases, leads, sign-ups |
| **App** | Firebase / SDK | In-app actions |
| **Phone calls** | Call tracking | Call-based leads |
| **Import** | CRM / offline upload | Offline sales, qualified leads |

## Primary vs Secondary Conversions

| Category | Column | Used for Bidding? | Purpose |
| :--- | :--- | :--- | :--- |
| **Primary** | `metrics.conversions` | Yes | Smart Bidding optimizes toward these |
| **Secondary** | `metrics.all_conversions` - `metrics.conversions` | No | Tracking/observation only |

**Key:** Miscategorizing conversions is one of the most common Google Ads mistakes. If a low-value action (like page view) is marked as primary, Smart Bidding will optimize for that instead of actual revenue events.

## Attribution Models

Google Ads supports these attribution models:
- **Data-Driven Attribution (DDA)** — ML-based, distributes credit across touchpoints (default and recommended)
- **Last Click** — 100% credit to last-clicked ad
- **First Click** — 100% credit to first-clicked ad
- **Linear** — Equal credit across all touchpoints
- **Time Decay** — More credit to recent touchpoints
- **Position-Based** — 40% first, 40% last, 20% middle

**Note:** Google is deprecating all non-DDA models. New conversion actions default to DDA.

## Conversion Lag

Conversions are attributed to the **click date**, not the conversion date. This creates a reporting lag:

| Business Type | Typical Lag |
| :--- | :--- |
| eCommerce (impulse) | 1-3 days |
| eCommerce (considered) | 3-7 days |
| B2B / Lead Gen | 7-30+ days |

**Practical impact:** The last 7 days of data will almost always show lower conversions than reality. When comparing periods, exclude the last 7 days or normalize for expected lag.

## Dynamic Values

Conversion value can be:
- **Static** — Same value for every conversion (e.g., $50 per lead)
- **Dynamic** — Actual transaction value passed via the tag (e.g., purchase amount)

For Smart Bidding with Target ROAS, dynamic values are essential. Static values work for Target CPA.

## Key Insight

"Conversions" in Google Ads is not a simple count — it's filtered by primary/secondary status, attribution model, and conversion window. Two accounts can have the same actual sales but report very different "conversion" numbers depending on their setup.

## Analysis Implications

- Always check which conversion actions are set as primary (`conversion_action.category` and `conversion_action.primary_for_goal`)
- Verify conversion counting: "One" (per click, for leads) vs "Every" (per click, for sales)
- Check conversion windows: default is 30 days for clicks, 1 day for view-through
- If CPA suddenly "improved" after a tracking change, it may be a measurement artifact, not real improvement
- For accounts importing offline conversions: check upload frequency and lag in reporting
