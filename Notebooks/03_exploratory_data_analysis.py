
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
project_path = Path(__file__).resolve().parent.parent

file_path = (
    project_path
    / "Data"
    / "Processed"
    / "Telco-Customer-Churn-Cleaned.csv"
)

df = pd.read_csv(file_path)

sns.set_theme(style="whitegrid")

# 1. Overall churn distribution
print("\n--- CUSTOMER CHURN DISTRIBUTION ---")
print(df["Churn"].value_counts())

churn_rate = df["Churn"].eq("Yes").mean() * 100
print(f"Overall churn rate: {churn_rate:.2f}%")

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Customer Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 2. Churn by contract type
print("\n--- CHURN BY CONTRACT TYPE ---")

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print(contract_churn.round(2))

contract_churn.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Churn Distribution by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Percentage of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.show()

# 3. Churn by tenure group
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0–12 months", "13–24 months",
            "25–48 months", "49–72 months"]
)

print("\n--- CHURN BY TENURE GROUP ---")

tenure_churn = pd.crosstab(
    df["TenureGroup"],
    df["Churn"],
    normalize="index"
) * 100

print(tenure_churn.round(2))

tenure_churn.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Churn Distribution by Customer Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Percentage of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.show()


# 4. Churn by payment method
print("\n--- CHURN BY PAYMENT METHOD ---")

payment_churn = (
    df.groupby("PaymentMethod", observed=True)["Churn"]
    .apply(lambda x: x.eq("Yes").mean() * 100)
    .sort_values(ascending=False)
)

print(payment_churn.round(2))

payment_churn.sort_values().plot(
    kind="barh",
    figsize=(9, 5)
)

plt.title("Churn Rate by Payment Method")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Payment Method")
plt.tight_layout()
plt.show()


# 5. Churn by tech support
print("\n--- CHURN BY TECH SUPPORT ---")

support_churn = (
    df.groupby("TechSupport", observed=True)["Churn"]
    .apply(lambda x: x.eq("Yes").mean() * 100)
    .sort_values(ascending=False)
)

print(support_churn.round(2))

support_churn.sort_values().plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Churn Rate by Tech Support")
plt.xlabel("Tech Support")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
