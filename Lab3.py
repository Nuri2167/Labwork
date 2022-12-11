from enum import Enum


class Account(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'

class BankAccount:
    name: str
    surname: str
    account: Account
    amount: float =0

    def __init__(self, name:str, surname:str, account: Account):
        self.name=name
        self.surname=surname
        self.account = account

    def add(self, cash_amount):
        self.cash_amount += cash_amount

    def substract(self, cash_amount):
        if cash_amount > self.cash_amount:
            print('Insufficient Funds')
        else:
            self.cash_amount -= cash_amount

    def transfer(self, toType:Account):
        if toType==Account.KZT:
            if self.account==Account.USD:
                self.amount*=470
            if self.account==Account.RUB:
                self.amount*=7
            if self.account==Account.EUR:
                self.amount*=495
            self.account=Account.KZT
        elif toType==Account.USD:
            if self.account==Account.KZT:
                self.amount/=470
            if self.account==Account.RUB:
                self.amount/=62
            if self.account==Account.EUR:
                self.amount/=1.05
            self.account=Account.USD
        elif toType==Account.RUB:
            if self.account==Account.KZT:
                self.amount/=7
            if self.account==Account.USD:
                self.amount/=62
            if self.account==Account.EUR:
                self.amount/=65
            self.account=Account.RUB
        elif toType==Account.EUR:
            if self.account==Account.KZT:
                self.amount/=495
            if self.account==Account.USD:
                self.amount/=65
            if self.account==Account.RUB:
                self.amount/=1.05
            self.account=Account.RUB

    def toString(self) -> str:
        return f'Your balance is: {self.amount} {self.account}'
    def set(self, amount:float):
        self.amount = amount
    def __repr__(self):
        return f'{self.name} {self.surname}'
    def __del__(self):
        print('Account was deleted')

accounts = []

while True:
    command = input('Choose a command: \n'
                    '1. Create an account\n'
                    '2. Choose an account\n'
                    '0. Exit\n')

    if command == '0':
        exit()

    if command == '1':
        name = input('Enter your name: ')
        surname = input('Enter your surname: ')
        password = input('Enter the password: ')
        currency = input('Enter the currency type: ')

        if currency == 'KZT':
            account = Account.KZT
        elif currency == 'RUB':
            account = Account.RUB
        elif currency == 'USD':
            account = Account.USD
        elif currency == 'EUR':
            account = Account.EUR

        user_account = BankAccount(name=name, surname=surname, account=account)
        accounts.append(user_account)
        print('Account was created')


    elif command == '2':
        if len(accounts) == 0:
            print('Account list is empty')
        else:
            for i in range(len(accounts)):
                print(f'{i}: {accounts[i]}')
            n = int(input('Choose the number: '))
            account=accounts[n]

            while True:
                opt = input('Choose a command: \n'
                            '1. Add to balance\n'
                            '2. Withdraw from balance\n'
                            '3. Convert Money\n'
                            '4. Show all information\n'
                            '5. Set an amount of money\n'
                            '6. Exit\n')
                if opt == '1':
                    amnt = int(input('Enter an amount of money: '))
                    account.add(cash_amount=amnt)
                    print(toString())
                elif opt == '2':
                    amnt = int(input('Enter an amount of money: '))
                    account.substract(cash_amount=amnt)
                    print(toString())
                elif opt == '3':
                    new_curr = input('Enter a new currency: ')
                    if new_curr == 'KZT':
                        account = Account.KZT
                    elif new_curr == 'RUB':
                        account = Account.RUB
                    elif new_curr == 'USD':
                        account = Account.USD
                    elif new_curr == 'EUR':
                        account = Account.EUR
                    account.transfer(toType=new_curr)
                elif opt == '4':
                    print(account.toString())
                elif opt == '5':
                    amnt = int(input('Enter an amount of money: '))
                    account.set(amount=amnt)
                elif opt == '6':
                    break

    else:
        print('invalid command, try again')
