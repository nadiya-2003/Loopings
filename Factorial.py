
def is_factorial(n):
    if n < 1:
        return False
    factorial = 1
    i = 1
    while factorial < n:
        i += 1
        factorial *= i   
    return factorial == n
n = int(input())
if is_factorial(n):
    print("Yes")
else:
    print("No")
