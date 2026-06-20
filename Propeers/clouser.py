def outer(x):
    def inner(y):
        return x + y
    return inner


d5 = outer(5)
print(d5(10))  # Output: 15