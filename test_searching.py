import re, openpyxl
book_DB = openpyxl.load_workbook("DB.xlsx", read_only='true')
sheet_DB = book_DB.active
def searching(template):
    #global i_main
    r = 1
    c = 4
    #получаем количество строк на рабочем листе
    i = sheet_DB.max_row
    #запускаем цикл поиска подходящей строки
    for row in range(1,i+1):
        #обнуляем переменную match в каждой итерации
        match = None
        #извлекаем из ячейки строку для сравнения
        print(sheet_DB.cell(row, column=c).value)
        print(row)
        #сравниваем строку в таблице "DB.xlsx" с шаблоном template
        match = re.search(template,sheet_DB.cell(row, column=c).value)
        print(match)
        #если строка найдена match не равен 0, то запускаем функцию creating_string_in_template_file() создания строки в файле moysklad.xlsx
        if match == None:
            creating_dont_search_string()
            print('строка не найдена')
        if match != None:
            #creating_string_in_template_file()
            print('найдена строка')
    # Close the workbook after reading
    #book_DB.close()
new_string = searching("Кольцо круглого сечения EPDM 102\D3,55")
