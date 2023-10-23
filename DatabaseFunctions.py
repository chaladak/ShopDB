import pyodbc
import Connection

def AddRecordToTable():
    cursor = Connection.conn.cursor()

    try:
        cursor.execute(f'''INSERT INTO Products (name, price) VALUES ('ananas', 1.3)''')
        Connection.conn.commit()
        print("Rekord został dodany do bazy danych.")
    except Exception as e:
        print(f"Błąd podczas dodawania rekordu")

    Connection.ConnectionClose()
