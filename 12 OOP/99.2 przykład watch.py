class UsefullStuff():
    def __init__(self, name):
        print(name, "is very useful")


class Watch(UsefullStuff):
    def __init__(self, brand):
        print(f'Watch {brand}, wear on hand')
        super().__init__("aaaa") # tu nie wiem o co chodzi

    def checktime(self):
        print('TIME')


class Phone(UsefullStuff):
    def __init__(self, name):
        print('Phone', '-> call with it')
        super().__init__('phone')
    def call(self):
        print("calling")


class SmartWatch(Watch, Phone):
    def __init__(self):
        print('Smartwatch is pratical')
        super().__init__("SmartWatch")



sw = SmartWatch()

print(SmartWatch.__mro__) # Kolejność dziedziczenia (mro - method resolution order)
