# prime number are only divisible by 1 and by it self are called prime numbers!


# n =int(input("enter the first number: "))

# if n<=1:
#     print("enter positive num")

# elif n==2:
#     print(f"{n} is a prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime")
#             break
#     else:
#         print("is a prime")


# print range of prime number example: 1 to 100

n=int(input("enter the first number"))
m=int(input("enter the last number"))
if n<0 and m<0:
    print("enter poitive number")
for number in range(n,m+1):
     if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)