from project.df import get_df, get_hotest_month


def test_get_hotest_month():
    df = get_df("GlobalLandTemperaturesByMajorCity.csv")
    assert get_hotest_month(df, 1980) == "July"
    assert get_hotest_month(df, 1981) == "June"
