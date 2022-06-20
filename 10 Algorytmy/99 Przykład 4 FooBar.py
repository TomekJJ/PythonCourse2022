def foo_bar(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 3 == 0:
            print('foobar')
        elif i % 3 == 0:
            print("foo")
        elif i % 5 == 0:
            print("bar")
        else:
            print(i)


def main():
    foo_bar(30)


if __name__ == '__main__':
    main()
