##############
# Groupe 3 -- projet "statistique"
# Ceylia DUPIN 
# Louis REBECHE
# https://github.com/uvsq22001048/-projet-stat
##############

#import des librairies 
import tkinter as tk
import random as rd

# définition des widgets
racine = tk.Tk()
racine.title("fenetre stat")
canvas = tk.Canvas(racine, width=600, height=600, bg="white")
bouton_trace = tk.Button(racine, text="tracer la droite")
bouton_color = tk.Button(racine, text="autre couleur")
bouton_quitter = tk.Button(racine, text="quitter", command = quit)
canvas.grid(column=1, row=0, rowspan=10)
bouton_trace.grid(row=0)
bouton_color.grid(row=1)
bouton_quitter.grid(row=2)

# boucle principale
racine.mainloop()
