t = (1, 2, 3, 4, 4, 4, "a", "b", "b", "b", "b", "b")
print(t)

t2 = (7, 8, 9, 0, "x", "y", "z")
print(t2)

print(t2[1:8])
print(t[4:9:2])
print(t[-1:-10:-1])
print(t[-1:-5:-1])


tp = (1,2,3,4)
print("Tuple: ", tp)
# tp[0] = 12    # Error, no re assign as it's immuatable


# Duplicate remove
s = set(t)
tx = tuple(s)
print(f"No Duplicate: {tx}")