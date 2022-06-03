"""
Source N. Reveret
Modifié par seram03
Avec l'aide de Verdurin
"""


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


def vecteur_depuis_points(a, b):
    """Créé un vecteur avec deux points

    Args:
        a (Point)
        b (Point)

    Returns:
        Vecteur
    """
    x = b.x - a.x
    y = b.y - b.y
    z = b.z - a.z
    return Vecteur(x, y, z)


def sont_colineaires(v1, v2):
    """vérifie si deux vecteurs sont colinéaires

    Args:
        v1 (Vecteur)
        v2 (Vecteur)

    Returns:
        bool: True si v1 et v2 sont colinéaires, False sinon
    """
    det1 = v1.x*v2.y-v2.x*v1.y
    det2 = v1.y*v2.z-v2.y*v1.z
    det3 = v1.x*v2.z-v2.x*v1.z
    return det1 == 0 and det2 == 0 and det3 == 0


def sont_paralleles(d1, d2):
    """vérifie que deux droites sont parallèles

    Args:
        d1 (Droite)
        d2 (Droite)

    Returns:
        bool: True si oui, False sinon
    """
    return sont_colineaires(d1.vecteur_directeur, d2.vecteur_directeur)


def sont_coplanaires(v1, v2, v3):
    a = v1.x*v2.y*v3.z + v2.x*v3.y*v1.z + v3.x*v1.y*v2.z
    b = v1.x*v3.y*v2.z + v3.x*v2.y*v1.z + v2.x*v1.y*v3.z
    return a-b == 0


def sont_secantes(d1, d2):
    """vérifie si deux droites sont sécantes 
    (on considère que des droites confondues sont sécantes)

    Args:
        d1 (Droite)
        d2 (Droite)

    Returns:
        bool: True si d1 et d2 sont sécantes, False sinon
    """
    # on vérifie si les droites sont coplanaires
    vecteur_d1 = d1.vecteur_directeur
    vecteur_d2 = d2.vecteur_directeur
    vecteur_AB = vecteur_depuis_points(d1.point_origine, d2.point_origine)  # on calcule le vecteur entre les points
                                                                            #    d'origine des deux droites.
    print("let's go")
    if sont_coplanaires(vecteur_d1, vecteur_d2, vecteur_AB):
        # on vérifie si les droites sont parallèles
        if sont_paralleles(d1, d2):
            # on vérifie ensuite si elles sont confondues
            if vecteur_AB.x * vecteur_d1.y == vecteur_AB.y * vecteur_d1.x:          # si AB et d1 sont colinéaires alors
                                                                                    #    les droites sont confondues
                return True
            return False
        return True
    return False


if __name__ == '__main__':
    u1 = Vecteur(6, -1, 5)
    u2 = Vecteur(2, 1, 1)
    A = Point(5, 4, 2)
    B = Point(9, 0, 7)
    d1 = Droite(A, u1)
    d2 = Droite(B, u2)

    assert sont_secantes(d1, d2)
