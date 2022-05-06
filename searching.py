#начало функции searching
#функция принимает строку шаблон
#функция
#функция ищет подходящую под шаблон ячейку и возвращает ее номер
def searching(template,i)
    r = 1
    с = 3
    #открываем таблицу DB.xlsx для поиска в ней нужной строки
    book = openpyxl.load_workbook("DB.xlsx", read_only=true)
    sheet = book.active
    
    #получаем количество строк на рабочем листе
    i = sheet.max_row
    #запускаем цикл поиска подходящей строки
    for row in range(1,i+1):
        #обнуляем переменную match в каждой итерации
        match = 0
        #извлекаем из ячейки строку для сравнения
        sheet.cell(row=r, column=c).value
        #сравниваем строку в таблице "DB.xlsx" с шаблоном template
        match = re.search(template,sheet.cell(row=r, column=c).value)
        #если строка найдена match не равен 0, то запускаем функцию creating_string_in_template_file() создания строки в файле moysklad.xlsx
        if match == 0:
            #
            creating_dont_search_string(i)
        if match != 0:
            creating_string_in_template_file()
    # Close the workbook after reading
    
    book.close()
