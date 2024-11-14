from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sys

txtToPdf = sys.argv[1]
toPdf = sys.argv[2]

def txt_to_pdf(txt_file, pdf_file):
    # Crear un objeto Canvas para el archivo PDF
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    # Leer el archivo .txt
    with open(txt_file, "r", encoding="utf-8") as file:
        text = file.readlines()

    # Configurar márgenes y posición inicial
    x_offset, y_offset = 50, height - 50
    line_height = 14  # Espacio entre líneas

    for line in text:
        if y_offset < 40:  # Si llegamos al final de la página, agregar una nueva
            c.showPage()
            y_offset = height - 50
        c.drawString(x_offset, y_offset, line.strip())
        y_offset -= line_height

    c.save()  # Guardar el PDF

# Llamada a la función
txt_to_pdf(txtToPdf,toPdf)
