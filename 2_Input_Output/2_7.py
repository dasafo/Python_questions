#Accept any three string from one input() call

# Write a program to take three names as input from 
# a user in the single input() function call.

def three_words():
    word1, word2, word3 = input("introduce three words: ").split()
    print("Word 1:", word1)
    print("Word 2:", word2)
    print("Word 3:", word3)

three_words()
