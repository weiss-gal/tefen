def print_template_1(n):
    if n == 0:
        return

    print_template_1(n-1)
    print("\\" * n) # print the character '\' n-times

def print_template_2(n):
    if n == 0:
        return

    print("/" * n) # print the character '/' n-times
    print_template_2(n-1)

print_template_1(10)
print_template_2(10)
