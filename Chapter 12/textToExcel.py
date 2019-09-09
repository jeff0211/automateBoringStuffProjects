import os, openpyxl

os.chdir()  # Change your current working directory to folder with text files.

fileList = []
for eachTextFile in os.listdir():
    if eachTextFile.endswith('.txt'):
        fileList.append(eachTextFile)

excelFileName = input('Spreadsheet Name(Without extension): ') + '.xlsx'
wb = openpyxl.Workbook()
wb.save(excelFileName)  # Save the workbook to current working directory.
for eachFile in range(len(fileList)):
    with open(fileList[eachFile]) as textFile:
        wb = openpyxl.load_workbook(excelFileName)
        sheet = wb.active
        rowNum = 1
        for eachLine in textFile.readlines():
            sheet.cell(row=rowNum, column=eachFile + 1).value = eachLine.strip('\n')
            rowNum += 1
        wb.save(excelFileName)
print('Contents of text files copied to {}.'.format(excelFileName))
