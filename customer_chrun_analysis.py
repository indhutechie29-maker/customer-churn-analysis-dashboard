import pandas as pd
print("customer churn analysis project started!")
print("pandas version:",pd.__version__)
df=pd.read_csv("customer_churn.csv")
print(df.head())
print(df.shape)

# Customer churn analysis
print("\nChurn distribution:")
print(df["Churn"].value_counts())

print("\nChurn percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

# Overall churn rate
churn_rate = (df["Churn"] == "Yes").mean() * 100

print("\nOverall customer churn rate:")
print(round(churn_rate, 2), "%")
# Churn rate by contract type

print("\nChurn rate by contract type:")

contract_churn = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print(contract_churn.round(2))
# Churn rate by payment method

print("\nChurn rate by payment method:")

payment_churn = df.groupby("PaymentMethod")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print(payment_churn.round(2).sort_values(ascending=False))

# Churn rate by customer tenure

print("\nChurn rate by tenure group:")

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=["0-12 months", "13-24 months",
            "25-48 months", "49-72 months"],
    include_lowest=True
)

tenure_churn = df.groupby(
    "TenureGroup", observed=False
)["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print(tenure_churn.round(2))

import matplotlib.pyplot as plt

tenure_churn.plot(kind="bar")
plt.title("Customer Churn Rate by Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

tenure_churn.plot(kind="bar")

plt.title("Customer Churn Rate by Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n--- RECOMMENDATION ---")

print(
    "Focus on retaining new customers "
    "during their first 12 months."
)

