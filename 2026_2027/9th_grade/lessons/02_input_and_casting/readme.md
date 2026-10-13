# קלט, המרות ועיגול

## מה נלמד

### קלט (input)

הפונקציה `input` מחכה שהמשתמש יקליד משהו וילחץ Enter, ומחזירה את מה שהוקלד.
כדי להסביר למשתמש מה להקליד, מדפיסים הודעה עם `print` לפני הקריאה ל-`input`.
חשוב: `input` תמיד מחזירה מחרוזת (string), גם אם המשתמש הקליד מספר.

```python
print("What is your name?")
name = input()
print("Hello, " + name)
```

[input ב-w3schools](https://www.w3schools.com/python/ref_func_input.asp)

### טיפוס (type)

לכל ערך בפייתון יש טיפוס. הפונקציה `type` מחזירה את הטיפוס של ערך:

- `str` - מחרוזת, טקסט
- `int` - מספר שלם
- `float` - מספר עשרוני

```python
print(type("hello"))   # <class 'str'>
print(type(7))         # <class 'int'>
print(type(7.5))       # <class 'float'>
```

[type ב-w3schools](https://www.w3schools.com/python/ref_func_type.asp)

### המרה (casting) למספר שלם - int

הפונקציה `int` ממירה ערך למספר שלם.
אם ממירים מספר עשרוני, החלק העשרוני נחתך (לא מעוגל!).
מחרוזת שנראית כמו מספר עשרוני אי אפשר להמיר ישירות ל-`int` - נקבל שגיאה.

```python
print(int("42"))     # 42
print(int(9.99))     # 9
```

[int ב-w3schools](https://www.w3schools.com/python/ref_func_int.asp)

### המרה למספר עשרוני - float

הפונקציה `float` ממירה ערך (מחרוזת או מספר שלם) למספר עשרוני.

```python
print(float("3.14"))   # 3.14
print(float(5))        # 5.0
```

[float ב-w3schools](https://www.w3schools.com/python/ref_func_float.asp)

### עיגול (rounding) - round

הפונקציה `round` מעגלת מספר.
עם ערך אחד היא מעגלת למספר שלם. אם מוסיפים מספר שני, הוא קובע כמה ספרות להשאיר אחרי הנקודה.

```python
print(round(3.7))          # 4
print(round(3.14159, 2))   # 3.14
```

[round ב-w3schools](https://www.w3schools.com/python/ref_func_round.asp)

### קלט של מספר

כדי לקבל מספר מהמשתמש, ממירים את מה ש-`input` החזירה:

```python
print("How old are you?")
age = int(input())
print(age + 1)
```

[המרות ב-w3schools](https://www.w3schools.com/python/python_casting.asp)

## מה יודפס?

נסו לנחש קודם, ורק אחר כך הריצו ובדקו. שימו לב: חלק מהשורות יגרמו לשגיאה.

```python
1.  print(type("10"))
2.  print(type(10))
3.  print(type(10.0))
4.  print(int("5") + int("5"))
5.  print("5" * 3)
6.  print(int("5") * 3)
7.  print(float("3"))
8.  print(int(10.9))
9.  print(type(int("10")))
10. print(type(int("10.1")))
11. print(int(float("10.1")))
12. print(round(7.4))
13. print(round(2.567, 2))
14. print(round(2.567, 1))
15. print(type(round(2.567, 2)))
```

בשאלות הבאות הקוד קורא קלט מהמשתמש. מה יודפס אם המשתמש מקליד את הערך שכתוב בהערה?

```python
# 16 - user types 15
print("How old are you?")
age = input()
print(age + age)
print(int(age) + int(age))
print(type(age))
```

```python
# 17 - user types 19.999
print("Price:")
price = float(input())
print(round(price, 2))
print(round(price))
print(int(price))
```

```python
# 18 - user types 7
print("Number:")
num = int(input())
num = num / 2
print(num)
print(type(num))
```

```python
# 19 - user types 3.5
print("Number:")
x = input()
print(int(x) + 1)
```

```python
# 20 - user types 4
print("Number:")
x = input()
y = x * 2
z = int(x) * 2
print(y)
print(z)
print(type(y))
```

## תרגיל: ממיר שקלים לדולרים

כתבו תוכנית שממירה שקלים לדולרים.

- שער הדולר קבוע: דולר אחד = 3.7 שקלים.
- התוכנית קוראת מהמשתמש שני מספרים שלמים: מספר השקלים ומספר האגורות (100 אגורות = שקל אחד).
- התוכנית מדפיסה את הסכום בדולרים, מעוגל ל-2 ספרות אחרי הנקודה.

דוגמת הרצה:

```
Shekels:
100
Agorot:
50
Dollars: 27.16
```

רמז: קודם חשבו את הסכום הכולל בשקלים (כמספר עשרוני), ורק אחר כך המירו לדולרים.

בונוס: הדפיסו גם את הטיפוס של כל משתנה בתוכנית.
