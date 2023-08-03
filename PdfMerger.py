import PyPDF2

pdfFile = ["1.pdf","2.pdf"]
merger =PyPDF2.PdfMerger()

for filename in pdfFile:
    pdfFile = open(filename , 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfFile)
pdfFile.close()
merger.write("merged.pdf")    

