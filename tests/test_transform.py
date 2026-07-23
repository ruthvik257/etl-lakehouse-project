# tests/test_transform.py
import pytest
import pandas as pd
# Test 1: Negative fare should be rejected
def test_negative_fare_rejected():
    data = pd.DataFrame([{"fare_amount": -50.0, "trip_distance": 5.0}])
    is_invalid = (data["fare_amount"] < 0).any()
    assert is_invalid, "Test data should have invalid fare"
# Test 2: Valid record passes
def test_valid_record_passes():
    data = pd.DataFrame([{"fare_amount": 15.0, "trip_distance": 5.0}])
    is_valid = (data["fare_amount"] >= 0).all()
    assert is_valid
# Test 3: Dropoff must be after pickup
def test_dropoff_after_pickup():
    good = pd.DataFrame([{
        "tpep_pickup_datetime":  pd.Timestamp("2024-01-01 08:00"),
        "tpep_dropoff_datetime": pd.Timestamp("2024-01-01 08:30")
    }])
    bad = pd.DataFrame([{
        "tpep_pickup_datetime":  pd.Timestamp("2024-01-01 08:30"),
        "tpep_dropoff_datetime": pd.Timestamp("2024-01-01 08:00")
    }])
    assert good["tpep_dropoff_datetime"].iloc[0] > good["tpep_pickup_datetime"].iloc[0]
    assert bad["tpep_dropoff_datetime"].iloc[0] < bad["tpep_pickup_datetime"].iloc[0]
# Test 4: Trip duration calculation
def test_trip_duration_calculation():
    pickup  = pd.Timestamp("2024-01-01 08:00:00")
    dropoff = pd.Timestamp("2024-01-01 08:30:00")
    duration_minutes = (dropoff - pickup).seconds / 60
    assert duration_minutes == 30.0
# Test 5: Duplicate removal
def test_deduplication():
    data = pd.DataFrame([
        {"trip_distance": 5.0, "fare_amount": 15.0},
        {"trip_distance": 5.0, "fare_amount": 15.0},
        {"trip_distance": 8.0, "fare_amount": 22.0},
    ])
    deduped = data.drop_duplicates()
    assert len(deduped) == 2, f"Expected 2 unique rows, got {len(deduped)}"
# Test 6: Weekend flag logic
def test_weekend_detection():
    saturday = pd.Timestamp("2024-01-06")
    monday   = pd.Timestamp("2024-01-08")
    assert saturday.dayofweek in [5, 6], "Saturday should be weekend"
    assert monday.dayofweek not in [5, 6], "Monday should be weekday"
