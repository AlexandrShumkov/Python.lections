#a = 123
#b = 2.34
#print(a)
#print(b)

#value = None
#value = 12345
#print(type(value)) определяет тип данных
#print(value)

#s = 'hello \nworld'   # объявление строки,\n-переход на новую строку
#s = "hello 'world"
#s = 'hello "world'
#s = 'hello "world"'
#print(s)  вывод строки

#Способы вывода в консоль.Все одинаковые.
#print(a, b, s)
#print(a,'-',b,'-',s,)
#print('{} - {} - {}'.format(a,b,s))
#print('{1} - {2} - {0}'.format(a,b,s))  # Устанавливаем порядок вывода переменных 
#print(f'{a} - {b} - {s}')

#f = True
#print(f)
#g = False
#print(g)

# Списки

#list = [1,2,3] список чисел
#list = ['1', '2', '3', 'hello']  # список строк
#list = ['hello', 12, 2.45, True]   можно смешивать типы данных,но лучше не делать.
#print(list)  # вывод списка

# Ввод ивывод данных.Преобразование типов.

#print('Введите a ')
#a = input()
#print('Введите b ')
#b = input()
#print(a, b)

# Для вывода сложения надо указать тип данных перед input


#print('Введите a ')
#a = int(input())
#print('Введите b ')
#b = int(input())
#print(a,' + ', b,' = ', a + b)

# Арифмитеческие операции
# +,-,*,/,%,//,**
# приоритет  **,++,--,*,/,//,%,+,-
# () скобки меняют приоритет

#a = 1.3
#b = 3
#c = a + b
#c = a - b
#c = a * b
#c = a / b
#c = b // a # деление в целых числах,без запятых
#c = a % b  # остаток от деления
#c = a ** b  # возведение в степень
#c = round(a * b, 5)# колво знаков после запятой,round - округляет
#print(c)
#print('a', '+','b','=',c)

# (), Сокращенные операции

#a = 3
#a = a + 5
#a += 5 # то же самое,для всех действий.
#print(a)

#Логические операции
# >,>=,<,<=,==,!=
# not,and,or- не путать с &,|,^
# is,is not, in, not in

#a = 1 > 4
#a = 1 < 4 and 5 > 2
#print(a)

#a = 'qwe'
#b = 'qwe'

#a = [1,2]
#b = [1,2]
#print(a == b)

#a = 1 < 3 < 5 < 10
#print(a)

#f = [1,2,3,4]
#print(f)
#print(2 in f) # находится ли 2 в списке?
#print(not 2 in f)

#is_odd = f[0] % 2 == 0  # четное ли число с индексом 0
#print(is_odd)

# Управляющие конструкции if, if-else

#a = int(input('a = '))
#b = int(input('b = ' ))
#if a > b:
#    print(a)
#else:
#    print(b)   

#username = input('Введите имя ')
#if username == 'Саша':
#    print('Ура, это Саша!')
#elif username == 'Далер':
#    print('Здорово')
#elif username == 'Замира':
#    print('Наконец то')
#else:
#    print('привет', username)

# Конструкция While 

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#print(inverted)

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#else:
#    print('пожалуй хватит')    
#print(inverted)      

# Конструкция for:

#for i in 1,2,3,4,5:
#    print(i**2)    # квадраты чисел в списке   
#list = [1,2,3,4,5]
#for i in list:
#    print(i**2)     

#r = range(10)  # получим числа от 0 до 9,for i in range(10)
#for i in r:
#    print(i)
#for i in range(1, 10, 2):
#    print(i) # диапазон от 1 до 9,черз 2 цифры

#for i in 'qwerty':
#    print(i)

# О строках

# text = 'покушай еще хлеба'
# print(len(text))  # длина строки
# print('еще' in text)
# print(text.isdigit())  # есть ли цифры
# print(text.islower())  # все ли в нижнем регистре
# print(text.replace('еще','ЕЩЕ'))   # заменить

#print(text[0])  # выведит нужный элемент строки
#print(text[-1])  # последний элемент строк
#print(text[2:6])  # диапазон элементов

# Списки.Пронумерованная,изменяемая коллекция объектов произвольных типов.

#numbers = [1,2,3,4,5]
#ran = range(1,6)
#numbers = list(ran) # приведение типа range к типу list
#print(numbers)
#print(len(numbers))  # колво элементов в списке
#for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)  

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)  # red,green,blue
# for e in colors:
#     print(e*2) # redred,greengreen,blueblue
# colors.append('gray')  # добавить в конец
# print(colors)
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red') # del colors[0]  удалить элемент
# print(colors)   

# Функции

def f(x):
    if x == 1:
        return 'целое'
    elif x ==2.3:
        return 23
    else:
        return     
# arg = 2.3
# print(f(arg))    

#import random
# print(random.random()) # случайное число
# print(random.randint(0,100)) # случайное целое число
# print(random.randrange(1,20,2)) # случайное целое число с шагом 2
#print(list[1,2,3,4,5])
# random.seed(5)
# print(random())