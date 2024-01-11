# Create a Python set such that it shows the element from both lists in a pair

set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

intersec = set1.intersection(set2)

for i in intersec:
    set1.remove(i)
print(set1)
