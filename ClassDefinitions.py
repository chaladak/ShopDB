import pyodbc                        #do obslugi bazy danych
import pandas                         #do drukowania w przejrzysty sposob tabeli z danymi
import Connection                    #plik w ktorym są wynkcje ktore wykorzystuje do łączenia z bazą danych
import warnings                      #użyłam aby wyłączyć ostrzeżenia spowodowane tym ze używam pandas z SQL managment studio co nie jest preferowane
import os                            #do czyszczenia ekranu
import msvcrt                       #do pobierania znaku z klawiatury


#zmiana koloru czcionki
def ChangeColorToPurple(text):
    print('\033[95m' + text + '\033[0m')

def ChangeColorToWhite(text):
    print('\033[0m'+ text + '\033[0m')

class Product:
    def __init__(self, name, price): 
            #konstruktor wieloargumentowy czyli jak sobie tworzysz obiekt typu obiekt(kalafior,12)
            #do tego obiektu obiekt.nazwa, obiekt.cena przypisuje sie to co przekazalas w nawiasie
            #self oznacza ze sie to przypisze do obiektu na ktorym to wywolujesz
            self.name = name
            self.price = price

    def add_product(self,menu):
        #tu tak samo, to sie wykona na produkcie na ktorym to wywolujesz 
        #czyli jak wywolalas object.add-product to sie tak jakby dane tego object zaktualizuja
        os.system('cls')
        print("------------------------------------------------------------------------------------")
        print("|                               DODAWANIE NOWEGO PRODUKTU                           |")
        print("------------------------------------------------------------------------------------")
        self.name = input("\nWprowadz nazwe produktu: ")
        self.price = input("Wprowadz cene produktu: ") #do zmiennych wprowadzasz z klawiatury nazwe i cene
        
        cursor = Connection.conn.cursor()
        try:
            #tu bede sprawdzac czy przypadkiem nie ma juz produktu o takiejsamej nazwie juz
            #pierwsze wybieram sobie z bazy i ładuje do cursora wszytskie elementy ktore mają taką sama nazwe jak wpisałam z klawiatury
            cursor.execute(f"SELECT * FROM Products WHERE name LIKE '{self.name}'")#cursr ma teraz w sobie to co wybierze zapytanie
            wiersze = cursor.fetchall()  
            #teraz dziele cobie zapytanie na wierszee pojedyncze bo normalnie to taki ciąg znaków
            #jeżeli dlugosc (rozmiar) tego wyniku jest = 0, to znaczy ze zapytanie nic nie wybralo to znaczy ze nie ma takiego produktu
            if len(wiersze) != 0:
                print("\nW bazie istnieje już produkt o takiej nazwie. ")
            else:
                #jeżeli nie ma takiego produktu to możesz dodac do bazy a jak jest to wyswietl komunikat i wyjscie
                cursor.execute(f"INSERT INTO Products (name, price) VALUES ('{self.name}', '{self.price}')")
                #cursor jest z pliku connection i to taki jakby kontener na dane, on pozwala wykonywać coś w tej bazie czyli on tak jakby trzyma wszytskie dane o tym polączeniu
                # i np pozwala ci czytac cos z bazy, pobierac jakies wyniki
                #kwerenda z SQL czyli bezposrednio do bazy to leci i to sie w niej wykonuje bo baza ma swoj specjalny jezyk
                #do tabeli Products w kolumne name proce dodaj wartosci nazwa i cena ktore sa wprowadzone z klawiatury
                Connection.conn.commit()
                print("\nRekord został dodany do bazy danych.")
        except Exception as e:
            print(f"\nBlad podczas dodawania rekordu: {e}")#jak system wykryje blad i sie nie doda poprawnie to wywala bląd
    
        ChangeColorToPurple("\nWYJSCIE")#ustawiasz kolor wyjscia na fioletowy zeby bylo ladnie
        #jak wcisniesz jakikolwiek znak to przezuci cie do menu
        msvcrt.getch()
        menu()


    #tu jest prawie to samo
    def delete_product(self,menu):
        os.system('cls')
        print("------------------------------------------------------------------------------------")
        print("|                               USUWANIE PRODUKTU                                  |")
        print("------------------------------------------------------------------------------------")
        self.name = input("\nWprowadz nazwe produktu ktory chcesz usunac: ")
        
        cursor = Connection.conn.cursor()
        try:
            #tu znowu sprawdzam czy wgl taki produkt co wpisalam istnieje w bazie
            #posluguje sie prawie takim samym zapytaniem jak wczesniej, w sensie ze wybieram sobie z bazy produkty o takiej nazwie
            #jezeli zapytanie zwroci 0  wynikow to znaczy ze nie ma takiego produktu i siema
            cursor.execute(f"SELECT * FROM Products WHERE name LIKE '{self.name}'")
            wiersze = cursor.fetchall()  
            
            if len(wiersze) == 0:
                print("\nW bazie nie istnieje produkt o takiej nazwie. ")
            else:
                #jesli istnieje to usun go takim zapytaniem z DELETE
                cursor.execute(f"DELETE FROM Products WHERE name LIKE '{self.name}'")
                Connection.conn.commit()
                print("\nUsuneto rekordy z bazy danych!")
        except Exception as e:
            print(f"\nBlad podczas usuwania rekordow: {e}")
       
        ChangeColorToPurple("\nWYJSCIE")
        msvcrt.getch()
        menu()


    def update_product(self, menu):
        os.system('cls')
        print("------------------------------------------------------------------------------------")
        print("|                               MODYFIKACJA CENY PRODUKTU                           |")
        print("------------------------------------------------------------------------------------")
        #wprowadzam nazwe produktu ktory chce zmodyfikowac
        self.name = input("\nWprowadz nazwe produktu ktory chcesz zmodyfikowac: ")
        
        #tu sprawdzam tak jak wczesiej czy taki produkt wgl jest w bazie 
        cursor = Connection.conn.cursor()
        cursor.execute(f"SELECT * FROM Products WHERE name LIKE '{self.name}'")
        wiersze = cursor.fetchall()  
        
        if len(wiersze) == 0:
            print("\nW bazie nie istnieje produkt o takiej nazwie. ")
            ChangeColorToPurple("\nWYJSCIE")
            msvcrt.getch()
            menu()
        else:
            #jesli istnieje to sobie robie modyfikacje ceny
            new_price = input("\nWprowadz nowa cene produktu: ")
            try:
                cursor.execute(f"UPDATE Products SET price = '{new_price}' WHERE name LIKE '{self.name}'")
                Connection.conn.commit()
                print("\nZaktualizowano rekordy!")
                ChangeColorToPurple("\nWYJSCIE")
                msvcrt.getch()
                menu()
            except Exception as e:
                print(f"\nBlad podczas aktualizowania rekordow {e}")
        
#tu sie konczą funkcje ktore bedziemy wywolywac na rzecz jednego obiektu czyli dodawanie, ususwnaie, 
# modyfikacja itp bo teraz bedziemy wyswietlac wszytskie produkty, albo jakas ich czesc w każdym razie nie jakis jeden konkretny
#dlatego nie bedzie przy wywolywaniu w Pliku Menu.py tego object. przed funkcja
def sort_products(menu):
    choice = 1
    while(1):
        os.system('cls')
        print("------------------------------------------------------------------------------------")
        print("|                               LISTA PRODUKTOW                                    |")
        print("------------------------------------------------------------------------------------") 
        print("\nWybierz kryterium sortowania:")
        if choice == 1:
            ChangeColorToPurple("\nNAZWA (A-Z)")
        else:
            ChangeColorToWhite("\nNAZWA (A-Z)")
        if choice == 2:
            ChangeColorToPurple("NAZWA (Z-A)")
        else:
            ChangeColorToWhite("NAZWA (Z-A)")
        if choice == 3:
            ChangeColorToPurple("CENA ROSNACO")
        else:
            ChangeColorToWhite("CENA ROSNACO")
        if choice == 4:
            ChangeColorToPurple("CENA MALEJACO")
        else:
            ChangeColorToWhite("CENA MALEJACO")

        zn = msvcrt.getch()
        
        if zn == b'H':
            choice -= 1
        if zn == b'P':
            choice += 1
        if choice == 5:
            choice = 1

        #jesli wybrałes 1 i enter jest wzisniety to przechodzisz jakby do zmieniania nazwy
        if (zn == b'\r') and (choice == 1): 
            #jeżeli wybór to 1 i nacisnieto enter to przypisuje zapytanie i leci z nim do funkcja która wyswietli jego wyniki (NIZEJ)
            #to jest polecenie bezposrednio do wrzucenia do bazy danych
            #tutaj zamiast wyswietlac wszytsko robie ppunkcje ktora wyswietla wszytskie produkty które wybierze zapytanie
            #wszedzie to wyglada tak samo tylko rożnią sie zapytaniaa
            query = 'SELECT * FROM Products ORDER BY name ASC'
            display_all_product_by_query(query,menu)
            
        if (zn == b'\r') and (choice == 2):
            query = 'SELECT * FROM Products ORDER BY name DESC'
            display_all_product_by_query(query,menu)
        
        if (zn == b'\r') and (choice == 3):
            query = 'SELECT * FROM Products ORDER BY price ASC'
            display_all_product_by_query(query,menu)
        
        if (zn == b'\r') and (choice == 4):
            query = 'SELECT * FROM Products ORDER BY price DESC'
            display_all_product_by_query(query,menu)


#funkcja do wyswietlania produktów które zostały wybrane zaputaniem(query) którebędzie różne, jest używana przy sortowniu i przy filtrowaniu
#za kazdym razem dziala tak samo tylko ze zmienia sie zapytanie wiec zmieniaja sie dane wyswietlane
#dodałam to żeby za kazdym razem nie powtarzac tego bo sie kod robi na pół kilometra
def display_all_product_by_query(query,menu):
    os.system('cls')
    print("------------------------------------------------------------------------------------")
    print("|                          WSZYTSKIE PRODUKTY W MAGAZYNIE                          |")
    print("------------------------------------------------------------------------------------")
    warnings.filterwarnings("ignore", category=UserWarning) 
    cursor = Connection.conn.cursor()                
    df = pandas.read_sql(query, Connection.conn) 
    #tu jest wstawiane zapytanie i cale wyniki ktore wybiera z bazy danych są ładowane ładnie sformatowane przez pandasa do konternera tak jakby który nazywa sie df
    print(df) #tu frukujesz kontener
    ChangeColorToPurple("\nWYJSCIE")
    msvcrt.getch() #jak nacisniesz jakikolwiek znak to cie wywali do menu
    menu()


def filter_products(menu):
    os.system('cls')
    print("------------------------------------------------------------------------------------")
    print("|                         FILTROWANIE PRODUKTOW PO CENIE                            |")
    print("------------------------------------------------------------------------------------")
    price_min = input("\nWprowadz poczatek przedzialu cenowego: ")
    price_max = input("\nWprowadz koniec przedzialu cenowego: ")
    query = f"SELECT * FROM Products WHERE price BETWEEN '{price_min}' and '{price_max}' ORDER BY price ASC"
    display_all_product_by_query(query,menu)


#zamykanie polaczenia z baza
def close_connection():
    Connection.conn.close()