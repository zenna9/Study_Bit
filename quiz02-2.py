#구구단

for c in range (1, 10, 1):
    print(c,"단")
    for h in range (1, 10):
        print("{} * {} = {}".format(c, h, c*h))
    print()