# Account Structure

## MCC Hierarchy

```
MCC (Manager Account)
├── Client Account A
│   ├── Search Campaign (Brand)
│   ├── Search Campaign (Non-Brand)
│   ├── PMax Campaign
│   └── Display Campaign
├── Client Account B
│   └── ...
└── Sub-MCC
    └── Client Account C
```

**MCC access:** When querying accounts through an MCC, you must set `login-customer-id` to the MCC's customer ID. The MCP server handles this via the `GOOGLE_ADS_LOGIN_CUSTOMER_ID` environment variable.

## Account Discovery

1. `list_accessible_customers` → returns all accessible customer IDs
2. Query each with `SELECT customer.id, customer.descriptive_name, customer.manager` to identify managers vs client accounts
3. Only query metrics on **non-manager** accounts (manager accounts don't have campaign data)

## Campaign Organization Best Practices

| Split | Why |
| :--- | :--- |
| **Brand vs Non-Brand** | Brand has higher CTR, lower CPA — mixing skews metrics |
| **By Match Type** | Exact match and broad match behave differently — separate allows better budget control |
| **By Intent** | High-intent (buy, pricing) vs low-intent (what is, how to) queries have different conversion rates |
| **By Product/Service** | Different products have different margins and CPAs |

## Naming Conventions

Consistent naming enables easier GAQL filtering and reporting. Common patterns:
- `[Type] - [Target] - [Match/Strategy]` (e.g., "Search - Brand - Exact")
- `[Product] | [Channel] | [Audience]` (e.g., "Shoes | PMax | Remarketing")

When analyzing, look for naming patterns to understand the account's structure intent.

## Budget Structure

| Level | What It Controls |
| :--- | :--- |
| **Campaign budget** | Max daily spend per campaign (or shared budget) |
| **Shared budget** | Pool of budget shared across multiple campaigns |
| **Account budget** | Overall account-level spend cap (rare) |

**Key:** Google can spend up to **2x the daily budget** on any given day, but averages to the daily budget over the month. Don't alarm on single-day overspend.

## Key Insight

Account structure directly impacts Smart Bidding performance. Too many campaigns with too few conversions each = insufficient data for ML to learn. Consolidation (fewer campaigns, more data each) often improves Smart Bidding outcomes.

## Analysis Implications

- Map the full account structure before analyzing performance
- Identify brand vs non-brand split — if mixed, metrics are unreliable
- Check if the account uses shared budgets (can cause unexpected budget allocation)
- Count conversions per campaign — Smart Bidding needs 30+/month per campaign
- If MCC access: query `customer.manager = TRUE` to skip manager accounts in metric pulls
