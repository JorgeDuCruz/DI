from reportlab.platypus import Table, SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


guion = []

tit = ['','','FACTURA SIMPLIFICADA','']
cab = ['Nombre de tu Empresa','','Logo de la Empresa','']
dic = ['Dirección','']
loc = ['Ciudad y País','']
NIF = ['CIF/NIF','','Fecha Emisión','DD/MM/AAAA']
tel = ['Teléfono','','Número de Factura','A0001']
mail = ['Mail','']
spc = ['']
desc =['Descripción','Importe','Cantidad','Total']
p1 = ['Producto 1','3,2','5','16,00']
p2 = ['Producto 2','2,1','3','6,30']
p3 = ['Producto 3','2,9','76','220,40']
p4 = ['Producto 4','5','23','115,00']
p5 = ['Producto 5','4,95','3','14,85']
p6 = ['Producto 6','6','2','12,00']
final = ['','','TOTAL','385€']

taboa = Table([
    tit,
    cab,
    dic,
    loc,
    NIF,
    tel,
    mail,
    spc,
    desc,
    p1,
    p2,
    p3,
    p4,
    p5,
    p6,
    spc,
    final
])

taboa.setStyle([('SPAN',(2,0),(-1,0)),
                ('SPAN',(2,1),(-1,1)),
                ('ALIGN',(2,0),(-1,1),'RIGHT'),
                ('TEXTCOLOR',(0,0),(-1,6),colors.darkgreen),
                ('FONT',(0,0),(-1,8),"Helvetica-Bold"),
                ('SIZE',(0,0),(-1,1),18),
                ('FONT',(-1,4),(-1,6),"Helvetica"),
                ('ALIGN',(0,8),(-1,15),'CENTER'),
                ('ALIGN',(-1,9),(-1,15),'RIGHT'),
                ('BACKGROUND',(0,8),(-1,8),colors.darkgreen),
                ('TEXTCOLOR',(0,8),(-1,8),colors.white),
                ('BACKGROUND',(0,9),(-1,14),colors.lightgreen),
                ('BACKGROUND',(2,16),(-1,16),colors.darkgreen),
                ('TEXTCOLOR',(2,16),(-1,16),colors.white),
                ('INNERGRID', (0,8), (-1, 15), 0.5, colors.white),
                ('FONT',(2,16),(-1,16),"Helvetica-Bold",12),
                ('ALIGN',(2,16),(-1,16),"CENTER"),
                ('TOPPADDING',(1,1),(-1,1),20),
                ('TOPPADDING',(0,2),(-1,2),20),
                ])
guion.append(taboa)



doc = SimpleDocTemplate("FacturaEjemplo.pdf",pagesize=A4)

doc.build(guion)
