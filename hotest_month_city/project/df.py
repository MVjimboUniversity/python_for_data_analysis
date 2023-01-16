import zipfile

import pandas as pd


def get_df(filename: str) -> pd.DataFrame:
    with zipfile.ZipFile("archive.zip") as z:
        with z.open(filename) as f:
            df = pd.read_csv(f, parse_dates=["dt"])
            df["dt"] = pd.to_datetime(df["dt"], yearfirst=True)
            return df


def get_hotest_month(df: pd.DataFrame, year: int) -> str:
    df = df.loc[df["dt"].dt.year == year, ["dt", "AverageTemperature"]]
    return df.groupby(pd.Grouper(key="dt", freq="M")).max().idxmax()[0].month_name()


def get_hotest_city(df: pd.DataFrame, year: int) -> str:
    df = df.loc[df["dt"].dt.year == year, ["City", "AverageTemperature"]]
    return df.groupby("City").max().idxmax()[0]
