numbers = [13, "hello", 3.14, True, None, [12,4]]

for i in numbers:
    try:
        results = 10/i
        print(results)
    except (TypeError, ZeroDivisionError):
        print(f'10/{i} nie mogę wykonać')