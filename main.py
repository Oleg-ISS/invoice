import openpyxl 
import re
#обьявляем функции
#создаем шаблон-строку для поиска по БД на основе файла invoice.xlsx 
creating_template()
#запускаем функцию поска строки, которая соответствует шаблону-строке в файле DB.xlsx

#открываем на запись файл-шаблон для импорта счета в мой склад
#запускаем функцию которая создаст шаблон из строки инвойса
#передадим шаблон в функцию поиска в базе мой склад
#если в базе есть строка соответствующая шаблону запустим функцию записи в файл-шаблон мой склад
#если строка не найдена запустим функцию записи состоянии не нашел
print("Работа программы завершена")
