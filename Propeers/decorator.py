def my_decorator(function):
    def wrapper(*args,**kwargs):
        print("Before the function call")
        result = function(*args,**kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Navneet")
