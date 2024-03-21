from sqlite3 import connect

import pandas as pd

if __name__ == "__main__":

    query = """
        SELECT C.name, C.phone
        FROM orders AS O
        LEFT JOIN customers AS C
        ON (O.customerid = C.customerid)
        INNER JOIN orders_items AS OI
        ON (OI.orderid = O.orderid)
        LEFT JOIN products AS P
        ON (OI.sku = P.sku)
        WHERE C.name LIKE 'J% P%'
        AND (P.desc LIKE '%bagel%' OR P.desc LIKE '%coffee%')
        AND STRFTIME('%Y', O.shipped) = '2017'
        GROUP BY C.customerid, O.orderid
        HAVING COUNT(*) >= 2
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    print(df)
