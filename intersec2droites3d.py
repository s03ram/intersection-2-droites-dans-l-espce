"""
Source N. Reveret
Modifié par seram03
"""
# import itertools

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Point ({self.x} ; {self.y} ; {self.z})"

    def __repr__(self):
        return self.__str__()


class Vecteur:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vecteur ({self.x} ; {self.y} ; {self.z})"

    def __repr__(self):
        return self.__str__()

    def coordonnees(self):
        return (self.x, self.y, self.z)



class Droite:
    """une droite est définie par un point et un vecteur directeur
    """
    def __init__(self, point_origine, vecteur_directeur):
        self.point_origine = point_origine
        self.vecteur_directeur = vecteur_directeur


def vecteur_depuis_points( a, b):
    """Créé un vecteur avec deux points 
    (pas forcément utile ici mais on sait jamais)

    Args:
        a (Point)
        b (Point)

    Returns:
        Vecteur
    """
    x = b.x - a.x
    y = b.y - b.y
    z = b.z - a.z
    return (x, y, z)


def paralleles(d1, d2):
    """vérifie si deux droites sont parallèles

    Args:
        d1 (Droite)
        d2 (Droite)

    Returns:
        bool: True si d1 et d2 sont parallèles, False sinon
    """
    (x1, y1, z1) = d1.vecteur_directeur.coordonnees()
    (x2, y2, z2) = d2.vecteur_directeur.coordonnees()
    d1 = x1 * y2 - x2 * y1
    d2 = x1 * z2 - x2 * z1
    d3 = y1 * z2 - y2 * z1
    return d1 == 0 and d2 == 0 and d3 == 0


def colineaires(v1, v2):
    """vérifie si deux vecteurs sont colinéaires

    Args:
        v1 (Vecteur)
        v2 (Vecteur)

    Returns:
        bool: True si v1 et v2 sont colinéaires, False sinon
    """
    return v1.x/v2.x == v1.y/v2.y == v1.z/v2.z


def secantes(d1, d2):
    """vérifie si deux droites sont sécantes 
    (on considère que des droites confondues sont sécantes)

    Args:
        d1 (Droite)
        d2 (Droite)

    Returns:
        bool: True si d1 et d2 sont sécantes, False sinon
    """
    # on vérifie si les droites sont confondues
    if paralleles(d1, d2):
        vecteur_AB = vecteur_depuis_points(d1.point_origine, d2.point_origine)  # on calcule le vecteur entre les points
                                                                                #    d'origine des deux droites.
        vecteur_d1 = d1.vecteur_directeur
        if vecteur_AB.x * vecteur_d1.y == vecteur_AB.y * vecteur_d1.x :         # si les deux sont colinéaires alors
                                                                                #    les droites sont confondues
            return True
    
    # on vérifie si les droites sont sécantes
        
    



if __name__ == '__main__':
    u1 = Vecteur(1, 2, 3)
    u2 = Vecteur(2, 4, 6)
    A = Point(0, 0, 0)
    B = (1, 1, 3)
    d1 = Droite(A, u1)
    d2 = Droite(B, u2)

    assert paralleles(d1, d2)


    """
    taille=2

    As = [k for k in range (-2,3)]
    Bs = [k for k in range(-2,3)]
    Cs = [k for k in range(-2,3)]

    droites = [Droite(A,B,C) for(A,B,C) in itertools.product(As,Bs,Cs)]
    """