# Concatenate two lists in the following order
# [a,b] amd [c,d]---> [ac,ad,bc,bd]

list1 = ["Hi ", "give "]
list2 = ["you", "me"]

list_conc = []

for i in list1:
    for j in list2:
        list_conc.append(i+j)

print(list_conc)

#Method 2
list_conc_2 = [i+j for i in list1 for j in list2]
print("Method 2: ",list_conc_2)

