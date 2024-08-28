def is_harshad(n):
    num=list(str(n))
    n_sum=0
   
    for i in num:
        n_sum+=int(i)
    return n_sum

def is_true(n):
    if n% is_harshad(n)==0:
        return f"{n} is harshad number!"
    else:
        return "not an harshad"
num=is_true(int(input()))

print(num)




