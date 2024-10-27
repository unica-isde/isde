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
    div1 = input("Value for div1: ")
    div2 = input("Value for div2: ")
    i = input("Value for i: ")

    if not div1.isdigit() or not div2.isdigit() or not i.isdigit():
        print("Error: some input is not valid."
              "Pleas pass only integers.")
        continue

    div1, div2, i = int(div1), int(div2), int(i)

    if div1 == 0 or div2 == 0:
        print("Error: you passed zero for a divisor.")
        continue

    fb(i, div1, div2)
