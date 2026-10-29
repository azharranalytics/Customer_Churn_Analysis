
from pathlib import Path
import pandas as pd

# Define project paths
project_path = Path(__file__).resolve().parent.parent

input_path = (
    project_path
    / "Data"
    / "Raw"
    / "Telco-Customer-Churn.csv"
)

output_path = (
    project_path
    / "Data"
    / "Processed"
    / "Telco-Customer-Churn-Cleaned.csv"
)

# Load the original dataset
df = pd.read_csv(input_path)

print("Original shape:", df.shape)

# Clean column names by removing surrounding spaces
df.columns = df.columns.str.strip()

# Clean whitespace in text columns
text_columns = df.select_dtypes(include=["object", "str"]).columns

for column in text_columns:
    df[column] = df[column].str.strip()

# Convert TotalCharges to numeric
# Blank strings become NaN
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print("\nMissing values after numeric conversion:")
print(df.isnull().sum())

# Documented business assumption:
# Zero-tenure customers with blank TotalCharges
# are treated as having zero accumulated charges.
new_customer_mask = (
    df["tenure"].eq(0)
    & df["TotalCharges"].isna()
)

print(
    "\nNew customers with blank TotalCharges:",
    new_customer_mask.sum()
)

df.loc[new_customer_mask, "TotalCharges"] = 0.0

# Validate remaining missing values
print("\nRemaining missing values:")
print(df.isnull().sum())

# Check duplicates and customer IDs
print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate customer IDs:", df["customerID"].duplicated().sum())

# Validate numeric data type
print("\nTotalCharges data type:", df["TotalCharges"].dtype)

# Calculate churn rate
churn_rate = df["Churn"].eq("Yes").mean() * 100

print(f"\nCustomer churn rate: {churn_rate:.2f}%")

# Save cleaned dataset
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("\nCleaned shape:", df.shape)
print("Cleaned dataset saved to:", output_path)
