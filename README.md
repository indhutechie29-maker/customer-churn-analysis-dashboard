Customer Churn Analysis Dashboard

Project Overview

This project analyzes telecom customer churn to identify customer segments with higher churn rates and support data-driven customer retention decisions.

An interactive dashboard was built using Python and Streamlit.

Objectives

- Calculate the overall customer churn rate.
- Analyze churn across contract types.
- Study churn patterns by customer tenure.
- Compare churn rates across payment methods.
- Present findings through interactive filters and charts.

Tools and Technologies

- Python
- Pandas
- Matplotlib
- Streamlit
- SQL
- MySQL Workbench

Key Findings

- Total customers analyzed: 7,043
- Customers who churned: 1,869
- Overall churn rate: 26.54%
- Customers with shorter tenure showed higher churn rates in the tenure analysis.

Dashboard Features

- KPI cards for total customers, customers lost, and churn rate.
- Contract and payment method filters.
- Customer churn distribution chart.
- Contract-wise churn rate analysis.
- Tenure-wise churn rate analysis.
- Payment method-wise churn rate analysis.
- Dataset preview.

Business Recommendations

- Investigate customer experiences during the first year.
- Compare churn patterns across contract types.
- Investigate factors associated with higher churn across payment methods.
- Use additional customer data to validate possible retention strategies.

How to Run the Dashboard

1. Install Python.

2. Install the required libraries:
   
   "pip install -r requirements.txt"

3. Keep "app.py" and "customer_churn.csv" in the same folder.

4. Run:
   
   "streamlit run app.py"

5. Open the local URL shown in the terminal.

Project Files

- "app.py" — Interactive dashboard
- "customer_churn_analysis.py" — Python analysis
- "customer_churn.csv" — Dataset
- "requirements.txt" — Required libraries
- "README.md" — Project documentation

Conclusion

This project demonstrates data cleaning, exploratory data analysis, SQL aggregation, data visualization, and interactive dashboard development to support customer retention analysis.