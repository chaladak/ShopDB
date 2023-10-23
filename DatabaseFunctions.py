import pyodbc
import pandas as pd
import Connection

cursor = Connection.conn.cursor()

def AddRecordToTable():
    try:
        cursor.execute(f'''INSERT INTO Products (name, price) VALUES ('ananas', 1.3)''')
        Connection.conn.commit()
        print("Rekord został dodany do bazy danych.")
    except Exception as e:
        print(f"Błąd podczas dodawania rekordu")


def DisplayTable():
    cursor = Connection.conn.cursor()
    sql_query = 'SELECT * FROM Products'                        #pobierasz sobie takim oto poleceniem wszystkie rekordy z tabeli Products
    df = pd.read_sql(sql_query, Connection.conn)                #tutaj ładujesz sobie do kontenera taką wbudowaną funkcją(read_sql) z biblioteki pandas i ci to tak jakby pakuje do tego kontenera ładnie ulożone    print(df) #
    print(df)                                                   #tutaj drukuje kontener
    Connection.ConnectionClose()                               