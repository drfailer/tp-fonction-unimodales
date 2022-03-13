###############################################################################
# TITLE: Méthode par recherche dichotomique
# DESC: Test de la méthode par recherche dichotomique pour trouver un minimum
# local sur des fonctions unimodales.
###############################################################################

import numpy as np

###############################################################################
#                              variables globales                             #
###############################################################################
# precision
SIGMA = .000000000001



###############################################################################
#                                  fonction                                   #
###############################################################################
def dichotomie_min(f, a, b):
    xc = a + (b - a)/2
    fxc = f(xc)
    while b - a > SIGMA:
        xg = a + (b - a)/4
        xd = a + 3*(b - a)/4
        fxg = f(xg)
        fxd = f(xd)
        if fxc > fxd:
            a = xc
            fxc = fxd # on ne recalcul jamais fxc
            xc = xd
        elif fxc > fxg:
            b = xc
            fxc = fxg
            xc = xg
        else:
            a = xg
            b = xd

    return a


###############################################################################
#                                fonctions test                               #
###############################################################################
def f1(x):
    return abs(x - 100)

def f2(x):
    if x >= 50:
        return np.sqrt(x - 5)
    else:
        return np.sqrt(-(x - 50))


def f3(x):
    return min(4*x, x + 5)


def f4(x):
    return -x**3


###############################################################################
#                                    tests                                    #
###############################################################################
print("f1: ", dichotomie_min(f1, -1000.0, 1000.0))
print("f2: ", dichotomie_min(f2, -1000.0, 1000.0))
print("f3: ", dichotomie_min(f3, -1000.0, 1000.0))
print("f4: ", dichotomie_min(f4, -1000.0, 1000.0))
