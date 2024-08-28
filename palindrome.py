# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
#In simpler terms, it's something that remains unchanged when its characters are reversed.


p=input("enter the input: ")
reverse=p[::-1]
r=reverse
if reverse==p:
    print("palindrome:",r)
else:
    print("not palindrome")