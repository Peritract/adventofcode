from sqlite3 import connect

import pandas as pd

def find_potential_matches(row, df, possibles):
    matches = df[(df["colour"] != row["colour"]) & (df["desc"] == row["desc"])
                 & (df["shipped"] == row["shipped"])
                 & (df["hour"] == row["hour"])]
    possibles.append(matches)

if __name__ == "__main__":

    query = """
        SELECT O.orderid, C.name, C.phone, P.desc, shipped
        FROM orders AS O
        LEFT JOIN customers AS C
        ON (O.customerid = C.customerid)
        INNER JOIN orders_items AS OI
        ON (OI.orderid = O.orderid)
        LEFT JOIN products AS P
        ON (OI.sku = P.sku)
        WHERE OI.qty = 1
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    df["colour"] = df["desc"].str.extract("\((\w+)\)")
    df["desc"] = df["desc"].str.replace("\s\(\w+\)", "", regex=True)
    df["shipped"] = pd.to_datetime(df["shipped"])
    df["hour"] = df["shipped"].dt.hour
    df["shipped"] = df["shipped"].dt.date

    colour_list = list(df["colour"].dropna().unique())

    df = df.dropna(subset=["colour"])

    emily_products = df[df["name"] == "Emily Randolph"]

    not_emily = df[df["name"] != "Emily Randolph"]

    possibles = []

    emily_products.apply(find_potential_matches, args=(not_emily, possibles), axis=1)

    matches = pd.concat(possibles)

    print(matches[["name", "phone"]])