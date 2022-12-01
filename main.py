import turtle

class STurtle(turtle.Turtle):
    def hgoto(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.speed(0)
# ['01010000', '01100001', '01111001', '01110100', '01101111', '01101110']

def main():
    t = STurtle()
    turtle.screensize(500, 500)
    screensize = turtle.screensize()
    screen = turtle.Screen()
    print(screensize)
    width, height = screensize

    screen.tracer(None)
    t.home()
    t.setheading(270)

    t.hgoto(0, height/2)

    i_x, i_y = t.pos()
    print(i_x, i_y)
    t.setheading(270)
    t.forward(110)

    turtle.exitonclick()

if __name__ == "__main__":
    #main()
    name = "Payton"
    bin_name = []
    for i in name:
        bin_name.append(str(format(ord(i), '08b')))
    print(bin_name)

    for i in bin_name:
        for j in range(len(i)):
            if i[j] == '1':
                print(i[j], end=" ")
        print()
