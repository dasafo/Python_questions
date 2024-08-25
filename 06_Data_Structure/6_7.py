# Checks if one set is a subset or superset of another set.
# If found, delete all elements from that set

set1 = {57, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

print("Set1 ", set1)
print("Set2 ", set2)

print("Set1 is subset of Set2: ", set1.issubset(set2))
print("Set2 is subset of Set1: ", set2.issubset(set1))

print("Set1 is Super set of Set2: ", set1.issuperset(set2))
print("Set2 is Super set of Set1 ", set2.issuperset(set1))

if set1.issubset(set2):
    set1.clear()

if set2.issubset(set1):
    set2.clear()

print("Set1 ", set1)
print("Set2 ", set2)
