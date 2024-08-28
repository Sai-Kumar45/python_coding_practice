print(input("enter a number")[::-1])

num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    #remainder = num % 10
    reverse = (reverse * 10) + num%10
    num = num // 10

print("The Given number is {} and Reverse is {}".format(temp, reverse))