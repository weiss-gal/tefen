# עבודת הגשה - מחשבון ריבית דריבית

מטרת המחשבון: 

המחשבון פועל באופן הבא

- קולט סכום כסף התחלתי
- עבור כל חודש:
  - קולט את הריבית באותו חודש, באחוזים. למשל 5.5
  - אם במקום מספר המשתמש כותב את המילה stop המחשבון מסיים את הפעולה ומפיק דוח
- מבנה הדוח:
  - מספר חודשים שנקלטו
  - סה"כ סכום כסף שהצטבר
  - רווח נקי (הסעיף הקודם פחות כמה התחלנו)


## דוגמא:

(שורות שמתחילו ב<< הן שורות שהמחשב כותב)

  ```
  >> What is the initial amount you deposit?
  1000
  >> What is the interest (ריבית) of month 1
  5.5
  >> What is the interest (ריבית) of month 2
  5
  >> What is the interest (ריבית) of month 3
  7
  >> What is the interest (ריבית) of month 4
  stop
  >>
  >>Summary:
  >>Amount Deposited: 1000
  >>Number of monthes: 3
  >>Total Amount: 1185.2825
  >>Profit: 185.2825
  ```

#  נוסחא לחישוב:

<img width="673" height="746" alt="image" src="https://github.com/user-attachments/assets/7a9ce519-c17c-47ca-b941-4302366b412f" />
