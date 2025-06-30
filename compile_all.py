import geopandas as gpd
import pandas as pd
import glob
import os

matches = []
base = r"C:\files\Bruce\data"

for shp in glob.glob(os.path.join(base, '**', '*.shp'), recursive=True):
    try:
        gdf = gpd.read_file(shp)
        if 'EOI' in gdf.columns:
            f = gdf[gdf['EOI'].astype(str).str.contains("POM24001|RTBC2500", na=False)].copy()
            if not f.empty:
                f.loc[:, 'source'] = os.path.relpath(shp, base)
                matches.append(f)
    except Exception as e:
        print(f"Failed to read {shp}: {e}")
        continue

if matches:
    pd.concat(matches).to_csv("filtered_shapes.csv", index=False)
