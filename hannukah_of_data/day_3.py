from sqlite3 import connect

import pandas as pd

if __name__ == "__main__":

    query = """
        SELECT *
        FROM customers;
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    df["birthdate"] = pd.to_datetime(df["birthdate"])

    df = df[df["birthdate"].dt.year.isin([1934, 1946, 1958, 1970, 1982, 1994])] # Year of the dog

    df = df[((df["birthdate"].dt.month == 3) & (df["birthdate"].dt.day >= 21))
            | ((df["birthdate"].dt.month == 4) & (df["birthdate"].dt.day <= 19))] # Aries
    
    df = df[df["citystatezip"] == "South Ozone Park, NY 11420"] # Same neighbourhood as #2

    print(df["phone"].iloc[0])