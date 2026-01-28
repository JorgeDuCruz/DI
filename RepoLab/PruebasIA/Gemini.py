from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor


def create_invoice(filename):
    # Definición de colores basados en la imagen
    DARK_GREEN = HexColor('#1f4e18')  # Verde oscuro (encabezados, total, barra sup)
    LIGHT_GREEN = HexColor('#dbebc9')  # Verde claro (filas tabla, barra lateral)
    TEXT_COLOR = colors.black

    # Configuración del documento
    # Dejamos margen izquierdo amplio para la barra lateral
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            leftMargin=25 * mm, rightMargin=15 * mm,
                            topMargin=15 * mm, bottomMargin=15 * mm)

    elements = []
    styles = getSampleStyleSheet()

    # --- Estilos de Texto Personalizados ---
    style_header_right = ParagraphStyle(
        'HeaderRight', parent=styles['Normal'], fontName='Helvetica-Bold',
        fontSize=14, textColor=colors.gray, alignment=2, spaceAfter=20
    )  # "FACTURA SIMPLIFICADA" suele ser grisáceo o verde oscuro, usaré gris oscuro/verde

    style_company_name = ParagraphStyle(
        'CompanyName', parent=styles['Normal'], fontName='Helvetica-Bold',
        fontSize=20, textColor=DARK_GREEN, spaceAfter=10
    )

    style_logo_placeholder = ParagraphStyle(
        'LogoPlace', parent=styles['Normal'], fontName='Helvetica-Bold',
        fontSize=14, textColor=DARK_GREEN, alignment=2
    )

    style_normal = ParagraphStyle(
        'MyNormal', parent=styles['Normal'], fontSize=10, leading=14, textColor=DARK_GREEN
    )  # Texto verde oscuro/negro para direcciones

    style_bold_label = ParagraphStyle(
        'BoldLabel', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, textColor=DARK_GREEN, alignment=2
    )

    style_value = ParagraphStyle(
        'Value', parent=styles['Normal'], fontSize=10, textColor=colors.black, alignment=2
    )

    # ==============================
    # 1. ENCABEZADO SUPERIOR
    # ==============================
    # "FACTURA SIMPLIFICADA" alineado a la derecha
    # Nota: En la imagen está muy arriba.
    elements.append(Paragraph("FACTURA SIMPLIFICADA",
                              ParagraphStyle('Title', parent=styles['Normal'],
                                             fontName='Helvetica-Bold', fontSize=16,
                                             textColor=colors.dimgray, alignment=2)))
    elements.append(Spacer(1, 10 * mm))

    # ==============================
    # 2. BLOQUE DE EMPRESA Y LOGO
    # ==============================
    # Usamos una tabla invisible para alinear izquierda (datos) y derecha (logo)

    # Columna Izquierda: Datos Empresa
    company_data = [
        [Paragraph("Nombre de tu Empresa", style_company_name)],
        [Paragraph("<i>Dirección</i>", style_normal)],
        [Paragraph("<i>Ciudad y País</i>", style_normal)],
        [Paragraph("<i>CIF/NIF</i>", style_normal)],
        [Paragraph("<i>Teléfono</i>", style_normal)],
        [Paragraph("<i>Mail</i>", style_normal)],
    ]

    # Columna Derecha: Logo y Datos de Factura
    # Primero el logo alineado con el nombre de la empresa
    logo_data = [[Paragraph("Logo de la Empresa", style_logo_placeholder)]]

    # Creamos tablas internas para organizar
    t_company = Table(company_data, colWidths=[100 * mm])
    t_company.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0)]))

    t_logo = Table(logo_data, colWidths=[70 * mm])
    t_logo.setStyle(TableStyle([('RIGHTPADDING', (0, 0), (-1, -1), 0)]))

    # Tabla contenedora superior
    data_header_layout = [[t_company, t_logo]]
    t_layout = Table(data_header_layout, colWidths=[100 * mm, 70 * mm])
    elements.append(t_layout)

    elements.append(Spacer(1, 10 * mm))

    # ==============================
    # 3. FECHA Y NÚMERO (Alineados a la derecha)
    # ==============================
    # Creamos una tabla que empuje el contenido a la derecha

    invoice_meta_data = [
        [Paragraph("Fecha Emisión", style_bold_label), Paragraph("DD/MM/AAAA", style_value)],
        [Paragraph("Número de Factura", style_bold_label), Paragraph("A0001", style_value)],
    ]

    t_meta = Table(invoice_meta_data, colWidths=[40 * mm, 30 * mm])
    t_meta.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    # Para alinearlo a la derecha de la página, lo metemos en otra tabla con una celda vacía a la izq
    t_meta_wrapper = Table([["", t_meta]], colWidths=[100 * mm, 75 * mm])
    elements.append(t_meta_wrapper)

    elements.append(Spacer(1, 10 * mm))

    # ==============================
    # 4. TABLA DE PRODUCTOS
    # ==============================
    data = [
        ["Descripción", "Importe", "Cantidad", "Total"],
        ["Producto 1", "3,2", "5", "16,00"],
        ["Producto 2", "2,1", "3", "6,30"],
        ["Producto 3", "2,9", "76", "220,40"],
        ["Producto 4", "5", "23", "115,00"],
        ["Producto 5", "4,95", "3", "14,85"],
        ["Producto 6", "6", "2", "12,00"],
    ]

    # Anchos de columna estimados
    col_widths = [75 * mm, 30 * mm, 30 * mm, 35 * mm]

    t_products = Table(data, colWidths=col_widths)

    # Estilos de la tabla
    t_products.setStyle(TableStyle([
        # Encabezado
        ('BACKGROUND', (0, 0), (-1, 0), DARK_GREEN),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),  # Alinear "Descripción" a la izquierda

        # Cuerpo
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_GREEN),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),  # Centrar números
        ('ALIGN', (-1, 1), (-1, -1), 'RIGHT'),  # Total a la derecha
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),  # Productos a la izquierda

        # Grid (Líneas blancas)
        ('GRID', (0, 0), (-1, -1), 1, colors.white),

        # Padding
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))

    elements.append(t_products)
    elements.append(Spacer(1, 5 * mm))

    # ==============================
    # 5. TOTAL
    # ==============================
    # Tabla para el total, alineada a la derecha
    total_data = [
        ["TOTAL", "385 €"]
    ]

    # Ajustamos anchos para que coincidan con las columnas de Cantidad y Total de la tabla anterior
    # Cantidad era 30mm, Total era 35mm
    t_total = Table(total_data, colWidths=[30 * mm, 35 * mm])

    t_total.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), DARK_GREEN),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),  # Texto "TOTAL"
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),  # Valor
        ('SIZE', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.white),  # Linea blanca vertical
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))

    # Wrapper para alinear a la derecha
    # Calculamos el espacio vacío: Ancho total tabla productos (170mm) - Ancho total (65mm) = 105mm
    t_total_wrapper = Table([["", t_total]], colWidths=[105 * mm, 65 * mm])
    elements.append(t_total_wrapper)

    # Construir el PDF
    doc.build(elements, onFirstPage=draw_background, onLaterPages=draw_background)


def draw_background(canvas, doc):
    """
    Función para dibujar los elementos gráficos estáticos (la barra lateral).
    """
    canvas.saveState()

    # Definir colores
    DARK_GREEN = HexColor('#1f4e18')
    LIGHT_GREEN = HexColor('#dbebc9')

    page_width, page_height = A4

    # Barra lateral izquierda
    sidebar_x = 0
    sidebar_width = 15 * mm

    # 1. Segmento Superior (Verde Oscuro)
    # Empieza arriba del todo, altura aprox 25mm
    canvas.setFillColor(DARK_GREEN)
    canvas.rect(sidebar_x, page_height - 35 * mm, sidebar_width, 35 * mm, stroke=0, fill=1)

    # 2. Segmento Principal (Verde Claro)
    # Debajo del oscuro, hasta casi el final, con un pequeño corte
    # Digamos que empieza en height-40mm y baja mucho
    top_y_light = page_height - 37 * mm  # Pequeño hueco blanco de 2mm
    height_light = 190 * mm
    canvas.setFillColor(LIGHT_GREEN)
    canvas.rect(sidebar_x, top_y_light - height_light, sidebar_width, height_light, stroke=0, fill=1)

    # 3. Segmento Inferior (Verde Claro - Bloque pequeño)
    # Simula el corte de abajo
    bottom_y = top_y_light - height_light - 2 * mm  # Otro hueco blanco
    canvas.rect(sidebar_x, bottom_y - 20 * mm, sidebar_width, 20 * mm, stroke=0, fill=1)

    canvas.restoreState()


if __name__ == "__main__":
    create_invoice("facturaGemini.pdf")
    print("PDF generado con éxito: factura_replicada.pdf")