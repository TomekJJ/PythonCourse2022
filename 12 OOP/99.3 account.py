class Account:
    def __init__(self, username):
        self.username = username
        self.__account_number = "PL 11 3333 3333 3222 3333" # __ powoduje, że pole staje się prywatne - nie da się nadpisać

    def show_num(self):
        print("Bank account number: ", self.__account_number )

    def set_number(self, number):
        self.__account_number = number

user = Account("tomjed3456")

user.show_num()

user.__account_number = 'PL 22 4444 4444 4444 4444' # nic się nie dzieje, nadpisuje lokalnie
print(user.__account_number)

user.account_number = 'PL 33 5555 4444 5555 555' # nic się nie dzieje, nadpisuje lokalnie
print(user.account_number)

user.set_number("PL 44 7777 7777 7777 7777")

user.show_num()
