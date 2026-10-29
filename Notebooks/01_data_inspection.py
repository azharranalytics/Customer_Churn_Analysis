
from pathlib import Path
import pandas as pd
import numpy as np

# Locate the project and dataset
project_path = Path(__file__).resolve().parent.parent
file_path = (
    project_path
    / "Data"
    / "Raw"
    / "Telco-Customer-Churn.csv"
)

# Load the dataset
df = pd.read_csv(file_path)

# 1. Dataset dimensions
print("\n--- DATASET SHAPE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. First five records
print("\n--- FIRST FIVE ROWS ---")
print(df.head())

# 3. Column names and data types
print("\n--- DATA TYPES AND NON-NULL COUNTS ---")
df.info()

# 4. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 5. Duplicate records
print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", df.duplicated().sum())

# 6. Check customer IDs
print("\n--- CUSTOMER ID CHECK ---")
print("Unique customer IDs:", df["customerID"].nunique())
print("Duplicate customer IDs:", df["customerID"].duplicated().sum())

# 7. Check blank TotalCharges values
print("\n--- TOTAL CHARGES CHECK ---")
blank_charges = (
    df["TotalCharges"]
    .astype("string")
    .str.strip()
    .eq("")
    .sum()
)
print("Blank TotalCharges:", blank_charges)

# 8. Basic numerical statistics
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe(include="number"))

print("\nInitial data inspection completed.")


# Investigate blank TotalCharges records

print("\n--- CUSTOMERS WITH BLANK TOTAL CHARGES ---")

blank_mask = (
    df["TotalCharges"]
    .astype("string")
    .str.strip()
    .eq("")
)

blank_customers = df.loc[
    blank_mask,
    ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]
]

print(blank_customers.to_string(index=False))

print("\n--- TENURE OF CUSTOMERS WITH BLANK CHARGES ---")
print(blank_customers["tenure"].value_counts(dropna=False))

print("\n--- CHECK ZERO-TENURE CUSTOMERS ---")
print("Total zero-tenure customers:", (df["tenure"] == 0).sum())
print(
    "Zero-tenure customers with blank charges:",
    ((df["tenure"] == 0) & blank_mask).sum()
)
