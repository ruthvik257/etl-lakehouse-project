# Bronze Ingestion — NYC Yellow Taxi Data
# Run this in a Microsoft Fabric Notebook attached to bronze_lakehouse

# Cell 1: Imports
from pyspark.sql import functions as F
from datetime import datetime
import uuid
print("Libraries loaded ✅")

# Cell 2: Configuration
SOURCE_FILES_PATH = "Files/"
BRONZE_TABLE_NAME = "bronze_yellow_taxi"
BATCH_ID = datetime.now().strftime("%Y%m%d_%H%M%S")
print(f"Batch ID: {BATCH_ID}")
print(f"Source path: {SOURCE_FILES_PATH}")

# Cell 3: Read all uploaded Parquet files
df_raw = spark.read.parquet("Files/")
print(f"Columns: {df_raw.columns}")
print(f"Total raw rows: {df_raw.count():,}")
df_raw.show(3)

# Cell 4: Add ingestion metadata
df_bronze = df_raw \
    .withColumn("_ingested_at", F.current_timestamp()) \
    .withColumn("_batch_id", F.lit(BATCH_ID)) \
    .withColumn("_source", F.lit("nyc_tlc_yellow_taxi")) \
    .withColumn("_pipeline_version", F.lit("1.0"))
print("Metadata columns added ✅")

# Cell 5: Write to Bronze as Delta Table (APPEND only)
df_bronze.write \
    .format("delta") \
    .mode("append") \
    .option("mergeSchema", "true") \
    .saveAsTable(BRONZE_TABLE_NAME)
final_count = spark.table(BRONZE_TABLE_NAME).count()
print(f"✅ Bronze ingestion complete!")
print(f"   Rows written this batch : {df_bronze.count():,}")
print(f"   Total rows in Bronze    : {final_count:,}")
print(f"   Batch ID                : {BATCH_ID}")
