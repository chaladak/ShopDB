import pyodbc #do polaczenia z baza danych

#tu jest laczenie do bazy danych ktora jest postawiona na moim kompie
conn = pyodbc.connect('DRIVER={SQL Server};''SERVER=THINKPAD-ALA;''DATABASE=ShopDB;''Trusted_Connection=yes;')


def ConnectionToDatabase():
    try:
        cursor = conn.cursor()#ten cursor potem wykorzystuje sie w class definitions do wykonywania poleceń w bazie
    except pyodbc.Error as ex:#to jest mechanizm wylapywania bledow, powiedz ze z neta, jak wystapi blad polaczenia to pisze ze nie udalo sie
        sqlstate = ex.args[0]
        print(f"Błąd połączenia z bazą danych: {sqlstate}")

def ConnectionClose():#zamykanie polaczenia z bazą zawsze po wykonaniu polecenie
    print("Zakończono połaczenie z bazą!")
    conn.close()

