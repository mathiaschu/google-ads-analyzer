# GAQL Queries Reference

Ready-to-use queries for each step of the analysis workflow. Replace date ranges as needed.

## Discovery

### Account info
```sql
SELECT customer.id, customer.descriptive_name, customer.currency_code, customer.time_zone
FROM customer
```

### Active campaigns overview
```sql
SELECT campaign.id, campaign.name, campaign.status, campaign.advertising_channel_type,
       campaign.bidding_strategy_type, campaign_budget.amount_micros,
       metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY metrics.cost_micros DESC
```

## Campaign Performance (daily granularity)

```sql
SELECT campaign.id, campaign.name, segments.date,
       metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.ctr,
       metrics.conversions, metrics.conversions_value, metrics.cost_per_conversion
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY segments.date DESC
```

## Impression Share

```sql
SELECT campaign.id, campaign.name,
       metrics.search_impression_share,
       metrics.search_budget_lost_impression_share,
       metrics.search_rank_lost_impression_share,
       metrics.search_top_impression_percentage,
       metrics.search_absolute_top_impression_percentage,
       metrics.cost_micros, metrics.impressions, metrics.clicks
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND campaign.advertising_channel_type = 'SEARCH'
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
```

## Quality Score (keyword level)

```sql
SELECT ad_group.name, ad_group_criterion.keyword.text,
       ad_group_criterion.keyword.match_type,
       ad_group_criterion.quality_info.quality_score,
       ad_group_criterion.quality_info.creative_quality_score,
       ad_group_criterion.quality_info.search_predicted_ctr,
       ad_group_criterion.quality_info.post_click_quality_score,
       metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM keyword_view
WHERE ad_group_criterion.status = 'ENABLED'
  AND campaign.status = 'ENABLED'
  AND metrics.impressions > 0
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY metrics.cost_micros DESC
```

## Search Terms

```sql
SELECT search_term_view.search_term, search_term_view.status,
       campaign.name, ad_group.name,
       metrics.impressions, metrics.clicks, metrics.cost_micros,
       metrics.conversions, metrics.ctr
FROM search_term_view
WHERE segments.date BETWEEN '2026-01-01' AND '2026-01-31'
  AND metrics.impressions > 0
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

## Asset Group Performance (Performance Max)

```sql
SELECT asset_group.id, asset_group.name, asset_group.status,
       asset_group.ad_strength, campaign.name,
       metrics.impressions, metrics.clicks, metrics.cost_micros,
       metrics.conversions, metrics.conversions_value
FROM asset_group
WHERE campaign.status = 'ENABLED'
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
```

## Device Segmentation

```sql
SELECT campaign.name, segments.device,
       metrics.impressions, metrics.clicks, metrics.ctr,
       metrics.cost_micros, metrics.conversions, metrics.cost_per_conversion
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
```

## Geographic Performance

```sql
SELECT campaign.name, geographic_view.country_criterion_id,
       geographic_view.location_type,
       metrics.impressions, metrics.clicks, metrics.cost_micros,
       metrics.conversions, metrics.cost_per_conversion
FROM geographic_view
WHERE campaign.status = 'ENABLED'
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

## Day of Week Performance

```sql
SELECT campaign.name, segments.day_of_week,
       metrics.impressions, metrics.clicks, metrics.cost_micros,
       metrics.conversions, metrics.cost_per_conversion
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date BETWEEN '2026-01-01' AND '2026-01-31'
```

## Notes

- **Date ranges:** Always adjust `BETWEEN` dates to the actual analysis period
- **Micros:** All `cost_micros` and `amount_micros` values must be divided by 1,000,000
- **Limits:** Use `LIMIT` on high-cardinality queries (search terms, keywords, geo)
- **Segments:** Adding `segments.date` enables daily granularity but increases rows
- **PMax limitations:** Performance Max has limited GAQL reporting — asset-level metrics are not available via standard GAQL, only asset group level
