def factorial(n):
    f = 1
    if not (n == 0 or n == 1):
        for i in range(2, n+1):
            f = f * i
    return f


if __name__=="__main__":
    import sys
    print("run as a standalone script")
    if len(sys.argv) > 1:
        print(factorial(int(sys.argv[1])))
else:
    print("I am a module")
