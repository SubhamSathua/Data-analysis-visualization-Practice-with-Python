n = int(input("Enter a number: "))
# n = 153
size = len(str(n))
# print(size)
sum = 0
v = str(n)
 
i = 0
while i < size:
    # print(n)
    temp = int(v[i])**size
    sum += temp
    i += 1

if sum == n:
    print(f"{n} is a Amstrong number.")
else:
    print(f"{n} is not a Amstrong number.")
'''
n[i]**size
'''