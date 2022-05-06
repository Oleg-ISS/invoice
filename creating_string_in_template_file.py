import openpyxl #Подключаем библиотеку Openpyxl
def creating_string_in_template_file(row)
    book_template = openpyxl.load_workbook("/home/igor/python/template.xlsx") #Открываем тестовый Excel файл
    sheet_template = book.active
    #worksheet = book['Sheet1'] #Делаем его активным
    r=1
    c=0#колонки начинаются с нуля
    sheet_template[r][c].value='We are writing to B4' #В указанную ячейку на активном листе пишем все, что в кавычках
    book_template.save("/home/igor/python/template.xlsx") #Сохраняем измененный файл
    book_template.close()
