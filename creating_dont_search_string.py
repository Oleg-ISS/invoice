#фукция создает запись в файле invoice.xlsx запись в пустой ячейки справа "не найден"
def creating_dont_search_strin()
    global row, sheet_invoice
    sheet_invoice[row][6] = "не найден"#записываем в ячейку в колонке G

