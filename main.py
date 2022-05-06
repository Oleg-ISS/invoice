import openpyxl 
import re
#обьявляем функции
#открываем файлы
r=1
c=1
book_invoice = openpyxl.load_workbook("invoice.xlsx", read_only=True)
sheet_invoice = book.active
#получаем количество строк на рабочем листе
i = sheet_invoice.max_row
for row in range(1,i+1):
    nazvanie = sheet_invoice.cell(row=r, column=c).value
    razmer = sheet_invoice.cell(row=r, column=c+1).value
    material = sheet_invoice.cell(row=r, column=c+2).value
    #создаем шаблон-строку для поиска по БД на основе файла invoice.xlsx 
    template = creating_template(nazvanie,razmer,material)
    #запускаем функцию поиска строки, которая соответствует шаблону-строке в файле DB.xlsx
    searching(template)
    #открываем на запись файл-шаблон для импорта счета в мой склад
    #запускаем функцию которая создаст шаблон из строки инвойса
    #передадим шаблон в функцию поиска в базе мой склад
    #если в базе есть строка соответствующая шаблону запустим функцию записи в файл-шаблон мой склад
    #если строка не найдена запустим функцию записи состоянии не нашел
print("Работа программы завершена")
