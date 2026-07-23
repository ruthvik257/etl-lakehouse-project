# Data Dictionary — Gold Layer
## Table: gold_daily_summary
One row per day. Used by dashboards and analysts for daily business reporting.
| Column | Type | Description | Example |
|---|---|---|---|
| pickup_date | Date | Date of taxi pickups | 2024-01-15 |
| total_trips | Integer | Total number of trips that day | 94,521 |
| total_fare_revenue | Double | Sum of base fare amounts ($) | 1,234,567.89 |
| total_revenue_incl_tips | Double | Total revenue including tips and taxes ($) | 1,456,789.00 |
| avg_trip_distance_miles | Double | Average trip distance in miles | 3.24 |
| avg_trip_duration_mins | Double | Average trip duration in minutes | 18.5 |
| avg_passengers_per_trip | Double | Average number of passengers | 1.4 |
| unique_pickup_zones | Integer | Number of distinct pickup zones active | 127 |
| weekend_trips | Integer | Trips on Saturday or Sunday | 24,310 |
| weekday_trips | Integer | Trips on Monday through Friday | 70,211 |
## Table: gold_hourly_patterns
One row per day per hour. Used by operations teams for demand forecasting.
| Column | Type | Description | Example |
|---|---|---|---|
| pickup_date | Date | Date of pickups | 2024-01-15 |
| pickup_hour | Integer | Hour of day (0-23) | 8 |
| trips_this_hour | Integer | Number of trips in that hour | 4,231 |
| avg_fare | Double | Average fare amount ($) | 14.50 |
| avg_distance | Double | Average trip distance (miles) | 2.87 |
## Silver Layer Reference: silver_yellow_taxi
Cleaned and enriched data used as input to the Gold layer.
| Column | Type | Description |
|---|---|---|
| tpep_pickup_datetime | Timestamp | Pickup date and time |
| tpep_dropoff_datetime | Timestamp | Dropoff date and time |
| passenger_count | Float | Number of passengers |
| trip_distance | Float | Trip distance in miles |
| fare_amount | Float | Base fare amount ($) |
| total_amount | Float | Total charge including tips and taxes ($) |
| PULocationID | Integer | Pickup location zone ID |
| DOLocationID | Integer | Dropoff location zone ID |
| trip_duration_minutes | Double | Calculated trip duration in minutes |
| pickup_date | Date | Extracted date from pickup timestamp |
| pickup_hour | Integer | Extracted hour from pickup timestamp |
| pickup_day_of_week | Integer | Day of week (1=Sunday, 7=Saturday) |
| is_weekend | Boolean | True if pickup was on Saturday or Sunday |
| _silver_processed_at | Timestamp | When this record was processed into Silver |
