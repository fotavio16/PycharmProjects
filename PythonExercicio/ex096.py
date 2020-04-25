# Rotina que mostra a área de um terreno
def área(largura, comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento}m2.')
    return

print(" Controle de Terrenos")
print("-"*30)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
área(l,c)

