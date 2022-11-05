# PDFTOPPMPATH = r"poppler\poppler-0.68.0\bin\pdftoppm.exe"
# PDFFILE = "345syllabus.pdf"

# import subprocess
# subprocess.Popen('"%s" -png "%s" out' % (PDFTOPPMPATH, PDFFILE))

# print("done")
import sys

sys.path
sys.executable


# import PyPDF2
 
#create file object variable
#opening method will be rb
pdffileobj=open('src/345syllabus.pdf','rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
 
# Store Pdf with convert_from_path function
images = convert_from_path('345syllabus.pdf')
 
#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
text=pageobj.extractText()
 
#save the extracted data from pdf to a txt file
#we will use file handling here
#dont forget to put r before you put the file path
#go to the file location copy the path by right clicking on the file
#click properties and copy the location path and paste it here.
#put "\\your_txtfilename"
file1=open(r"C:\Users\SIDDHI\AppData\Local\Programs\Python\Python38\\1.txt","a")
file1.writelines(text)