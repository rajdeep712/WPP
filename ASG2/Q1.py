word = input("Enter a word : ")
newWord = ""
for index,letter in enumerate(word):
    if(index % 2 != 0):
        newWord+=str(letter.upper())
    else:
        newWord+=letter
        
print(newWord)