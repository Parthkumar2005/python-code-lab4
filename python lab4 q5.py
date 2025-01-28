string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
words1 = string1.split()
words2 = string2.split()
common_words = [word for word in words1 if word in words2]
print("Common words:", " ".join(common_words))
