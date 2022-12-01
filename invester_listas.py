lista_principal = [["Periodo","Entradas","Saidas"],
["jan","1000","1000"],
["fev","1203","1100"],
["mar","3245","2345"],
["abr","7433","5362"],
["mai","1293","1267"],
["jun","7832","7382"],
["jul","1832","2910"],
["ago","2189","3920"],
["set","2093","1902"],
["out","1256","1920"],
["nov","2309","1029"],
["dez","4378","4032"]]

quant_colunas = 1
a=0
lista_nova = []
#Função com alta complexidade => Cuidado na utilizaç
while a < quant_colunas:
    nova_lista_interna =[]
    for lista_interna in lista_principal:
        if len(lista_interna)>quant_colunas:
            quant_colunas=len(lista_interna)
        if len(lista_interna)>a:
            nova_lista_interna.append(lista_interna[a])
        else:
            nova_lista_interna.append("###")
    lista_nova.append(nova_lista_interna)
    a+=1


for row in (lista_nova):
    print(row)
