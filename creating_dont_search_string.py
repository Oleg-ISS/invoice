#фукция создает запись в файле invoice.xlsx запись в пустой ячейки справа "не найден"
def creating_dont_search_string():
    global sheet_invoice, coordinates
    sheet_invoice[coordinates] = "не найден"#записываем в ячейку в колонке G
    book_invoice.save("/home/igor/python/invoice.xlsx") #Сохраняем измененный файл

