s=input()
time=s[0:2]
n=s[2:8]
y=s[:8]
PM_AM=s[-2]

if 'P' in PM_AM:
    if time!='12':
        p=int(s[0:2])+12
        print(str(p)+n)
    else:
        print(y)

else:
    if 'A' in PM_AM:
        if time[0:2]=='12':
            print("00"+n)
        else:
            print(y)
