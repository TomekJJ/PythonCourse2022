# hermetyzacja/enkapsulacja
class Point:
    def __init__(self,num):
        self.__street = "wileńska"
        self.num = num

    def get_address(self):
        return self.__street

    def set_address(self, value):
        self.__street = value


address = Point(10)
print(address.num)
#print(address.__street)
print(address.get_address())

address.set_address("mickiewicza")
print(address.get_address())
