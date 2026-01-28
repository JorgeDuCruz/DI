from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm

def generar_factura_pdf(nombre_archivo="factura.pdf"):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    width, height = A4

    # Colores
    verde_oscuro = colors.HexColor("#2f5d1e")
    verde_claro = colors.HexColor("#e6f2df")

    # === BARRA LATERAL ===
    c.setFillColor(verde_claro)
    c.rect(0, 0, 2 * cm, height, stroke=0, fill=1)

    # === TITULO EMPRESA ===
    c.setFillColor(verde_oscuro)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(3 * cm, height - 3 * cm, "Nombre de tu Empresa")

    c.setFont("Helvetica", 10)
    texto_empresa = [
        "Dirección",
        "Ciudad y País",
        "CIF/NIF",
        "Teléfono",
        "Mail"
    ]

    y = height - 4 * cm
    for linea in texto_empresa:
        c.drawString(3 * cm, y, linea)
        y -= 0.5 * cm

    # === FACTURA + LOGO ===
    c.setFont("Helvetica-Bold", 16)
    c.drawRightString(width - 2 * cm, height - 3 * cm, "FACTURA SIMPLIFICADA")

    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(width - 2 * cm, height - 4.2 * cm, "Logo de la Empresa")

    c.setFont("Helvetica", 10)
    c.drawRightString(width - 2 * cm, height - 5.2 * cm, "Fecha Emisión:  DD/MM/AAAA")
    c.drawRightString(width - 2 * cm, height - 5.8 * cm, "Número de Factura:  A0001")

    # === TABLA DE PRODUCTOS ===
    data = [
        ["Descripción", "Importe", "Cantidad", "Total"],
        ["Producto 1", "3,20", "5", "16,00"],
        ["Producto 2", "2,10", "3", "6,30"],
        ["Producto 3", "2,90", "76", "220,40"],
        ["Producto 4", "5,00", "23", "115,00"],
        ["Producto 5", "4,95", "3", "14,85"],
        ["Producto 6", "6,00", "2", "12,00"],
    ]

    tabla = Table(
        data,
        colWidths=[8 * cm, 3 * cm, 3 * cm, 3 * cm],
        rowHeights=0.8 * cm
    )

    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), verde_oscuro),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONT", (0, 1), (-1, -1), "Helvetica"),
        ("BACKGROUND", (0, 1), (-1, -1), verde_claro),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.white),
    ]))

    tabla.wrapOn(c, width, height)
    tabla.drawOn(c, 3 * cm, height - 14 * cm)

    # === TOTAL ===
    c.setFillColor(verde_oscuro)
    c.rect(width - 8 * cm, height - 18 * cm, 6 * cm, 1.5 * cm, stroke=0, fill=1)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width - 5 * cm, height - 17.4 * cm, "TOTAL   385 €")

    # Finalizar PDF
    c.showPage()
    c.save()

if __name__ == "__main__":
    generar_factura_pdf("facturaChatGPT.pdf")