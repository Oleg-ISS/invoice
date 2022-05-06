import openpyxl #Подключаем библиотеку Openpyxl
def creating_string_in_template_file(r):
    #берем из DB.xlsx сроку что бы создать запись в файле template.xlsx
    book_DB = openpyxl.load_workbook("/home/igor/python/DB.xlsx", read_only=True)
    sheet_DB = book_DB.active
    kod = sheet_DB.cell(row=r, column=1).value
    artikul = sheet_DB.cell(row=r, column=2).value
    naimenovanie = sheet_DB.cell(row=r, column=3).value
    book_template = openpyxl.load_workbook("/home/igor/python/template.xlsx") #Открываем тестовый Excel файл
    sheet_template = book_template.active
    #worksheet = book['Sheet1'] #Делаем его активным
    r=1
    c=0#колонки начинаются с нуля
    sheet_template[r][0].value= kod  #
    sheet_template[r][1].value= artikul  #
    sheet_template[r][2].value= naimenovanie  #
    book_template.save("/home/igor/python/template.xlsx") #Сохраняем измененный файл
    book_template.close()
