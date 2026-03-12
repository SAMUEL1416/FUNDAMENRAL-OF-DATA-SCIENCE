import pandas as pd

sales_data = pd.DataFrame({
    "Product": ["A","B","C","A","B"],
    "Price": [100,200,150,100,200],
    "Quantity": [2,1,3,1,2]
})

sales_data["Total Sales"] = sales_data["Price"] * sales_data["Quantity"]

print(sales_data)

total_sales = sales_data.groupby("Product")["Total Sales"].sum()
print("\nTotal Sales per Product:\n", total_sales)
