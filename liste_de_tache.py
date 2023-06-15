class Taches:
    def __init__(self):
        self.taches  = [] # initialiser la liste à 0 (car la liste ne contient aucune tâche pour l'instant)
        self.termine = [] # initialiser la liste à 0
    
    def ajouter(self, tache):
        self.taches.append(tache)
        self.termine.append(False) #initialise tache à false, car de base la tâche n'est pas terminé (True sera ajouter plustard si tache terminé)

    def idx_valide(self, idx): #représente l'indice de la tâche
        if idx >= 0 and idx < len(self.taches): #sélèctionne les indices de la liste termine / sélèctionne la longueur de la liste et vérifie si il est inférieur à la taille de la liste 
            return True
        else:
            print("Erreur: Indice hors limites")
            return False

    def terminer(self, idx): 
        if self.idx_valide(idx): #utiliser la méthode pour vérifier si valide ou nn 
            self.termine[idx] = True 


    def supprimer(self, idx):
        if self.idx_valide(idx):
            del self.taches[idx]
            del self.termine[idx]


    def afficher(self):
        print("--------------------")
        for i, t in enumerate(self.taches):
            print(f"{i} : {t} - {self.termine[i]}") #[i] fait réfférence à false car de base termine est sur false (la tâche viens juste d'être ajouté)
                                                    


taches = Taches()

while True:
    cmd = input("Entrez une commande (+: Ajouter, -: Terminer, s: Supprimer, a: Afficher, q: Quitter) ")

    if cmd == "+":
        tache = input("Entrez le nom: ")
        taches.ajouter(tache)

    elif cmd == "-":
        idx = int(input("Entrez l'id de la tâche: "))
        taches.terminer(idx)

    elif cmd == "s":
        idx = int(input("Entrez l'id de la tâche: "))
        taches.supprimer(idx)

    elif cmd == "a":
        taches.afficher()

    elif cmd == "q":
        break
    else:
        print("Commande invalide")





