import turtle

def arbre(longueur, niveau):
    if niveau == 0:
        return
    turtle.forward(longueur)
    turtle.left(30)
    arbre(longueur * 0.7, niveau - 1)
    turtle.right(60)
    arbre(longueur * 0.7, niveau - 1)
    turtle.left(30)
    turtle.backward(longueur)

turtle.speed(0)
turtle.left(90)          # la tortue regarde vers le haut
arbre(100, 10)
turtle.done()