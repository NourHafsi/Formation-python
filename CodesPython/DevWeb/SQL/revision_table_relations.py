import mysql.connector  
# connecting to the database
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_table_rev",
)

# creating a cursor object to execute SQL queries
cursor=conn.cursor()
#creating tables for one to one relationship: user et profile
cursor.execute("create table users (user_id int auto_increment primary key, name varchar(255), email varchar(255), password varchar(255), role varchar(255)))")
print  ("table users created successfully")
cursor.execute("create table profile (profile_id int auto_increment primary_key, id_user int, bio varchar(255), FOREIGN KEY (id_user) REFERENCES users(user_id))")
print ("table profile created successfully")
#inserting data into the users and profile tables
cursor.execute("insert into users(name,email,password,role)values('mohamed','mohamed@example.com','1234','student')")
conn.commit()
print("data inserted successfully")
cursor.execute("insert into profile(id_user,bio) values (1,'i'm a python student')")
conn.commit()
print("data inserted successfully")
cursor.execute("insert into users(name, email, password, role) values ('faten', 'faten@example.com', '5678', 'student')")
conn.commit()
print("data inserted successfully")
cursor.execute("insert into profile(id_user,bio) values (2, 'i am a java student')")
conn.commit()
print("data inserted successfully")

#affichage des données one to one
cursor.execute("select users.name, profile.bio from users join profile on users.user_id = profile.id_user where users.name='mohamed'")
for user in cursor.fetchall():
    print(user)
med=cursor.fetchone()
print(med)

#many to many relationship: courses and users
cursor.execute("create table courses (id int auto_increment primary key, name varchar(255), description varchar(255))")
cursor.execute("insert into courses(name, description) values ('python', 'python course for beginners')")
cursor.execute("insert into courses(name, description) values ('java', 'java course for beginners')")
conn.commit()   
print("table courses created successfully and data inserted successfully")

cursor.execute("create table users_courses (id_user int, id_cours int, primary key (id_user, id_cours), foreign key(id_user) references users(user_id), foreign key(id_cours) references courses(id))")
cursor.execute("insert into users_courses(id_user, id_cours) values (1, 7)")
conn.commit()
print("table users_courses created successfully and data inserted successfully")
cursor.execute("insert into users_courses(id_user, id_cours) values (1, 8)")
conn.commit()
print("data inserted successfully")
cursor.execute("insert into users_courses(id_user, id_cours) values (2, 7)")
conn.commit()
print("data inserted successfully")
cursor.execute("insert into users_courses(id_user, id_cours) values (2, 8)")
conn.commit()
print("data inserted successfully")

#add colonne date to table users_courses
cursor.execute("alter table users_courses add column date varchar(255)")
conn.commit()
print("column date added successfully to users_courses table")

#affichage des données many to many
cursor.execute("select *from users_courses join users on users_courses.id_user = users.user_id join courses on users_courses.id_cours = courses.id")
for user in cursor.fetchall():
    print(user) 
