#начало функции cycle
#функция принимает строку шаблон
#функция ничего не возвращает
#функция ищет подходящую под шаблон ячейку и возвращает ее номер
def(str)
    #открываем таблицу DB.xlsx для поиска в ней нужной строки
    book = openpyxl.open("DB.xlsx", read_only=true)
    #запускаем цикл поиска подходящей строки
    #если строка найдена , то запускаем функцию создания строки в файле moysklad.xlsx

