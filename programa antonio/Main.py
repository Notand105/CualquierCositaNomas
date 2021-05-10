import pyautogui
import PyPDF2
from os import remove

#Abrir el archivos pdf, texto para escribir y texto para leer
PdfFile=open("Check.pdf","rb")
txtFile=open("archivodeTexto.txt","w")
#Leer el pdf en la variable pdfreader
pdfReader= PyPDF2.PdfFileReader(PdfFile)
#imprimir numero de paginas
#print(pdfReader.numPages)
i=0
text=""
#codigo para dejar en text toda la informacion de los pdf
while i<pdfReader.numPages:  
    pageObj = pdfReader.getPage(i)
    text=text+pageObj.extractText()
    i=i+1 
#agregar al archivo de texto todo el string text
txtFile.write(text)
txtFile.close()
#abrimos otra vez el archivo pero esta vez como lectura
textFile2=open("archivodeTexto.txt","r")
lista=textFile2.readlines()
i=0
lista2=[]
while i<len(lista):
    cadena="Libre"
    if(cadena in lista[i] and cadena in lista[i+1] and cadena in lista[i+2]):
        cadena2=""+lista[i-4]+lista[i-3]+"Esta libre\n\n"
        lista2.append(cadena2)
        #pyautogui.alert(cadena2,"Programa","Aceptar")       
    i=i+1
textFile2.close()
textFile3=open("Resultado.txt","w")
showText=""
i=0
while i<len(lista2):   
    showText=showText+lista2[i]
    i=i+1

textFile3.write(showText)

pyautogui.alert("Listo por favor revisa el txt resultado","Programa","Aceptar")
remove("archivodeTexto.txt")
textFile3.close()
PdfFile.close()