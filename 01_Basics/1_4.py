# Remove first n characters from a string 
# Write a program to remove characters from 
# a string starting from zero up to n and 
# return a new string.

def remove_chars(word, n):
    x = word[n:]
    return x

print(remove_chars("Ananas", 3))
