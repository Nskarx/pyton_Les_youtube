print(1.5 + 1)  # = 2.5

# Фукнция int  в данном примере преобразует строку в число (убирает ковычки с числа)
print(int('10') + 10)

# age = input ( " enter your age: ")
# print(int(age) + 1)

# age = int (input ( " enter your age: "))
# print(age + 1)

# age = float (input ( " enter your age: "))
# print(age + 1)

print(len('hello'))  # функция len позволяет посчитать количество символов

x = 1000
y = - 1000
# таким образом число переносим в строку и считает количество символов
print(len(str(x)))

print(type(x))  # int

print(len(str(abs(x))))  # abs -это абсолютная функция
print(len(str(abs(y))))

print(str(10) + "10")  # переводит число в строку и обьединяет

# сдесь наоборот переводит из строки в число и прибавляет = 20
print(int('10') + 10)

print(str(int('10')) + str(10))  # 1010 -это конкатанация


print(bool(1000)) # True
print(bool(-1000)) # True  в данных строках преобразует числа в решения
print(bool(0)) # False
print(bool('hello')) # True
print(bool('')) # False   в данных строках преобразует строки
print(bool(' ')) # True
print(bool(None)) # False

int(str(int(str(10)))) + int(str(5))

print(int(str(int(str(10)))) + int(str(5)))


print(not bool('hello')) # False

bool(10 % 3)
print(bool(10 % 3)) # True

bool('' + '')
print(bool('' + ''))  # False

# bool(input('enter the number: '))
# print(bool(input('enter the number: '))) # True