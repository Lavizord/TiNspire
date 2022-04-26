from decimal import *

UNDEFINED = 'UNDEFINED'

# Retorna dicionário que representa uma variável.
# Returns Dict 
def pede(nome, sigla, unidade = UNDEFINED):
    opcoes = {"imprimir":"imprimido"}
    valor = Decimal(input(f'Insira valor [{sigla}] em [{unidade}]\t'))    
    return constroi(nome, sigla, valor, unidade)


def imprime(nome, valor, unidade):
    print(f'\tNome:{nome},\t Valor: {valor} {unidade} ')
    

def constroi(nome, sigla, valor, unidade = UNDEFINED, opcoes = {"imprimir": "Imprime valor e descrição da variável."}):
    var = {
        "nome": nome,
        "sigla": sigla,
        "valor": valor,
        "unidade": unidade,
        "opcoes": opcoes
    }
    return var