import pandas as pd

# df1 = pd.DataFrame({ "name": ["A", "B", "C", "D"],
#                      "value": [1, 2, 3, 4]})

# df2 = pd.DataFrame({ "name": ["A", "B", "C", "D"],
#                      "value": [5, 6, 7, 8]})
# df3 = pd.merge(df1, df2, on="name", how="inner")



df1 = pd.DataFrame({ "country": ["Chile", "México", "Colombia", "España"],
                     "date": [1, 2, 3, 4]})
df1.set_index("country", inplace=True)

df2 = pd.DataFrame({ "country": ["Chile", "México", "Colombia", "España"],
                     "date": [5, 6, 7, 8]})

df2.set_index("country", inplace=True)

df3 = df1.join(df2, lsuffix="_1990", rsuffix="_1991", how="inner")

print(df3)
