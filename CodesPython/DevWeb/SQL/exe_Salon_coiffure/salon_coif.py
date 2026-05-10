#exercie1:
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
    database="salon_coiffure"
)
# creating a cursor object to execute SQL queries
cursor=conn.cursor()

def verif_creneau_service(Creneau, service):
    cursor.execute("SELECT * from reservations where Creneau = %s and service =%s ", (Creneau, service)) #requete pour selectionner les reservations avec le meme creneau et service
    reservation=cursor.fetchone() #recuperation de la premiere reservation qui correspond a la requete
    if reservation: #si une reservation existe deja avec le meme creneau et service
        return False #le creneau et service ne sont pas disponibles
    else:
        return True #le creneau et service sont disponibles
    


@app.route("/")
def home():
    try:
        cursor.execute("SELECT * from reservations") #requete pour selectionner tous les reservations
        reservations=cursor.fetchall() #recuperation  all results from the executed query
        print(reservations)
        return render_template("reservations.html", reservations=reservations) #affichage de la page html avec les reservations
    except:
        return render_template("reservations.html", reservations=[]) #affichage de la page html sans reservations en cas d'erreur

@app.route("/ajouter_reservation", methods=["GET", "POST"])
def ajouter_reservation():
    x=""
    y=""
    if request.method == "POST":
        Nom=request.form["Nom"] #recuperation du nom du client depuis le formulaire
        Prenom=request.form["Prenom"] #recuperation du prenom du client depuis le formulaire
        Numero_telephone=request.form["Numero_telephone"] #recuperation du numero de telephone du client depuis le formulaire
        Creneau=request.form["Creneau"] #recuperation du creneau de reservation depuis le formulaire
        service=request.form["service"] #recuperation du service de reservation depuis le formulaire
        if verif_creneau_service(Creneau, service): #verification de la disponibilite du creneau et service
            cursor.execute("INSERT INTO reservations (Nom, Prenom, Numero_telephone, Creneau, service) VALUES (%s, %s, %s, %s, %s)", (Nom, Prenom, Numero_telephone, Creneau, service))
            conn.commit() #commit the transaction to save changes to the database
            print("reservation added successfully")
            y="reservation ajoutée avec succès"
            
        else:
            print("reservation not available")
            x="ce Creneau et service sont deja reserves, veuillez choisir un autre Creneau ou service"
    return render_template("ajouter_reservation.html", x=x, y=y) #affichage de la page html avec le message adequat en fonction de la disponibilite du creneau et service

@app.route("/verification_reservation", methods=["GET", "POST"])
def verification_reservation():
    if request.method == "POST":
        Creneau=request.form["Creneau"] #recuperation du creneau de reservation depuis le formulaire
        cursor.execute("SELECT * from reservations where Creneau = %s ", (Creneau,)) #requete pour selectionner les reservations avec le meme creneau
        reservations=cursor.fetchall() #recuperation de all results from the executed query
        if reservations: #si des reservations existent avec le meme creneau
            return render_template("verification_reservation.html", reservations=reservations) #affichage de la page html avec les reservations correspondantes
        else:
            return render_template("verification_reservation.html", reservations=[]) #affichage de la page html sans reservations en cas d'absence de reservations avec le meme creneau
    return render_template("verification_reservation.html", reservations=[]) #affichage de la page html sans reservations en cas d'absence de reservations avec le meme creneau        
      
@app.route("/supprimer_reservation/<int:id>")
def supprimer_reservation(id):
    cursor.execute("DELETE from reservations where id =%s", (id,)) #requete pour supprimer la reservation avec l'id specifie
    conn.commit() #commit the transaction to save changes to the database
    print("reservation deleted successfully")
    return redirect("/") #redirection vers la page d'accueil apres la suppression de la reservation


        









if __name__ == "__main__":
    app.run(debug=True)
