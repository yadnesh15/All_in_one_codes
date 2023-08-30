import pandas as pd
import numpy as np

df = pd.DataFrame({"Type":['Revenue','Expense','Profit'],"value":['100','70','']})
# df = pd.DataFrame(columns =["Value"],index=['Revenue','Expense','Profit'] )
# rev = df[df["Type"]=="Revenue"]["Value"]
print("Before: \n")
print(df)
rev = int(df[df["Type"]=="Revenue"]["value"][0])
exp = int(df[df["Type"]=="Expense"]["value"][1])
pft = rev - exp
# df1 = pd.DataFrame(df)
# df["value"] = np.where(df["Type"]=="Profit", pft, df["value"])
df.loc[df["Type"]=="Profit",["value"]]= pft
print(df)


