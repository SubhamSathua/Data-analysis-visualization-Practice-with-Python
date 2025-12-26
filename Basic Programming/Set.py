x = {1,2,3,4}
y = {5,6,7,8, 9, 0}
z = {7,8}

print(y-x)
print(y-z)
diff = z.symmetric_difference(y)
print(diff) 


a = set('abcdef')
b = set('klmnopqrstuvwxyz')

print(a, b)
result = a ^ b
print(sorted(result))


a = {12, 1,1,1,1,1,1,1,1}
print(a)

a.add(1000000)
# a.update([2], 111111)
a.remove(1)
a.pop()

print(a)


