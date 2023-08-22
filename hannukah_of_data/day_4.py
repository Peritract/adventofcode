from sqlite3 import connect

import pandas as pd

if __name__ == "__main__":

    query = """
        SELECT C.name, C.phone, COUNT(*)
        FROM orders AS O
        LEFT JOIN customers AS C
        ON (O.customerid = C.customerid)
        INNER JOIN orders_items AS OI
        ON (OI.orderid = O.orderid)
        LEFT JOIN products AS P
        ON (OI.sku = P.sku)
        WHERE C.citystatezip LIKE '%NY%'
        AND P.sku LIKE 'BKY%'
        AND CAST(STRFTIME('%H', shipped) AS INT) < 5
        AND OI.qty > 1
        GROUP BY C.customerid
        ORDER BY COUNT(*) DESC;
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    print(df.iloc[0]["phone"])