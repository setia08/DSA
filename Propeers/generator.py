def fibonacci(n):
    if n>0:
        return n*fibonacci(n-1)
    return 1


print(fibonacci(5))  # Output: 120