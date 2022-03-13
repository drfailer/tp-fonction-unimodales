---
title: TP1 - Fonction unimodale
author: Rémi CHASSAGNOL
geometry: margin=2cm
---

# Méthode de recherche dichotomique

## Question 1

On sait que $x^{*} \in [ a_{k} ; b_{k} ]$ et $f$ unimodale donc pour monter que
pour chaque cas, cette propriété est conservée, il faut montrer que le nouvel
intervalle obtenu ) la fin de chaque cas est inclus dans $[ a_{k} ; b_{k} ]$ et
que $x^{*}$ se trouve bien dans la partie conservée.

1. $f(x^{C}_{k}) > f(x^{G}_{k}) \Rightarrow a_{k} = x^{C}_{k}, b_{k+1} = b_{k}$ et
   $x^{C}_{k+1} = x^{D}_{k}$
   On recherche un minimum local de $f$. Comme $f$ est **unimodale**, $f$
   n'admet qu'un seul minimum local sur $[ a_{k} ; b_{k} ]$ et le sens de
   variation de $f$ ne change qu'une fois sur cet intervalle, donc $f$ est
   décroissante sur $[ a_{k} ; y_{k} ]$ avec $y_{k} \in [ x^{C}_{k} ; b_{k} ]$
   (comme $f(x^{C}_{k}) > f(x^{D}_{k})$) et $x^{D}_{k} \in [ a_{k} ; b_{k} ]$.
   Donc si $a_{k+1} = x^{C}_{k}$ et $b_{k+1} = b_{k}$ alors, $x^{*} \in [ a_{k+1} ; b_{k+1} ]$
   et $f$ toujours unimodale sur $[ a_{k+1} ; b_{k+1} ]$, car
   $[ a_{k+1} ; b_{k+1} ] \subseteq [ a_{k} ; b_{k} ]$.
2. $f(x^{C}_{k}) > f(x^{G}_{k}) \Rightarrow a_{k+1} = a_{k}, b_{k+1} = x^{C}_{k}$.
   Même raisonnement que pour le premier cas mais sur l'autre partie de
   l'intervalle.
3. $f(x^{C}_{k}) \leqslant f(x^{D}_{k})$ et $f(x^{C}_{k}) \leqslant
   f(x^{G}_{k}) \Rightarrow a_{k+1} = x^{G}_{k}n b_{k+1} x^{D}_{k}$
   $f$ reste unimodale sur le nouvel intervalle nouvel intervalle est inclus
   dans l'ancien). De plus, comme $f$ unimodale, dans ce cas, on a forcement
   $x^{*} \in [ x^{G}_{k} ; x^{D}_{k} ]$ donc $x^{*} \in [ a_{k+1} ; b_{k+1} ]$

## Question 2

### Fonction de recherche dichotomique

```python
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
```

### Fonction de tests

```python
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
```

### Retour des tests

```python
print("f1: ", dichotomie_min(f1, -1000.0, 1000.0))
print("f2: ", dichotomie_min(f2, -1000.0, 1000.0))
print("f3: ", dichotomie_min(f3, -1000.0, 1000.0))
print("f4: ", dichotomie_min(f4, -1000.0, 1000.0))
```

retour:

```
f1:  99.99999999999964
f2:  49.999999999999375
f3:  -1000.0
f4:  999.9999999999991
```

# Méthode du nombre d'or

## Question 3

1. $f(x^{G}_{k}) > f(x^{D}_{k}) \Rightarrow a_{k+1} = x^{G}_{k}$
  - $[ a_{k+1} ; b_{k+1}  ] \in [ a_{k} ; b_{k}  ]$ comme l'intervalle est
    réduit, donc $f$ reste unimodale.
  - $f$ unimodale donc le sens de variation ne change qu'au plus une fois sur
    $[ a_{k} ; b_{k}  ]$ donc dans si $f(x^{G}_{k}) > f(x^{D}_{k})$ alors
    $x^{*} \in [ x^{G}_{k} ; b_{k} ]$ et donc $x^{*} \in [ a_{k+1} ; b_{k+1} ]$
2. Même raisonnement.
3. Ce cas se démontre de façon similaire à celui de la question 1.

## Question 4

$\alpha = \frac{w}{v} = \frac{b_{k} - a_{k}}{b_{k} - x^{G}_{k}} = \frac{b_{k} -
a_{k}}{x^{D}_{k} - a_{k}}$

Donc:

- $\alpha = \frac{b_{k} - a_{k}}{b_{k} - x^{G}_{k}} \Rightarrow b_{k} -
  x^{G}_{k} = \frac{b_{k} - a_{k}}{\alpha} \Rightarrow x^{G}_{k} = b_{k} -
  \frac{b_{k} - a_{k}}{\alpha}$
- $\alpha = \frac{b_{k} - a_{k}}{x^{D}_{k} - a_{k}} \Rightarrow x^{D}_{k} -
  a_{k} = \frac{b_{k} - a_{k}}{\alpha} \Rightarrow x^{D}_{k} = \frac{b_{k} -
  a_{k}}{\alpha} + a_{k}$

## Question 5

$\alpha = \frac{w}{v}$

On peu poser $w = 1$ et $v = \frac{2}{3} \Rightarrow \alpha = \frac{3}{2}$,
pour les 2 premiers cas et on aura $v = 3$ dans le troisième cas, donc
l'intervalle sera divisé par $3$.

## Question 6

Il faut calculer $f(x^{G}_{k})$ et $f(x^{D}_{k})$, donc la fonction $f$ est
appelée **2** fois.

## Question 7

Pour réduire l'intervalle au maximum, $x^{G}_{k}$ et $x^{D}_{k}$ doivent être
proche du centre ie, il faut réduire au maximum la distance $x^{D}_{k} -
x^{G}_{k}$.

## Question 8

$\alpha = \frac{w}{v} = \frac{v}{u}$ donc si on pose $a = v$ et $b = u$ alors
on a:

$\alpha = \frac{a + b}{a} = \frac{a}{b} \Rightarrow 1 + \frac{b}{a} = \frac{b}{a}$

Si on multiple cette équation par $\frac{a}{b}$ on obtient:

$\frac{a}{b} + 1 = (\frac{a}{b})^{2}$

On pose $X = \frac{a}{b}$ donc l'équation devient:

$\frac{a}{b}\alpha = X^{2} = X + 1$

ce qui donne le système suivant:

\begin{equation}
  \begin{cases}
  \frac{a}{b}\alpha = (\frac{a}{b})^{2} \\
  \frac{a}{b}\alpha = \frac{a}{b} + 1
  \end{cases}
  \Rightarrow
  \begin{cases}
  X\alpha = X^{2} \\
  X\alpha = X + 1
  \end{cases}
\end{equation}

Donc la solution est la valeur de $\alpha$. En résolvant $X^{2} -X - 1 = 0$, on
obtient:

$\alpha = \frac{1 + \sqrt{5}}{2} \approx 1.6180\dots$
