def greet(hello, name):
    name = name.capitalize()
    print(hello, name, '****')

def main():
    phase = "Helllo!!"

    girl = 'anna'
    greet(phase, girl)

    print(phase, girl, anna) # !!! błąd bo name jest zmienną lokalną w funkcji greet

main()