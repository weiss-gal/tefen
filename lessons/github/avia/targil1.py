# you mission, should you choose to accept it, is to fix the following function.
# here are the steps:
# 1. read the function description 
# 2. run the code 
# 3. find the bug 
# 4. fix the bug
# 5. push the fix back to github


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
    for i in range(start, stop, 1):
        print(i)

start = int(input("type the first number: "))
stop = int(input("type the last number: "))

print_nums(start, stop+1)

