import ctypes

pasta = input("Pasta a ser ocultada: ")
atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")

else:
    print("Arquivo nao foi ocultado")