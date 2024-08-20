
with open("test_2_10.txt", "r") as f:
    lines = f.readlines()
    
with open("tesss.txt", "w") as f:
    count = 0
    for line in lines:
        if count == 4:
            count +=1
            continue
        else:
            f.write(line)
        count+=1