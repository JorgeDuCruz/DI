from reportlab.pdfgen import canvas

folla = canvas.Canvas("Primeiro_Documento.pdf")

folla.drawString(0,0,"Posición inicio (x,y) = (0,0)")
folla.drawString(50,833,"Posición (x,y) = (50,100)")
folla.drawString(150,20,"Posición (x,y) = (150,20)")

folla.drawImage("tic16x16.jpg",20,700)
folla.drawImage("equis23x23.jpg",20,716)

folla.showPage()
folla.save()