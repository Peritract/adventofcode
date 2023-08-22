from sqlite3 import connect

import pandas as pd



if __name__ == "__main__":

    query = """
        SELECT C.name, C.phone, COUNT(DISTINCT P.desc) AS unique_count
        FROM orders AS O
        LEFT JOIN customers AS C
        ON (O.customerid = C.customerid)
        INNER JOIN orders_items AS OI
        ON (OI.orderid = O.orderid)
        LEFT JOIN products AS P
        ON (OI.sku = P.sku)
        WHERE OI.qty = 1
        AND P.desc LIKE 'Noah''s %'
        GROUP BY C.name
        ORDER BY unique_count DESC;
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    print(df.iloc[0]["phone"])