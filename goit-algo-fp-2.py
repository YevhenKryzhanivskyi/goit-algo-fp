import turtle
import math

# Налаштування екрану
WIDTH, HEIGHT = 1000, 800
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Фрактальне дерево Піфагора")

# Налаштування пера
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("green")
t.pensize(1)

def draw_branch(length, level):
    # Базовий випадок рекурсії
    if level == 0 or length < 2:
        return

    # Малюємо основну гілку
    t.forward(length)

    # Зберігаємо поточну позицію і напрямок
    pos = t.position()
    heading = t.heading()

    # Ліва гілка
    t.left(45)
    draw_branch(length * 0.7, level - 1)

    # Повертаємось
    t.setposition(pos)
    t.setheading(heading)

    # Права гілка
    t.right(45)
    draw_branch(length * 0.7, level - 1)

    # Повертаємось назад
    t.setposition(pos)
    t.setheading(heading)
    t.backward(length)

def main():
    try:
        level = int(screen.numinput("Рівень рекурсії",
                                    "Введіть рівень рекурсії (рекомендовано 8–12):",
                                    default=10, minval=1, maxval=15))
    except Exception:
        level = 10

    # Початкова позиція
    t.penup()
    t.setposition(0, -HEIGHT // 2 + 50)
    t.setheading(90)  
    t.pendown()

    draw_branch(100, level)
    turtle.done()

if __name__ == "__main__":
    main()