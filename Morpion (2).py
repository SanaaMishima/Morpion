from random import *

def Morpion(joueur):
    """Ceci est le jeu du morpion. Il faut indiquer le nombre de joueur (1 ou 2) dans les parenthèses pour lancer une partie. Les règles s'afficheront automatiquement à chaque début de partie"""
    print("Bienvenue au jeu du morpion !")
    t=[['-','-','-'],['-','-','-'],['-','-','-']]#créer le plateau de jeu
    if joueur==2: #lance une partie pour deux joueurs
        print("Vous avez décidé de jouer à deux joueurs, vous jouerez chacun votre tour. Déterminez le Joueur 1 (qui aura les O) et le Joueur 2 (qui aura les X). Attention, la première colonne correspond au numéro 0, la deuxième au numéro 1 et la troisième au numéro 2. Il en va de même pour les lignes. Pensez-y avant d'entrer vos positions. Bonne partie !") #annonce les règles
        for i in t:
            print(i)#affiche le plateau de jeu
        while True in Verification(t) : #vérifie s'il reste des cases libres
            j1=input("Joueur 1, donnez la position de votre pion sous forme de ligne,colonne ")#demande l'emplacement du pion
            j1l=int(j1[0])#affecte les valeurs données à j1l et j1c
            j1c=int(j1[2])
            while t[j1l][j1c]!='-' : #vérifie si l'emplacement n'est pas déjà pris
                j1=input("Joueur 1, vous avez entré une position déjà prise. Donnez une autre position pour votre pion sous forme de ligne,colonne ")
                j1l=int(j1[0])
                j1c=int(j1[2])
            t[j1l][j1c]='O'#donne un emplacement dans la matrice à partir des valeurs données
            for i in t:
                print(i)#affiche plateau avec nouvelles données
            if Alignement(t)=="Gagné1": #vérifie s'il n'y a pas un alignement
                return ("Le Joueur 1 a gagné ! Félicitation !")
            if not Verification(t) : #vérifie s'il reste des cases libres
                return ("Il n'y a plus de cases libres... C'est la fin de la partie. Personne n'a gagné et tout le monde a perdu")
            j2=input("Joueur 2, donnez la position de votre pion sous forme de ligne,colonne ")#demande l'emplacement du pion
            j2l=int(j2[0])#affecte les valeurs données à j2l et j2c
            j2c=int(j2[2])
            while t[j2l][j2c]!='-' : #vérifie si l'emplacement n'est pas déjà pris
                j2=input("Joueur 2, vous avez entré une position déjà prise. Donnez une autre position pour votre pion sous forme de ligne,colonne ")
                j2l=int(j2[0])
                j2c=int(j2[2])
            t[j2l][j2c]='X'#donne un emplacement dans la matrice à partir des valeurs données
            for i in t:
                print(i)#affiche plateau avec nouvelles données
            if  Alignement(t)=="Gagné2":#vérifie s'il n'y a pas un alignement
                return ("Le Joueur 2 a gagné ! Félicitation !")
        else:
            return ("Il n'y a plus de cases libres... C'est la fin de la partie")
    elif  joueur==1:  #lance une partie pour un joueur
        print("Vous avez décidé de jouer contre l'ordinateur. \nVous aurez les O et l'ordinateur les X. \nAttention, la première colonne correspond au numéro 0, la deuxième au numéro 1 et la troisième au numéro 2. \nIl en va de même pour les lignes. Pensez-y avant d'entrer vos positions. \nBonne partie !")  #annonce les règles
        for i in t:
                print(i)#affiche le palteau de jeu
        while Verification(t) : #vérifie s'il reste des cases libres
            j=input("Joueur, donnez la position de votre pion sous forme de ligne,colonne ") #demande l'emplacement du pion
            jl=int(j[0])#affecte les valeurs données à jl et jc
            jc=int(j[2])
            while t[jl][jc]!='-' : #vérifie si l'emplacement est déjà pris
                j=input("Joueur, vous avez entré une position déjà prise. Donnez une autre position pour votre pion sous forme de ligne,colonne ")
                jl=int(j[0])
                jc=int(j[2])
            t[jl][jc]='O'#donne un emplacement dans la matrice à partir des valeurs données
            for i in t:
                print(i) #affiche plateau avec nouvelles données
            if Alignement(t)=="Gagné1": #vérifie s'il n'y a pas un alignement
                return ("Joueur, vous avez gagné ! Félicitation !")
            print(Verification(t))
            if not Verification(t) : #vérifie s'il reste des cases libres
                return ("Il n'y a plus de cases libres... C'est la fin de la partie. Personne n'a gagné et tout le monde a perdu")
            print("C'est au tour de l'ordinateur") #annonce le changement de tour
            ol=randint(0,2)#tire deux nombres aléatoirement entre 0 et 2 compris
            oc=randint(0,2)
            while t[ol][oc]!='-': #vérifie si l'emplacement est déjà pris
                ol=randint(0,2)
                oc=randint(0,2)
            else :
                t[ol][oc]='X'#donne un emplacement dans la matrice à partir des valeurs tirées
            for i in t:
                print(i) #affiche plateau avec nouvelles données
            if  Alignement(t)=="Gagné2": #vérifie s'il n'y a pas un alignement
                print(("L'ordinateur a gagné ! Vous n'avez pas eu de chance (ou de talent)"))
                return None
        else:
            return ("Il n'y a plus de cases libres... C'est la fin de la partie")
    else:
        return("Vous ne pouvez pas entrer un nombre de joueur autre que 1 ou 2... Relancez une partie")
            
        
def Alignement(t):
    for i in t: #vérifie l'alignement des lignes
        if i==['O','O','O'] : 
            return ("Gagné1")
        elif i==['X','X','X'] :
            return ("Gagné2")
    for i in range(0,3): #vérifie l'alignement des colonnes
        if t[0][i]==t[1][i]==t[2][i]=='O' :
            return ("Gagné1")
        elif t[0][i]==t[1][i]==t[2][i]=='X' :
            return ("Gagné2")
    if t[0][0]==t[1][1]==t[2][2]=='O': #vérifie l'alignement des diagonales
        return ("Gagné1")
    elif t[0][0]==t[1][1]==t[2][2]=='X':
        return ("Gagné2")
    elif t[0][2]==t[1][1]==t[2][0]=='O':
        return ("Gagné1")
    elif t[0][2]==t[1][1]==t[2][0]=='X':
        return ("Gagné2")

def Verification(t):
    a='-' in t[0] #vérifie si la valeur de base (cases vides) est présente dans la 1re liste
    b='-' in t[1] #vérifie si la valeur de base (cases vides) est présente dans la 2e liste
    c='-' in t[2] #vérifie si la valeur de base (cases vides) est présente dans la 3e liste
    return (a,b,c)

Morpion(1)