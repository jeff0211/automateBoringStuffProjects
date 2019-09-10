import os, openpyxl

os.chdir()  # Change directory to where the spreadsheet file is located.
wb = openpyxl.load_workbook('sampleBook1.xlsx')  # Load the spreadsheet.
sheet = wb.active
columns = tuple(sheet.columns)

for eachCol in columns:
    with open('textFileNo.{}.txt'.format(columns.index(eachCol) + 1), 'w') as textFile:
        for eachRow in eachCol:
            textFile.write(str(eachRow.value) + '\n')
