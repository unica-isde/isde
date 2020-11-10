def is_palindrome1(s):
    # pros: one-line function. Readability
    # cons ?

    return s == s[::-1]


def is_palindrome(s):
    # pros: it checks only AT MAXIMUM half of the characters. Quick.
    # cons: more complex and less readable than is_palindrome1

    half_n = int(len(s) / 2)
    for idx in range(half_n):
        inverted_idx = -idx - 1
        if s[idx] != s[inverted_idx]:
            return False

    return True


def split_palindrome_nonpalindrome(s):
    #  find the biggest palindrome substring and split the string
    #   i.e. 'ABCBAXY'->  ('ABCBA' , 'XY')
    #        'ABCDE'->   ('A' , 'BCDE')
    #        'ABCBA'->  ('ABCBA' , '')

    for i in range(len(s), 0, -1):
        substring_to_check = s[0:i]
        if is_palindrome(substring_to_check):
            # i is the index of the  non-palindrome substring
            break
    # split
    s_palindrome = substring_to_check
    s_nonpalindrome = s[i:]  # it means: from i to the end of the string

    return s_palindrome, s_nonpalindrome


def create_palindrome(s):
    # 1. split into palindrome, non_palinbdrome
    # 2. add the (inverted) non-palindrome part of the string on the left of the original string

    # PROS: easy to understand - modularity
    # CONS: slow. it is possible to optimize the function.

    s_palindrome, s_nonpalindrome = split_palindrome_nonpalindrome(s)

    s_new = s_nonpalindrome[::-1] + s
    return s_new


## --------------------------------------------------------------
##  TEST
## --------------------------------------------------------------

list_of_strings = ['A',
                   'AA', 'AX',
                   'ABA', 'AAX', 'AXY',
                   'ABBA', 'ABAX', 'AAXY', 'AXYW',
                   'ABCBA', 'ABBAX', 'ABAXY', 'AAXYW', 'AXYWZ']

# test split_palindrome_nonpalindrome
print('\nsplit\n')
for s in list_of_strings:
    s_pal, s_npal = split_palindrome_nonpalindrome(s)
    if not is_palindrome(s_pal):
        print('ERROR! The string is not palindrome!')

    print(s, '->',s_pal, s_npal)

# test create_palindrome
print('\nPALINDROME\n')
for s in list_of_strings:
    s_pal = create_palindrome(s)
    print(s, '->', s_pal)
    if not is_palindrome(s_pal):
        print('ERROR! The string is not palindrome!')

