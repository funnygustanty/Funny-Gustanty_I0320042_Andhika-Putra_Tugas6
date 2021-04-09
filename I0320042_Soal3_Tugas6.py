n = 24
for f in range(10, n + 1):
    if f > 1:
        for i in range(2,f):
            if (f % i) == 0:
                print(f, "bukan bilangan prima")
                break
        else:
            print(f, "adalah bilangan prima")