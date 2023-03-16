# this function will print all the numbers from 'start' to 'stop'
# example:
# type the first number: -1
# type the last number: 3
# -1
# 0
# 1
# 2
# 3

def print_nums(first, last):
    for i in range(first, last, 1):
        print(i)

first = int(input("type the first number: "))
last = int(input("type the last number: "))

print_nums(first, last)

