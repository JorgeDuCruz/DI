from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4

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

d2 = Drawing(400,200)

graficoLinhas = HorizontalLineChart()
graficoLinhas.x = 30
graficoLinhas.y = 50
graficoLinhas.height = 125
graficoLinhas.width = 350
graficoLinhas.data = datos
graficoLinhas.categoryAxis.categoryNames = lendaDatos
graficoLinhas.categoryAxis.labels.boxAnchor = 'n'
graficoLinhas.valueAxis.valueMin = 0
graficoLinhas.valueAxis.valueMax = 100
graficoLinhas.valueAxis.valueStep = 20
graficoLinhas.lines[0].strokeWidth = 2
graficoLinhas.lines[0].symbol = makeMarker('FilledCircle')
graficoLinhas.lines[1].strokeWidth = 1.5
d2.add(graficoLinhas)

doc = SimpleDocTemplate("ExemploGrafico.pdf",pagesize=A4)
doc.build([d,Spacer(20,20),d2])