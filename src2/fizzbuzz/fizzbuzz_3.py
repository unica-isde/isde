def is_multiple_of(n, d):
    return n % d == 0


def is_greater_than(a, b):
    return a > b


def gfb(v, dict_of_conditions, f_eval_condition):
    string_to_print = ''

    # if the condition has been met, build a string by replacing a number with a value to be printed
    for d, s in dict_of_conditions.items():
        if f_eval_condition(v, d):
            string_to_print += s

    # if no condition has been met,
    #    transform the initial number into a string.
    if not string_to_print:
        string_to_print = str(v)

    # Sequences (like strings) are evaluated as False (empty) or True (not empty) in a Boolean context.
    # They are *not* equal to False or True.
    # https://docs.python.org/3/library/stdtypes.html#truth-value-testing

    return string_to_print


# pythonic way: the function consists of only two lines of code!
def gfb2(v, dict_of_conditions, f_eval_condition):
    ans = [s for d, s in dict_of_conditions.items() if f_eval_condition(v, d)]
    return ''.join(ans) if ans else str(v)


# ---------------------------------------------

dict1 = {3: 'A', 5: 'B', 7: 'C'}
dict2 = {10: 'X', 20: 'Y', 30: 'Z'}

print(gfb(21, dict1, is_multiple_of))  # AC

print(gfb(8, dict1, is_multiple_of))  # 8

print(gfb(7, dict2, is_greater_than))  # 7

print(gfb(20, dict2, is_greater_than))  # X
