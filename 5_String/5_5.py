# Count all letters, digits, and special symbols from a given string

def count_letter_digits_symbols(str1):
    count_l = 0
    count_d = 0
    count_s = 0

    for i in str1:
        if i.isalpha():
            count_l += 1
        elif i.isdigit():
            count_d += 1
        else:
            count_s += 1

    print("Letters: ", count_l, "\n", "Digits: ", count_d, "\n", "Symbols: ", count_s)

count_letter_digits_symbols("sjd8fl9aj9?s#~kdf6")
