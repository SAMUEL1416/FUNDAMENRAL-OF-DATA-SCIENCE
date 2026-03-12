import pandas as pd

sales_df = pd.DataFrame({
    "Product": ["A", "B", "C", "A", "B", "D", "E", "F", "A", "C"],
    "Quantity": [10, 15, 8, 5, 20, 7, 12, 9, 6, 14]
})


total_sales = sales_df.groupby("Product")["Quantity"].sum()


top5 = total_sales.nlargest(5)

print("Top 5 Most Sold Products:\n", top5)
