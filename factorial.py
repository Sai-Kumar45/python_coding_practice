# # formula of factorial is (n!=n*n-1*n-2*n-3....1)

# # factorial using conditional statement
# num = int(input("Enter a number:"))    
# factorial = 1   
# if num < 0:    
#    print(" Factorial does not exist for negative numbers")    
# elif num == 0:    
#    print("The factorial of 0 is 1")    
# else:    
#    for i in range(1,num + 1):    
#        factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)

# num=int(input("enter the num "))
# n=1
# for i in range(1,num+1):
#    n=n*i
# print(n)
# # using built in function

# import math 
# n=int(input("enter a number:"))
# print(math.factorial(n))   

# #using recursion method

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# n=int(input("enter a number"))
# print(fact(n))

# # # using while loop

# n = int(input("enetr a number"))

# i = 1
# factorial = 1

# while i <= n:
#     factorial = i * factorial
#     i = i + 1
    
# print("The factorial of the given number is:", factorial)

f=int(input())
n=1
for i in range(1,f+1):
    n=n*i
print(n)