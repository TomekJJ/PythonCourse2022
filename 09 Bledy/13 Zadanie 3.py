def main():
    items = ['a', 'abc', 5, 5.0, [5, 3], (1, 3), 0, True, None, {}]

    try:
        id = int(input('podaj index'))
        print(1 / items[id])
    except ValueError:
        print('value error')
    except TypeError:
        print('type error')
    except ZeroDivisionError:
        print('Zero division')
    except IndexError:
        print('poza zakresem')

if __name__ == '__main__':
        main()

