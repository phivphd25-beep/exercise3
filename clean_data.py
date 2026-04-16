
import pandas as pd

df = pd.read_csv("data/sample_data.csv")

print("Missing values:\n", df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

df.to_csv("data/cleaned_data.csv", index=False)

print("Data cleaned successfully")
