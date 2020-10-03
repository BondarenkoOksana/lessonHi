# Генератор списков
# my_list = [-8, 1, 20, 34, 12, -8, 12, 1, -8, 1]
# возвести в квадрат на четных местах и остальные оставить без изменения

# for index in renge(len(my_list)):
#     if index % 2 == 0:
#          print(my_list[index]** 2)
#     else:
#         print(my_list[index])

# for index, value in enumerate(my_list):
#     if index % 2 == 0:
#         print(value ** 2)
#     else:
#         print(value)

# возвести элемент списка в степень его индекса
# for index, value in enumerate(my_list):
#     print(value ** index)

# в new_list  поместить числовые значения из my_list (в виде int) учитывая что числа могут быть строкой
# my_list = [1, 2, 3, '4', '5', 6, 7, 'qwe', "88"]
# new_list = []
# просить прощения
# for value in my_list:
#     try:
#         value = int(value)
#         new_list.append(value)
#     except ValueError:
#         pass
# просить разрешения, второй вариант решения
# for value in my_list:
#     if type(value) == str:
#         if value.isdigit():
#             value = int(value)
#             new_list.append(value)
#     else:
#         new_list.append(value)
#
# print(new_list)

# Множество Set:
# 1 - набор уникальных данных (без повторов)
# 2 - порядок не важен или не соблюдается
# 3 - изменяемый объект

# my_set = set('my_list')
# print(my_set)

# my_str = "bla BLA CarDDD"
# print(len(set(my_str.lower())))

# методы set

my_set_1 = {1, 2, 3}
my_set_2 = {2, 3, 4}
# добавить один єлемент
my_set_1.add(7)

print(my_set_1)
# добавить множество