from sqlite3 import connect

import pandas as pd

if __name__ == "__main__":

    query = """
        SELECT name, phone, COUNT(*), citystatezip
        FROM
            (SELECT C.name, C.phone, O.total, C.citystatezip,
                SUM(ROUND(OI.qty * OI.unit_price, 2)) AS expected_price,
                SUM(ROUND(OI.qty * P.wholesale_cost, 2)) AS break_even_price
            FROM orders AS O
            LEFT JOIN customers AS C
            ON (O.customerid = C.customerid)
            INNER JOIN orders_items AS OI
            ON (OI.orderid = O.orderid)
            LEFT JOIN products AS P
            ON (OI.sku = P.sku)
            GROUP BY O.orderid)
        WHERE total < break_even_price
        GROUP BY name
        ORDER BY COUNT(*) DESC
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    print(df.iloc[:2][["name", "phone"]])