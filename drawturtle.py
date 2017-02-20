import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.lt(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    branden = turtle.Turtle()
    branden.shape('turtle')
    branden.speed(2)
    branden.color('blue')

    for i in range(1,37):
        draw_square(branden)
        branden.right(10)




    #joshua = turtle.Turtle()
    #joshua.shape('arrow')
    #joshua.circle(100)



    window.exitonclick()

draw_art()

   

