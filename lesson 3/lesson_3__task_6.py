""" Урок 3, завдання 6
Створіть командно (2-3 учні) програму-калькулятор. Перший учень створює проєкт/файл/клас,
де буде знаходитися програма й надіслати його за допомогою інструментів IDE на віддалений сервер.
Кожний наступний учень повинен клонувати проєкт на свій комп’ютер, додати свої частинки програми,
зробити коміти й надіслати ці зміни на віддалений сервер.
"""


class Calculator:
    def __init__(self):
        self.result = None

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b != 0:
            self.result = a / b
            return self.result
        else:
            return 'Error: cannot divide by zero'

    def power(self, a, b):
        try:
            self.result = a ** b
            return self.result
        except ZeroDivisionError:
            return 'Error: 0 cannot be raised to a negative power'


def main():
    calc = Calculator()

    while True:
        print("""
            Select operation:
         1. Add
         2. Subtract
         3. Multiply
         4. Divide
         5. Power
         6. Exit""")
        operation = input('Enter operation number: ')
        if operation not in ['1', '2', '3', '4', '5', '6']:
            print('Wrong operation number')
            continue
        if operation == '6':
            break
        arg_1 = arg_2 = None
        try:
            arg_1 = float(input('Enter first argument: '))
            arg_2 = float(input('Enter second argument: '))
        except ValueError:
            print('   Wrong argument input')
            continue
        if arg_1 is not None and arg_2 is not None:
            if operation == '1':
                print(f'{arg_1} + {arg_2} = {calc.add(arg_1, arg_2)}')
            elif operation == '2':
                print(f'{arg_1} - {arg_2} = {calc.subtract(arg_1, arg_2)}')
            elif operation == '3':
                print(f'{arg_1} * {arg_2} = {calc.multiply(arg_1, arg_2)}')
            elif operation == '4':
                print(f'{arg_1} / {arg_2} = {calc.divide(arg_1, arg_2)}')
            elif operation == '5':
                print(f'{arg_1} ** {arg_2} = {calc.power(arg_1, arg_2)}')
            else:
                print('Wrong operation')


if __name__ == "__main__":
    main()
