# ETL Data Pipeline — NYC Yellow Taxi Lakehouse
## Enterprise Bronze → Silver → Gold Architecture on Microsoft Fabric
---
## Architecture
## Tech Stack

| Layer | Tool |
|---|---|
| Storage | Microsoft Fabric OneLake |
| Compute | Microsoft Fabric Notebooks (PySpark) |
| File Format | Delta Lake |
| Orchestration | Fabric Data Pipelines (ETL_Master_Pipeline) |
| Schema Validation | Pandera 0.18 |
| Testing | pytest |
| CI/CD | GitHub Actions |
| Version Control | GitHub |
| Language | Python 3.11+ |

## Dataset

NYC TLC Yellow Taxi Trip Records — January and February 2024
- Source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Format: Parquet
- Size: ~5.9 million rows

## Pipeline Results

| Layer | Rows | Notes |
|---|---|---|
| Bronze | 5,972,150 | Raw data, append-only |
| Quarantine | 6,221 | 1.24% rejection rate |
| Silver | 5,450,489 | Clean, deduped, enriched |
| Gold Daily | 65 | One row per day |
| Gold Hourly | 1,446 | Trips per hour per day |

## How to Run Locally

git clone https://github.com/ruthvik257/etl-lakehouse-project
cd etl-lakehouse-project
pip install -r requirements.txt
pytest tests/ -v

## How to Run in Microsoft Fabric

1. Import notebooks into your Fabric workspace
2. Attach each notebook to its corresponding Lakehouse
3. Run ETL_Master_Pipeline to execute all stages in order
4. View results in the Gold Lakehouse Tables

The pipeline runs automatically every day at 2:00 AM.

## Key Architectural Principles

| Principle | Description |
|---|---|
| Immutability | Bronze layer is never overwritten, only appended |
| Idempotency | Re-running any stage produces the same result |
| Schema-on-write | Silver rejects bad records, never silently drops |
| Observability | Every run logs row counts, batch IDs, and timestamps |

## CI/CD

Every push to GitHub automatically runs:
1. Black - code formatting check
2. flake8 - lint for code errors
3. pytest - 6 unit tests
4. Pandera smoke test - schema validation check
