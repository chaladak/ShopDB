import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};''SERVER=THINKPAD-ALA;''DATABASE=ShopDB;''Trusted_Connection=yes;')

def ConnectionToDatabase():
    try:
        cursor = conn.cursor()
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Błąd połączenia z bazą danych: {sqlstate}")

def ConnectionClose():
    print("Zakończono połaczenie z bazą!")
    conn.close()

