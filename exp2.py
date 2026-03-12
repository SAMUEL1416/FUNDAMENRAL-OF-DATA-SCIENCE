import pandas as pd
import numpy as np

# Sample Data
order_data = pd.DataFrame({
    "customer_id": [101, 102, 101, 103, 102, 101],
    "order_date": ["2024-01-01","2024-01-02","2024-01-05",
                   "2024-01-07","2024-01-10","2024-01-15"],
    "product_name": ["Laptop","Phone","Tablet",
                     "Laptop","Tablet","Phone"],
    "order_quantity": [1,2,1,3,2,1]
})

order_data["order_date"] = pd.to_datetime(order_data["order_date"])


orders_per_customer = order_data.groupby("customer_id").size()
print("Orders per customer:\n", orders_per_customer)


avg_qty = order_data.groupby("product_name")["order_quantity"].mean()


avg_qty_floor = np.floor(avg_qty).astype(int)

print("\nAverage quantity per product (Floor Value):\n", avg_qty_floor)

print("\nEarliest Date:", order_data["order_date"].min())
print("Latest Date:", order_data["order_date"].max())
