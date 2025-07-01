import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

file_path = r"data.csv"
df = pd.read_csv(file_path, parse_dates=['DateTime'])

apsley_data = df[
    (df['RTU'] == 'Apsley') &
    (df['SM020'].notna()) &
    (df['DateTime'] >= '2025-06-06') &
    (df['DateTime'] <= '2025-06-08')
]

print(len(apsley_data))

plt.figure(figsize=(10, 5))
print(apsley_data['SM020'])
plt.plot(apsley_data['DateTime'], apsley_data['SM020'])
plt.title('SM020 over Time – Apsley (6–8 June 2025)')
plt.xlabel('Date')
plt.ylabel('SM020')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
