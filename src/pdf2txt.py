# PDFTOPPMPATH = r"poppler\poppler-0.68.0\bin\pdftoppm.exe"
# PDFFILE = "345syllabus.pdf"

# import subprocess
# subprocess.Popen('"%s" -png "%s" out' % (PDFTOPPMPATH, PDFFILE))

# print("done")


import PyPDF2
from os import listdir
from os.path import isfile, join

#create file object variable
#opening method will be rb

#listing all pdf files in directory
fn = [f for f in listdir('syllabipdf') if isfile(join('syllabipdf', f))]

print('\n', fn, '\n')

for filename in fn:
    pfilename = 'syllabipdf/' + filename
    pdffileobj=open(pfilename,'rb')
    
    #create reader variable that will read the pdffileobj
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)

    #This will store the number of pages of this pdf file
    x=pdfreader.numPages

    for i in range(x):
        #create a variable that will select the selected number of pages
        pageobj=pdfreader.getPage(i)
        
        #(x+1) because python indentation starts with 0.
        #create text variable which will store all text datafrom pdf file
        text=pageobj.extractText()
        
        #save the extracted data from pdf to a txt file
        #we will use file handling here
        #dont forget to put r before you put the file path
        #go to the file location copy the path by right clicking on the file
        #click properties and copy the location path and paste it here.
        #put "\\your_txtfilename"
        tfilename = 'syllabitxt/' + filename.split(".")[0] + '.txt'
        file1=open(tfilename,"a", encoding="utf-8")
        file1.writelines(text)