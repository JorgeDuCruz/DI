from reportlab.platypus import Table, SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


guion = []

tit = ['FACTURA SIMPLIFICADA','','','']
cab = ['Nombre de tu Empresa','Logo de la Empresa']
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
    final
])

taboa.setStyle([('SPAN',(0,0),(-1,0)),
                ('ALIGN',(0,0),(-1,0),'RIGHT'),
                ('TEXTCOLOR',(0,0),(-1,6),colors.darkgreen),
                ('FONT',(0,0),(-1,6),"Helvetica-Bold"),
                ])
guion.append(taboa)



doc = SimpleDocTemplate("FacturaEjemplo.pdf",pagesize=A4)

doc.build(guion)
