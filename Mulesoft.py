import sqlite3
import pandas as pd

my_favorite=[["Inception","DiCaprio","Marion",2010,"Nolan"],
            ["Interstellar","McConaughey","Jessica",2014,"Nolan"],
            ["The Prestige","Bale","Scarlett",2006,"Nolan"],
            ["Iron man","Robert Downey jr","Paltrow",2008,"Favreau"],
            ["Dhrisyam","Mohanlal","Meena",2013,"Jithu"]]

# create database or connect if its exist
def create_database(name):
    try:
        connection = sqlite3.connect(name)
        return connection
    except Exception as e:
        print("connection error"+e)

# create table Movies 
def create_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS Movies (Name TEXT,Actor TEXT,Actress TEXT,Released INT,Director TEXT)")

def insert_values(conn):
    with conn:
        for i in my_favorite:
            conn.execute("INSERT INTO Movies values(?,?,?,?,?)",(i[0],i[1],i[2],i[3],i[4]))

# print values in table
def display(conn):
    data=pd.read_sql_query("SELECT * FROM Movies", conn)
    if data.empty:
        print("Table is empty")
    else:
        print(data)

def main():
    conn = create_database("MovieDB.db")
    cursor = conn.cursor()
    create_table(cursor)
    insert_values(conn)
    display(conn)
    cursor.close()
    conn.close()

if __name__=="__main__":main()