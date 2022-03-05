# Файлы.Хранение данных,передача данных в клиент-серверных проектах.
# Хранение конфигов.Логирование действий. 

# Связать файловую переменную с файлом,определив модификатор работы.
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных, w+;r+

# exit() - позволяет не выполнять дальнейший код

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# #data.writelines(colors) # без разделителей
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n') 

# path = 'file.txt'   # Чтение файла
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close() 

# Функции и модули.

# import lect    # Вытягиваем функцию из другого файла.
# print(lect.f(1))

# import lect as l   # Вытягиваем функцию из другого файла.
# print(l.f(1))

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!

# def new_string(symbol, count = 3):
#      return symbol * count
# print(new_string('!'))  # !!!
# print(new_string(4))   # 12 

# Возможность передачи неограниченого кол-ва аргументов.

# def concateenatic(*params):
#     res: str = ""   # Для чисел: res: int = 0
#     for item in params:
#         res += item
#     return res
# print(concateenatic('a', 's', 'd', 'f'))  # asdf
# print(concateenatic('a', '1'))  # a1
# print(concateenatic(1, 2, 3, 4))  # Error 


# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи - неизменяемые списки

# #a, b = 3, 4 # обычное присваивние
# a = (3, 4) # кортеж
# print(a)
# print(a[0]) # можно обращаться к определенному элементу

# a = (3,) # Кортеж из одного элемента 

# T = tuple(['red', 'green', 'blue'])
# red, green, blue = T
# print('r:{} g:{} b:{}' .format(red, green, blue)) # пример 
# преобразования списка в кортеж и элементов списка в отдельные переменные


# Словари - неупорядоченные коллекции произвольных объектов
# с доступом по ключу.

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'down': '↓',
#         'left': '←',
#         'rigth': '→'
#     }
# print(dictionary)
# print(dictionary['left'])
# # типы ключей могут отличаться

# for k in dictionary.keys(): # просмотр ключей
#     print(k)

# for k in dictionary.values(): # просмотр значений
#     print(k)

# print(dictionary['up'])
# dictionary['up'] = 'asd' # изменение значения по ключу
# print(dictionary['up'])

# Множества 

# from subprocess import list2cmdline


# colors = {'red', 'green', 'blue'}
# print(type(colors))  
# print(colors) # {'red', 'green', 'blue'}

# colors.add('red') # при добавлении уже имеющегося элемета ничего непроизойдет
# colors.add('gray')
# print(colors)

# colors.remove('red') # удаление элемента
# print(colors)

# colors.discard('red')
# print(colors)

# colors.clear() # очистка мн-ва
# print(colors)

# # Операции с мн-вами

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}

# s = frozenset(a) # неизменяемое мн-во

# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list1[0] = 123  # меняя значение эл-та в одном списке оно меняется и в другом.
# list2[1] = 333
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
# print() 

# удаление эл-та

# list1 = [1, 2, 3, 4, 5]
# # print(list1.pop()) # значение удаленного эл-та.Без указания позиции эл-та,удалится последний.
# # # print(list1.pop(0))  указание положения эл-та
# # print(len(list1))
# # print(list1) 

# # вставка эл-та

# # list1.insert(0, 11) # (позиция, значение)
# # print(list1)

# list1.append(11) # добавление в конец
# print(list1)