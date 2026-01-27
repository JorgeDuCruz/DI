import sqlite3

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, SimpleDocTemplate, Spacer, Paragraph

from ExemploUsoDrawing import guion


def obter_clientes_mais_facturacion(path, limite = 10):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT c.nome, COUNT(DISTINCT f.id_factura) as num_facturas,
        SUM(if.cantidade * if.prezo_unitario * (1-if.desconto/100)*(1+p.iva/100)) as facturacion_total
        FROM clientes c
        JOIN facturas f ON c.id_cliente = f.id_cliente
        JOIN linhas_factura if ON f.id_factura = if.id_factura
        JOIN produtos p ON if.id_produto = p.id_produto
        GROUP BY c.id_cliente, c.nome
        ORDER BY facturacion_total DESC
        LIMIT ?
    """,(limite,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

def pdf():
    guion = []
    datos = obter_clientes_mais_facturacion("bdTendaOrdeadoresBig.bd",5)

    fila0 = ['Pos.', 'Cliente', 'Nº Facturas', 'Facturacion total']
    tabla = [fila0]



    for orde, linea in enumerate(datos):
        fila = [orde+1, linea[0], linea[1], '%0.2f€' % (linea[2],)]
        tabla.append(fila)



    estilo = [
        # Cabeceira
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        # Corpo
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('ALIGN', (2, 1), (2, -1), 'CENTER'),
        ('ALIGN', (-1, 1), (-1, -1), 'RIGHT'),
    ]

    for i in range(2,len(datos),2):
        estilo.append(('BACKGROUND', (0,i), (-1, i), colors.lightgreen))

    tab = Table(tabla)
    tab.setStyle(estilo)
    guion.append(tab)

    #-----------------------------Tabla----------------------------------


    #-----------------------------Tarta----------------------------------
    ancho = 400
    alto = 350
    debuxo = Drawing(ancho,alto)
    tarta = Pie()
    facturacion = []
    etiquetas = []
    for linea in datos:
        facturacion.append(linea[-1])
        etiquetas.append(linea[0])

    tarta.x = ancho/2-100
    tarta.y = alto/2 -50
    tarta.width = 200
    tarta.height = 200
    tarta.data = facturacion
    tarta.labels = etiquetas
    tarta.sideLabels = 1

    debuxo.add(tarta)
    guion.append(Spacer(0,40))
    guion.append(debuxo)

    #------------------------------Tarta----------------------------------

    #-----------------------------Analisis--------------------------------

    elemetos = []
    follaestilo = getSampleStyleSheet()
    estiloTitulo = follaestilo["Title"]
    titulo = Paragraph("Informe de clientes por facturación",estiloTitulo)

    doc = SimpleDocTemplate("CorreccionExamenReportLab(JorgeDuranCruz).pdf", pagesize=A4)
    doc.build(guion)
pdf()