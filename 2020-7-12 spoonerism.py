#Dominik Zimny
#12/7/2020
#spoonerism
word = input("Enter two words: ")
if word.count(" ") == 1:
    if word.replace(" ", "").isalpha():
        first = word[0]
        space = word.find(" ")
        second = word[space+1]
        word = list(word)
        word[0] = second
        word[space+1] = first
        word = "".join(word)
        print(word)
