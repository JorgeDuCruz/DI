from reportlab.graphics.shapes import Image,Drawing
from  reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

guion = []

imaxe = Image (0,0,500,102,"equis23x23.jpg")

debuxo = Drawing(500,102)
debuxo.add(imaxe)

debuxo2 = Drawing(300,102)
debuxo2.add(imaxe)
debuxo2.translate(0,100)

debuxo3 = Drawing()
debuxo3.add(imaxe)
debuxo3.translate(0,200)
debuxo3.rotate(45)

debuxo4 = Drawing()
debuxo4.add(imaxe)
debuxo4.translate(0,500)
debuxo4.scale((23/500)*5,(23/102)*5)


guion.append(debuxo)
guion.append(debuxo2)
guion.append(debuxo3)
guion.append(debuxo4)

folla = Drawing (A4[0],A4[1])

for elemento in guion:
    folla.add(elemento)

renderPDF.drawToFile(folla,"exemploConDrawing.pdf")