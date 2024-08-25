# Check file is empty or not
# Write a program to check if the given file is empty or not

import os

size = os.stat("test_2_6.txt").st_size
if size == 0:
    print("The file is empty")
else:
    print("The file has data")
