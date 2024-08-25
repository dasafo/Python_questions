# Write all content of a given file into a new 
# file by skipping line number 5

with open("test_2_6.txt", 'r') as text:
    lines = text.readlines()

with open('testWrite_2_6.txt', 'w') as text:
    count = 0
    for line in lines:
        if count == 4: #Skip the number 5
            count += 1
            continue
        else:
            text.write(line)
        count += 1
        


