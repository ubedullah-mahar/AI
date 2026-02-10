# task 02
import pandas as pd
df = pd.read_csv("lab 04/workout.csv")
print(df.head(5))
print(df.tail(5))
small_df=df[["Duration","pulse"]]