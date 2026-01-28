# -*- coding: utf-8 -*-
"""
factura_reportlab.py
Genera una factura simplificada estilo ejemplo usando reportlab.
Instalar: pip install reportlab
Ejecutar: python factura_reportlab.py
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import locale

# Opcional: establecer locale para formateo numérico (no imprescindible)
# locale.setlocale(locale.LC_ALL, '')  # Descomentar si tu sistema tiene locale configurado

PAGE_SIZE = landscape(A4)
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE

def format_number_es(val):
    # Formatea número con 2 decimales y coma como separador decimal
    return f"{val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def draw_sidebar(c, x, y, width, height, dark_color, light_color, dot_color):
    # Barra lateral oscura
    c.setFillColor(dark_color)
    c.rect(x, y, width, height, stroke=0, fill=1)

    # Banda clara al lado con patrón de puntos
    band_x = x + width + 6*mm
    band_width = 18*mm
    c.setFillColor(light_color)
    c.rect(band_x, y, band_width, height, stroke=0, fill=1)

    # Dots pattern (repeating puntos)
    c.setFillColor(dot_color)
    dot_spacing_x = 6
    dot_spacing_y = 6
    dot_r = 0.8
    # dibujar puntos en una rejilla dentro de la banda
    start_x = band_x + 4
    start_y = y + 4
    end_x = band_x + band_width - 4
    end_y = y + height - 4
    yy = start_y
    while yy < end_y:
        xx = start_x
        while xx < end_x:
            c.circle(xx, yy, dot_r, stroke=0, fill=1)
            xx += dot_spacing_x
        yy += dot_spacing_y

def main():
    c = canvas.Canvas("facturaCopilot.pdf", pagesize=PAGE_SIZE)
    c.setTitle("Factura Simplificada - Ejemplo")

    # Colores aproximados a la imagen
    dark_green = colors.HexColor("#234d15")   # verde oscuro
    mid_green = colors.HexColor("#cfe6c9")    # verde claro para filas
    header_green = colors.HexColor("#234d15") # mismo que dark para cabecera
    light_band = colors.HexColor("#e6f0df")   # banda clara lateral
    dot_color = colors.HexColor("#d1e6c8")

    margin_left = 18*mm
    margin_right = 18*mm
    top_margin = 18*mm
    bottom_margin = 18*mm

    # Dibujar barra lateral
    sidebar_x = margin_left - 8*mm
    sidebar_y = bottom_margin
    sidebar_width = 12*mm
    sidebar_height = PAGE_HEIGHT - bottom_margin - top_margin
    draw_sidebar(c, sidebar_x, sidebar_y, sidebar_width, sidebar_height, dark_green, light_band, dot_color)

    # Titulos y textos
    # Empresa (izquierda)
    company_x = margin_left + 10*mm
    company_y_top = PAGE_HEIGHT - top_margin - 10*mm

    # Nombre de la empresa (grande)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(dark_green)
    c.drawString(company_x, company_y_top, "Nombre de tu Empresa")

    # Datos de la empresa (itálica)
    c.setFont("Helvetica-Oblique", 11)
    c.setFillColor(dark_green)
    company_info_y = company_y_top - 22
    line_height = 14
    company_lines = [
        "Dirección",
        "Ciudad y País",
        "CIF/NIF",
        "Teléfono",
        "Mail"
    ]
    for i, line in enumerate(company_lines):
        c.drawString(company_x, company_info_y - i*line_height, line)

    # Encabezado derecho (FACTURA SIMPLIFICADA)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(dark_green)
    header_x = PAGE_WIDTH - margin_right - 160*mm/2
    # aproximación: ubicarlo en la parte superior derecha
    c.drawString(PAGE_WIDTH - margin_right - 160, PAGE_HEIGHT - top_margin - 8*mm, "FACTURA SIMPLIFICADA")

    # Logo placeholder (rectángulo con texto)
    logo_w = 80
    logo_h = 40
    logo_x = PAGE_WIDTH - margin_right - logo_w
    logo_y = PAGE_HEIGHT - top_margin - 40
    c.setStrokeColor(dark_green)
    c.setFillColor(colors.whitesmoke)
    c.rect(logo_x, logo_y, logo_w, logo_h, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_green)
    c.drawCentredString(logo_x + logo_w/2, logo_y + logo_h/2 - 4, "Logo de la Empresa")

    # Fechas y número de factura (derecha, bajo logo)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(dark_green)
    info_right_x = PAGE_WIDTH - margin_right - 160
    info_right_y = logo_y - 8
    c.drawString(info_right_x, info_right_y, "Fecha Emisión")
    c.drawRightString(PAGE_WIDTH - margin_right, info_right_y, "DD/MM/AAAA")
    c.drawString(info_right_x, info_right_y - 16, "Número de Factura")
    c.drawRightString(PAGE_WIDTH - margin_right, info_right_y - 16, "A0001")

    # Datos de tabla (ejemplo)
    products = [
        ("Producto 1", 3.2, 5),
        ("Producto 2", 2.1, 3),
        ("Producto 3", 2.9, 76),
        ("Producto 4", 5.0, 23),
        ("Producto 5", 4.95, 3),
        ("Producto 6", 6.0, 2),
    ]
    # Preparar datos para la tabla
    table_data = []
    header = ["Descripción", "Importe", "Cantidad", "Total"]
    table_data.append(header)
    total_sum = 0.0
    for desc, price, qty in products:
        total = price * qty
        total_sum += total
        # Formato con coma decimal
        price_str = format_number_es(price)
        total_str = format_number_es(total)
        table_data.append([desc, price_str, str(qty), total_str])

    # Añadir fila de separación vacía si queremos espacio antes de TOTAL
    # Definir la tabla
    # Ubicación de la tabla: ancho amplio en la parte media-izquierda/derecha
    table_x = margin_left + 10*mm
    table_y_top = info_right_y - 60  # punto por encima donde empezamos a dibujar la tabla
    # Para Platypus Table, necesitamos definir ancho y luego dibujar con wrapOn/drawOn
    col_widths = [250, 80, 80, 80]  # en puntos (ajusta según necesidad)

    table_style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), header_green),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1, -1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.whitesmoke),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ])

    # Crear la tabla
    table = Table(table_data, colWidths=col_widths, hAlign='LEFT')
    table.setStyle(table_style)

    # Aplicar colores alternos a las filas (desde la primera fila de datos: index 1)
    for i in range(1, len(table_data)):
        if i % 2 == 1:
            bg = mid_green
        else:
            # un tono ligeramente más claro
            bg = colors.HexColor("#eaf3e7")
        table_style.add('BACKGROUND', (0,i), (-1,i), bg)
    table.setStyle(table_style)

    # Calcular posición para dibujar la tabla
    # wrapOn necesita un ancho y alto máximos
    max_table_width = sum(col_widths)
    # Ubicar la tabla a la altura deseada
    table_wrap_width, table_wrap_height = table.wrapOn(c, max_table_width, 400)
    # Dibujar la tabla un poco más abajo de company info
    table_draw_x = table_x
    table_draw_y = table_y_top - table_wrap_height
    table.drawOn(c, table_draw_x, table_draw_y)

    # Recuadro TOTAL a la derecha inferior (oscuro)
    total_box_w = 220
    total_box_h = 70
    total_box_x = PAGE_WIDTH - margin_right - total_box_w
    # colocarlo por debajo de la tabla con un poquito de margen
    total_box_y = table_draw_y - 30 - total_box_h
    if total_box_y < bottom_margin:
        total_box_y = bottom_margin + 10

    # Fondo oscuro
    c.setFillColor(dark_green)
    c.rect(total_box_x, total_box_y, total_box_w, total_box_h, stroke=0, fill=1)

    # Dividir el recuadro en dos columnas: etiqueta y cantidad
    # Texto "TOTAL" (blanco) en la parte izquierda del recuadro
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.white)
    c.drawString(total_box_x + 12, total_box_y + total_box_h/2 + 6, "TOTAL")

    # Cantidad (a la derecha) en grande
    amount_text = format_number_es(total_sum) + " €"
    c.setFont("Helvetica-Bold", 22)
    c.drawRightString(total_box_x + total_box_w - 12, total_box_y + total_box_h/2 + 6, amount_text)

    # Firma o nota inferior (opcional)
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.grey)
    c.drawString(margin_left + 10*mm, bottom_margin + 6*mm, "Esta es una factura simplificada de ejemplo generada con ReportLab.")

    c.showPage()
    c.save()
    print("PDF generado: factura_ejemplo.pdf")

if __name__ == "__main__":
    main()