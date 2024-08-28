s=input("enter the input: ")
v={'a','e','i','o','u','A','E','I','O','U'}
r=' '
for i in range(len(s)):
    if s[i]  not in v:
        r+=s[i]
print(r)



# using list comprehension method

# s=input("enter the input: ")
# v='aeiouAEIOU'
# output=''.join([char for char in s if char not in v])
# print(output)