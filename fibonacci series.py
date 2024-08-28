#Fn = Fn-1 + Fn-2,where f0=0,f1=1

#using recursion method
def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))

num=int(input("enter a number"))
if num <=0:
    print("Please enter a Positive Number")
else:
    
    for n in range(num):
        print(fib(n))


#using normal method

# n=int(input("enter a number:"))
# a=0
# b=1
# if n==1:
#     print(a)
# elif n<0:
#     print("Please enter a positve number")
# else:   
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)

