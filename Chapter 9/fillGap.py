import os, re, shutil

# C:\Users\User\Documents\myPythonProjects\AutomateBoringStuffsProjects\Chapter_9\Ch9_Test
srcFolder = r'C:\Users\User\Documents\myPythonProjects\AutomateBoringStuffsProjects\Chapter_9\Ch9_Test'
    # input('Enter source folder to search from:\n')
# C:\Users\User\Documents\myPythonProjects\AutomateBoringStuffsProjects\Chapter_9\Ch9_Test\Ch9_NewCopy
desFolder = r'C:\Users\User\Documents\myPythonProjects\AutomateBoringStuffsProjects\Chapter_9\Ch9_Test\Ch9_NewCopy'
    # input('Enter destination folder to move and rename:\n')

prefixCount = 1
list_files = []

fileRegex = re.compile(r'(\w+)(\d{3})(\.\w+)')
for folders, subfolders, files in os.walk(srcFolder):
    for file in files:
        fileObj1 = fileRegex.search(file)
        if fileObj1 != None:
            list_files.append(file)

for each in sorted(list_files):
    fileObj2 = fileRegex.search(each)
    if fileObj2 != None:
            prefix = str(prefixCount).zfill(3)
            newFileName = fileObj2.group(1) + prefix + fileObj2.group(3)
            prefixCount += 1
            print(newFileName)
            shutil.move(os.path.join(srcFolder, each), os.path.join(desFolder, newFileName))
