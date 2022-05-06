# import openpyxl module
import openpyxl
# Call a Workbook() function of openpyxl 
# to create a new blank Workbook object
book = openpyxl.Workbook()
sheet = book.active
r=1
c=1
sheet.cell(row=r, column=c) = 1
book.save("/home/igor/python/template.xlsx")
book.close()
