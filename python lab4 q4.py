string = input("Enter a string: ")
result = ' '.join([word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper() for word in string.split()])
print(result)
