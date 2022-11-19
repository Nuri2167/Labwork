# 1. Гипотенуза
katet1 = int(input('a: '))
katet2 = int(input('b: '))
print(((katet1 ** 2) + (katet2 ** 2)) ** 0.5)
# 2. Число десятков
number = int(input('number: '))
print(number // 10 % 10)
# 3. Следующее четное
n = int(input('n: '))
print(((n) // 2) * 2 + 2)
# 4. Конец уроков
lessons = int(input('lessons: '))
m = lessons // 2
r = lessons % 2
minutes = lessons * 45 + m * 5 + (m - 1 + r) * 15
hr = minutes // 60
min_remain = minutes % 60
print(9 + hr, min_remain)
# 5. Какое из чисел больше?
n1 = int(input())
n2 = int(input())
if n1 > n2:
    print(1)
elif n1 == n2:
    print(0)
else:
    print(2)
# 6. Максимум из трех
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
# 7. Ладья
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 == x2 or y1 == y2):
    print('YES')
else:
    print('NO')
# 8. Существует ли треугольник?
side1 = int(input())
side2 = int(input())
side3 = int(input())
if (side1 + side2) > side3:
    if (side2 + side3) > side1:
        if (side1 + side3) > side2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
# 9. Количество равных из трех
c1 = int(input())
c2 = int(input())
c3 = int(input())
if (c1 == c2 & c2 == c3):
    print(3)
elif c1 == c2 or c1 == c2 or c2 == c3:
    print(2)
else:
    print(0)
# 10. Упорядочить три числа
nmb1 = int(input())
nmb2 = int(input())
nmb3 = int(input())
if nmb1 > nmb2:
    nmb1, nmb2 = nmb2, nmb1
if nmb2 > nmb3:
    nmb2, nmb3 = nmb3, nmb2
if nmb1 > nmb2:
    nmb1, nmb2 = nmb2, nmb1
print(nmb1, nmb2, nmb3)
