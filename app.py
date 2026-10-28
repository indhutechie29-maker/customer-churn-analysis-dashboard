import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Analysis Dashboard")
st.write("Explore customer churn and retention patterns.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("customer_churn.csv")

    # Convert TotalCharges to numeric if available
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"], errors="coerce"
        )

    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "customer_churn.csv not found. "
        "Keep it in the same folder as app.py."
    )
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")

if "Contract" in df.columns:
    contracts = sorted(df["Contract"].dropna().unique())
    selected_contracts = st.sidebar.multiselect(
        "Select Contract",
        contracts,
        default=contracts
    )
    df = df[df["Contract"].isin(selected_contracts)]

if "Churn" not in df.columns:
    st.error("The dataset does not contain a Churn column.")
    st.stop()


# Payment Method Filter
if "PaymentMethod" in df.columns:
    payment_methods = sorted(
        df["PaymentMethod"].dropna().unique()
    )

    selected_payments = st.sidebar.multiselect(
        "Select Payment Method",
        payment_methods,
        default=payment_methods
    )

    df = df[df["PaymentMethod"].isin(selected_payments)]
# Calculate KPIs
total_customers = len(df)
customers_lost = (df["Churn"] == "Yes").sum()
churn_rate = (
    customers_lost / total_customers * 100
    if total_customers > 0 else 0
)

# KPI cards
c1, c2, c3 = st.columns(3)
c1.metric("Total Customers", f"{total_customers:,}")
c2.metric("Customers Lost", f"{customers_lost:,}")
c3.metric("Churn Rate", f"{churn_rate:.2f}%")

st.divider()

# Churn distribution
st.subheader("Customer Churn Distribution")

churn_counts = df["Churn"].value_counts()

fig1, ax1 = plt.subplots()
churn_counts.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Churn")
ax1.set_ylabel("Number of Customers")
ax1.set_title("Customers: Stayed vs Churned")
ax1.tick_params(axis="x", rotation=0)
st.pyplot(fig1)
plt.close(fig1)

# Contract analysis
if "Contract" in df.columns:
    st.subheader("Churn Rate by Contract")

    contract_churn = (
        df.assign(churn_flag=(df["Churn"] == "Yes").astype(int))
        .groupby("Contract")["churn_flag"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    fig2, ax2 = plt.subplots()
    contract_churn.plot(kind="bar", ax=ax2)
    ax2.set_ylabel("Churn Rate (%)")
    ax2.set_xlabel("Contract Type")
    ax2.tick_params(axis="x", rotation=20)
    st.pyplot(fig2)
    plt.close(fig2)

# Tenure analysis
if "tenure" in df.columns:
    st.subheader("Churn Rate by Customer Tenure")

    tenure_df = df.copy()
    tenure_df["Tenure Group"] = pd.cut(
        tenure_df["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=[
            "0-12 months",
            "13-24 months",
            "25-48 months",
            "49-72 months"
        ]
    )

    tenure_churn = (
        tenure_df.assign(
            churn_flag=(tenure_df["Churn"] == "Yes").astype(int)
        )
        .groupby("Tenure Group", observed=False)["churn_flag"]
        .mean()
        .mul(100)
    )

    fig3, ax3 = plt.subplots()
    tenure_churn.plot(kind="bar", ax=ax3)
    ax3.set_ylabel("Churn Rate (%)")
    ax3.set_xlabel("Customer Tenure")
    ax3.tick_params(axis="x", rotation=15)
    st.pyplot(fig3)
    plt.close(fig3)
# Payment Method Churn Analysis
if "PaymentMethod" in df.columns:
    st.subheader("Churn Rate by Payment Method")

    payment_churn = (
        df.assign(
            churn_flag=(df["Churn"] == "Yes").astype(int)
        )
        .groupby("PaymentMethod")["churn_flag"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    fig4, ax4 = plt.subplots()
    payment_churn.plot(kind="bar", ax=ax4)

    ax4.set_ylabel("Churn Rate (%)")
    ax4.set_xlabel("Payment Method")
    ax4.set_title("Customer Churn by Payment Method")
    ax4.tick_params(axis="x", rotation=20)

    st.pyplot(fig4)
    plt.close(fig4)
st.subheader("💡 Business Insights & Recommendations")

st.info(
    "1. Focus on new customers during their first 12 months, "
    "as this group has the highest observed churn rate."
)

st.info(
    "2. Compare churn rates across contract types to identify "
    "customer segments that may need retention support."
)

st.info(
    "3. Review payment methods with higher churn rates and "
    "investigate possible reasons before deciding on actions."
)


st.subheader("Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)

st.caption("Customer Churn Analysis | Python • Pandas • Streamlit") 
