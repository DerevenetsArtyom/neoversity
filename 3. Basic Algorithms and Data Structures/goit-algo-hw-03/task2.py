import turtle


def koch_curve(t, level, size):
    if level == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, level - 1, size / 3)
            t.left(angle)


def koch_snowflake(t, level, size):
    for _ in range(3):
        koch_curve(t, level, size)
        t.right(120)


def main():
    screen = turtle.Screen()
    screen.title("Koch Snowflake")

    screen.setup(800, 800)
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.color("white")
    t.goto(-300, 173)
    t.pendown()

    level = int(input("Enter the recursion level (recommended 0-5): "))

    koch_snowflake(t, level, 600)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
