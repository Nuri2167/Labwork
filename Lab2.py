# 1. Четные числа
a = int(input('a: '))
b = int(input('b: '))
alln = ''
for i in range (a, b+1) :
    if i % 2 == 0:
        alln = alln + str(i) + ' '
print(alln)
# 2. Минимальный делитель
mindiv = int(input())
for i in range (2, mindiv+1):
    if (mindiv % i) == 0:
        print(i)
        break
# 3. Делители числа
div = int(input())
divs = ''
for i in range (1, div+1):
    if (div % i) == 0:
        divs = divs + str(i) + ' '
print(divs)
# 4. Сумма чисел
count = int(input('Количество чисел: '))
sum = 0
for i in range(count):
    n = int(input())
    sum = sum + n
print(sum)
# 5. Перевод числа
bi = list(input())
bilen = len(bi)
dec = 0
for i in range (bilen):
    dec = dec + int(bi[i]) * (2**(bilen-i-1))
print(dec)
# 6. Степень
np = input().split()
nmb = float(np[0])
pow = int(np[1])
def power (a, n):
    return (a**n)
print (int(power (nmb, pow)))
# 7. Голосование
votes = input().split()
x = int(votes[0])
y = int(votes[1])
z = int(votes[2])
def election (x, y, z):
    return (x+y+z) > 1
print(int(election(x, y, z)))
# 8. Реализуйте следующие функции для банковского счета
bankAccount = 0
def addToBankAccount (money):
    global bankAccount
    bankAccount = bankAccount + money
    return bankAccount
def substractFromBankAccount (money):
    global bankAccount
    bankAccount = bankAccount - money
    return bankAccount
def moneyConversation (money, fromC, toC):
    if fromC == 'USD':
        converted = money * 470
    if toC == 'USD':
        converted = money / 470
    return converted
print(addToBankAccount(500))
print(substractFromBankAccount(200))
print(moneyConversation(300, 'USD', 'KZT'))
