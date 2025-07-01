import os
import pandas as pd

base_path = r"C:\files\DDDR\Data"
all_data = []

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().endswith('.csv'):
                file_path = os.path.join(folder_path, file)
                df = pd.read_csv(file_path)
                df.insert(0, 'RTU', folder)
                all_data.append(df)

merged = pd.concat(all_data, ignore_index=True)
merged.to_csv('data.csv', index=False)
