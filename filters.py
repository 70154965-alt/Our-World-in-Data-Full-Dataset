import pandas as pd

def load_data():
    df = pd.read_csv("data/owid-energy-data.csv")
    return df

def apply_filters(df, countries, year_range, energy_col, search_text):
    if countries:
        df = df[df["country"].isin(countries)]
    df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]
    if search_text:
        df = df[df["country"].str.contains(search_text, case=False, na=False)]
    return df