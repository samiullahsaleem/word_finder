#This a word finder program which can find the word which you want to know in the whole text
print("Welcome to word finder program")
text = input("Paste here your text!\n")
print("Please type your word now")
word = input("Type the word!")
location = text.find(word)
print("Location of your word is "+ str(location))

Enter = input("Press any key to exit!")
