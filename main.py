from ClassDefinitions import Product
from ClassDefinitions import System
import ClassDefinitions
import os                               #wykorzystalam do czyszczenia ekranu
import msvcrt                           #wykorzystalam do pobierania kodu znaku z klawiatury
import pandas as pd

warehouse = Product("",0)
sys = System()

def ChangeColorToPurple(text):
    print('\033[95m' + text + '\033[0m')

def ChangeColorToWhite(text):
    print('\033[0m'+ text + '\033[0m')

def addProduct():
    os.system('cls')
    print("------------------------------------------------------------------------------------")
    print("|                               DODAWANIE NOWEGO PRODUKTU                           |")
    print("------------------------------------------------------------------------------------")
    warehouse.name = input("\nWprowadz nazwe produktu: ")
    warehouse.price = input("Wprowadz cene produktu: ")
    warehouse.add_product()
    ChangeColorToPurple("\nWYJSCIE")
    msvcrt.getch()
    menu()

def deleteProduct():
    os.system('cls')
    print("------------------------------------------------------------------------------------")
    print("|                               USUWANIE PRODUKTU                                  |")
    print("------------------------------------------------------------------------------------")
    warehouse.name = input("\nWprowadz nazwe produktu ktory chcesz usunac: ")
    warehouse.delete_product()
    ChangeColorToPurple("\nWYJSCIE")
    msvcrt.getch()
    menu()

def updateProduct(): #ta funkcja jest do poprawy
    while(1):
        os.system('cls')
        print("------------------------------------------------------------------------------------")
        print("|                               MODYFIKACJA PRODUKTU                                |")
        print("------------------------------------------------------------------------------------")
        choice = 1
        warehouse.name = input("\nWprowadz nazwe produktu ktory chcesz zmodyfikowac: ")
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

        if (zn == b'\r') and (choice == 1):
            new_name = input("Wprowadz nowa nazwe produktu: ")
            warehouse.update_product_name(new_name)
        if (zn == b'\r') and (choice == 2):
            new_price = input("\nWprowadz nowa cene produktu: ")
            warehouse.update_product_price(new_price)
        
        ChangeColorToPurple("\nWYJSCIE")
        msvcrt.getch()
        menu()

def displayAllProducts():
    os.system('cls')
    print("------------------------------------------------------------------------------------")
    print("|                          WSZYTSKIE PRODUKTY W MAGAZYNIE                          |")
    print("------------------------------------------------------------------------------------")
    sys.display_products()
    ChangeColorToPurple("\nWYJSCIE")
    msvcrt.getch()
    menu()

def menu():
    zm = 1
    while(1):
        os.system('cls')
        
        print("------------------------------------------------------------------------------------")
        print("|                               SYSTEM OBSLUGI MAGAZYNU                            |")
        print("------------------------------------------------------------------------------------")
        if zm == 1:
            ChangeColorToPurple("\nDODAJ PRODUKT")
        else:
            ChangeColorToWhite("\nDODAJ PRODUKT")
        if zm==2:
            ChangeColorToPurple("MODYFIKUJ PRODUKT")
        else:
            ChangeColorToWhite("MODYFIKUJ PRODUKT")
        if zm==3:
            ChangeColorToPurple("USUN PRODUKT")
        else:
            ChangeColorToWhite("USUN PRODUKT")
        if zm==4:
            ChangeColorToPurple("WYSWIETL WSZYTSKIE PRODUKTY")
        else:
            ChangeColorToWhite("WYSWIETL WSZYTSKIE PRODUKTY")
        if zm==5:
            ChangeColorToPurple("FILTRUJ PRODUKTY")
        else:
            ChangeColorToWhite("FILTRUJ PRODUKTY")
        if zm==6:
            ChangeColorToPurple("WYJSCIE")
        else:
            ChangeColorToWhite("WYJSCIE")

        znakAscii = msvcrt.getch()
        
        if znakAscii == b'H':
            zm -= 1
        if znakAscii == b'P':
            zm += 1
        if zm == 7:
            zm = 1

        
        if (znakAscii == b'\r') and (zm == 6):
            os.system("cls" if os.name == "nt" else "clear")
            exit(1)

        if (znakAscii == b'\r') and (zm == 1):
            addProduct()

        if (znakAscii == b'\r') and (zm == 3):
            deleteProduct()
        
        if (znakAscii == b'\r') and (zm == 4):
            displayAllProducts()
        
        if (znakAscii == b'\r') and (zm == 2):
            updateProduct()

menu()

