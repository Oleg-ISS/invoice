def creating_template(nazvanie,razmer,material):
    item = 0
    item = re.sub('O-ring','Кольцо круглого сечения',nazvanie)
    if item == nazvanie:
        item = re.sub('Oil Seal','Манжета армированная',nazvanie)
    if item == nazvanie:
        item = re.sub('cord','Шнур',nazvanie)
    size = re.sub('x',r'\\D',razmer)
    size = re.sub('\*',r'\\D',razmer)
    return item + ' ' + size + ' ' + material
