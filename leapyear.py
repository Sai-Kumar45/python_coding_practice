year=int(input("enter year"))
if (year%400==0 or year%100!=0 and year%4==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
# n=int(input())
# sum=1
# for i in range(1,n+1):
#     sum+=i
# print(sum)