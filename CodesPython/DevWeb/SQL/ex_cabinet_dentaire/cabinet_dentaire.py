
from flask import Flask, session, flash
from flask import render_template
from flask import request
from flask import redirect
import mysql.connector

app = Flask(__name__)
app.secret_key = "ma_cle_secrete_123"

# connecting to the database
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cabinet_dentiste"
)
# creating a cursor object to execute SQL queries
cursor=conn.cursor()

@app.route("/Accueil")
def home():
    if "user_id" in session:
        return render_template("index.html")
    else:
        return redirect ("/login")

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        nom= request.form.get("nom_user")
        email= request.form.get("email")
        password= request.form.get("password")
        role= request.form.get("role")
        cursor.execute("INSERT INTO utilisateurs (nom_user, email, password, role) VALUES (%s, %s, %s, %s)", (nom, email, password, role))
        conn.commit()
        return redirect("/login")
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect("/Accueil")
    if request.method == "POST":
        email= request.form.get("email")
        password= request.form.get("password")
        cursor.execute("SELECT * FROM utilisateurs WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        if user:
           session["user_id"]=user[0]
           session["user_name"]=user[1]
           session["user_role"]=user[4]
           flash("connexion succeed")
           return redirect("/Accueil")
        else:
           return redirect("/login")
    return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/patients")
def patients():
    cursor.execute("SELECT * FROM patients")
    patients= cursor.fetchall()
    for p in patients:
        print(p)    
    if session.get("user_role") == "secretaire":
        x = True
    else:
        x = False
    return render_template("patients.html", patients=patients, x=x)

@app.route("/add_patient", methods=["GET", "POST"])
def add_patient():
    if session.get("user_role") == "secretaire":
        if request.method == "POST":
            nom = request.form.get("nom_patient")
            date_naissance = request.form.get("date_naissance")
            telephone = request.form.get("telephone")
            email = request.form.get("email")
            cursor.execute(""" INSERT INTO patients (nom_patient, date_naissance, telephone, email) VALUES (%s, %s, %s, %s) """, (nom, date_naissance, telephone, email))
            conn.commit()
            return redirect("/patients")
        return render_template("add_patient.html")
    else:
        return redirect("/patients")

@app.route("/edit_patient/<int:id_patient>", methods=["GET", "POST"])
def edit_patient(id_patient):
    if session.get("user_role") == "secretaire":
        if request.method =="POST":
            nom = request.form.get("nom_patient")
            date_naissance = request.form.get("date_naissance")
            telephone = request.form.get("telephone")
            email = request.form.get("email")
            cursor.execute(""" UPDATE patients SET nom_patient = %s, date_naissance = %s, telephone = %s, email = %s WHERE id_patient = %s """, (nom, date_naissance, telephone, email, id_patient))
            conn.commit()
            return redirect("/patients")
        # 1. récupérer les données du patient à éditer
        cursor.execute(""" SELECT * FROM patients WHERE id_patient = %s """, (id_patient,))
        patient = cursor.fetchone()
        return render_template("edit_patient.html", patient=patient)
    else:
        return redirect("/patients")
        

@app.route("/delete_patient/<int:id_patient>")
def delete_patient(id_patient):
    if session.get("user_role") == "secretaire":
        cursor.execute("""DELETE FROM patients WHERE id_patient = %s """, (id_patient,))
        conn.commit()
        return redirect("/patients")
    else:
        return redirect("/patients")
    


@app.route("/dentists")
def dentists():
    cursor.execute(""" SELECT d.id_dentist, d.utilisateur_id, u.nom_user, d.specialite, u.email FROM dentists d JOIN utilisateurs u ON d.utilisateur_id = u.id_utilisateur""")
    dentists = cursor.fetchall()
    x = session.get("user_role") == "administrateur"
    return render_template("dentists.html", dentists=dentists, x=x)

@app.route("/add_dentist", methods=["GET", "POST"])
def add_dentist():
    if request.method == "POST":
        specialite = request.form.get("specialite")
        user_id = request.form.get("utilisateur_id")

        cursor.execute("""SELECT id_utilisateur FROM utilisateurs WHERE id_utilisateur = %s AND role = 'dentiste' """, (user_id,))
        user = cursor.fetchone()

        if user:
            cursor.execute(""" INSERT INTO dentists (utilisateur_id, specialite) VALUES (%s, %s) """, (user_id, specialite))
            conn.commit()
        return redirect("/dentists")

    cursor.execute(""" SELECT id_utilisateur, nom_user FROM utilisateurs WHERE role = 'dentiste' """)
    dentists_users = cursor.fetchall()
    return render_template("add_dentist.html", dentists_users=dentists_users)

@app.route("/edit_dentist/<int:id_dentist>", methods=["GET", "POST"])
def edit_dentist(id_dentist):

    if request.method == "POST":
        name = request.form.get("nom_user")
        email = request.form.get("email")
        specialite = request.form.get("specialite")

        cursor.execute(""" SELECT utilisateur_id FROM dentists WHERE id_dentist = %s """, (id_dentist,))
        result = cursor.fetchone()

        if result:
            user_id = result[0]

# 2. modification dans utilisateurs:

            cursor.execute(""" UPDATE utilisateurs SET nom_user = %s, email = %s WHERE id_utilisateur = %s """, (name, email, user_id))

# 3. modification dans dentists:

            cursor.execute(""" UPDATE dentists SET specialite = %s WHERE id_dentist = %s """, (specialite, id_dentist))
            conn.commit()

        return redirect("/dentists")

    cursor.execute(""" SELECT d.id_dentist, d.utilisateur_id, u.nom_user, d.specialite, u.email FROM dentists d JOIN utilisateurs u ON d.utilisateur_id = u.id_utilisateur WHERE d.id_dentist = %s """, (id_dentist,))
    dentist = cursor.fetchone()
    return render_template("edit_dentist.html", dentist=dentist)

@app.route("/delete_dentist/<int:id_dentist>")
def delete_dentist(id_dentist):

    # 1. récupérer l'utilisateur lié
    cursor.execute(""" SELECT utilisateur_id FROM dentists WHERE id_dentist = %s """, (id_dentist,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]

        # 2. supprimer dans dentists
        cursor.execute(""" DELETE FROM dentists WHERE id_dentist = %s """, (id_dentist,)) 
        
        # 3. supprimer dans utilisateurs
        cursor.execute(""" DELETE FROM utilisateurs WHERE id_utilisateur = %s """, (user_id,))
        conn.commit()
    return redirect("/dentists")


@app.route("/appointments")
def appointments():
    if session.get("user_role") == "secretaire":
        x= True
        cursor.execute(""" SELECT r.id, p.nom_patient, u.nom_user, r.date_heure, r.statut FROM rendez_vous r JOIN patients p ON r.patient_id = p.id_patient JOIN dentists d ON r.dentiste_id = d.id_dentist JOIN utilisateurs u ON d.utilisateur_id = u.id_utilisateur """)
        appointments = cursor.fetchall()
    elif session.get("user_role") == "dentiste":  
        x = False
        cursor.execute(""" SELECT r.id, p.nom_patient, u.nom_user, r.date_heure, r.statut FROM rendez_vous r JOIN patients p ON r.patient_id = p.id_patient JOIN dentists d ON r.dentiste_id = d.id_dentist JOIN utilisateurs u ON d.utilisateur_id = u.id_utilisateur WHERE d.utilisateur_id = %s """, (session.get("user_id"),))
        appointments = cursor.fetchall()
    else:
        x = False
        cursor.execute(""" SELECT r.id, p.nom_patient, u.nom_user, r.date_heure, r.statut FROM rendez_vous r JOIN patients p ON r.patient_id = p.id_patient JOIN dentists d ON r.dentiste_id = d.id_dentist JOIN utilisateurs u ON d.utilisateur_id = u.id_utilisateur """)
        appointments = cursor.fetchall()
        
    return render_template("appointments.html", appointments=appointments, x=x)

@app.route("/add_appointment", methods=["GET","POST"])
def add_appointment():
    if session.get("user_role") == "secretaire":

        if request.method == "POST":
            patient_id = request.form.get("patient_id")
            dentiste_id = request.form.get("dentiste_id")
            date_heure = request.form.get("date_heure")
            statut = request.form.get("statut")

            # DEBUG
            print(request.form.to_dict())

            # sécurité
            if not patient_id or not dentiste_id:
                return "Erreur: patient ou dentiste non sélectionné"

            cursor.execute("""INSERT INTO rendez_vous (patient_id, dentiste_id, date_heure, statut) VALUES (%s, %s, %s, %s) """, (patient_id, dentiste_id, date_heure, statut))

            conn.commit()
            return redirect("/appointments")

        cursor.execute("SELECT id_patient, nom_patient FROM patients")
        patients = cursor.fetchall()

        cursor.execute("SELECT id_dentist, specialite FROM dentists")
        dentistes = cursor.fetchall()

        return render_template("add_appointment.html", patients=patients, dentistes=dentistes)

    return redirect("/appointments")


@app.route("/edit_appointment/<int:id>", methods=["GET", "POST"])
def edit_appointment(id):
    if session.get("user_role") == "secretaire":

        if request.method == "POST":
            patient_id = request.form.get("patient_id")
            dentiste_id = request.form.get("dentiste_id")
            date_heure = request.form.get("date_heure")
            statut = request.form.get("statut")

            # update dans la table rendez_vous
            cursor.execute(""" UPDATE rendez_vous SET patient_id = %s, dentiste_id = %s, date_heure = %s, statut = %s WHERE id = %s """, (patient_id, dentiste_id, date_heure, statut, id))
            conn.commit()
            return redirect("/appointments")
        
        # 1. récupérer les données du rendez-vous à éditer

        cursor.execute(""" SELECT patient_id, dentiste_id, date_heure, statut FROM rendez_vous WHERE id = %s """, (id,))
        appointment = cursor.fetchone()

        # 2. récupérer la liste des patients et des dentistes pour les afficher dans les listes déroulantes du formulaire

        cursor.execute("SELECT id_patient, nom_patient FROM patients")
        patients = cursor.fetchall()

        cursor.execute("SELECT id_dentist, specialite FROM dentists")
        dentistes = cursor.fetchall()

        return render_template("edit_appointment.html", appointment=appointment, patients=patients, dentistes=dentistes)

    return redirect("/appointments")



@app.route("/delete_appointment/<int:id>")
def delete_appointment(id):
    if session.get("user_role") == "secretaire":
        cursor.execute(""" DELETE FROM rendez_vous WHERE id = %s """, (id,))
        conn.commit()
        return redirect("/appointments")
    else:
        return redirect("/appointments")
    



if __name__ == "__main__":
    app.run(debug=True)
