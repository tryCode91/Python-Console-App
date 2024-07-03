import PyPDF2
import os

filename = os.path.join('static', 'pdf/application.pdf')

reader = PyPDF2.PdfReader(filename)

print("pages: ", len(reader.pages))

print(reader.pages[0].extract_text())