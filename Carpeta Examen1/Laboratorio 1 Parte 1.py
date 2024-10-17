from collections import Counter

# Función para mostrar el mensaje con las sustituciones aplicadas
def aplicar_sustituciones(mensaje, sustituciones):
    mensaje_sustituido = mensaje
    for letra_cifrada, letra_clara in sustituciones.items():
        mensaje_sustituido = mensaje_sustituido.replace(letra_cifrada, letra_clara)
    return mensaje_sustituido

# Función para mostrar las letras más frecuentes en el mensaje cifrado
def mostrar_frecuencia_letras(mensaje):
    mensaje_limpio = mensaje.replace(" ", "").replace("\n", "").replace(",", "").replace(".", "").replace("-", "")
    frecuencia = Counter(mensaje_limpio.upper())  # Convertimos todo a mayúsculas para un conteo uniforme
    print("\nFrecuencia de letras en el mensaje cifrado:")
    for letra, cantidad in frecuencia.most_common():
        print(f"{letra}: {cantidad}")

# Mensaje cifrado
mensaje = """
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE.
"""

# Mostrar las letras más frecuentes en el mensaje cifrado
mostrar_frecuencia_letras(mensaje)

# Diccionario de sustituciones
sustituciones = {}

# Ciclo para realizar sustituciones
while True:
    # Mostrar el mensaje actual con las sustituciones aplicadas
    print("\nMensaje actual:")
    print(aplicar_sustituciones(mensaje, sustituciones))
    
    # Preguntar al usuario si quiere realizar una sustitución
    respuesta = input("\n¿Quieres realizar una sustitución? (s/n): ").lower()
    if respuesta != 's':
        break
      
  # Pedir la letra cifrada y la letra clara
    letra_cifrada = input("Introduce la letra cifrada que quieres sustituir: ").upper()
    letra_clara = input("Introduce la letra por la que la quieres sustituir: ").lower()
    
    # Realizar la sustitución
    sustituciones[letra_cifrada] = letra_clara

# Mostrar el mensaje final con todas las sustituciones aplicadas
print("\nMensaje final con las sustituciones:")
print(aplicar_sustituciones(mensaje, sustituciones))
