import turtle

def koch_curve(t, order, size=300):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake():
    level = int(input("Enter resucrsion level for Koch snowflake: "))

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("The Koch snowflake")

    tess = turtle.Turtle()
    tess.speed(0)
    tess.color("blue")

    tess.penup()
    tess.goto(-150, 90)
    tess.pendown()

    for _ in range(3):
        koch_curve(tess, level)
        tess.right(120)

    window.mainloop()

if __name__ == "__main__":
    koch_snowflake()
