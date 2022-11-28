from random import randint

lista1=["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z"] 
lista2=["a" ,"b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z"]
lista3=["0" ,"1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]
lista4 =["!" ,"@" ,"#" ,"$" ,"%"]
lista_geral = [lista1,lista2,lista3,lista4]

#gerador de senhas seguras tamanho>6 e <20
def gerar_senha(tamanho=8):
    if tamanho<6:
        tamanho=6
    elif tamanho>20:
        tamanho=20
    senha="" 
    tamanhoi=tamanho   
    while tamanho>0: 
        lista = lista_geral[randint(0,len(lista_geral)-1)]
        senha +=str(lista[randint(0,len(lista)-1)])
        tamanho-=1     

    if not senha_segura(senha):
        senha = gerar_senha(tamanhoi)     
    return(senha)

def senha_segura(senha):
    if not senha.isalnum():
        if senha.upper():
            if senha.lower():
                return(True)
    return(False)

for i in range(10):
    print(gerar_senha())
