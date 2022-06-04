from intersec2droites3d import *
from random import randint
from itertools import combinations
from time import time

"""
structure de la liste droites[]:
[Droite( Point(x,y,z), Vecteur(x,y,z) ), Droite( (Point(x,y,z), Vecteur(x,y,z) ) , ...from infinite to beyond...]
"""
debut = time()
droites = []
nb_de_droites = 1_000
for _ in range(nb_de_droites):
    coord_pt = Point(randint(-9,9), randint(-9,9), randint(-9,9))
    coord_vect = Vecteur(randint(-9,9), randint(-9,9), randint(-9,9))
    while coord_vect == (0,0,0):
        coord_vect = Vecteur(randint(-9,9), randint(-9,9), randint(-9,9))
    droites.append(Droite(coord_pt,coord_vect))

""" on est sûr que ces deux-là sont sécantes
droites.append(Droite(Point(5, 4, 2),Vecteur(6, -1, 5)))
droites.append(Droite(Point(9, 0, 7),Vecteur(2, 1, 1)))
"""

secantes = 0
nb_comp = 0
for A,B in combinations(droites, 2):
    nb_comp += 1
    if sont_secantes(A, B):
        secantes += 1
        
fin = time()
print("pour", nb_de_droites,"droites")
print ("temps de calcul =", fin-debut,'s')
print ("comparaisons =", nb_comp)
print("droites sécantes =",secantes)
print("ratio =",secantes/nb_comp)
