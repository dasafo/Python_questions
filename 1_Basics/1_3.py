# Print characters from a string that are present at an even index number



def even_string():
    
    sentence = input('Enter you word or sentence: ')
    for i in range(0, len(sentence)-1, 2):
        print("Index: [", i, "]", sentence[i])

print(even_string())
