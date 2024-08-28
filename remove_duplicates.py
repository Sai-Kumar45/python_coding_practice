a=input("enter the input: ")

d=''
for i in range (len(a)):
    if a[i] not in d:
        d+=a[i]
print(d)

