from classes.Etudiant import Etudiant

fichier="etudiants.txt"

while(True):
    print("1. Ajouter un étudiant")
    print("2. Modifier un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Rechercher un étudiant")
    print("5. Afficher tous les étudiants")
    print("6. Quitter")
    choix = input("Entrez votre choix: ")

    if choix == "1":
        # Ajouter un étudiant
        matricule = int(input("Entrez le matricule: ")) 
        nom = input("Entrez le nom: ")
        prenom = input("Entrez le prénom: ")
        licence = input("Entrez la licence: ")
        promotion = input("Entrez la promotion: ")
        notes = []
        for matiere in ['genie_logiciel', 'php', 'oracle', 'windev', 'python']:
            note = float(input(f"Entrez la note pour {matiere}: "))
            notes.append({matiere: note})
        nouveau_etudiant = Etudiant(matricule, nom, prenom, licence, promotion, notes)
        test_ajout = Etudiant.ajouter_etudiant(nouveau_etudiant, fichier)
        if test_ajout:
            print("Étudiant ajouté avec succès.")

    elif choix == "2":
        # Modifier un étudiant
        matricule_a_modifier = int(input("Entrez le matricule de l'étudiant à modifier: "))
        matricule = int(input("Entrez le nouveau matricule: "))
        nom = input("Entrez le nouveau nom: ")
        prenom = input("Entrez le nouveau prénom: ")
        licence = input("Entrez la nouvelle licence: ")
        promotion = input("Entrez la nouvelle promotion: ")
        notes = []
        for matiere in ['genie_logiciel', 'php', 'oracle', 'windev', 'python']:
            note = float(input(f"Entrez la nouvelle note pour {matiere}: "))
            notes.append({matiere: note})
        modifier_etudiant = Etudiant(matricule, nom, prenom, licence, promotion, notes)
        test = Etudiant.modifier_etudiant(modifier_etudiant, matricule_a_modifier, fichier)
        if test:
            print("Étudiant modifié avec succès.")
    elif choix == "3":
        # Supprimer un étudiant
        matricule = int(input("Entrez le matricule de l'étudiant à supprimer: "))
        test_sup= Etudiant.supprimer_etudiant(matricule, fichier)   
        if test_sup:
            print("Étudiant supprimé avec succès.")
                      
    elif choix == "4":
        # Rechercher un étudiant
        matricule = int(input("Entrez le matricule de l'étudiant à rechercher: "))
        etudiant = Etudiant.rechercher_etudiant(matricule, fichier)
        if etudiant:
            print("Étudiant trouvé:")
            print(etudiant)
        else:
            print("Étudiant non trouvé.")
            
    elif choix == "5":
        # Afficher tous les étudiants
        Etudiant.afficher_etudiants(fichier)
    elif choix == "6":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
        break
