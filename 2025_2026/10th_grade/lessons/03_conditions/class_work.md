# תרגיל: רכבת הרים 🎢  

בתרגיל הזה נבנה בהדרגה תוכנית שבודקת אם מותר למשתמש לעלות על רכבת הרים. בכל שלב נוסיף עוד תנאים וכללים.  

---

### שלב 1 – קבלת שם  
בקשו מהמשתמש להקליד את שמו.  
הציגו לו הודעת שלום, לדוגמה:  

What is your name? Dan
Hello Dan


---

### שלב 2 – הוספת גיל  
בקשו מהמשתמש להקליד את גילו.  
הציגו לו הודעה שמחזירה את מה שהכניס, למשל:  

How old are you? 15
You are 15 years old


---

### שלב 3 – תנאי ראשון (גיל)  
בדקו: אם המשתמש בן 12 ומעלה – הוא יכול לעלות. אחרת – הוא לא יכול.  
דוגמאות:  

How old are you? 14
You are 14 years old
You can ride the rollercoaster!

How old are you? 10
You are 10 years old
Sorry, you are too young.


---

### שלב 4 – הוספת גובה  
בקשו מהמשתמש גם את הגובה שלו בס"מ.  
כדי לעלות צריך גם להיות לפחות בגובה 140 ס"מ.  
דוגמאות:  

How old are you? 13
How tall are you (in cm)? 145
You can ride the rollercoaster!

How old are you? 13
How tall are you (in cm)? 130
Sorry, you are not tall enough.


---

### שלב 5 – מקרה מיוחד: גבוהים במיוחד  
אם המשתמש צעיר מגיל 12, אבל גבוה מ־160 ס"מ – בכל זאת לאפשר לו לעלות.  
דוגמאות:  

How old are you? 11
How tall are you (in cm)? 165
You are unusually tall — you can ride!

How old are you? 11
How tall are you (in cm)? 150
Sorry, you are too young and not tall enough.


---

### שלב 6 – אישור הורים  
אם המשתמש בן 10 עד 11 (כלומר בין 10 ל־12) ויש לו אישור הורים – לאפשר לו לעלות.  
דוגמאות:  

How old are you? 11
How tall are you (in cm)? 150
Do you have parental permission (yes/no)? yes
Great, with permission you can ride!

How old are you? 11
How tall are you (in cm)? 150
Do you have parental permission (yes/no)? no
Sorry, without permission you cannot ride