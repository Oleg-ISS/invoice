#фукция создает запись в файле invoice.xlsx запись в пустой ячейки справа "не найден"
def creating_dont_search_string()
    global i_main, sheet_invoice
    sheet_invoice[i_main][6] = "не найден"#записываем в ячейку в колонке G

