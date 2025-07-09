import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from shapely.geometry import Point

df = pd.read_csv("data_geo.csv", parse_dates=["DateTime"])
latest = df.sort_values("DateTime").groupby("RTU").tail(1)
latest = latest.dropna(subset=["SM010", "Long", "Lat"])

bins = [0, 0.1, 0.2, 0.3, 1]
colors = ["red", "orange", "yellow", "green"]
cmap = mcolors.ListedColormap(colors)
norm = mcolors.BoundaryNorm(bins, cmap.N)

geometry = [Point(xy) for xy in zip(latest["Long"], latest["Lat"])]
gdf = gpd.GeoDataFrame(latest, geometry=geometry, crs="EPSG:4326")

fig, ax = plt.subplots(figsize=(12, 8))
gdf.plot(ax=ax, column="SM010", cmap=cmap, norm=norm, markersize=80, edgecolor="black", legend=True)

for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf["RTU"]):
    ax.text(x, y, str(label), fontsize=6, ha="center", va="center")

ax.set_title("Topsoil Moisture Status Map (Latest Reading)", fontsize=14)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.show()
