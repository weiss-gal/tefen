# עבודת בית – חישוב עלות קנייה ותשלומים

## מטרת העבודה
לכתוב תוכנה שתעזור לנו לחשב את עלות המוצרים במכולת/סופר ואת גודל התשלומים.

## דרישות
1. התוכנה תקלוט **שלושה מוצרים**.  
   לכל מוצר יש להזין:
   - שם המוצר  
   - מחיר המוצר (בשקלים ואגורות)  
   - כמות מהמוצר  

2. לאחר הקליטה התוכנה תציג "חשבון" הכולל:  
   - שורה לכל מוצר עם פירוט: שם, כמות, מחיר ליחידה, מחיר כולל  
   - שורת **סיכום** עם הסכום הכולל לתשלום  

3. בשלב הבא התוכנה תשאל: **"כמה תשלומים לעשות?"** 
   - המשתמש יקליד מספר שלם (מספר התשלומים).  
   - אם המשתמש הקליד _1_ התכנה תדפיס הודעה בסגנון הבא
     - Total payment: 100
   - לעומת זאת, אם המשתמש יקליד מספר גדול מ1 התכנה תדפיס הודעה בסגנון הבא:
     - Each payment: 50
   - שימו לב שכדי לחשב את גודל התשלום יש לחלק את הסכום במספר התשלומים
   

## דוגמה 1 - עם תשלומים
```
Enter product 1 name: Bread
Enter product 1 price (₪): 5.90
Enter product 1 quantity: 2

Enter product 2 name: Milk
Enter product 2 price (₪): 7.20
Enter product 2 quantity: 1

Enter product 3 name: Cheese
Enter product 3 price (₪): 12.50
Enter product 3 quantity: 3

Product: Bread | Quantity: 2 | Price per unit: 5.90 | Total: 11.80
Product: Milk  | Quantity: 1 | Price per unit: 7.20 | Total: 7.20
Product: Cheese | Quantity: 3 | Price per unit: 12.50 | Total: 37.50
---------------------------------------------------
Grand Total: 56.50 ₪

How many payments? 2
Each payment: 28.25 ₪

```

## דוגמא 2 - תשלום אחד
```
Enter product 1 name: Bread
Enter product 1 price (₪): 5.90
Enter product 1 quantity: 2

Enter product 2 name: Milk
Enter product 2 price (₪): 7.20
Enter product 2 quantity: 1

Enter product 3 name: Cheese
Enter product 3 price (₪): 12.50
Enter product 3 quantity: 3

Product: Bread | Quantity: 2 | Price per unit: 5.90 | Total: 11.80
Product: Milk  | Quantity: 1 | Price per unit: 7.20 | Total: 7.20
Product: Cheese | Quantity: 3 | Price per unit: 12.50 | Total: 37.50
---------------------------------------------------
Grand Total: 56.50 ₪

How many payments? 1
Total payment: 56.50 ₪

```

