def frequency_char(input_str):
    if not input_str:
        return "enter the valid input"
    res=""
    count=1
    char_order=sorted(list(input_str))
    sorted_str="".join(char_order)
    input_str=sorted_str
    for i in range(len(input_str)):
        if (i+1<len(input_str) and input_str[i]==input_str[i+1]):
            count+=1
        else:
            res+=input_str[i]+str(count)
            count=1
    return res
input_str="aaabaabbc"
print(frequency_char(input_str))