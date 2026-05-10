""" 
Q1.
Créer une application Flask minimale qui affiche le message
"Ma To-Do List" lorsque l’utilisateur accède à l’URL /.
Q2.
Créer une liste Python contenant au moins 3 tâches et afficher ces tâches
dans une page HTML à l’aide de Flask.
Q3.
Ajouter un formulaire HTML permettant à l’utilisateur d’ajouter une
nouvelle tâche.
Q4.
Créer une route Flask qui récupère la tâche envoyée par le formulaire
(POST) et l’ajoute à la liste, puis redirige vers la page principale. 
"""
from flask import Flask 
from flask import render_template
from flask import request

app= Flask(__name__)
@app.route("/")
def home():
    return "Ma To-Do List"

Task_list = ["aller au travail", "faire du sport", "regarder un film"]

@app.route("/tasks")
def tasks():
    return render_template("tasks.html", TASK=Task_list)

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        New_Task = request.form["New_Task"]
        Task_list.append(New_Task)
        return f"New task added: {New_Task}"
    return render_template("form.html")

    """ new_task = request.form.get("new_task")
    if new_task:
        Task_list.append(new_task)
    return render_template("form.html", TASK=Task_list) """

if __name__=="__main__":
    app.run(debug=True)