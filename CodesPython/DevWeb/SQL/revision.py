import mysql.connector
# connecting to the database
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_revision"
)

# creating a cursor object to execute SQL queries
cursor=conn.cursor()

#verifying the connection by showing the databases
#cursor.execute("show databases")
#for i in cursor:
    #print(i)

#creating a table named 'utilisateurs' with columns 'id', 'name', 'email'
cursor.execute ("create table utilisateurs (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50), prenom VARCHAR(50), email VARCHAR(100), age INT)")
print ("table created successfully")

#inserting data into the 'utilisateurs' table
cursor.execute("insert into utilisateurs (nom, prenom, email, age) values ('Dupont', 'Jean', 'jean.dupont@example.com', 30)")
conn.commit() #committing the transaction to save changes to the database
print("data inserted successfully") 

#inserting data into the 'utilisateurs' table using the variables
n="galon"
p="Alice"
e="alice.galon@example.com"
a=25

cursor.execute("insert into utilisateurs (nom, prenom, email, age) values (%s,%s,%s,%s)", (n, p, e, a))
conn.commit()
print("data inserted successfully")
#-----------------------------------------------------------------------------------------------------------


#partie:selection des données 
#selecting all data (toutes les colonnes) from the 'utilisateurs' table and printing
cursor.execute ("select * from utilisateurs")
utilisateurs= cursor.fetchall() #fetching (=recuperer ou extraire) all results from the executed query
for utilisateur in utilisateurs:
    print(utilisateur)  

#selecting only the 'email' column from the 'utilisateurs' table and printing
cursor.execute("select email from utilisateurs")
emails=cursor.fetchall()
for email in emails:
    print (email)

#selecting a specific user by id and printing
cursor.execute("select * from utilisateurs where id=1")
utilisateurs=cursor.fetchone() #fetching only one row from the executed query
print(utilisateurs)
#selecting specific columns (name and email) for a user with a specific id and printing
cursor.execute("select nom, email from utilisateurs where id=2")
utilisateur=cursor.fetchone() #printing the selected user's name and email
print(utilisateur)

#selecting all users and printing their names and emails
cursor.execute("select nom, email from utilisateurs")
utilisateurs= cursor.fetchall()
for utilisateur in utilisateurs:
    print(utilisateur)
#-----------------------------------------------------------------------------------------------------------------   

#partie: mise à jour des données
#updating the nom and prenom of a user with a specific  id and committing the changes
cursor.execute("update utilisateurs set nom='giraffe', prenom='Alice' where id=2")
conn.commit() #committing the to save changes to the database
#selecting the updated user's nom and email to verify the update
cursor.execute("select nom , email from utilisateurs where id=2")
utilisateur=cursor.fetchone()
print(utilisateur)

#deleting a user with a specific id and committing the changes
cursor.execute("delete from utilisateurs where id=2")
conn.commit () #committing the transaction to save changes to the database
#selecting the deleted user to verify the deletion (should return None)
cursor.execute("select nom, email from utilisateurs where id=2")
utilisateur=cursor.fetchone()
print(utilisateur) #should print None since the user has been deleted   
#-----------------------------------------------------------------------------------------------------------------



#partie: modification de la structure de la table
#update a table:
#adding a new column 'job' to the 'utilisateurs' table and committing the changes
cursor.execute("alter table utilisateurs add column job VARCHAR(50)")
conn.commit() #committing the transaction to save changes to the database

#delete a column:
#dropping the 'job' column from the 'utilisateurs' table and committing the changes
cursor.execute("alter table utilisateurs drop column job")
conn.commit() #committing the transaction to save changes to the database

#rename a column:
#renaming the 'nom' column to 'name' in the 'utilisateurs' table
cursor.execute("alter table utilisateurs change nom name VARCHAR(50)")
conn.commit() #committing the transaction to save changes to the database

#rename a table:
#renaming the 'utilisateurs' table to 'users' and committing the changes

cursor.execute("alter table utilisateurs rename to users")
conn.commit() #committing the transaction to save changes to the database

#drop a table:
#dropping the 'users' table and committing the changes
cursor.execute("drop table users")
conn.commit() #committing the transaction to save changes to the database

#drop a database:
#dropping the 'db_revision' database and committing the changes
cursor.execute("drop database db_revision")
conn.commit() #committing the transaction to save changes to the database

#closing the cursor and connection to free up resources
cursor.close()
conn.close()