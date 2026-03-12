import pandas as pd
import numpy as np
DISCOUNT_RATE = 10   
TAX_RATE = 5         
n = int(input("Enter number of products: "))
products = []
prices = []
quantities = []
for i in range(n):
    print(f"\nEnter details for product {i+1}")
    name = input("Product Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    
    products.append(name)
    prices.append(price)
    quantities.append(qty)

df = pd.DataFrame({"Product": products,"Price": prices,"Quantity": quantities})

df["Total"] = df["Price"] * df["Quantity"]
total = np.sum(df["Total"])

discount_amount = total * DISCOUNT_RATE / 100
after_discount = total - discount_amount


tax_amount = after_discount * TAX_RATE / 100
final_total = after_discount + tax_amount


print("\n----------- BILL -----------")
print(df)
print("\nTotal before discount:", total)
print("Discount (10%):", discount_amount)
print("After discount:", after_discount)
print("Tax (5%):", tax_amount)
print("Final Total to Pay:", final_total)
print("----------------------------")
