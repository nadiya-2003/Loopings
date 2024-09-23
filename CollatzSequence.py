

n = int(input())
count = 0
print(n)
while n != 1:
    if n % 2 == 0:
        n = n // 2  # n is even
    else:
        n = 3 * n + 1  # n is odd
    print(n)  # Print the current number
    count += 1
print(count + 1)  # Including the final step to reach 1
