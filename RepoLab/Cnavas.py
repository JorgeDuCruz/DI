from reportlab.pdfgen import canvas

texto = ('Este texto é para exemplo','da utilización de canvas','para usar con texto',
         'Alongo o texto','para ter mais', 'espazo')

obxCanvas = canvas.Canvas("textoCanvas.pdf")

obxTexto = obxCanvas.beginText()
obxTexto.setTextOrigin(100,300)
obxTexto.setFont("Courier",16)

for linha in texto:
    obxTexto.textLine(linha)

obxTexto.setFillGray(0.5)
textoLongo = """Outro texto con varias
                liñas incoroporadas,
                con retornos de carro
                incluidos."""

obxTexto.textLines(textoLongo)

obxTexto.setTextOrigin(20,800)
for tipo_letra in obxCanvas.getAvailableFonts():
    obxTexto.setFont(tipo_letra,16)
    obxTexto.textLine("Texto de exemplo coa fonte: "+tipo_letra)

obxTexto.setFont("Helvetica",16)
obxTexto.setFillColorRGB(0.2,0,0.6)
obxTexto.setFillColor("Pink",1)
for linha in texto:
    obxTexto.moveCursor(20, 15)
    obxTexto.textOut(linha)
obxTexto.moveCursor(-120,15)
espazoCaracteres = 0
for linha in  texto:
        obxTexto.setCharSpace(espazoCaracteres)
        obxTexto.textLine("Espazo %s: %s" %(espazoCaracteres,linha))
        espazoCaracteres +=1

obxTexto.setTextOrigin(20,100)
obxTexto.setCharSpace(1)
obxTexto.setWordSpace(8)
obxTexto.textLines(textoLongo)

obxCanvas.drawText(obxTexto)
obxCanvas.showPage()
obxCanvas.save()