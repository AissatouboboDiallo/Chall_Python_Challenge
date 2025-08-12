# Classe représentant un étudiant
class Etudiant():
    def __init__(self, matricule : int, nom : str, prenom : str, licence : str, promotion : str, notes : list[{'genie_logiciel':0.00},
                                                                                                              {'php':0.00},
                                                                                                              {'oracle':0.00},
                                                                                                              {'windev':0.00},
                                                                                                              {'python':0.00}
                                                                                                              ]):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.licence = licence
        self.promotion = promotion
        self.notes = notes
        self.moyenne = self.calculer_moyenne()
        
    # Méthode pour afficher les informations de l'étudiant
    def __str__(self):
        return f"{self.matricule},{self.nom},{self.prenom},{self.moyenne},{self.notes}"

    
    # Méthodes d'accès (getters et setters)
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_matricule(self):
        return self.matricule
    def get_licence(self):
        return self.licence
    def get_promotion(self):
        return self.promotion
    def get_notes(self):
        return self.notes
    def get_moyenne(self):
        return self.moyenne

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_matricule(self, matricule):
        self.matricule = matricule

    def set_licence(self, licence):
        self.licence = licence

    def set_promotion(self, promotion):
        self.promotion = promotion

    def set_notes(self, notes):
        self.notes = notes
        self.moyenne = self.calculer_moyenne()

    def calculer_moyenne(self):
        total = 0
        for note in self.notes:
            total += list(note.values())[0]
        return total / len(self.notes)

    def ajouter_etudiant(self, fichier):
        with open(fichier, 'a') as f:
            f.write(f"{self.matricule},{self.nom},{self.prenom},{self.licence},{self.promotion},{self.moyenne},{self.notes}\n")
        return True
            
    def supprimer_etudiant(matricule, fichier):
        lignes = []
        with open(fichier, 'r') as f:
            lignes = f.readlines()
        with open(fichier, 'w') as f:
            for ligne in lignes:
                parts = ligne.strip().split(",")
                if not parts[0] == str(matricule):
                    f.write(ligne)
        return True
                    
    def modifier_etudiant(self, matricule, fichier):
        lignes = []
        with open(fichier, 'r') as f:
            lignes = f.readlines()
        with open(fichier, 'w') as f:
            for ligne in lignes:
                parts = ligne.strip().split(",")
                if parts[0] == str(matricule):
                    f.write(f"{self.matricule},{self.nom},{self.prenom},{self.licence},{self.promotion},{self.moyenne},{self.notes}\n")
                else:
                    f.write(ligne)
        return True
                    
    def rechercher_etudiant(matricule, fichier):
        with open(fichier, 'r') as f:
            lignes = f.readlines()
            for ligne in lignes:
                parts = ligne.strip().split(",")
                if parts[0] == str(matricule):
                    return str(ligne)
        return None
    
    @staticmethod
    def afficher_etudiants(fichier):
        with open(fichier, 'r') as f:
            lignes = f.readlines()
            for ligne in lignes:
                print(ligne.strip())
    

if __name__ == "__main__":
    etudiant1 = Etudiant(1, "Dupont", "Jean", "Informatique", "2023", [{'genie_logiciel': 15.0}, {'php': 12.0}, {'oracle': 14.0}, {'windev': 13.0}, {'python': 16.0}])
    etudiant2 = Etudiant(2, "Martin", "Sophie", "Informatique", "2023", [{'genie_logiciel': 18.0}, {'php': 17.0}, {'oracle': 16.0}, {'windev': 15.0}, {'python': 19.0}])
    etudiant3 = Etudiant(3, "Durand", "Pierre", "Informatique", "2023", [{'genie_logiciel': 10.0}, {'php': 12.0}, {'oracle': 11.0}, {'windev': 13.0}, {'python': 14.0}])

    print(etudiant1)
    print(etudiant2)
    print(etudiant3)
