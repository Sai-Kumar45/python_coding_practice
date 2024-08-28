# print the count words in given string
def countwords(sentence):
    c=sentence.split()
    return len(c)
sen=countwords("hello world")
print(sen)