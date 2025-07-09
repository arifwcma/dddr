import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_geo.csv", parse_dates=["DateTime"])
RTU = "Crowlands"
apsley = df[df["RTU"] == RTU].dropna(subset=["SM010", "ST010", "RAIN"])
apsley = apsley.sort_values("DateTime")

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(apsley["DateTime"], apsley["SM010"], color="green", label="SM010 (Moisture)")
ax1.set_ylabel("Topsoil Moisture (SM010)", color="green")
ax1.tick_params(axis="y", labelcolor="green")

ax2 = ax1.twinx()
ax2.plot(apsley["DateTime"], apsley["ST010"], color="orange", label="ST010 (Soil Temp)")
ax2.bar(apsley["DateTime"], apsley["RAIN"], color="blue", alpha=0.3, label="Rainfall")
ax2.set_ylabel("Soil Temp (°C) / Rainfall (mm)", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")

fig.suptitle(f"{RTU}: SM010, ST010, and Rainfall Over Time", fontsize=14)
fig.tight_layout()
plt.show()
