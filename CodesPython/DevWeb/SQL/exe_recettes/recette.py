#exercice2:
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import mysql.connector

app = Flask(__name__)
# connecting to the database
conn = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="",
    database="recettes_db"
)

# creating a cursor object to execute SQL queries
cursor = conn.cursor()

@app.route("/")
def home():
    try:
        cursor.execute("SELECT * from recettes")#requete pour selectionner tous les recettes
        recettes = cursor.fetchall()#recuperation  all results from the executed query
        print(recettes)
        return render_template("recettes.html", recettes= recettes) #affichage de la page html avec les recettes
    except:
        return render_template("recettes.html", recettes= []) #affichage de la page html sans recettes en cas d'erreur
    

@app.route("/ajouter_recette", methods=["GET", "POST"])
def ajouter_recette():
    if request.method == "POST":
        Nom= request.form["Nom"] #recuperation du nom de la recette depuis le formulaire
        Ingredients= request.form["Ingredients"]
        Preparation= request.form["Preparation"]
        cursor.execute("INSERT INTO recettes (Nom, Ingredients, Preparation) VALUES (%s, %s, %s)", (Nom, Ingredients, Preparation))
        conn.commit() 
        print("recette ajoutée avec succes")

    return render_template("ajouter_recette.html") #affichage de la page html pour ajouter une recette


@app.route("/details_recette/<int:id>")
def details_recette(id):
    cursor.execute("SELECT * from recettes where id = %s", (id,))
    recette = cursor.fetchone()
    return render_template("details_recette.html", recette=recette) #affichage de la page html avec les details de la recette selectionnée


@app.route("/modifier_recette/<int:id>", methods=["GET", "POST"])
def modifier_recette(id):
    if request.method == "POST":
        Nom = request.form["Nom"]
        Ingredients = request.form["Ingredients"]
        Preparation = request.form["Preparation"]
        cursor.execute("UPDATE recettes SET Nom =%s, Ingredients = %s, Preparation =%s where id =%s", (Nom, Ingredients, Preparation, id))
        conn.commit()
        print("recette modifiée avec succes")
        return redirect("/") #redirection vers la page d'accueil apres la modification de la recette

    #récupérer les données pour affichage
    cursor.execute("SELECT * FROM recettes WHERE id=%s", (id,))
    recette = cursor.fetchone()

    return render_template("modifier_recette.html", recette=recette)

@app.route("/supprimer_recette/<int:id>")
def supprimer_recette(id):
    cursor.execute("DELETE from recettes where id = %s", (id,))
    conn.commit()
    print("recette supprimée avec succes")
    return redirect("/") #redirection vers la page d'accueil apres la suppression de la recette

if __name__ == "__main__":
    app.run(debug=True)
