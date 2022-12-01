import turtle

class STurtle(turtle.Turtle):
    COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
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

    t.hgoto(-width/2, height/2)

    name = "Name Here"
    bin_name = []
    for i in name:
        bin_name.append(str(format(ord(i), '08b'))[1:])
    print(bin_name)

    t.setheading(270)
    offset_x = 50
    offset_y = 30

    for i in range(len(bin_name)):
        t.hgoto(-width/2 - 10, height/2 - i*offset_y)
        t.pencolor("black")
        t.write(name[i], move=True, align="left")

        for j in range(len(bin_name[i])):
            if bin_name[i][j] == '1':
                t.hgoto(-width/2 + j*offset_x, height/2 - i*offset_y)
                t.pencolor(t.COLORS[j])
                t.forward(20)

    i_x, i_y = t.pos()
    print(i_x, i_y)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
