import pandas as pd

df1 = pd.read_csv("portal_names.csv")
df2 = pd.read_csv("bron_id_name_coord.csv")

df1["_key"] = df1["Site"].astype(str).str.strip().str.lower()
df2["_key"] = df2["Portal location"].astype(str).str.strip().str.lower()

merged = pd.merge(df1, df2[["Portal location", "EOI_SITE", "SiteAddres", "_key"]], on="_key", how="outer")

merged = merged[["Site", "Portal location", "EOI_SITE", "SiteAddres"]]

merged = merged.sort_values(by=["Site", "Portal location"])

merged.to_csv("portal_site_eoi.csv", index=False)
