import pandas as pd

df = pd.read_csv("data_geo.csv")
rtu_counts = df["RTU"].value_counts().sort_values(ascending=False)
print(rtu_counts)
