tech = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(tech[:])
print(tech[2:])
print(tech[0:])
print(tech[2:7])
print(tech[0:2121])
print(tech[0:13:])
print(tech[0::3])

print(tech[-1:-7:-1])
"""Reverse :
0   1  2  3  4
A   B  C  D  E
-5 -4 -3 -2 -1
"""

# Duplicate values remove from List
demo_list = [2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9]
print(demo_list)
unique = list(set(demo_list))
print(unique)
