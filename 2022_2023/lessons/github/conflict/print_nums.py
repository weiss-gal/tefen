import random as rnd


# this function will print all the numbers from 'start' to 'stop'
# example:
# type the first number: -1
# type the last number: 3
# -1
# 0
# 1
# 2
# 3

def print_nums(start, stop):
    for i in range(start, stop + 1, 1):
        print(i)

start = int(input("type the first number: "))
stop = int(input("type the last number: "))

print_nums(start, stop)

