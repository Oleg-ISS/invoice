import openpyxl #Подключаем библиотеку Openpyxl
book = openpyxl.load_workbook("/home/igor/python/template.xlsx") #Открываем тестовый Excel файл
sheet = book.active
#worksheet = book['Sheet1'] #Делаем его активным
r=1
c=0#колонки начинаются с нуля
sheet[r][c].value='We are writing to B4' #В указанную ячейку на активном листе пишем все, что в кавычках
book.save("/home/igor/python/template.xlsx") #Сохраняем измененный файл
book.close()
