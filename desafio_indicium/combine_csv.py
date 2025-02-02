import pandas as pd
import os

csv_orders = "../code-challenge/data/output/public-orders.csv"
csv_order_details = "../code-challenge/data/output/public-order_details.csv"

df_orders = pd.read_csv(csv_orders)
df_order_details = pd.read_csv(csv_order_details)

df_final = pd.merge(df_orders, df_order_details, on="order_id", how="inner")

output_path = "../code-challenge/data/output/query_orders_and_order_details.csv"
df_final.to_csv(output_path, index=False)
