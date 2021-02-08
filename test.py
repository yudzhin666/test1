import URL

def Debug(key, value, writeToFile = False):
    print("Пип-пип, я робот дебагер")
    print(key, value)
    if (writeToFile == True):
        print("Пишу в файл важные данные")
        # записать в файл

def Sum(a, b): # вход
    result = a + b
    return result # выход

s = Sum(1,2)

print(s)

URL.parsed_string

# x = 1
# y = "Hello"
# z = True
# a = [x, y, z]
# d = {'banana': 100500, 'apple': 2, 'myArray' : a}
# r = None
#
# Debug("Проверяю что лежит в массиве а под индексом 2", a[2])
#
# a[2] = False
#
# print("Проверяю что лежит в массиве а под индексом 2", a[2])
#
# d["myArray"][2] = "BOGDAN TOP PROGRAMMER"
#
# Debug(y, z, True)
#
# print(z)
# print(a[2])