import turtle as t
import time

# Setup screen
screen = t.Screen()
screen.bgcolor("#a7c7e7")   # pastel blue background
screen.title("Cartoon Character with Glitter Eyes ✨")

pen = t.Turtle()
pen.speed(10)

# Function to draw a filled circle
def draw_circle(color, x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)  # adjust for turtle circle drawing
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# --- Background elements ---
# Grass
draw_circle("#0af50e", 0, -250, 300)

# Sun
draw_circle("#e2e213", 200, 180, 60)

# Clouds
draw_circle("white", -200, 150, 40)
draw_circle("white", -170, 150, 50)
draw_circle("white", -140, 150, 40)

# --- Face ---
draw_circle("#e9d606", 0, 0, 120)   # pastel peach face

# --- Eyes ---
# Left eye (white)
draw_circle("white", -50, 40, 15)
# Left pupil (black)
draw_circle("black", -40, 40, 7)
# Left sparkle ✨
draw_circle("white", -37, 45, 2)

# Right eye (white)
draw_circle("white", 50, 40, 15)
# Right pupil (black)
draw_circle("black", 40, 40, 7)
# Right sparkle ✨
draw_circle("white", 43, 45, 2)

# --- Mouth ---
pen.pensize(5)
pen.penup()
pen.goto(-50, -20)
pen.setheading(-60)
pen.pendown()
pen.circle(60, 120)   # smile arc

# --- Glitter Animation ✨ ---
def glitter(x, y):
    for i in range(3):  # blink 3 times
        # sparkle on
        draw_circle("white", x, y, 2)
        time.sleep(0.3)
        # sparkle off (cover with black again)
        draw_circle("black", x, y, 2)
        time.sleep(0.3)
    # final sparkle back on
    draw_circle("white", x, y, 2)

# Call glitter for both eyes
glitter(-37, 45)   # left eye sparkle
glitter(43, 45)    # right eye sparkle

pen.hideturtle()
screen.mainloop()
