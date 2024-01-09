# Read line number 4 from the following file
# test.txt file:

# line1
# line2
# line3
# line4
# line5
# line6
# line7

with open("test_2_10.txt", "r") as file:
    count = 0
    lines = file.readlines()
    for line in lines:
        if count == 3:
            print(line)
            break
        else:
            count +=1
