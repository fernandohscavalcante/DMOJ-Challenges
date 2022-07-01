words = input("Enter the words to count ")
def Convert(string):
    li=list(string.split(" "))
    return li   
wordlist = Convert(words)
print(len(wordlist))