# צבים

## התקנה של הספרייה turtle
נפתח את שורת הפקודה של חלונות (לוחצים על מקש מיקרוסופט פעם אחת ומקלידים "cmd") ונפעיל את הפקודה הבאה. 
```bash
pip install turtle
```

## תכנית דוגמא ראשונה
התכנית הבאה תפתח מסך חדש, תיצור "צב" אחד בשם t ותיצור קו ישר:

```python
import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
```
## ציור ריבוע
```python
import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

for i in range(4):
    t.left(90)
    t.forward(100)

```

## ציור מעגל
באמצעות לולאה ומספר גדול של פניות נצייר מעגל בקירוב:

```pyhton
import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

for i in range(120):
    t.left(3)
    t.forward(3)

```

## ציור בצבעים
באמצעות הפקודה color ניתן לבחור את הצבע על ידי שימוש בשם הצבע כמחרוזת, ניתן גם להעביר שלושה פרמטרים עבור RGB (מספרים בין 0 ל 255)

```python
import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'indigo', 'violet']

color_index = 0
for i in range(60):
    for i in range(120):
        t.color(rainbow_colors[color_index])
        t.left(3)
        t.forward(3)
        
    t.left(6)
    color_index = (color_index+1) % len(rainbow_colors)


```

## הרמת ה"עט" והורדה
באמצעות הפקודות up ו down ניתן לבחור אם הצב מצייר כאשר הוא נע או לא. נשתמש בכך כדי ליצור סדרת פסים:

```python
import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# Move to the left side of the screen and point up
t.up()
t.left(180)
t.forward(200)
t.right(90)


for i in range(30):
    t.down()
    t.forward(100)
    t.up()
    t.right(175)
    t.forward(99)
    t.left(175)
```

## סתם דוגמא מעניינת

```python
import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

turtle.colormode(255) # set the turtle to work with 1-255 as color levels
num_of_triangles = 120
size = 10
color_level = 255 - num_of_triangles

for i in range(num_of_triangles):
    t.color(color_level, 0, 0)
    t.forward(size)
    t.left(60)

    t.color(0, color_level, 0)
    t.forward(size)
    t.left(60)

    t.color(0,0, color_level)
    t.forward(size)
    t.left(120)
    
    t.right(3)
    color_level+=1
    size+=1

```
