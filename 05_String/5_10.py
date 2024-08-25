# Write a program to count occurrences of all characters within a string

str = "DepartmentdA"
letter_dic = {}
for i in str:
    counter = str.count(i)
    letter_dic[i] = counter

print(letter_dic)
