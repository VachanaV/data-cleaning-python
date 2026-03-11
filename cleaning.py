import pandas as pd

df = pd.read_csv("dataset.csv")

print("Dataset Preview")
print(df.head())

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

df = df.rename(columns={"Salary":"Income"})

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Income"] = df["Income"].fillna(df["Income"].mean())

df["Age"] = df["Age"].astype(int)

df["City"] = df["City"].str.lower().str.strip()

df["Gender"] = df["Gender"].replace({
"M":"Male",
"F":"Female"
})

df.to_csv("cleaned_dataset.csv", index=False)

print("Data Cleaning Completed")