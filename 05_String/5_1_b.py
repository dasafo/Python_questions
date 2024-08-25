# Create a string made of the middle three characters

# Write a program to create a new string made of the
# middle hree characters of an input string.

def middle_words(str1):
    mid = int(len(str1) / 2)
    res = str1[mid-1:mid+2]
    print(res)

print(middle_words("Schmetterling"))
