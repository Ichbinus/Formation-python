import turtle

t=turtle.Turtle()

def escalier(taille,nb):
    for i in range (0,nb):
        t.forward(taille)
        t.left (90)
        t.forward(taille)
        t.right (90)
    t.forward(taille)

escalier (30,5)

turtle.done()