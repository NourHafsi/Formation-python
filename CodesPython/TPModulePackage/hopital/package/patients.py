PatientListe=[]
def ajouter_patient(nom,prenom,age):
    patient={
        "nom":nom,
        "prenom":prenom,
        "age":age
    }
    PatientListe.append(patient)
    return patient