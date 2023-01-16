from project.df import get_df, get_hotest_city


def test_get_hotest_city():
    df = get_df("GlobalLandTemperaturesByMajorCity.csv")
    assert get_hotest_city(df, 1980) == "Baghdad"
    assert get_hotest_city(df, 1981) == "Jaipur"
