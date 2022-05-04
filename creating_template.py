import openpyxl 
import re
def pattern():
    #извлекаем содержимое ячейки sheet.cell(row=r, column=c).value
    r=1
    c=1
    book = openpyxl.open("invoice.xlsx", read_only=True)
    sheet = book.active
    print(sheet.cell(row=r, column=c).value)
    print(re.sub('O-ring','Кольцо круглого сечения',sheet.cell(row=r, column=c).value))
    #
    #
    #
    #
    #берем из ячейки sheet.cell(row=r, column=c+1).value содержимое, это строковая переменная

    a = sheet.cell(row=r, column=c+1).value
    print('Содержимое ячейки ',a)
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
    #меняем в этой переменной символ "*" на символ "\D"
    x = '\*'
    print('Меняем символ из кирилицы "*" на "\D" ',re.sub(x,r'\\D',a))
    a = re.sub(x,r'\\D',a)
    #print('Выполним проверку на соответствие с помощию match = re.search(a, b)')
    #match = re.search(re.sub(x,r'\\D',a), a)
    #print(match[0] if match else 'Not found')
    #
    #
    #
    #объединяем название товара и шаблон размера в одну строку
    return re.sub('O-ring','Кольцо круглого сечения',sheet.cell(row=r, column=c).value)+' '+a
print(pattern())
