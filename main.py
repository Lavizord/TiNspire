from exercicios import *

# TODO: Ver com o Paulo se todos os valor que são fornecidos no exemplo
#       da aula 10_10_2021, são valores dados em exame / teste, ou se
#       será pedido para ele obter esses valores.

# TODO: Ver se a estrutura de menus faz sentido para ele.
#       Pensar na forma como vai interagir com o exame e a calculadora.


'''
    REGISTO DE TEMPO
    
** (Aula 11_10_2021)    - Total: 170mins

    - 10/04/2022        - Total Dia: 110mins
        18:10 - 18:30
        18:45 - 19:05
        19:20 - 21:00
        22:10 - 22:30
        Notas: Tempo gasto a criar as formulas iniciais e e a organizar o ficheiro de calcula.

    - 11/04/2022        - Total Dia: 30mins
        23:00 - 23:30
        Notas: Implementação de novas formulas, pequeno sistema de menu inicial
    
    - 12/04/2022        - Total Dia: 30mins
        14:00 - 14:30
        
    - 13/04/2022        - Total Dia: 2h 40 mins
        Notas: Não contabilizado para o total. Tempo gasto a:
                - Estruturar o código para os próximos exercicios.
                - Expandir o sistema de menus
                - Debug
                - Compliação de informação que vou necessitar.
    
    - dd/mm/yyyy        - Total Dia: xmins
    
'''

menu_options = {
    1: 'Exercícios - Materia Aula = 10_10_2021',
    2: 'Exercícios - Materia Aula = dd_mm_202a',
    3: 'Exercícios - Materia Aula = dd_mm_202a',
    4: 'Sair',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )


def do_option(option):
    if option == 1:
        ex = Normal2015_10_11_10_2021()
        # ex.initVars()
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        print('Saindo...')
        exit()
    else:
        print('Opção inválida. Insira um número entre 1 e 4.')


def main():
    
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Insira a escolha: '))
        except:
            print('Input errado. Por favor insira um número ...')
        #Check what choice was entered and act accordingly
        do_option(option)
        

if __name__ == "__main__":
    main()
























































































































































































































































