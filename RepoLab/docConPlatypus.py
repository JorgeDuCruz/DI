from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
from reportlab.platypus import Paragraph, Table
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os

guion = []

follaEstilo = getSampleStyleSheet()

print(follaEstilo.list())
cabeceira = follaEstilo ["Heading4"]

cabeceira.pageBreakBefore = 0
cabeceira.backColor = colors.lightblue

paragrafo = Paragraph("Cabeceira do documento",cabeceira)
guion.append(paragrafo)

cabeceiraCursiva = follaEstilo ["Heading3"]

cabeceiraCursiva.pageBreakBefore = 0
cabeceiraCursiva.fontSize = 18
cabeceiraCursiva.fontName = "Helvetica-Oblique"
cabeceiraCursiva.alignment = 1
cabeceiraCursiva.borderColor = colors.blue
cabeceiraCursiva.borderWidth = 2

paragrafo3 = Paragraph("Cabeceira do documento",cabeceiraCursiva)
guion.append(paragrafo3)

texto = "Texto incluido no documento, e que forma o contido." * 1000

corpoTexto = follaEstilo["BodyText"]
corpoTexto.fontSize = 12
paragrafo2 = Paragraph(texto,corpoTexto)

guion.append(Spacer(0,30))
guion.append(paragrafo2)

imaxe = Image("equis23x23.jpg",23,23)
#guion.append(imaxe)

texto = Paragraph("Libre")


tit = ['Horario','','','','','','','']
cab = ['','Luns','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
actM = ['Mañán','Clases','Correr',[imaxe,texto],'-','-','Estudar','Traballar']
actT = ['Tarde','Traballar','Clases','Clases','Clases','Traballar','Traballar','Ler']
actN = ['Noite','-','Traballar','Traballar','Traballar','-','-','-']

taboa = Table([tit,cab,actM,actT,actN])
taboa.setStyle([('TEXTCOLOR',(1,-4),(7,-4),colors.red),
                ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                ('BOX',(0,0),(-1,-1),1,colors.green),
                ('INNERGRID',(1,2),(-1,-1),0.25,colors.black),
                ('LINEBELOW',(1,1),(7,1),0.25,colors.black),
                ('LINEBEFORE',(1,2),(1,-1),0.25,colors.black),
                ('SPAN',(0,0),(-1,0)),
                ('ALIGN',(0,0),(-1,0),'CENTER'),
                ('BACKGROUND',(1,-4),(-1,-4),colors.lightgrey)])
guion.append(taboa)


d = Drawing(400,200)
titulo = Label()
titulo.setOrigin(200,190)
titulo.setText("Porcentaxe contratados/aprobados")
d.add(titulo)

lendaLateral = Label()
lendaLateral.setOrigin(10,100)
lendaLateral.angle = 90
lendaLateral.setText("Porcentaxe")
d.add(lendaLateral)

datos = [(13.3,8,14.3,25,33.3,37.5,21.1,28.6,45.5,38.1,54.6,36.0,42.3),
         (67,69,68,81,92,90,87,82,77,79,59,69,61)]
lendaDatos = ['11/12','12/13','13/14','14/15','15/16','16/17','17/18','18/19','19/20','20/21','21/22','22/23','23/24','24/25']

graficoBarras = VerticalBarChart()

graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 100
graficoBarras.valueAxis.valueStep = 10
graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.dx = 8
graficoBarras.categoryAxis.labels.dy = -10
graficoBarras.categoryAxis.labels.angle = 30
graficoBarras.categoryAxis.categoryNames = lendaDatos
graficoBarras.groupSpacing = 10
graficoBarras.barSpacing = 5

d.add(graficoBarras)
guion.append(Spacer(0,20))
guion.append(d)

doc = SimpleDocTemplate("exemploPlatypus.pdf",pagesize=A4,showBoundary = 1)

doc.build(guion)