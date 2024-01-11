def function_c(n):
    print(n)

def function_b(n):
    print(n)
    function_c(n-1)

def function_a(n):
    print(n)
    function_b(n-1)

function_a(10)
