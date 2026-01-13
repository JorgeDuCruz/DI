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



doc = SimpleDocTemplate("exemploPlatypus.pdf",pagesize=A4,showBoundary = 1)

doc.build(guion)