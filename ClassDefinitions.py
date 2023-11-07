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

#główna funkcja menu
def menu():
    object = Product("",0) #tworze przykładowy obiekt na rzecz którego bedę wywoływać metody (funkcje w klasie)
    
    zm = 1 #zmienna obslugujaca przeskakiwanie
    while(1): #petla nieskonczona, warunek zawsze jest spelniony, dlatego za kazym razem jak wcisniesz coś to program bedzie aktualizowal sie
        os.system('cls') #czyszcze ekranpo kliknieciu każdego znaku
        
        print("------------------------------------------------------------------------------------")
        print("|                               SYSTEM OBSLUGI MAGAZYNU                            |")
        print("------------------------------------------------------------------------------------")
        if zm == 1:
            ChangeColorToPurple("\nDODAJ PRODUKT")#jesli zmiana jest rowna 1 czyli wybrano pozycje 1 to zmien kolor 
        else:
            ChangeColorToWhite("\nDODAJ PRODUKT")#jak nie to wypisz ten tekst normalnie w kolorze bialym
        if zm==2:
            ChangeColorToPurple("MODYFIKUJ PRODUKT")
        else:
            ChangeColorToWhite("MODYFIKUJ PRODUKT")
        if zm==3:
            ChangeColorToPurple("USUN PRODUKT")
        else:
            ChangeColorToWhite("USUN PRODUKT")
        if zm==4:
            ChangeColorToPurple("FILTROWANIE PRODUKTOW")
        else:
            ChangeColorToWhite("FILTROWANIE PRODUKTOW")
        if zm==5:
            ChangeColorToPurple("WYSWIETL WSZYTSKIE PRODUKTY")
        else:
            ChangeColorToWhite("WYSWIETL WSZYTSKIE PRODUKTY")
        if zm==6:
            ChangeColorToPurple("WYJSCIE")
        else:
            ChangeColorToWhite("WYJSCIE")

        znak = msvcrt.getch() #ta sunkcja zwraca kod znaku, ktory jest wcisniety
        
        if znak == b'H': #jesli znak to strzalka w gore to idziemy ze zmianą w góre
            zm -= 1
        if znak == b'P': #jesli strzalka w dol to zmiekszamy zmienna i idziemy na dól
            zm += 1
        if zm == 7: #jak dojdziemy do końca bo mamy 7 pozycji to wracamy na początek czyli ustawiomy zmiane na 1 i lecimy dalej
            zm = 1

        
        if (znak == b'\r') and (zm == 6): #jesli znak to enter (b'\r' - taki ma kod) i zmiana jest 6 to wylazimy z programu
            os.system("cls" if os.name == "nt" else "clear")
            close_connection() #zamykam polaczenie z baza
            exit(1) #koniec programu

        if (znak == b'\r') and (zm == 1): #jak jest enter i zmiana to 1 czyli wybrano 1 pozycje to idzie do classdefinitions do funkcji add_product
            object.add_product()

        if (znak == b'\r') and (zm == 3): #tu tak samo i niżej tez
            object.update_product()
        
        if (znak == b'\r') and (zm == 4):
            filter_products()
        
        if (znak == b'\r') and (zm == 2):
            object.update_product()
        
        if (znak == b'\r') and (zm == 5):
            sort_products()



###############################################################################################################


class Product:
    def __init__(self, name, price): 
            #konstruktor wieloargumentowy czyli jak sobie tworzysz obiekt typu obiekt(kalafior,12)
            #do tego obiektu obiekt.nazwa, obiekt.cena przypisuje sie to co przekazalas w nawiasie
            #self oznacza ze sie to przypisze do obiektu na ktorym to wywolujesz
            self.name = name
            self.price = price

    def add_product(self):
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
            cursor.execute(f"INSERT INTO Products (name, price) VALUES ('{self.name}', '{self.price}')") 
            #cursor jest z pliku connection i on pozwala wykonywać coś w tej bazie czyli on tak jakby trzyma wszytskie dane o tym polączeniu
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
    def delete_product(self):
        os.system('cls')
        print("------------------------------------------------------------------------------------")
        print("|                               USUWANIE PRODUKTU                                  |")
        print("------------------------------------------------------------------------------------")
        self.name = input("\nWprowadz nazwe produktu ktory chcesz usunac: ")
        
        cursor = Connection.conn.cursor()
        try:
            cursor.execute(f"DELETE FROM Products WHERE name LIKE '{self.name}'")
            Connection.conn.commit()
            print("\nUsuneto rekordy z bazy danych!")
        except Exception as e:
            print(f"\nBlad podczas usuwania rekordow: {e}")
        ChangeColorToPurple("\nWYJSCIE")
        msvcrt.getch()
        menu()


        #tu jest troche wiecej zabawy bo jak wchodzisz do trybu aktualizowania to mozesz wybrac co chcesz zaktualizowac czyli masz tak jakby drugie menu
        #ktore dziala tak samo tylko zamiast zm jest choice zeby zmienne sie nie dublowały
    def update_product(self):
        choice = 1
        while(1):
            os.system('cls')
            print("------------------------------------------------------------------------------------")
            print("|                               MODYFIKACJA PRODUKTU                                |")
            print("------------------------------------------------------------------------------------")
            
            self.name = input("\nWprowadz nazwe produktu ktory chcesz zmodyfikowac: ")
            if choice == 1:
                ChangeColorToPurple("\nZMIEN NAZWE")
            else:
                ChangeColorToWhite("\nZMIEN NAZWE")
            if choice == 2:
                ChangeColorToPurple("ZMIEN CENE")
            else:
                ChangeColorToWhite("ZMIEN CENE")

            zn = msvcrt.getch()
            
            if zn == b'H':
                choice -= 1
            if zn == b'P':
                choice += 1
            if choice == 3:
                choice = 1

            #jesli wybrałes 1 i enter jest wzisniety to przechodzisz jakby do zmieniania nazwy
            if (zn == b'\r') and (choice == 1):
                new_name = input("Wprowadz nowa nazwe produktu: ")
                cursor = Connection.conn.cursor()
                try:
                    cursor.execute(f"UPDATE Products SET name = '{new_name}' WHERE name LIKE '{self.name}'")
                    #tym zapytaniem aktualizujesz wszytsko w tabeli Products co ma nazwe self.name czyli nazwe tego oiektu na ktorym
                    #wywolujesz i wprowadzasz nowa nazwe ktarą wpisalaś na klawiaturze
                    Connection.conn.commit()#wysylanie do bazy danych zapytania
                    print("\nZaktualizowano rekordy!")#jak sie uda to ci mowi ze jest git a jak nie to ze blad, tak samo jest z aktualizacja ceny
                except Exception as e:
                    print(f"\nBlad podczas aktualizowania rekordow: {e}")
                
            if (zn == b'\r') and (choice == 2):
                new_price = input("\nWprowadz nowa cene produktu: ")
                cursor = Connection.conn.cursor()
                try:
                    cursor.execute(f"UPDATE Products SET price = '{new_price}' WHERE name LIKE '{self.name}'")
                    Connection.conn.commit()
                    print("\nZaktualizowano rekordy!")
                except Exception as e:
                    print(f"\nBlad podczas aktualizowania rekordow: {e}")

            ChangeColorToPurple("\nWYJSCIE")
            msvcrt.getch()
            menu()
        
#tu sie konczą funkcje ktore bedziemy wywolywac na rzecz jednego obiektu czyli dodawanie, ususwnaie, 
# modyfikacja itp bo teraz bedziemy wyswietlac wszytskie produkty, albo jakas ich czesc w każdym razie nie jakis jeden konkretny
def sort_products():
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
            ChangeColorToPurple("\nNAZWA (Z-A)")
        else:
            ChangeColorToWhite("\nNAZWA (Z-A)")
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
            #wszedzie to wyglada tak samo tylko rożnią sie zapytania
            query = 'SELECT * FROM Products ORDER BY name ASC'
            display_all_product_by_query(query)
            
        if (zn == b'\r') and (choice == 2):
            query = 'SELECT * FROM Products ORDER BY name DESC'
            display_all_product_by_query(query)
        
        if (zn == b'\r') and (choice == 3):
            query = 'SELECT * FROM Products ORDER BY price ASC'
            display_all_product_by_query(query)
        
        if (zn == b'\r') and (choice == 4):
            query = 'SELECT * FROM Products ORDER BY price DESC'
            display_all_product_by_query(query)


#funkcja do wyswietlania produktów które zostały wybrane zaputaniem(query) którebędzie różne, jest używana przy sortowniu i przy filtrowaniu
#za kazdym razem dziala tak samo tylko ze zmienia sie zapytanie wiec zmieniaja sie dane wyswietlane
#dodałam to żeby za kazdym razem nie powtarzac tego bo sie kod robi na pół kilometra
def display_all_product_by_query(query):
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


def filter_products():
    os.system('cls')
    print("------------------------------------------------------------------------------------")
    print("|                         FILTROWANIE PRODUKTOW PO CENIE                            |")
    print("------------------------------------------------------------------------------------")
    price_min = input("\nWprowadz poczatek przedzialu cenowego: ")
    price_max = input("\nWprowadz koniec przedzialu cenowego: ")
    query = f"SELECT * FROM Products WHERE price BETWEEN '{price_min}' and '{price_max}' ORDER BY price ASC"
    display_all_product_by_query(query)


#zamykanie polaczenia z baza
def close_connection():
    Connection.conn.close()