
import pandas as pd

# Load dataset
df = pd.read_csv("/content/CSV Cleaned_Analytics_Dataset.csv")

# Convert date
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Create RFM metrics
today = df['Order_Date'].max()

rfm = df.groupby("Customer_Id").agg({
    "Order_Date": lambda x: (today - x.max()).days,
    "Order_ID": "count",
    "Revenue": "sum"
})

rfm.columns = ["Recency","Frequency","Monetary"]

# Identify churn customers
rfm["Churn_Risk"] = "No"
rfm.loc[(rfm["Recency"] > 90) & (rfm["Frequency"] < 3),"Churn_Risk"] = "Yes"

# Save output
rfm.to_csv("Churn_Risk_Customers.csv")

print("ETL Pipeline Completed Successfully")
