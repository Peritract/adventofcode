from sqlite3 import connect

import pandas as pd

if __name__ == "__main__":

    query = """
        SELECT C.name, C.phone, C.citystatezip, COUNT(*)
        FROM orders AS O
        LEFT JOIN customers AS C
        ON (O.customerid = C.customerid)
        INNER JOIN orders_items AS OI
        ON (OI.orderid = O.orderid)
        LEFT JOIN products AS P
        ON (OI.sku = P.sku)
        WHERE C.name LIKE 'J% D%'
        AND (P.desc LIKE '%bagel%' OR P.desc LIKE 'Coffee%')
        GROUP BY C.customerid
        ORDER BY COUNT(*) DESC
        LIMIT 1;
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    print(df.iloc[0][["phone", "citystatezip"]])