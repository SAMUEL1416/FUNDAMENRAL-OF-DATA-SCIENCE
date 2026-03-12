import pandas as pd

property_data = pd.DataFrame({
    "property_id":[1,2,3,4],
    "location":["Chennai","Mumbai","Chennai","Delhi"],
    "bedrooms":[3,5,4,6],
    "area_sqft":[1200,2000,1500,2500],
    "listing_price":[5000000,9000000,6500000,12000000]
})


avg_price = property_data.groupby("location")["listing_price"].mean()
print("Average price per location:\n", avg_price)


more_than_4 = property_data[property_data["bedrooms"] > 4]
print("\nProperties with >4 bedrooms:\n", more_than_4)


largest = property_data.loc[property_data["area_sqft"].idxmax()]
print("\nLargest property:\n", largest)
'
