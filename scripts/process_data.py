from pathlib import Path
import pandas as pd

data_dir = Path(__file__).parent.parent / "data"/ "raw"
data_path = data_dir/ "framingham.csv"

df = pd.read_csv(data_path)
print(df.head())
print(df["TenYearCHD"].value_counts())
df.drop(['education'], inplace = True, axis = 1)
df.rename(columns ={'male':'Sex_male'}, inplace = True)
df.dropna(axis=0, inplace=True)

print(df["TenYearCHD"].value_counts())

processed_data_dir = Path(__file__).parent.parent / "data"/ "processed"
processed_path = processed_data_dir/ 'disease_data.csv'

df.to_csv(processed_path, index = False)
