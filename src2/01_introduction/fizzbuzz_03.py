def is_multiple_of(n, d):
    return n % d == 0


def fb(i, div1=3, div2=5):
    cond1 = is_multiple_of(i, div1)
    cond2 = is_multiple_of(i, div2)
    if cond1 and cond2:
        print("fizzbuzz")
    elif cond1:
        print("fizz")
    elif cond2:
        print("buzz")
    else:
        print(i)


while True:
    div1 = int(input("Value for div1: "))
    div2 = int(input("Value for div2: "))
    i = int(input("Value for i: "))
    fb(i, div1, div2)
