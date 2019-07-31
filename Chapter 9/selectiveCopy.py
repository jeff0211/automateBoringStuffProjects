import os, shutil

extCopy = input('Enter the extension for files to be copied:\n')
srcFolder = input('Enter source folder to copy from:\n')
desFolder = input('Enter destination folder to copy to:\n')

for folders, subfolders, files in os.walk(srcFolder):
    for each in files:
        if each.endswith(extCopy):
            shutil.copy(os.path.join(folders, each), desFolder)

print('Files with extension ' + extCopy + ' copied to destination.')
