
lista_nomes = ["ABEL ANTONIO DA SILVA",
"ABEL ANTONIO DA SILVA",
"ABEL ANTONIO DA SILVA",
"ABEL ANTONIO DA SILVA",
"ABRAO SANTANA RODRIGUES",
"ABRAO SANTANA RODRIGUES",
"ABRAO SANTANA RODRIGUES",
"ABRAO SANTANA RODRIGUES",
"ADAIR GOMES MEDEIROS",
"ADAIR GOMES MEDEIROS",
"ADAIR GOMES MEDEIROS",
"ADAIR GOMES MEDEIROS",
"ADAO NUNES DE ARAUJO",
"ADAO NUNES DE ARAUJO",
"ADAO NUNES DE ARAUJO",
"ADAO NUNES DE ARAUJO",
"ADELINA VIEIRA DOS SANTOS",
"ADELINA VIEIRA DOS SANTOS",
"ADELINA VIEIRA DOS SANTOS",
"ADELINA VIEIRA DOS SANTOS",
"ADELSON JOSE DE MORAIS",
"ADELSON JOSE DE MORAIS",
"ADEMAR PEREIRA DOS SANTOS",
"ADEMAR PEREIRA DOS SANTOS",
"ADEMAR PEREIRA DOS SANTOS",
"ADEMAR PEREIRA DOS SANTOS",
"ADEMAR PEREIRA DUARTE",
"ADEMAR PEREIRA DUARTE",
"ADEMAR PEREIRA DUARTE",
"ADEMAR PEREIRA DUARTE",
"ADEMIL RODRIGUES DE AMORIM",
"ADEMIL RODRIGUES DE AMORIM",
"ADEMIL RODRIGUES DE AMORIM",
"ADEMIL RODRIGUES DE AMORIM",
"ADEMILTON CORRESMA",
"ADEMILTON CORRESMA",
"ADEMILTON CORRESMA",
"ADEMILTON CORRESMA"]

#retira o nome so nome comleto retornando so o sobrenome
def retirar_primeiro_nome(lista):
    #cria uma nova lista para retorno
    lista_nova = []
    #percorre a lista principla
    for item in lista:
        # pega o item e separa para pegar o primeiro elemento
        item_separado = item.split()
        #o primeiro elemento na posição 0 é o nome 
        primeiro_elemento_do_item = item_separado[0]
        #verifica o tamanho do nome e joga numa variavel atravez da função len()
        tamanho_do_primeiro_elemento_do_item = len(primeiro_elemento_do_item)
        #pega o retante do item fazendo uma partição na string
        #apartir do tamanho do primeiro item + 1 até o final
        restante_dos_elementos = item[tamanho_do_primeiro_elemento_do_item+1:]
        #adiciona o restante na lista de retorno
        lista_nova.append(restante_dos_elementos)
    return lista_nova

#remove itens repetidos
def remover_itens_repetidos(lista):
    #cria uma nova lista que será retornada    
    lista_nova = []
    #laço que percorre toda a lista 
    for item in lista:
        #adiciona o item da lista na nova lista 
        lista_nova.append(item)
        #laço que repete enquanto esse item existir na linha principal
        while item in lista:
            #remove o item na lista enquanto tiver no laço
            #fazendo com que a lista principal não tenha mais esse item 
            lista.remove(item)
    #retorna a lista nova 
    return lista_nova

#retira o nome da lista de nomes completos 
lista_sobrenome = retirar_primeiro_nome(lista_nomes)
#remove os itens repetidos na lista gerada anteriormente
lista_sobrenomes_sem_repetir = remover_itens_repetidos(lista_sobrenome)
#faz impressão da lista sem repetição
print(lista_sobrenomes_sem_repetir)
