import pandas as pd

from project.df import get_df


def test_get_df_check_type():
    assert type(get_df("GlobalLandTemperaturesByMajorCity.csv")) == pd.DataFrame


def test_get_df_shape():
    df = get_df("GlobalLandTemperaturesByMajorCity.csv")
    assert df.shape == (239177, 7)
