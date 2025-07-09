import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_geo.csv", parse_dates=["DateTime"])
latest = df.sort_values("DateTime").groupby("RTU").tail(1)
latest = latest.dropna(subset=["SM010", "RAIN", "ST010"])

fig, ax = plt.subplots(figsize=(10, 7))
scatter = ax.scatter(latest["RAIN"], latest["SM010"], s=latest["ST010"] * 10, alpha=0.7, c="skyblue", edgecolors="black")

for i, row in latest.iterrows():
    ax.text(row["RAIN"], row["SM010"], row["RTU"], fontsize=6, ha="center", va="center")

ax.set_title("Soil Moisture vs Rainfall (Bubble Size = Temp)", fontsize=14)
ax.set_xlabel("Rainfall (mm)")
ax.set_ylabel("Topsoil Moisture (SM010)")
plt.grid(True)
plt.tight_layout()
plt.show()
