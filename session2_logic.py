# Booleans always only return either FALSE or TRUE
print(1 == 1)

print(True == True)

print(False == False)

print(10 > 10)

print((9 >= 10) and (1==1))

print((9 >= 10) or (1==1))

print(True and True and False)

# Change this variable for different outputs
temperature = 27

if temperature > 30:
    print("it's too hot")
elif temperature > 25:
    print("it's good")
else:
    print("it's cold actually")

# Increment
def increment(a):
    return (a+1)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in a:
    print(str(num) + " is a prime")

def isPrime (num):
    for divCan in list(range(2, num)):
        if (num % divCan == 0):
            return False
        return True

for num in a:
    if isPrime(num):
        print(str(num) + ' is a prime')
    else:
        print(str(num) + ' is not a prime')
