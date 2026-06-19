Hello={
    "a": 1,
    "b": 2,
    "c": 3
}

print(Hello.get("a",0))  # 1
print(Hello.get("d"))  # None
print(Hello.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(Hello.update({"d": 4}))
print(Hello)
