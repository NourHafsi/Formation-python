import mysql.connector
#conncting to the data base
CONN= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db"
)

#cursor: il va cherchr ligne par ligne et apres runner(excuter) le code MySQL
CURS= CONN.cursor()
""" CURS.execute("SHOW DATABASES")
for i in CURS:
    print(i) """

CURS.execute("create table users (id int primary key, nom varchar(255), prenom varchar(255), email varchar(255))")
print("table created successfully")


CURS.close()
CONN.close()