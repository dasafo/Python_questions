# Write a program to find how many times substring
# “Emma” appears in the given string.

# with COUNT() method
sentence = input("Enter the sentence with Emma several times: ")

cnt = sentence.count("Emma")
print("Emma: ", cnt)

# without count()
print("************", "\n")
def emma_count(sentence):
    count = 0

    for i in range(len(sentence)-1):
        count += sentence[i: i + 4] == "Emma"  # 4 words in Emma
    return count

count = emma_count("Emma doesnt anything about the other Emma.")
print(count, " times Emma show up in the sentence.")
