# fizzbuzz_2
# - avoid 'magic numbers'
# - DRY: don't repeat yourself
# - Single-responsibility principle

def is_multiple_of(n, d):
    return n % d == 0


def fb(i, v1, v2):
    cond_1 = is_multiple_of(i, v1)
    cond_2 = is_multiple_of(i, v2)

    if cond_1 and cond_2:
        print('fizzbuzz')
    elif cond_1:
        print('fizz')
    elif cond_2:
        print('buzz')
    else:
        print(i)


#  MAIN

value_1 = 3
value_2 = 5

N = 30
for i in range(1, N+1):
    fb(i, value_1, value_2)
