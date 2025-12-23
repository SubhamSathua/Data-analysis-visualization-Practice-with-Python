def checkPrime(n):
    
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

n = int(input("Enter a number: "))
value = checkPrime(n)

if value == False:
    print(f"{n} is not a prime number.")
else:
    print(f"{n} is a prime number.")

