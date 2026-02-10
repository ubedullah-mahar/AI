# Task 01
import pandas as pd

df = pd.read_csv("lab 04/workout.csv")

# 1. Filter by quality FIRST
df = df.dropna(thresh=3)

# 2. Handle missing values
df = df.fillna(0)

# 3. Remove duplicate rows
df = df.drop_duplicates()

print(df)


