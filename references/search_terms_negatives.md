# Search Terms & Negative Keywords

## Search Term Report

The search term report shows the **actual queries** users typed that triggered your ads. This is different from your keywords — especially with broad match and close variants.

Access via GAQL:
```sql
SELECT search_term_view.search_term, search_term_view.status,
       metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM search_term_view
WHERE segments.date BETWEEN '...' AND '...'
ORDER BY metrics.cost_micros DESC
```

**`search_term_view.status`** values:
- `ADDED` — Already exists as a keyword
- `EXCLUDED` — Already a negative keyword
- `ADDED_EXCLUDED` — Both (rare)
- `NONE` — Not added as keyword or negative

## Match Types

| Match Type | Syntax | Triggers On |
| :--- | :--- | :--- |
| **Broad Match** | `keyword` | Related searches, synonyms, implied intent |
| **Phrase Match** | `"keyword"` | Queries that include the meaning of the keyword |
| **Exact Match** | `[keyword]` | Queries with the same meaning as the keyword |

**Key:** Since 2024, all match types include close variants (misspellings, plurals, implied words). Broad match + Smart Bidding is Google's recommended default, but it requires active search term management.

## Negative Keywords

Negative keywords prevent your ads from showing for irrelevant queries.

| Level | Scope |
| :--- | :--- |
| **Ad Group** | Only blocks within that ad group |
| **Campaign** | Blocks across entire campaign |
| **Account** (via negative keyword list) | Blocks across all campaigns using the list |

**Negative match types:**
- Broad negative: blocks queries containing all negative terms (any order)
- Phrase negative: blocks queries containing the exact phrase
- Exact negative: blocks only the exact query

**Key difference:** Negative broad match does NOT include close variants or synonyms. Be explicit — add misspellings and variations manually.

## Wasted Spend Analysis

How to identify wasted spend from search terms:

1. Sort search terms by cost (descending)
2. Filter for terms with $0 conversions and high spend
3. Look for patterns: irrelevant topics, informational queries, competitor names
4. Check cost per conversion for converting terms — are they within target CPA?

## Key Insight

In broad match campaigns, 30-50% of search terms may be irrelevant. Regular search term reviews (weekly or bi-weekly) are essential. The cost of neglecting negatives compounds over time.

## Analysis Implications

- Pull the search term report sorted by cost to find the biggest waste first
- Group irrelevant terms into themes for efficient negative keyword creation
- Check if the account has negative keyword lists at account level
- For PMax: search term visibility is limited (Google only shows a subset)
- Calculate "wasted spend ratio" = cost on non-converting irrelevant terms / total spend
- If wasted spend > 20%, the account has a structural matching problem
