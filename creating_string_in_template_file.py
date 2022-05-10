#import openpyxl #Подключаем библиотеку Openpyxl
def creating_string_in_template_file(r):
    #@@@@@@@@@@@@@ берем из DB.xlsx сроку что бы создать запись в файле template.xlsx
    kod = sheet_DB.cell(row=r, column=2).value
    #artikul = sheet_DB.cell(row=r, column=3).value
    #naimenovanie = sheet_DB.cell(row=r, column=4).value
    #@@@@@@@@@@@@ ЗАПИСЫВАЕМ В template.xlsx @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    sheet_template[coordinates_kod].value = kod  #
    #sheet_template[coordinates_artikul].value= artikul  #
    #sheet_template[coordinates_naimenovanie].value= naimenovanie  #
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@ СО[РАНЯЕМ ФАЙЛ @@@@@@@@@@@@@@@@@@@@@@@@
    book_template.save("template.xlsx") #Сохраняем измененный файл
    
