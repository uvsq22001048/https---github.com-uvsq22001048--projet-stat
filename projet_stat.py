##############
# Groupe 3 -- projet "statistique"
# Ceylia DUPIN 
# Louis REBECHE    
# https://github.com/uvsq22001048/https---github.com-uvsq22001048--projet-stat
##############

#import des librairies 
import tkinter as tk
import random as rd
from random import randrange
#########################
#variable
coul ="dark green"
x1, y1, x2, y2 = 10, 190, 190, 10
#variable provenant de SWINNEN_apprendre_python3_5.pdf
# les variable x et y servent a vérifier que la fonction def changecolor marche bien


#fonctions
#########################
#outil
#########################
#fonction creer fichier
def cree_fichier_alea(nb, nomfichier):
    fic = open(nomfichier,"w")
    for i in range (nb):
        x = rd.uniform(0,600)
        y = rd.uniform(0, 600)
        fic.write(str(x) + "  "+ str(y)+ "\n")
    fic.close()

# fonction lecture de fichier
    #def lit_fichier(nomfic)
    
# fonction pour faire le nuage
    #def trace_Nuage(nomf)
     #lit_fichier()

# fonction pour tracer la droite
    #def trace_droite(a, b)


#def drawline():
 #global x1, y1, x2, y2, coul
 #canvas.create_line(x1,y1,x2,y2,width=2,fill=coul)

def changecolor():
 "Changement aléatoire de la couleur du tracé"
 global coul
 pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
 c = randrange(8) # => génère un nombre aléatoire de 0 à 7
 coul = pal[c]

 #def drawline() et def changecolor() provient de SWINNEN_apprendre_python3_5.pdf

###########################
###########################
# calcul statistique
###########################
# fonction moyenne
def moyenne(serie):
    somme = 0
    for x in serie :
        somme = somme + x
    moyen = somme / len(serie)
    return moyen

# fonction variance
def variance(serie):
    m = sum(moyenne(serie)) / len(moyenne(serie))
    var = sum((c - m) ** 2 for c in moyenne(serie)) / len(moyenne(serie))
# programme trouvé  et modifier donc a vérifier
# il provient de https://askcodez.com/comment-puis-je-calculer-la-variance-dune-liste-en-python.html

# fonction covariance
#def covariance(serieX, serieY):
  # moyenne(serie)

# fonction corrélation
    #def  correlation(serieX, serieY)
   #covariance(serieX, serieY)
   #variance(serie)

# fonction forte corrélation
    #def forteCorrelation(serieX, serieY)
   #correlation()

# fonction calcul coefficient
    #def droite_reg(serieX, serieY)
###########################


# définition des widgets
racine = tk.Tk()
racine.title("fenetre stat")
canvas = tk.Canvas(racine, width=600, height=600, bg="white")
bouton_trace = tk.Button(racine, text="tracer la droite")
bouton_color = tk.Button(racine, text="autre couleur", command = changecolor)
bouton_quitter = tk.Button(racine, text="quitter", command = quit)
bouton_activer = tk.Button(racine, text="activer mode dessin")
bouton_desactiver = tk.Button(racine, text= "desactiver mode dessin")
canvas.grid(column=1, row=0, rowspan=10)
bouton_trace.grid(row=0)
bouton_color.grid(row=1)
bouton_quitter.grid(row=2)
bouton_activer.grid(row=3)
bouton_desactiver.grid(row=4)


# boucle principale
racine.mainloop()
