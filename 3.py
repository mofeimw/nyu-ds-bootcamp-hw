import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme()

df = pd.read_csv("https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv", usecols=["hour_beginning", "Pedestrians"], parse_dates=["hour_beginning"], index_col=False)
df["hour_beginning"] = pd.to_datetime(df["hour_beginning"], format="%A", errors="coerce")
df["hour_beginning"]=df["hour_beginning"].dt.strftime("%A")
df = df.groupby(["hour_beginning"]).agg({"hour_beginning":"first","Pedestrians":"sum"}).reset_index(drop=True)
df = df.drop([2,3])

print(df)

graph = sns.lineplot(data=df)
graph.get_figure().savefig("graph.png")

df = pd.read_csv("https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv",  parse_dates=["hour_beginning"],index_col=False)
df["hour_beginning"] = pd.to_datetime(df["hour_beginning"], format="%Y", errors="coerce")
df["hour_beginning"] = df["hour_beginning"].dt.strftime("%Y")
df = df.groupby(["weather_summary"]).agg({"weather_summary": "first", "Pedestrians": "sum"}).reset_index(drop=True)
print(df)
print(df.corr(numeric_only=True))

def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 24:
        return "Evening"
    else:
        return "Night"

df = pd.read_csv("https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv",  parse_dates=["hour_beginning"],index_col=False)
df["time_of_day"] = df["hour_beginning"].dt.hour.apply(categorize_time_of_day)
print(df.groupby("time_of_day")["Pedestrians"].sum())
