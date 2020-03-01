def test(a, b, c=[]):
    for x in range(3):
        if x == 2:
            return
        print(x, a)
        print(x, b)
        print(c)
        c.append(x)
        test(a, b, c)


if __name__ == "__main__":
    test(2, 3)
