import os

srcFolder = input('Enter source folder to search from:\n')
delFileSize = int(input('Show file with file size more than (In MegaBytes):\n')) * 1000000

for folders, subfolders, files in os.walk(srcFolder):
    for file in files:
        fileSize = int(os.path.getsize(os.path.join(folders, file)))
        if int(fileSize) > delFileSize:
            mypath = os.path.split(os.path.join(folders, file))
            print('Absolute path: ' + mypath[0])
            print('File name: ' + mypath[1])
            print('File size: ' + str('{:,}'.format(fileSize)) + ' bytes\n')
