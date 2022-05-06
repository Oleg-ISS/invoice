def creating_template(nazvanie,razmer,material):
    item = re.sub('O-ring','Кольцо круглого сечения',nazvanie)
    item = re.sub('Oil Seal','Манжета армированная',nazvanie)
    size = re.sub('x',r'\\D',razmer)
    size = re.sub('\*',r'\\D',razmer)
    return item + ' ' + size + ' ' + material
