# half pyramid
# n=int(input("enter num"))

# for i in range(n+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# n=int(input("enter num"))

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


num_rows = 5

# Loop through each row
for i in range(num_rows):
    # Print spaces before the stars
    for j in range(num_rows - i - 1):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line after printing each row
    print()


    