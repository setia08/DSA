Name="Navneet"
print(f"Hello, {Name}!")

print(Name[1:3])

print(Name.lower())
print(Name.upper())
print(Name.replace("N","n"))
print(Name.split("v"))
print(Name.strip("a"))
print(Name.join("Hello"))

print('Hello,{}'.format(Name))


# what should i write code to explain diffrence between -> and ==
print(Name[1:3] == Name[1:3])
print(Name[1:3] is Name[1:3])


Name = "Hello"

a = Name[1:3]
b = Name[1:3]

print(a)        # el
print(b)        # el
print(a == b)   # True  — same value
print(a is b)   # False — different objects (different id)
print(id(a))    # e.g. 140234567890
print(id(b))    # e.g. 140234567920  ← different address!
