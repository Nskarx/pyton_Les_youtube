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


