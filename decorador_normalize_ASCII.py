from unicodedata import normalize

def normaliza(*palavras):
    def ajudante(palavra):
        normalizado = normalize('NFKD', palavra)
        return normalizado.encode('ASCII', 'ignore').decode('ASCII')
    return [ajudante(palavra) for palavra in palavras]
