#начало функции searching
#функция принимает строку шаблон
#функция
#функция ищет подходящую под шаблон ячейку и возвращает ее номер
def searching(str)
    r = 1
    #открываем таблицу DB.xlsx для поиска в ней нужной строки
    book = openpyxl.load_workbook("DB.xlsx", read_only=true)
    sheet = book.active
    #получаем количество строк на рабочем листе
    i = book.max_row
    #запускаем цикл поиска подходящей строки
    #если строка найдена , то запускаем функцию создания строки в файле moysklad.xlsx
    # Close the workbook after reading
    openpyxl.close()
