tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    #CHECK MAXIMUM WIDTH COLUMNS
    columnNum = []
    for each in range(len(tableData)):
        maxlength = []
        for i in tableData[each]:
            maxlength.append(len(i))
        columnNum.append(max(maxlength))
    print(columnNum)
    #PRINTING ITEMS IN TABLE
    for each in range(4):
        for i in range(len(tableData)):
            if i < int(len(tableData)-1):
                print(tableData[i][each].rjust(columnNum[i]) + ' ', end='')
            else:
                print(tableData[i][each].rjust(columnNum[i]) + ' ')
printTable()
