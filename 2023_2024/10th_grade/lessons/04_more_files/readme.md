# קבצים - תרגול בכתה

## קריאת קובץ שלם 
בתרגיל זה נקרא את כל הקובץ ב"מכה אחת" ואז נדפיס למסך את מספר המילים, מספר השורות, מספר התווים בקובץ ואת הטקסט עצמו. 

כדי להתחיל, הורידו את הקובץ 
[yesterday.txt](https://github.com/weiss-gal/data_science_project/blob/main/2023_2024/10th_grade/lessons/04_more_files/yesterday.txt)
לתוך הספרייה בה אתם עובדים (חייבת להיות אותה ספרייה בה אנחנו שומרים את קובץ הפייתון)

בשלב ראשון, נקרא את כל הקובץ באופן הבא:

```
file_name = "./yesterday.txt"

print(f"Opening file {file_name} ...")
print() # empty line for readability 

f = open(file_name)
file_contents = f.read()

print(file_contents)
f.close()
```

כשנריץ את הקובץ, אנחנו אמורים לקבל את התוכן שלו על המסך

כפי שאפשר לראות 


