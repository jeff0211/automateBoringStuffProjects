import sys, shelve, pyperclip

myshelve = shelve.open('shelve1')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    myshelve[sys.argv[2]] = pyperclip.paste()
    print('Keyword saved.')
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    myshelve.pop(sys.argv[2])
    print('Keyword deleted.')
elif len(sys.argv) == 2:
    if sys.argv[1] in myshelve:
        pyperclip.copy(myshelve[sys.argv[1]])
        print('Value for keyword copied.')
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(myshelve.keys())))
        print('List of keywords copied.')
    elif sys.argv[1].lower() == 'delete':
        myshelve.clear()
        print('All keywords cleared.')
myshelve.close()

# Values for Testing - alpha:ABCDE number:12345
