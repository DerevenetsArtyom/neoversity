import math
import turtle


def draw_tree(branch_length, level, t):
    if level > 0:
        t.forward(branch_length)

        angle = 45
        t.left(angle)
        draw_tree(branch_length * math.sqrt(2) / 2, level - 1, t)

        t.right(2 * angle)
        draw_tree(branch_length * math.sqrt(2) / 2, level - 1, t)

        t.left(angle)
        t.backward(branch_length)


def main():
    while True:
        try:
            recursion_level = int(input("Введіть рівень рекурсії (1-9): "))
            if 0 < recursion_level < 10:
                break
            else:
                print("Рівень рекурсії повинен бути більше 0 але менше 10")
        except ValueError:
            print("Введіть ціле число в діапазоні від 1 до 9")

    screen = turtle.Screen()
    t = turtle.Turtle()

    t.left(90)
    t.speed(0)

    draw_tree(100, recursion_level, t)

    screen.exitonclick()


if __name__ == "__main__":
    main()
