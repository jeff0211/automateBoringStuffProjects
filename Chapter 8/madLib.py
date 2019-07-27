import re

with open(r'Chapter_8/myMadLib/madLibText.txt') as madLibFile:
    madLib = madLibFile.read()
    list_terms = re.findall(r'ADJECTIVE|NOUN|VERB', madLib)
    for each in list_terms:
        regex_terms = re.compile(each)
        if each == 'ADJECTIVE':
            userinput = input('Enter an ' + each + ' :\n')
        elif each == 'NOUN' or each == 'VERB':
            userinput = input('Enter a ' + each + ' :\n')
        madLib = regex_terms.sub(userinput, madLib, 1)

with open(r'Chapter_8/myMadLib/newMadLib.txt', 'w') as newMadLibFile:
    newMadLibFile.write(madLib)
