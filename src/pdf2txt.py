# PDFTOPPMPATH = r"poppler\poppler-0.68.0\bin\pdftoppm.exe"
# PDFFILE = "345syllabus.pdf"

# import subprocess
# subprocess.Popen('"%s" -png "%s" out' % (PDFTOPPMPATH, PDFFILE))

# print("done")


import PyPDF2

#create file object variable
#opening method will be rb

filename = 'Syllabus APS360 Fall 2022'
pfilename = 'syllabipdf/' + filename + '.pdf'
pdffileobj=open(pfilename,'rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)

#This will store the number of pages of this pdf file
x=pdfreader.numPages

print("NUM PAGES:",x)

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
    tfilename = 'syllabitxt/' + filename + '.txt'
    file1=open(tfilename,"a")
    file1.writelines(text)