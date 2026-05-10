from flask import Flask, render_template, request, redirect
from services.user_service import UtilisateurService
from services.course_service import Cours_service
from services.enrollement_service import InscriptionService

app = Flask(__name__)

# Initialisation des services
user_service = UtilisateurService()
course_service = Cours_service()
enroll_service = InscriptionService()

# -------------------------
# PAGE ACCUEIL
# -------------------------
@app.route("/")
def home():
    return render_template("base.html")

# -------------------------
# USERS
# -------------------------
@app.route("/users")
def users():
    users = user_service.lister_utilisateurs()
    return render_template("users.html", users=users)

@app.route("/add_user", methods=["POST"])
def add_user():
    nom = request.form["user_name"]
    email = request.form["user_email"]
    role = request.form["user_role"]
    user_service.ajouter_utilisateur(nom, email, role)
    return redirect("/users")

# -------------------------
# COURSES
# -------------------------
@app.route("/courses", methods=["GET", "POST"])
def courses():
    if request.method == "POST":
        code = request.form["course_id"]
        titre = request.form["course_name"]
        teacher_nom = request.form["enseignant_nom"]
        capacite = int(request.form["capacite_max"])

        course_service.ajouter_cours(
            code_cours=code,
            titre=titre,
            enseignant=teacher_nom,
            administrateur=None,  # obligatoire pour correspondre à la signature
            capacite_cours=capacite
        )
        return redirect("/courses")

    courses_list = course_service.lister_cours()
    return render_template("courses.html", courses=courses_list)

@app.route("/search_students", methods=["POST"])
def search_students():
    course_id = request.form["course_id"]
    cours = course_service.chercher_cours(course_id)

    students_list = []
    course_name = ""
    if cours:
        course_name = cours.titre
        for etu_id in cours.etudiants_inscrits:
            etudiant = user_service.get_user_by_id(etu_id)
            if etudiant:
                students_list.append(etudiant)

    # On renvoie la même page courses.html mais avec la liste des étudiants
    courses_list = course_service.lister_cours()
    return render_template(
        "courses.html",
        courses=courses_list,
        students=students_list,
        course_name=course_name
    )
# -------------------------
# ENROLLMENTS
# -------------------------
@app.route("/enrollments", methods=["GET", "POST"])
def enrollments():
    if request.method == "POST":
        user_id = request.form["user_id"]
        course_id = request.form["course_id"]

        user = user_service.get_user_by_id(user_id)
        course = course_service.get_course_by_id(course_id)

        if user and course:
            enroll_service.inscrire_etudiant(course_id, user_id)

        return redirect("/enrollments")

    users_list = user_service.lister_utilisateurs()
    courses_list = course_service.lister_cours()
    inscrits = enroll_service.lister_inscriptions()

    return render_template("enroll.html", users=users_list, courses=courses_list, inscrits=inscrits)

# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)