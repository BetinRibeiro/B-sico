from pixqrcode import PixQrCode
import base64

#link para consultar a biblioteca precisa ser instalada com pip
#https://pypi.org/project/pixqrcode/ 

nome ="NomePessoa"
chave = "numeroFone"
cidade = "Juazeiro do norte CE"
#valor abaixo refere-se a 1 real
valor = "100"
codigo = "45123678945126"

#valor quando não passado fica a disposição do usuario
#codigo é campo opcional
def criar_pagamento(nome, chave, cidade, valor=None, codigo=None):
        pix = PixQrCode(nome, chave, cidade, valor, codigo)
        #salva o pix, na pasta qrs e com o codigo gerado pelo generate_code()
        pix.save_qrcode("qrs",pix.generate_code())
        return pix.export_base64()

def salvar_imagem(descricao, link_imagem):
    data = link_imagem.replace('data:image/png;base64,', '')
    imgdata = base64.b64decode(data)
    with open(f'{descricao}.jpg', 'wb') as imagem:
        try:
            imagem.write(imgdata)
        except:
            return "ERRO"
        
    return ("Salvo com sucesso, status!")

link_imagem = criar_pagamento(nome, chave, cidade, valor, codigo)

#não precisa dessa função, existe uma função na propria biblioteca para salvar !!
#verificar criar_pagamento
#salvar_imagem("nome_do_arquivo", link_imagem)

#link para verificar o registro na blockchain publica
# https://openpix.com.br/qrcode/scanner/
