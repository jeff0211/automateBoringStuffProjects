import re, os

folder_path = r'C:\Users\User\Documents\myPythonProjects\AutomateBoringStuffsProjects\Chapter_8\myRegSearch\regSrchFolder'
list_dir = os.listdir(folder_path)

# Regex pattern for searching email addresses = \w+@.*\.com (User Input Sample)
regex_email = re.compile(input('Enter a regex:\n'))
for each in list_dir:
    with open(os.path.join(folder_path,each)) as my_file:
        file_contents = my_file.read()
        regex_found = regex_email.findall(file_contents)
        if regex_found == []:
            print('No results found in ' + each + '.')
        else:
            print('Search results for ' + each + ':')
            print('\n'.join(i for i in regex_found))



