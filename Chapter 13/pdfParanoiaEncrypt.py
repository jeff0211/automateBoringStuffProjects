import os, sys, PyPDF2

password = sys.argv[1]
srcFolder = str(input('Source folder: '))
os.chdir(srcFolder)

for folders, subfolders, files in os.walk(srcFolder):
    # Creating a duplicate copy of the PDF files.
    print('Creating copies of encrypted files...')
    for eachFile in files:
        pdfFile = open(eachFile, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        # Create and encrypt the PDF files with suffix _encrypted.pdf.
        pdfWriter.encrypt(password)
        fileName = os.path.splitext(eachFile)[0] + '_encrypted.pdf'
        encryptedPdf = open(fileName, 'wb+')
        pdfWriter.write(encryptedPdf)
        # Check if the new PDF file created is correctly encrypted or not.
        pdfReader2 = PyPDF2.PdfFileReader(encryptedPdf)
        if pdfReader2.isEncrypted:
            print(f'{eachFile} is successfully encrypted!')
        else:
            print(f'{eachFile} is not encrypted!')

pdfFile.close()
encryptedPdf.close()
