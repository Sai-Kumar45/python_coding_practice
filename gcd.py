num1 = 6
num2 = 12
gcd = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print( gcd)

def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)


num1 = 12
num2 = 6

print("GCD of", num1, "and", num2, "is", getGCD(num1, num2))