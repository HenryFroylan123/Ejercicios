import re #libreria de expresiones regulares

filename = "ExpresionesRegulares.txt"

try:
  #lectura del archivo, pasandolo a una variable
  archivo = open(filename, 'r')
except:
  print ('El archivo que intentas abrir no existe')
  quit()

texto = ''

#lectura de lineas del archivo para ser pasados a una variable vacia.
for linea in archivo:
  texto += linea

#EJERCICIO 1:
print("----------------Ejercicio 1-Variables válidas----------------\n")
regex = r"(\b[A-Za-z0-9-_]+\s*[=])+"
resultado = re.findall(regex, texto)
print("Las variables que estan en el archivo son: ", resultado,"\n")

#EJERCICIO 2
print("----------------Ejercicio 2- Enteros y decimales---------------\n")
regex = r"([\d]+[.]?[\d])"
resultado = re.findall(regex, texto)  # busca las coincidencias y devuelve un arreglo
print("Los enteros y decimales encontrados en el archivo son: ", resultado,"\n")

#EJERCICIO 3
print("----------------Ejercicio 3- Operadores aritmeticos-------------\n")
regex = r"([+-]|[\/]|[*]|[%])"
resultado = re.findall(regex, texto)  # busca las coincidencias y devuelve un arreglo
print("Los operadores aritmeticos encontrados en el archivo son: ", resultado,"\n")

#EJERCICIO 4
print("-----------------Ejercicio 4- Operadores relacionales------------\n")
regex = r"<|<=|>=|=|==|!="
resultado = re.findall(regex, texto)  # busca las coincidencias y devuelve un arreglo
print("Los operadores relacionales encontrados en el archivo son: ", resultado,"\n")

#EJERCICIO 5
print("-----------------Ejercicio 5-Palabras reservadas------------------\n")
regex = r"\bint|\babstract|\bassert|\bboolean|\bbreak|\bbyte|\bcase|\bcatch|\bchar|\bclass|\bconst|\bcontinue|\bdefault|\bdo|\bdouble|\belse|\benum|\bextends|\bfinal|\bfinally|\bfloat|\bfor|\bgoto|\bif|\bimplements|\bimport|\binstanceof|\binterface|\blong|\bnative|\bnew|\bpackage|\bprivate|\bprotected|\bpublic|\breturn|\bshort|\bstatic|\bstrictfp|\bsuper|\bswitch|\bsynchronized|\bthis|\bthrow|\bthrows|\btransient|\btry|\bvoid|\bvolatile|\bwhile"
resultado = re.findall(regex, texto)  # busca las coincidencias y devuelve un arreglo
print("Las palabras reservadas encontradas en el archivo son: ", resultado,"\n")
