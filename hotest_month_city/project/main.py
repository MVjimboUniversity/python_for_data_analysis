import argparse

from .df import get_df, get_hotest_city, get_hotest_month


def get_args() -> tuple[str, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("year")
    namespace = parser.parse_args()
    return namespace.filename, int(namespace.year)


def main():
    filename, year = get_args()
    df = get_df(filename)
    month = get_hotest_month(df, year)
    city = get_hotest_city(df, year)
    print(f"""Hotest month in {year} year was {month}.\n
          Hotest city in {year} year was {city}.""")


if __name__ == "__main__":
    main()
