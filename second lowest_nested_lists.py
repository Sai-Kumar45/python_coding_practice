n=int(input("enter the input: "))

scorelist=[]
names=[]
target=0
for _ in range(n):
    name = input()
    score = float(input())
        
    scorelist.append([name,score])
scorelist.sort(key= lambda x:x[1])
for i in scorelist:
    if i[1]>scorelist[0][1]:
        target=i[1]
        break
for i in scorelist:
    if i[1]==target:
        names.append(i[0])
            
names.sort()
for i in names:
    print(i)
