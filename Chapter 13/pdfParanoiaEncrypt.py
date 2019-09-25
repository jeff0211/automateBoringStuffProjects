import os, sys, PyPDF2

password = sys.argv[1]
srcFolder = str(input('Source folder: '))

print('Creating copies of encrypted files...')
for folders, subfolders, files in os.walk(srcFolder):
    for eachFile in files:
        # Add pages of PDF file to be encrypted to pdfWriter.
        if eachFile.endswith('.pdf'):
            srcFile = os.path.join(folders, eachFile)
            pdfFile = open(srcFile, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            # Create and encrypt the PDF files with suffix _encrypted.pdf.
            pdfWriter.encrypt(password)
            fileName = os.path.splitext(eachFile)[0] + '_encrypted.pdf'
            encryptedPdf = open(os.path.join(folders, fileName), 'wb+')
            pdfWriter.write(encryptedPdf)
            # Check if the new PDF files created are correctly encrypted.
            pdfReader2 = PyPDF2.PdfFileReader(encryptedPdf)
            if pdfReader2.isEncrypted:
                print(f'{eachFile} is successfully encrypted!')
            else:
                print(f'{eachFile} is not encrypted!')
pdfFile.close()
encryptedPdf.close()
