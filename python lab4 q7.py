string = input("Enter a string: ")
words = string.split()
print("The smallest word is:", min(words, key=len))
