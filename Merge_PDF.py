# AD1 Systems - PDF Merger

# This project uses the PdfMerger module from the PyPDF2 package which helps merge 2 PDF files

from PyPDF2 import PdfMerger

pdf1 = input("Input the first PDF you want to merge: ")
pdf2 = input("Input the second PDF you want to merge: ")

listofpdfs = [pdf1, pdf2]

merger = PdfMerger()

for pdf in listofpdfs:
    merger.append(pdf)

newname = input("Input name of merged PDF: ")

merger.write(newname + ".pdf")
merger.close()