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
global actif
actif = True
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
def lit_fichier(nomfic):
    fic = open(nomfic,"r")
    s = fic.read()
    s.split()
    fic.close()
# a finir
    
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
    m = moyenne(serie)
    var = sum((c - m) ** 2 for c in serie) / len(serie)
    return var
# il provient de https://askcodez.com/comment-puis-je-calculer-la-variance-dune-liste-en-python.html

# fonction covariance
def covariance(serieX, serieY):
  m = moyenne()
  covar = (sum.y((c - m)** 2 for c in serieX))*(sum.x((e - m)** 2 for e in serieY))/ len(serieX)+ len(serieY)
  return covar
#a verifier

# fonction corrélation
def  correlation(serieX, serieY):
    r = covariance(serieX, serieY) / pow(variance(serieX)* variance(serieY))
    return r


# fonction forte corrélation
def forteCorrelation(serieX, serieY):
    r = correlation(serieX, serieY)
    if (r >= 0.8) or (r <= -0.8):
        return True
    else:
        return False  



# fonction calcul coefficient
def droite_reg(serieX, serieY):
    coeff_dir = covariance(serieX, serieY) / variance(serieX)
    ord_orig =  moyenne(serieY) - coeff_dir * moyenne(serieX)
    return(coeff_dir, ord_orig)
###########################

###########################
#mode dessin
#fonction dessin actif
def dessin_actif():
    global actif
    actif = True  
    print(actif)

def dessin_inactif():
    global actif
    actif = False
    print(actif)

#fontion clic de la souris
def clic_souris(event):
    global actif
    if actif == True:
        canvas.focus_set()
        x = event.x
        y = event.y
        canvas.create_rectangle(x,y, x+5, y+5, fill = "black")
        print(actif)
        lserieX = [x]
        lserieY = [y]
        print(lserieX , lserieY)
    else:
        print(actif)



# video: [Python] Souris avec tkinter


# définition des widgets
racine = tk.Tk()
racine.title("fenetre stat")
canvas = tk.Canvas(racine, width=600, height=600, bg="white")
bouton_trace = tk.Button(racine, text="tracer la droite", command = droite_reg)
bouton_color = tk.Button(racine, text="autre couleur", command = changecolor)
bouton_quitter = tk.Button(racine, text="quitter", command = quit)
bouton_activer = tk.Button(racine, text="activer mode dessin", command = dessin_actif)
bouton_desactiver = tk.Button(racine, text= "desactiver mode dessin", command = dessin_inactif)
if actif == True:
    canvas.bind("<Button-1>", clic_souris)
canvas.grid(column=1, row=0, rowspan=10)
bouton_trace.grid(row=0)
bouton_color.grid(row=1)
bouton_quitter.grid(row=2)
bouton_activer.grid(row=3)
bouton_desactiver.grid(row=4)


# boucle principale
racine.mainloop()
