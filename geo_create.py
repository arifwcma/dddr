import pandas as pd

data = pd.read_csv("data.csv")
site_info = pd.read_csv("portal_site_list.csv")

site_info = site_info.rename(columns={"Site Name": "RTU"})
merged = pd.merge(data, site_info[["RTU", "Long", "Lat"]], on="RTU", how="left")
merged.to_csv("data_geo.csv", index=False)
