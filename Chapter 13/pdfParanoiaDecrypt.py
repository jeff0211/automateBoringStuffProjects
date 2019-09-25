import os, sys, PyPDF2

password = sys.argv[1]
srcFolder = str(input('Source folder: '))

print('Decrypting files...')
for folders, subfolders, files in os.walk(srcFolder):
    for eachFile in files:
        if eachFile.endswith('.pdf'):
            srcFile = os.path.join(folders, eachFile)
            pdfFile = open(srcFile, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            if pdfReader.isEncrypted:
                # Try to decrypt the PDF file with a given password.
                try:
                    pdfReader.decrypt(password)
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    fileName = os.path.splitext(eachFile)[0] + '_decrypted.pdf'
                    decryptedPdf = open(os.path.join(folders, fileName), 'wb')
                    pdfWriter.write(decryptedPdf)
                    print(f'{eachFile} is successfully decrypted!')
                # Throws an exception error when password given is wrong.
                except Exception as err:
                    print(str(err) + f', wrong password: {eachFile}')
pdfFile.close()
decryptedPdf.close()
