from reportlab.pdfgen.canvas import Canvas
import datetime
import os

date = datetime.datetime.now()

pdf_name = date.strftime("%d%m%Y_%f") + ".pdf"

save_name = os.path.join(os.path.expanduser("~"), "/Python/backend/program/static/pdf/", pdf_name)

letter = "Hello Petrus Dughem Wrote the Code for this PDF to automaticly Generate! PETRUS IS THE KING!"

c = Canvas(save_name, pagesize=letter)

c.setTitle("PETRUS DID THIS")

c.drawString(100, 750, pdf_name)

c.save()

