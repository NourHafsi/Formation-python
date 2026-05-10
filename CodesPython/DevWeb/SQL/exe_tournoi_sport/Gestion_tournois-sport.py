#exercie3:
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import mysql.connector

app = Flask(__name__)

# connecting to the database
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Tournois_Esport"
)
# creating a cursor object to execute SQL queries
cursor=conn.cursor()

def get_tournoi():
    cursor.execute("SELECT ID_Tournoi, Nom_Tournoi FROM Tournois")
    return cursor.fetchall()

def recherche_joueurs(Nom_Tournoi):
    cursor.execute("select * from Tournois join Joueurs on Tournois.ID_Tournoi=Joueurs.Tournoi_ID where Tournois.Nom_Tournoi=%s", (Nom_Tournoi,))
    return cursor.fetchall()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Tournois", methods=["GET", "POST"])
def Tournois():
    if request.method == "POST":
        Nom_Tournoi = request.form.get("search")
        cursor.execute("SELECT * FROM Tournois join Joueurs on Tournois.ID_Tournoi=Joueurs.Tournoi_ID where Tournois.Nom_Tournoi=%s", (Nom_Tournoi,))
        Tournois = cursor.fetchall()
        return render_template("Tournois.html", Tournois=Tournois)
    try:
        cursor.execute("SELECT * from Tournois join Joueurs on Tournois.ID_Tournoi=Joueurs.Tournoi_ID") #selectionner toutes les reservations des Tournois.
        Tournois=cursor.fetchall()
        return render_template("Tournois.html", Tournois=Tournois)
    except:
        return "No reservations found"
    
@app.route("/Joueurs", methods=["GET", "POST"])
def Joueurs():
    if request.method == "POST":
        Nom_Tournoi = request.form.get("search")
        cursor.execute("SELECT * FROM Joueurs JOIN Tournois ON Joueurs.Tournoi_ID = Tournois.ID_Tournoi WHERE Tournois.Nom_Tournoi=%s",(Nom_Tournoi,))
        Joueurs = cursor.fetchall()
        return render_template("Joueurs.html", Joueurs=Joueurs)
    try:
        cursor.execute("SELECT * from Joueurs join Tournois on joueurs.Tournoi_ID=Tournois.ID_Tournoi") #selectionner toutes les reservations des Joueurs.
        Joueurs=cursor.fetchall()
        #print(Joueurs)
        
        return render_template("Joueurs.html", Joueurs=Joueurs)
    except:
        return "No reservations found"
    
    

@app.route("/Ajout_Joueur", methods=["GET","POST"])
def Ajout_Joueur():
    # recuperer les noms et ID des tournois dans une balise select
    tournois = get_tournoi()    
    if request.method == "POST":
        Nom=request.form["Nom"] 
        Prenom=request.form["Prenom"] 
        Age=request.form["Age"] 
        Nom_Sport=request.form["Nom_Sport"]
        tournoi_id=request.form["Tournoi_ID"] 
        cursor.execute("INSERT INTO Joueurs (Nom, Prenom, Age, Nom_Sport, Tournoi_ID) VALUES (%s, %s, %s, %s, %s)", (Nom, Prenom, Age, Nom_Sport, tournoi_id))
        conn.commit()
        print("joueur added successfully")
    return render_template("Ajout_Joueur.html", tournois=tournois)

@app.route("/Ajout_Tournoi", methods=["GET","POST"])
def Ajout_Tournoi():
    if request.method == "POST":
        Nom_Tournoi=request.form["Nom_Tournoi"] 
        Date_Tournoi=request.form["Date_Tournoi"] 
        Lieu=request.form["Lieu"] 
        Nombre_Participants=request.form["Nombre_Participants"] 
        cursor.execute("INSERT INTO Tournois (Nom_Tournoi, Date_Tournoi, Lieu, Nombre_Participants) VALUES (%s, %s, %s, %s)", (Nom_Tournoi, Date_Tournoi, Lieu, Nombre_Participants))
        conn.commit()
        print("tournoi added successfully")
    return render_template("Ajout_Tournoi.html")

@app.route("/Modifier_Joueur/<int:id>", methods=["GET","POST"])
def Modifier_Joueur(id):
    if request.method == "POST":
        Nom=request.form["Nom"] 
        Prenom=request.form["Prenom"] 
        Age=request.form["Age"] 
        Nom_Sport=request.form["Nom_Sport"] 
        cursor.execute("UPDATE Joueurs SET Nom=%s, Prenom=%s, Age=%s, Nom_Sport=%s WHERE ID_Joueur=%s", (Nom, Prenom, Age, Nom_Sport, id))
        conn.commit()
        print("joueur updated successfully")

        return redirect("/") #redirection vers la page d'accueil apres la modification de la recette

    #récupérer les données pour affichage
    cursor.execute("SELECT * FROM Joueurs WHERE ID_Joueur=%s", (id,))
    joueur = cursor.fetchone()
    return render_template("Modifier_Joueur.html", joueur=joueur)




@app.route("/Supprimer_Joueur/<int:id>", methods=["GET","POST"])
def Supprimer_Joueur(id):
    cursor.execute("DELETE FROM Joueurs WHERE ID_Joueur=%s", (id,))
    conn.commit()
    print("joueur deleted successfully")
    return redirect("/Joueurs")

@app.route("/Modifier_Tournoi/<int:id>", methods=["GET","POST"])
def Modifier_Tournoi(id):
    if request.method == "POST":
        Nom_Tournoi=request.form["Nom_Tournoi"] 
        Date_Tournoi=request.form["Date_Tournoi"] 
        Lieu=request.form["Lieu"] 
        Nombre_Participants=request.form["Nombre_Participants"] 
        cursor.execute("UPDATE Tournois SET Nom_Tournoi=%s, Date_Tournoi=%s, Lieu=%s, Nombre_Participants=%s WHERE ID_Tournoi=%s", (Nom_Tournoi, Date_Tournoi, Lieu, Nombre_Participants, id))
        conn.commit()
        print("tournoi updated successfully")


    #récupérer les données pour affichage
    cursor.execute("SELECT * FROM Tournois WHERE ID_Tournoi=%s", (id,))
    tournoi = cursor.fetchone()

    return render_template("Modifier_Tournoi.html", tournoi=tournoi)

@app.route("/Supprimer_Tournoi/<int:id>", methods=["GET","POST"])
def Supprimer_Tournoi(id):
    cursor.execute("DELETE FROM Tournois WHERE ID_Tournoi=%s", (id,))
    conn.commit()
    print("tournoi deleted successfully")
    return redirect("/Tournois")

if __name__ == "__main__":
    app.run(debug=True)