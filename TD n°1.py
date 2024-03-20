#Exercice 1

# Algorithme :
# Si la liste n'est pas rangée par ordre décroissant du mot le plus long, la trier
# Prendre le mot le plus long et vérifier si les lettres sont disponibles
# Recommencer pour chaque mot jusqu'à trouver le mot le plus long

#Exercice 2



#Functions

def read_file(path):
    # Fonction pour lire le contenu de path
    f = open(path,"r")
    liste = []
    for ligne in f :
        mot = ligne[0:len(ligne) - 1] # J'enlève les retour à la ligne
        if len(mot) <= 8 :
            liste.append(mot)
    f.close()
    return liste

path = "mots.sansaccent.txt"
mots = []
mots = read_file(path)


# Générer les mots possibles

tirage = ['a','o','f','v','i','o','e','r']

def generation(tirage):
    mots_possibles = []
    for mot in mots:  # Je parcours la liste de mots dans le lexique
        A = True
        for lettre in mot:  # Je parcours les lettres de chaque mot
            if lettre not in tirage:
                A = False
        if A == True:  #  Si toutes les lettres sont dans le tirage, le mot est possible
            mots_possibles.append(mot)
    return mots_possibles

# Garder les plus grands mots

mots_possibles = generation(tirage)

def plus_grand(mots_possibles):
    candidat = mots_possibles[0]  # J'initialise le premier mot et sa taille
    taille = len(mots_possibles[0])
    for mot in mots_possibles:
        if len(mot) > taille :   #  Je parcours la liste des mots pour les comparer
            candidat = mot
            taille = len(mot)    #  Je remplace le candidat et sa taille
    return candidat, taille


#Exercice 3

# J'utilise la structure de tuples

L1 = [(['A','E','I','L','N','O','R','S','T','U'],1)]
L2 = [(['D','G','M'],2)]
L3 = [(['B','C','P'],3)]
L4 = [(['F','H','V'],4)]                    # Chaque liste est associé avec sa valeur
L5 = [(['J','Q'],8)]
L6 = [(['K','W','X','Y','Z'],10)]

L = L1 + L2 + L3 + L4 + L5 + L6
n = len(L)

def score(mot):
    if  len(mot)==1:
        for (lettres,s) in L :
            if mot[0] in lettres:
                return s

    s = 0           # Disjonction de cas en fonction du nombre de lettres
    for c in mot :
        s+=score(c)
    return s

def max_score(liste_mots) :
    max_score = 0
    max_mot = ""
    for mot in liste_mots:
        s = score(mot)                            # Comparaison au score max
        if s > max_score :
            max_score = s
            max_mot = mot
    return (max_mot,max_score)


