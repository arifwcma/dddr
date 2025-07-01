import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

file_path = r"data.csv"
df = pd.read_csv(file_path, parse_dates=['DateTime'])

df = df[df['SM020'].notna()]
unique_rtus = sorted(df['RTU'].unique())
fig, axes = plt.subplots(8, 10, figsize=(25, 18), sharex=True, sharey=True)
axes = axes.flatten()

for i, rtu in enumerate(unique_rtus):
    ax = axes[i]
    rtu_data = df[df['RTU'] == rtu]
    print(rtu, len(rtu_data))
    ax.plot(rtu_data['DateTime'], rtu_data['SM020'])
    ax.set_title(rtu, fontsize=8)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    ax.tick_params(axis='x', rotation=45, labelsize=6)
    ax.tick_params(axis='y', labelsize=6)

for j in range(len(unique_rtus), len(axes)):
    fig.delaxes(axes[j])

fig.suptitle('SM020 over Time for Each RTU', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("sm20.png",dpi=600)
plt.show()
