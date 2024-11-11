# צבים

## התקנה של הספרייה turtle
נפתח את שורת הפקודה של חלונות (לוחצים על מקש מיקרוסופט פעם אחת ומקלידים "cmd") ונפעיל את הפקודה הבאה. 
```
pip install turtle
```

## תכנית דוגמא ראשונה
התכנית הבאה תפתח מסך חדש, תיצור "צב" אחד בשם t ותיצור קו ישר:

```
import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
```
## ציור ריבוע
```
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

```
import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

for i in range(120):
    t.left(3)
    t.forward(3)

```


