import pandas as pd

#initialise and assign main df and temp df
df = pd.read_csv("data/daily_sales_data_0.csv")

#assign the 2nd csv file to temp df and concat it to the main one
tempdf = pd.read_csv("data/daily_sales_data_1.csv")
df = pd.concat([df, tempdf], ignore_index=True)

#do the same for the 3rd csv file
tempdf = pd.read_csv("data/daily_sales_data_2.csv")
df = pd.concat([df, tempdf], ignore_index=True)

#now remove any product that isnt pink morsel
df = df[df["product"] == "pink morsel"]

#new column called sales
df["sales"] = (df["price"].str.replace("$", "").astype(float) * df["quantity"]).apply(lambda x: f"${x:.2f}")

#remove  column price and quantity
df = df.drop(columns=["price", "quantity", "product"])
#resetting the index
df = df.reset_index(drop=True)

df = df[["sales", "date", "region"]]
df.to_csv("formatted_data.csv", index=False)

