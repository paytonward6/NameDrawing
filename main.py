import turtle

class STurtle(turtle.Turtle):
    COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]

    def hgoto(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()

    def dwrite(self, string, dfont=('Arial', 15, 'normal')):
        self.write(string, move=False, align="left", font=dfont)

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.speed(0)

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

    t.hgoto(-width/2, height/2)

    name = "Your Name"
    bin_name = []
    for i in name:
        bin_name.append(str(format(ord(i), '08b'))[1:])
    print(bin_name)

    t.setheading(270)
    offset_x = 50
    offset_y = 30
    pensize = 10
    t.pensize(pensize)  

    for i in range(len(bin_name)):
        t.hgoto(-width/2 - 20, height/2 - i*offset_y - offset_y/2)
        t.pencolor("black")
        if name[i] == " ":
            t.dwrite("_")
        else:
            t.dwrite(name[i])

        for j in range(len(bin_name[i])):
            if bin_name[i][j] == '1':
                t.hgoto(-width/2 + j*offset_x, height/2 - i*offset_y)
                t.pencolor(t.COLORS[j])
                t.forward(20)

    i_x, i_y = t.pos()

    turtle.exitonclick()

if __name__ == "__main__":
    main()
