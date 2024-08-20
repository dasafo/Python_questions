# Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. 
# For example, 545, is the palindrome numbers

# Method 1
def palindrome_num(num):
    num_org = num
    num_palind = 0

    while num > 0:
        reminder = num % 10
        num_palind = num_palind * 10 + reminder
        num = num // 10

    if num_palind == num_org:
        print(f"The number {num_org} IS a palindrome number.")

    else:
        print(f"The number {num_org} IS NOT a palindrome number.")

palindrome_num(124)


# Method 2
def palindrome(num):
    
    str_num = str(num)
    
    if str_num == str_num[::-1]:
        print("Es palindromo")
        
    else:
        print("No es palindromo")
        
palindrome(123321)