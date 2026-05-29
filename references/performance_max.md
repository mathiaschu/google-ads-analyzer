# Performance Max

## What It Is

Performance Max (PMax) is Google's fully automated, all-channel campaign type. It runs across Search, Display, YouTube, Gmail, Maps, and Discover simultaneously. Google's ML decides:
- Which channels to show ads on
- What creative combinations to use
- Which audiences to target
- How much to bid

## Structure

```
Performance Max Campaign
└── Asset Group(s)
    ├── Assets (headlines, descriptions, images, videos, logos)
    ├── Audience Signals (suggested audiences for ML)
    ├── Final URL(s)
    └── Listing Groups (for Shopping feeds)
```

## Asset Groups

Each PMax campaign has 1+ asset groups. Think of them as "ad group equivalents" — each serves different themes or product categories.

**Asset requirements per group:**
| Asset Type | Min | Max | Recommended |
| :--- | :--- | :--- | :--- |
| Headlines (30 chars) | 3 | 15 | 5+ |
| Long Headlines (90 chars) | 1 | 5 | 3+ |
| Descriptions (90 chars) | 2 | 5 | 4+ |
| Images (landscape, square, portrait) | 1 each | 20 total | 5+ landscape, 5+ square |
| Logos | 1 | 5 | 2+ |
| Videos (10+ sec) | 0 | 5 | 1+ (or Google auto-generates) |

## Ad Strength

Diagnostic score per asset group:
- **Excellent** — Full asset mix, good variety
- **Good** — Adequate but could improve
- **Average** — Missing assets or low variety
- **Poor** — Insufficient assets, limiting ML optimization

**Key:** Ad Strength below "Good" limits the system's ability to test combinations. Always aim for "Good" or better.

## Audience Signals

Audience signals are **suggestions** to the ML, not hard targeting:
- Custom segments (keywords, URLs, apps)
- Your data (remarketing lists, customer match)
- Interests and detailed demographics

The system uses these as starting points but will expand beyond them if it finds better-performing audiences.

## Cannibalization with Search

**Critical issue:** PMax can bid on branded search queries, inflating its conversion numbers at the expense of existing Search campaigns.

How to detect:
1. Check Search campaign IS — if it dropped when PMax launched, PMax is cannibalizing
2. Look at PMax conversion sources — if most conversions come from Search network, branded queries are likely a factor
3. Add brand exclusions to PMax (available via negative keyword lists at account level)

## Key Insight

PMax reports aggregate metrics across all channels. A "$5 CPA" from PMax might be $2 from branded Search (cannibalizing your brand campaign) and $15 from prospecting Display. Always dig deeper.

## Analysis Implications

- Pull `asset_group` level data to see per-group performance
- Check `asset_group.ad_strength` — anything below "Good" needs more assets
- If PMax has Shopping feed: review listing group structure and product feed quality
- Compare Search campaign IS before vs after PMax launch to detect cannibalization
- PMax conversion reporting has limited transparency — conversion paths are not fully visible
- GAQL access is limited: asset-level performance (individual headlines/images) is not available via API, only through the Google Ads UI
