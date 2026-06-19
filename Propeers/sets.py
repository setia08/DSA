s1={1,2,3}
s1.add(4)
print(s1)


s2={1,2,3}
 

print(s1.union(s2))  # {1, 2, 3, 4}
print(s1.intersection(s2))  # {1, 2, 3}
print(s1.difference(s2))  # {4}
print(s2.difference(s1))  # set()
print(s1.symmetric_difference(s2))  # {4}