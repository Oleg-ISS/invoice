import openpyxl 
import re
#
#
#
#
#берем из ячейки "С17" содержимое, это строковая переменная
book = openpyxl.open("invoice.xlsx", read_only=True)
sheet = book.active
a = sheet["C17"].value
print('Содержимое ячейки С17 ',a)
print(type(a))
#меняем в этой переменной символ "x" на символ "\D"
#!!!!! символ х из кирилической раскладки
x = 'х'
print('Меняем символ из кирилицы "х" на "\D" ',re.sub(x,r'\\D',a))
print('Выполним проверку на соответствие с помощию match = re.search(a, b)')
match = re.search(re.sub(x,r'\\D',a), a)
print(match[0] if match else 'Not found')
#
#
#
#
#берем из ячейки "С1" содержимое, это строковая переменная
book = openpyxl.open("invoice.xlsx", read_only=True)
sheet = book.active
a = sheet["C1"].value
print('Содержимое ячейки С1 ',a)
print(type(a))
#меняем в этой переменной символ "*" на символ "\D"
x = '\*'
print('Меняем символ из кирилицы "*" на "\D" ',re.sub(x,r'\\D',a))
print('Выполним проверку на соответствие с помощию match = re.search(a, b)')
match = re.search(re.sub(x,r'\\D',a), a)
print(match[0] if match else 'Not found')
