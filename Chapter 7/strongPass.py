import re

# Check minimum password length
passRegexLen = re.compile(r'\w{8,}')
# Check if password has any digits
passRegexNoDig = re.compile(r'[0-9]+')
# Check if password has lowercase characters
passRegexLowCase = re.compile(r'[a-z]+')
# Check if password has uppercase characters
passRegexUpCase = re.compile(r'[A-Z]+')

def checkpword(pword):
    if passRegexLen.search(pword) == None:
        print("Please enter a password with minimum 8 characters.")
    elif passRegexNoDig.search(pword) == None:
        print("Please enter a password with at least 1 digit.")
    elif passRegexLowCase.search(pword) == None:
        print("Please enter a password with at least 1 lowercase character.")
    elif passRegexUpCase.search(pword) == None:
        print("Please enter a password with at least 1 uppercase character.")
    else:
        print("Strong password created.")

checkpword(str(input()))
