import pyodbc
import pandas as pd
import Connection
import warnings


class Product:
    def __init__(self, name, price):
            self.name = name
            self.price = price

    def add_product(self):
        cursor = Connection.conn.cursor()
        try:
            cursor.execute(f"INSERT INTO Products (name, price) VALUES ('{self.name}', '{self.price}')")
            Connection.conn.commit()
            print("\nRekord został dodany do bazy danych.")
        except Exception as e:
            print(f"\nBlad podczas dodawania rekordu: {e}")
    
    def delete_product(self):
         cursor = Connection.conn.cursor()
         try:
              cursor.execute(f"DELETE FROM Products WHERE name LIKE '{self.name}'")
              Connection.conn.commit()
              print("\nUsuneto rekordy z bazy danych!")
         except Exception as e:
            print(f"\nBlad podczas usuwania rekordow: {e}")

    def update_product_price(self,price):
        cursor = Connection.conn.cursor()
        try:
            cursor.execute(f"UPDATE Products SET price = '{price}' WHERE name LIKE '{self.name}'")
            Connection.conn.commit()
            print("\nZaktualizowano rekordy!")
        except Exception as e:
            print(f"\nBlad podczas akrualizowania rekordow: {e}")
    
    def update_product_name(self,name):
        cursor = Connection.conn.cursor()
        try:
            cursor.execute(f"UPDATE Products SET name = '{name}' WHERE name LIKE '{self.name}'")
            Connection.conn.commit()
            print("\nZaktualizowano rekordy!")
        except Exception as e:
            print(f"\nBlad podczas akrualizowania rekordow: {e}")

class System:
    @staticmethod
    def display_products():
        warnings.filterwarnings("ignore", category=UserWarning)
        cursor = Connection.conn.cursor()
        sql_query = 'SELECT * FROM Products'                        
        df = pd.read_sql(sql_query, Connection.conn)                
        print(df)

    @staticmethod
    def close_connection():
        Connection.conn.close()