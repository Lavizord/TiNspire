import math
import vars
from decimal import *

UNDEFINED = 'UNDEFINED'


#TODO: Implementar modo debug, em que imprime as formulas ou não


# Calculo do Wy com base no Aula 11_10_2021 
#   -Return de um dict  -Print da Formula
def wy(hz, by):
    result = (( hz * ( by ** 2)) / 6) 
    result = round(result, 4)
    print(f'FORMULA Wy: | ( hz * (by^2)) / 6 | => | ( {hz} x ({by}^2) ) / 6 = {result} |')
    opcoes = {
        "imprimir": "Imprime valor e descrição da variável.",
        "formula": "FORMULA HERE"
    }
    return vars.constroi("wy", "wy", result, "m3", opcoes)


def wy_BACKUP(hz, by):
    result = (( hz * ( by ** 2)) / 6) 
    result = round(result, 4)
    print(f'FORMULA Wy: | ( hz * (by^2)) / 6 | => | ( {hz} x ({by}^2) ) / 6 = {result} |')
        
    return {'nome': "wy", 'valor': result, 'unidade': "m3" }


# Calculo do Wz com base no Aula 11_10_2021
#   -Return de um dict  -Print da Formula 
def wz(hz, by):
    result = (by * ( hz ** 2) / 6)
    result = round(result, 4)
    print(f'FORMULA Wz: | ( hz * (by^2)) / 6 | => | ( {hz} x ({by}^2) ) / 6 = {result} |')
    opcoes = {
        "imprimir": "Imprime valor e descrição da variável.",
        "formula": "FORMULA HERE"
    }
    return vars.constroi("wz", "wz", result, "m3", opcoes)


def wz_BACKUP(hz, by):
    result = (by * ( hz ** 2) / 6)
    result = round(result, 4)
    print(f'FORMULA Wz: | ( hz * (by^2)) / 6 | => | ( {hz} x ({by}^2) ) / 6 = {result} |')
    
    nome = "wz"
    unidade = "m3"
    
    var = {
        "nome": nome,
        "valor": result,
        "unidade": unidade 
    }
    
    return var



# Calculo do fmod com base no Aula 11_10_2021
#   -Return de um dict  -Print da Formula 
def fmod(fmk, kmod, ym):
    result = fmk * (kmod/ym)
    result = round(result, 4)
    print(f'FORMULA Fmod: | fmk * (kmod/ym)  | => | {fmk} * ({kmod}/{ym}) = {result} |')
    
    variavel = {
        "nome": "wz",
        "valor": result,
        "unidade": "m3" 
    }
    
    return variavel


# Calculo do ftd com base no Aula 11_10_2021
#   -Return de um dict  -Print da Formula 
def ftd(ftk, kmod, ym):
    result = ftk * (kmod/ym)
    result = round(result, 4)
    print(f'FORMULA ftd: | ftk * (kmod/ym) | => | {ftk} * ({kmod}/{ym}) = {result} |')
    
    variavel = {
        "nome": "wz",
        "valor": result,
        "unidade": "m3" 
    }
    
    return variavel


# Calculo do fcd com base no Aula 11_10_2021
#   -Return de um dict  -Print da Formula 
def fcd(fck, kmod, ym):
    result = fck * (kmod/ym)
    result = round(result, 4)
    print(f'FORMULA fcd: | fck * (kmod/ym) | => | {fck} * ({kmod}/{ym}) = {result} |')
    
    variavel = {
        "nome": "wz",
        "valor": result,
        "unidade": "m3" 
    }
    
    return variavel


# Calculo do fvd com base no Aula 11_10_2021
#   -Return de um dict  -Print da Formula 
def fvd(fvk, kmod, ym):
    result = fvk * (kmod/ym)
    result = round(result, 4)
    print(f'FORMULA fvd: | fvk * (kmod/ym) | => | {fvk} * ({kmod}/{ym}) = {result} |')
    
    variavel = {
        "nome": "wz",
        "valor": result,
        "unidade": "m3" 
    }
    
    return variavel


# Calculo do A: Secção do pilar, com base no Aula 11_10_2021
#   -Return de um dict  -Print da Formula 
def secao_pilar(by, hz):
    result = by * hz
    result = round(result, 4)
    print(f'FORMULA secao_pilar: | by * hz | => | {by} * {hz} = {result} |')
    opcoes = {
        "imprimir": "Imprime valor e descrição da variável.",
        "formula": "FORMULA HERE"
    }
    return vars.constroi("Seção pilar", "??", result, "m3", opcoes)

def secao_pilar_BACKUP(by, hz):
    result = by * hz
    result = round(result, 4)
    print(f'FORMULA secao_pilar: | by * hz | => | {by} * {hz} = {result} |')
    
    nome = "wz"
    unidade = "m3"
    
    var = {
        "nome": nome,
        "valor": result,
        "unidade": unidade 
    }
    
    return var


# Conversão de um valor dado em GPa para KPa
#   -Return de um dict  -Print da Formula
def converteGpaKpa(valor, nome):
    result = valor * 1000000
    #result = round(result, 4)
    #print(f'FORMULA Wy: | ( hz * (by^2)) / 6 | => | ( {hz} x ({by}^2) ) / 6 = {result} |')
    
    variavel = {
        "nome": nome,
        "valor": result,
        "unidade": "Kpa" 
    }
    
    return variavel


# Cálculo da ELU_Verificação de segurança => C1
# -Return de um dict  -Print da Formula
def verificacaoC1(nc1, a, fcd, mc1, wy, fmd):
    result = ( ((nc1/a) * fcd) ** 2 ) + (mc1/wy) / fmd 
    result = round(result, 4)
    print(f'FORMULA Verificação - C1: | ( ((nc1/a) * fcd) ** 2 ) + (mc1/wy) / fmd | => ( (({nc1}/{a}) * {fcd}) ** 2 ) + ({mc1}/{wy}) / {fmd} |  = {result} |')
    
    variavel = {
        "nome": "C1",
        "valor": result,
        "unidade": UNDEFINED 
    }

    return variavel


# Cálculo da ELU_Verificação de segurança => C2
# -Return de um dict  -Print da Formula
def verificacaoC2(nc2, a, ftd, mc2, wy, fmd):
    result = ( ((nc2/a) * ftd) ** 2 ) + (mc2/wy) / fmd 
    result = round(result, 4) 
    print(f'FORMULA Verificação - C2: | ( ((nc2/a) * fcd) ** 2 ) + (mc2/wy) / fmd | => ( (({nc2}/{a}) * {fcd}) ** 2 ) + ({mc2}/{wy}) / {fmd} |  = {result} |')
    
    variavel = {
        "nome": "C2",
        "valor": result,
        "unidade": UNDEFINED 
    }

    return variavel


# Cálculo 
# -Return de um dict  -Print da Formula
def iy(h, b):
    result = (h * (b ** 3)) / 12
    result = round(result, 4) 
    print(f'FORMULA Iy: (h * (b ** 3)) / 12 | => | ({h} * ({b} ** 3)) / 12 |  = {result} |')
    
    variavel = {
        "nome": "Iy",
        "valor": result,
        "unidade": "m4" 
    }

    return variavel


# Cálculo 
# -Return de um dict  -Print da Formula
def iy(h, b):
    result = (b * (h ** 3)) / 12
    result = round(result, 4) 
    print(f'FORMULA Iy: (b * (h ** 3)) / 12 | => | ({b} * ({h} ** 3)) / 12 |  = {result} |')
    
    variavel = {
        "nome": "Iz",
        "valor": result,
        "unidade": "m4" 
    }

    return variavel


# Cálculo 
# -Return de um dict  -Print da Formula
def lambda_y(le, y, iy, a):
    result = le*y / math.sqrt(iy/a)
    result = round(result, 2)
    print(f'FORMULA λy: | le*y / \u221A(iy/a) | => | {le}*{y} / \u221A({iy}/{a}) |  = {result} |')

    variavel = {
        "nome": "λy",
        "valor": result,
        "unidade": UNDEFINED 
    }

    return variavel


# Cálculo 
# -Return de um dict  -Print da Formula
def lambda_Z(le, Z, iz, a):
    result = le*Z / math.sqrt(iz/a)
    result = round(result, 2)
    print(f'FORMULA λz: |  le*y / \u221A(iy/a) | => | {le}*{Z} / \u221A({iz}/{a}) |  = {result} |')

    variavel = {
        "nome": "λz",
        "valor": result,
        "unidade": UNDEFINED 
    }

    return variavel


# Cálculo 
# -Return de um dict  -Print da Formula
def lambda_rely(lambda_y, fck, e5):
    result = lambda_y / math.pi * math.sqrt(fck/e5) 
    result = round(result, 4)
    print(f'FORMULA λz: |  ( λy / \u03C0 ) *  \u221A(fck/e5%) | => | ( {lambda_y} / \u03C0 ) *  \u221A({fck}/{e5}) |  = {result} |')
    variavel = {
        "nome": "λrel.y",
        "valor": result,
        "unidade": UNDEFINED 
    }
    
    pass