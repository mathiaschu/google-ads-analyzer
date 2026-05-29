# Segmentation

## GAQL Segments

Add `segments.*` fields to GAQL queries to break down metrics by dimension. Adding a segment creates one row per unique segment value.

## Available Segments

| Segment | Values | Best For |
| :--- | :--- | :--- |
| `segments.date` | YYYY-MM-DD | Daily trend analysis |
| `segments.device` | DESKTOP, MOBILE, TABLET | Device performance comparison |
| `segments.day_of_week` | MONDAY through SUNDAY | Identifying best/worst days |
| `segments.ad_network_type` | SEARCH, SEARCH_PARTNERS, CONTENT, YOUTUBE_SEARCH, YOUTUBE_WATCH | Channel breakdown |
| `segments.hour` | 0-23 | Hourly performance patterns |
| `segments.click_type` | Multiple (HEADLINE, SITELINK, etc.) | Understanding click composition |
| `segments.conversion_action` | Conversion action resource name | Breaking down by conversion type |
| `segments.conversion_action_category` | PURCHASE, LEAD, SIGNUP, etc. | Conversion type analysis |

## When to Segment

| Analysis Goal | Segment to Use |
| :--- | :--- |
| Performance trends | `segments.date` |
| Mobile vs desktop gap | `segments.device` |
| Day-of-week patterns | `segments.day_of_week` |
| Search vs partners performance | `segments.ad_network_type` |
| Which conversions are firing | `segments.conversion_action` |
| Hour-of-day optimization | `segments.hour` |

## Segment Compatibility

Not all segments work with all resources. Key restrictions:
- `segments.date` works with most resources
- `segments.device` and `segments.ad_network_type` work with campaign and ad group
- `segments.hour` cannot be combined with `segments.date` in some resources
- Some segments are mutually exclusive — GAQL will error if incompatible segments are combined

## Geographic Segmentation

Geographic data uses a separate resource (`geographic_view`) rather than a segment:

```sql
SELECT geographic_view.country_criterion_id, geographic_view.location_type,
       metrics.clicks, metrics.impressions, metrics.cost_micros, metrics.conversions
FROM geographic_view
```

`location_type` values:
- `AREA_OF_INTEREST` — User searched for this location
- `LOCATION_OF_PRESENCE` — User is physically in this location

## Key Insight

Segmentation is powerful but must be used carefully. Over-segmenting (e.g., daily + device + hour) creates sparse data that's hard to interpret. Start broad (campaign level), then segment one dimension at a time to isolate patterns.

## Analysis Implications

- Always start with `segments.date` to see trends before adding other segments
- Device segmentation is critical for eCommerce (mobile often has lower conversion rates but higher traffic)
- `ad_network_type = SEARCH_PARTNERS` often has lower quality — check if it's dragging down overall metrics
- Day-of-week analysis needs at least 4 weeks of data to be reliable
- When comparing periods, ensure same day-of-week distribution (compare full weeks, not partial)
