import os                            #do czyszczenia ekranu
import msvcrt                       #do pobierania znaku z klawiatury
import ClassDefinitions

#główna funkcja menu
def menu():
    object = ClassDefinitions.Product("",0) 
    #to classDefinitions. oznacza ze ciągne ten Product z innego pliku Class definitions, 
    #tworze przykładowy obiekt na rzecz którego bedę wywoływać metody (funkcje w klasie), "" oznacza ze nazwa domyslnie jest pusta
    #0 oznacza ze cena domyslnie po utworzeniu to 0, przewiń sobie do definicji placy Product i tam w pierwszych liniach masz _init_ coś tam
    #za pomocą tego konstruktora możesz sobie tworzyć obiekt z wartościami podanymi w nawiasie
    
    zm = 1 #zmienna obslugujaca przeskakiwanie
    while(1): #petla nieskonczona, warunek zawsze jest spelniony, dlatego za kazym razem jak wcisniesz coś to program bedzie aktualizowal sie
        os.system('cls') #czyszcze ekran za kazdym razem po kliknieciu jakiego znaku
        
        print("------------------------------------------------------------------------------------")
        print("|                               SYSTEM OBSLUGI MAGAZYNU                            |")
        print("------------------------------------------------------------------------------------")
        if zm == 1: #to ClassDefinitions.costam oznacza ze w tym pliku nie ma tej funkcji ale ona jest w pliku classdefinitions, tak to bylaby nierozpoznana
            ClassDefinitions.ChangeColorToPurple("\nDODAJ PRODUKT")#jesli zmiana jest rowna 1 czyli wybrano pozycje 1 to zmien kolor 
        else:
            ClassDefinitions.ChangeColorToWhite("\nDODAJ PRODUKT")#jak nie to wypisz ten tekst normalnie w kolorze bialym
        if zm==2:
            ClassDefinitions.ChangeColorToPurple("MODYFIKUJ PRODUKT")
        else:
            ClassDefinitions.ChangeColorToWhite("MODYFIKUJ PRODUKT")
        if zm==3:
            ClassDefinitions.ChangeColorToPurple("USUN PRODUKT")
        else:
            ClassDefinitions.ChangeColorToWhite("USUN PRODUKT")
        if zm==4:
            ClassDefinitions.ChangeColorToPurple("FILTROWANIE PRODUKTOW")
        else:
            ClassDefinitions.ChangeColorToWhite("FILTROWANIE PRODUKTOW")
        if zm==5:
            ClassDefinitions.ChangeColorToPurple("WYSWIETL WSZYTSKIE PRODUKTY")
        else:
            ClassDefinitions.ChangeColorToWhite("WYSWIETL WSZYTSKIE PRODUKTY")
        if zm==6:
            ClassDefinitions.ChangeColorToPurple("WYJSCIE")
        else:
            ClassDefinitions.ChangeColorToWhite("WYJSCIE")

        znak = msvcrt.getch() #ta sunkcja zwraca kod znaku, ktory jest wcisniety
        
        if znak == b'H': #jesli znak to strzalka w gore to idziemy ze zmianą w góre
            zm -= 1
        if znak == b'P': #jesli strzalka w dol to zmiekszamy zmienna i idziemy na dól
            zm += 1
        if zm == 7: #jak dojdziemy do końca bo mamy 7 pozycji to wracamy na początek czyli ustawiomy zmiane na 1 i lecimy dalej
            zm = 1

        
        if (znak == b'\r') and (zm == 6): #jesli znak to enter (b'\r' - taki ma kod) i zmiana jest 6 to wylazimy z programu
            os.system("cls" if os.name == "nt" else "clear")
            ClassDefinitions.close_connection() #zamykam polaczenie z baza
            exit(1) #koniec programu
        #wszedzie w nawiasie dodaje menu bo w tych funkcjach bede wracac spowrotem do menu
        #te funkcje są w innym pliku i one nie widza tej funkcji menu ale jak podasz im w nawiasie to juz bedą widzieć
        #tutaj nie moglam sobie zrobić import bo importowałam do tego pliku ClassDefinitions a jesli chce użyc tego menu w class definitions
        #to musiałabym zaimportowac do niego menu a tak nie moża
        #python nie pozwala zeby jeedn plik importował sie do drugiego, a drugi do pierwszego => tak unikamy importowania cyklicznego
        if (znak == b'\r') and (zm == 1): #jak jest enter i zmiana to 1 czyli wybrano 1 pozycje to idzie do classdefinitions do funkcji add_product
            object.add_product(menu)

        if (znak == b'\r') and (zm == 3): #tu tak samo i niżej tez
            object.delete_product(menu)
        
        if (znak == b'\r') and (zm == 4):
            ClassDefinitions.filter_products(menu)#to takie info ze ciagne sobie funcje filter z pliku ClassDefinitions
        
        if (znak == b'\r') and (zm == 2):
            object.update_product(menu)
        
        if (znak == b'\r') and (zm == 5):
            ClassDefinitions.sort_products(menu)#tu sobie ciagne funkcje tez z innego pliku

menu() #tu sie wykonuje caly kod programu bo odpala sie funkcja menu, najwazniejsze miejsce