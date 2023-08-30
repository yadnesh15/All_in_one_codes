import pandas as pd

df= pd.read_excel(r"E:\Yadnesh\Oceania_PCData\Oceania_PCData.xlsx")


# df = df[df['Room']=='Deluxe King Bed Mountain View']

df = pd.DataFrame(df)
df1 = df[['Stay Date','1 Person']]

df1['Stay Date'].unique()
# df = df['Stay Date'].unique()
print(df1)