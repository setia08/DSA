d1={
    'a': 1,
    'b': 2,
    'c': 3
}

d2={k:v**2 for k,v in zip(d1.keys(),d1.values())}
print(d2)

