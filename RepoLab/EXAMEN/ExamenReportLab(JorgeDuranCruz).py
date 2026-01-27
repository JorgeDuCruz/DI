import sqlite3

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph
from reportlab.lib.pagesizes import A4


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

def crearPDF(limite = 5):
    datos = obter_clientes_mais_facturacion("bdTendaOrdeadoresBig.bd",limite)
    print(datos)

    nombres = []
    facturas = []

    for nom in datos:
        nombres.append(nom[0])
        facturas.append(nom[2])
    print(nombres)
    print(facturas)

    d3 = Drawing(400,200)
    graficoTarta = Pie()
    graficoTarta.x = 100
    graficoTarta.y = 15
    graficoTarta.height = 170
    graficoTarta.width = 170
    graficoTarta.data = facturas
    graficoTarta.labels = nombres
    graficoTarta.slices.strokeWidth = 0.5
    graficoTarta.sideLabels = 1

    colores = [colors.blue,colors.darkgreen,colors.pink,colors.red,colors.peru]
    for i, color in enumerate(colores):
        graficoTarta.slices[i].fillColor = color


    d3.add(graficoTarta)

    fila0 = ['Pos.','Cliente','Nº Facturas', 'Facturacion total']
    tabla = [fila0]
    it = 1
    estilo = [('BACKGROUND',(0,0),(-1,0),colors.green),
                  ('BOX',(0,0),(-1,-1),1,colors.black),
                  ('INNERGRID',(0,0),(-1,-1),0.25,colors.black)]

    for da in datos:
        fila = [it,da[0],da[1],'%0.2f€'%(da[2],)]
        tabla.append(fila)
        it = it+1
        if it%2 == 0:
            estilo.append(('BACKGROUND',(0,it),(-1,it),colors.lightgreen))

    tab = Table (tabla)

    tab.setStyle(estilo)



    guion = []

    follaEstilo = getSampleStyleSheet()

    cabeceira = follaEstilo["Title"]

    cabeceira.pageBreakBefore = 0
    cabeceira.fontSize = 18
    cabeceira.fontName = "Helvetica-Oblique"
    cabeceira.alignment = 1

    titulo = Paragraph("Titulo do informe",cabeceira)
    guion.append(titulo)
    guion.append(Spacer(0,40))


    sub = follaEstilo["Heading3"]

    sub.pageBreakBefore = 0
    sub.fontSize = 15
    sub.fontName = "Helvetica"
    sub.alignment = 1

    subTItuloTorta = Paragraph("Subtítulo gráfico torta",sub)
    guion.append(subTItuloTorta)
    guion.append(Spacer(0,15))
    guion.append(d3)

    subTItuloTabla = Paragraph("Subtítulo tabla",sub)
    guion.append(Spacer(0,80))
    guion.append(subTItuloTabla)
    guion.append(tab)

    subTItuloAnalise = Paragraph("Subtitulo analise", sub)
    guion.append(subTItuloAnalise)

    textoSty = follaEstilo["BodyText"]

    facturacionTotal = 0
    mediaFacturas = 0
    for i in datos:
        facturacionTotal += i[2]
        mediaFacturas += i[1]
    mediaFacturas = mediaFacturas/ len(datos)


    analise = ("O cliente con maior facturación é %s con %0.2f €. Os %i principais clientes representan unha facturación total de %0.2f €. A media de facturas por cliente dos %i primeiros clientes é de %0.1f facturas."
               %(datos[0][0],datos[0][2], len(datos),facturacionTotal, len(datos),mediaFacturas))
    print(analise)

    txtAnalise = Paragraph(analise,textoSty)
    guion.append(txtAnalise)


    doc = SimpleDocTemplate("ExamenReportLab(JorgeDuranCruz).pdf", pagesize=A4)
    doc.build(guion)

if __name__ == "__main__":
    crearPDF(5)
