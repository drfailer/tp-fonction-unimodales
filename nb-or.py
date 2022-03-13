###############################################################################
# TITLE: Méthode du nombre d'or
# DESC: Test de la méthode du nombre d'or pour trouver un minimum local sur des
# fonctions unimodales.
###############################################################################

import numpy as np

###############################################################################
#                              variables globales                             #
###############################################################################
# precision
SIGMA = .000000000001
ALPHA = (1 + np.sqrt(5))/2 # nombre d'or


###############################################################################
#                                  fonction                                   #
###############################################################################
def nb_or(f, a, b):
    xg = b - (b - a) / ALPHA # b - v
    xd = a + (b - a) / ALPHA # a + v
    fg = f(xg)
    fd = f(xd)
    while b - a > SIGMA:
        if fg > fd:
            a = xg
            xg, fg = xd, fd
            xd = a + (b - a) / ALPHA # a + v
            fd = f(xd)
        elif fg < fd:
            b = xd
            xd, fd = xg, fg
            xg = b - (b - a) / ALPHA # b - v
            fg = f(xg)
        else:
            a, b = xg, xd
            xg = b - (b - a) / ALPHA # b - v
            xd = a + (b - a) / ALPHA # a + v
            fg = f(xg)
            fd = f(xd)

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
print("f1: ", nb_or(f1, -1000.0, 1000.0))
print("f2: ", nb_or(f2, -1000.0, 1000.0))
print("f3: ", nb_or(f3, -1000.0, 1000.0))
print("f4: ", nb_or(f4, -1000.0, 1000.0))
