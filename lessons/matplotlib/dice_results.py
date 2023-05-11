import random as rnd
import matplotlib.pyplot as plt

ATTEMPTS = 10000

dice_num = int(input("How many dice would you like to roll? "))


max_x = dice_num * 6

x_values = range(max_x + 1)
abs_results = [0 for i in range(max_x + 1)]


for attempt in range(ATTEMPTS):
    dice_result = 0
    for dice in range(dice_num):
        dice_result += rnd.randint(1, 6)
    
    abs_results[dice_result] += 1

y_values = [i / ATTEMPTS for i in abs_results]
plt.bar(x_values, y_values)
plt.show()

