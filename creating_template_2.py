def creating_template(nazvanie,razmer,material):
    item = 0
    item = re.sub('O-ring cord','Шнур круглого сечения',nazvanie)
    if item == nazvanie:
        item = re.sub('Oil Seal','Манжета армированная',nazvanie)
    if item == nazvanie:
        item = re.sub('O-ring','Кольцо круглого сечения',nazvanie)
    size = re.sub('x',r'\\D',razmer)
    size = re.sub('\*',r'\\D',razmer)
    return item + ' ' + size + ' ' + material
