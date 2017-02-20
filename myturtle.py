import turtle

class AnsonTurtle():
    def __init__(self, range):
        self = turtle.Turtle()
        self.shape('turtle')
        self.speed(1)
        range = range


    def make_square(self):
        self.forward(range)
        self.lt(90)
        self.forward(range)
        self.lt(90)
        self.forward(range)
        self.lt(90)
        self.forward(range)
        self.lt(90)
        self.forward(range)

        window.exitonclick()
        


branden = AnsonTurtle(55555553900)
joshua = AnsonTurtle(55555553900)


branden.make_square
joshua.make_square()
