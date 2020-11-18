# fizzbuzz_1

def fb(i):
    if (i % 3 == 0) and (i % 5 == 0):
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)


# MAIN

N = 30
for i in range(1, N + 1):
    fb(i)
