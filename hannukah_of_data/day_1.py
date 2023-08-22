from sqlite3 import connect

import pandas as pd



def name_to_num(name: str) -> str:
    digits = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    num = ""
    for c in name:
        for i in range(len(digits)):
            if c.lower() in digits[i]:
                num += str(i + 2)
    return num


if __name__ == "__main__":

    query = """
        SELECT name, phone
        FROM customers;
    """

    con = connect("./data/noahs.sqlite")

    df = pd.read_sql(query, con)

    df["surname"] = df["name"].str.split(" ").str[1]

    df["translated_name"] = df["surname"].apply(name_to_num)

    df = df[df["phone"].str.replace("-", "") == df["translated_name"]]

    print(df.iloc[0]["phone"])