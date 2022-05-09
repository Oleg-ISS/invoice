import re
book_DB = openpyxl.load_workbook("DB.xlsx", read_only='true')
sheet_DB = book_DB.active
def searching(template):
    #global i_main
    r = 1
    с = 3
    #получаем количество строк на рабочем листе
    i = sheet_DB.max_row
    #запускаем цикл поиска подходящей строки
    for row in range(1,i+1):
        #обнуляем переменную match в каждой итерации
        match = 0
        #извлекаем из ячейки строку для сравнения
        sheet_DB.cell(row=r, column=c).value
        #сравниваем строку в таблице "DB.xlsx" с шаблоном template
        match = re.search(template,sheet_DB.cell(row=r, column=c).value)
        #если строка найдена match не равен 0, то запускаем функцию creating_string_in_template_file() создания строки в файле moysklad.xlsx
        if match == 0:
            #
            creating_dont_search_string()
        if match != 0:
            #creating_string_in_template_file()
            print('найдена строка')
    # Close the workbook after reading
    book_DB.close()
new_string = searching("Манжета армированная 14\D28\D7 FKM")
