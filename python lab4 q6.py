string = input("Enter a string: ")
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
string = string.lower()
for char in string:
    if char in vowel_count:
        vowel_count[char] += 1
for vowel, count in vowel_count.items():
    print(f"Frequency of '{vowel}': {count}")
