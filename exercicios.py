import vars
import calcula

class Normal2015_10_11_10_2021:
    variaveis = {}

    def __init__(self):
        print("\n==>Inicio de folha de cálculo com base na aula de 11_10_2021") 
        self.variaveis = {
            "by" : vars.pede("By", "By", "m" ),
            "nc1": vars.pede("Nc1", "Nc1", "kN" ),
            "mc1": vars.pede("Mc1", "Mc1", "kN m" ),
            "nc2": vars.pede("Nc2", "Nc2", "kN" ),
            "mc2": vars.pede("Mc2", "Mc2", "kN m" ),
            "hz": vars.pede("Hz", "Hz", "m" ),
            "fmk": vars.pede("fmk", "fmk", "MPa" ),
            "ftk": vars.pede("ftk", "ftk", "MPa" ),
            "fck": vars.pede("fck", "fck", "MPa" ),
            "fvk": vars.pede("fvk", "fvk", "MPa" )                
        }                     
        self.variaveis['wy'] = calcula.wy(self.variaveis['hz']['valor'], self.variaveis['by']['valor'])
        self.variaveis['wz'] =  calcula.wz(self.variaveis['hz']['valor'], self.variaveis['by']['valor']) 
        self.variaveis['a'] = calcula.secao_pilar(self.variaveis['by']['valor'], self.variaveis['hz']['valor'])
        
        # Criação das Opções de Menu para esta class.
        # Cada Opção vai ser uma variável com opção para obter a formula desse valor.
        # TODO: Na implementação final adicionar uma 'desc' ao Dict das Variáveis
        #       Realizar a impressao dessa desc aqui no menu
        # -------------------------------------------------------------------------------------------
        # TODO: Na implementação final adicionar uma 'formula' ao Dict das Variáveis
        #       Será uma string, que será o resultado do print() que já existe a fazer o cálculo
        
        menu_options = {}
        key = 1
        for var in self.variaveis:
            ## print(var)
            ## menu_options[key] = "Formula de: " + self.variaveis[var]['nome'] + ' =>  ' + str(self.variaveis[var]['valor']) + ' ' + self.variaveis[var]['unidade']
            ## TODO: protótipo para ter o menu com base nas vares.
            ##       - Talvez possa simplificar o dicionário principal variaveis[]
            ##       - Talvez seja melhor implementar um sistema de navegacao. Para não ter tantas opcoes no menu?
            for opcao in self.variaveis[var]['opcoes']:
                menu_options[key] = self.variaveis[var]['opcoes'][opcao]
                key += 1
                
        menu_options[99] = ' -Sair'
        self.menu(menu_options)
    
    # Imprime a Key e o valor do menu de opcoes 
    def print_menu(self, menu_options):
        linha = 1
        for key in menu_options.keys():
            if linha < 10:
                print(key, '--', menu_options[key] )
            else:
                print(key, '-', menu_options[key] )
            linha += 1
            
    # Este sistema de menu vai ser replicado para as outras classes.
    # Basta copiar a função e adicionar novas opções   
    # TODO: Nesta função posso tentar replicar o que fiz no menu_option, caso contrário sempre que adicionar uma variável,
    #       Vou ter que adicionar outra opção manualmente ao menu. Pensar num sistema que me diga que opção existe para cada var         
    def do_option(self, option):
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 99:
            print('Saindo...')
            exit()
        else:
            print('Opção inválida. Insira um número entre 1 e 4.')

    
    def menu(self, menu_options):       
        while(True):
            self.print_menu(menu_options)
            option = ''
            try:
                option = int(input('Insira a escolha: '))
            except:
                print('Input errado. Por favor insira um número ...')
            #Check what choice was entered and act accordingly
            self.do_option(option)
        
