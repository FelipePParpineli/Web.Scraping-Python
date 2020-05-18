# importar bibliotecas
import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from colorama import init, Fore, Back

# 2 inserir init() para que o colocarama funcione no windows
init(autoreset = True)

# 3 definir número de jogos
def num_jogos():
    global número_de_jogos
    número_de_jogos = int(input('Quantos jogos você gostaria de cadastrar? '))

# 4 definir os jogos
def jogos():
    jogo = list()
    global jogos_num
    jogos_num = list()
    posição = 1
    número = 1
    for c in range(1, número_de_jogos+1):
        for números in range(1, 16):
            jogo.append(int(input(f'Qual o {posição}º número do {número}º jogo: ')))
            posição += 1
        print(f'{"----------":>70}')
        jogos_num.append(jogo[:])
        jogo.clear()
        número += 1
        posição = 1
    return jogos_num

# 5 criar função para mostrar os jogos
def mostra_jogos():
    for pos, números in enumerate(jogos_num):
        time.sleep(0.3)
        print(f'jogo {pos+1}: {números}')

# 6 criar funções para as opções do Menu
def opção1():
    num_jogos()
    jogos()
    print(f'Total de {len(jogos_num)} jogos cadastrados')
    print('--'*35)
    print('Jogos cadastrados com sucesso.')
    print('No menu, vá para a opção desejada.')
    print('--'*35)

def opção1_menu():
    números_novos = int(input('Quantos jogos a mais você gostaria de cadastrar? '))
    jogo = list()
    número = 1
    posição = 1
    for c in range(1, números_novos+1):
        for números in range(1, 16):
            jogo.append(int(input(f'Qual o {posição}º número do {número}º novo jogo: ')))
            posição += 1
        print(f'{"----------":>70}')
        jogos_num.append(jogo[:])
        jogo.clear()
        número += 1
        posição = 1
    return jogos_num

def opção2():
    print('--'*35)
    print(f'{"JOGOS CADASTRADOS":^70}')
    print('--'*35)
    if len(jogos_num) > 0:
        mostra_jogos()
        print('--'*35)
    else:
        print(f'Você não possui jogos cadastrados.\nPor favor, volte ao menu anterior e selecione a opção 1.')

def opção3():
    pergunta_jogos = str(input('Gostaria que seus jogos fossem mostrados novamente? S/N  ')).upper()
    print(f'{"----------":>70}')
    if pergunta_jogos == 'S':
        mostra_jogos()
        print(f'{"----------":>70}')
    pergunta_num = int(input('Qual jogo você gostaria de alterar?  '))
    print('--'*35)
    if pergunta_num == 0 or pergunta_num > len(jogos_num):
        time.sleep(0.3)
        print('Opção inválida, por favor refaça.')
        print(f'{"----------":>70}')
        print(f'   O jogo {pergunta_num} não existe.')
        print('   Volte ao menu anterior.')
    else:
        jogos_num.pop(pergunta_num-1)
        substituir_jogo = list()
        for c in range(1, 16):
            substituir_jogo.append(int(input(f'Qual o {c}º número do novo {pergunta_num}º jogo: ')))
        jogos_num.insert(pergunta_num-1, substituir_jogo[:])
        substituir_jogo.clear()
        print(f'jogo {pergunta_num} alterado com sucesso.')

def opção4():
    time.sleep(0.3)
    pergunta_jogos = str(input('Gostaria que seus jogos fossem mostrados novamente? S/N  ')).upper()
    print(f'{"----------":>70}')
    time.sleep(0.3)
    if pergunta_jogos == 'S':
        mostra_jogos()
        print(f'{"----------":>70}')
    pergunta = int(input('Qual jogo você gostaria de excluir?  '))
    print(f'{"----------":>70}')
    if pergunta == 0 or pergunta > len(jogos_num):
        time.sleep(0.3)
        print('Opção inválida, por favor refaça.')
        print(f'{"----------":>70}')
        print(f'  * O jogo {pergunta} não existe.')
        print('  * Volte ao menu anteior')
    else:
        jogos_num.pop(pergunta-1)
        time.sleep(0.3)
        print(f'jogo {pergunta} excluído com sucesso.')
        print(f'{"----------":>70}')
        time.sleep(0.3)
        print('   Seus jogos receberam uma nova numeração.')
        time.sleep(0.3)
        print('   Selecione a OPÇÃO 2 para nova visualização.')

def opção5():
    url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/'

    option = Options()
    option.headless = True
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(15)

    def concurso():
        try:
            element = driver.find_element_by_xpath("//div[@class='title-bar clearfix']//h2//span")
            html_content = element.get_attribute('outerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.get_text().split()
        except:
            return 'Tente mais tarde'

    print(f' {concurso()[0]}  {concurso()[1]}  {concurso()[2]}')


    def números_sorteio():
        try:
            element2 = driver.find_element_by_xpath("//table[@class='simple-table lotofacil']//tbody")
            html_content2 = element2.get_attribute('outerHTML')
            soup2 = BeautifulSoup(html_content2, 'html.parser')
            números = soup2.get_text().split()
            num = list()
            índice = 0
            # for c in range(0,3): # Forma maior
            #     for pos, núm in enumerate(números[índice]):
            #         num.append(núm)
            #     índice += 1
            for c in range(0, 3):
                [num.append(núm) for pos, núm in enumerate(números[índice])] # Forma contraída
                índice += 1
            soma = 0
            posi = 0
            posiç = 1
            resultado = list()
            for c in range(0, 15):
                resultado.append(num[posi] + num[posiç])
                soma += 1
                posi += 2
                posiç += 2
            resultado_inteiros = [int(num) for num in resultado]
            return resultado_inteiros
        except:
            return 'Tente mais tarde'

    print(f' Num sorteados: {números_sorteio()}')

    def acertos():
        global acertos_jogos
        acertos_jogos = list()
        for números in jogos_num:
            acertos_jogos.append(list(set(números)&set(números_sorteio())))
        return acertos_jogos
    acertos()
    print(f'{"-----------":>70}')

    def mostra_jogos():
        for pos, números in enumerate(acertos_jogos):
            print(Fore.GREEN + f' jogo {pos+1}:  ACERTOS  {números}  TOTAL = {len(números)}')
            
    mostra_jogos()

    time.sleep(0.3)

    print('--'*35)
    print(f'{"Confira o seu bilhete no site oficial da Loteria !":^70}')
    print(f'{"O resultado pode conter erros, não é um programa oficial !":^70}')
    print(f'{"NÃO RASGUE O SEU BILHETE, CONFIRA ANTES NO SITE DA LOTERIA !":^70}')
    print(f'{"O USO DESTE PROGRAMA É DE SUA ÚNICA E EXCLUSIVA RESPONSABILIDADE !":^70}')
    print(f'{"ESTE PROGRAMA É APENAS PARA FINS ACADÊMICOS !":^70}')
    print('--'*35)
   

    driver.quit()

# 7 criar Menu de opções
def menu():
    print('--'*35)
    print(f'{"BEM VINDO AO VERIFICADOR DE JOGOS DE 15 NÚMEROS":^70}')
    print(f'{"O resultado pode conter erros, não é um programa oficial !":^70}')
    print(f'{"NÃO RASGUE O SEU BILHETE, CONFIRA ANTES NO SITE DA LOTERIA !":^70}')
    print(f'{"O USO DESTE PROGRAMA É DE SUA ÚNICA E EXCLUSIVA RESPONSABILIDADE !":^70}')
    print(f'{"ESTE PROGRAMA É APENAS PARA FINS ACADÊMICOS !":^70}')
    print('--'*35)
    print('--'*35)
    print((Back.WHITE + Fore.BLACK + f'{"Menu de Opções":^70}'))
    print('--'*35)
    time.sleep(0.3)
    print(Fore.BLUE + '''    1 - Cadastrar mais jogos
    2 - Mostrar jogos cadastrados
    3 - Alterar jogo cadastrado
    4 - Excluir jogo cadastrado
    5 - Executar Programa
    6 - Interromper programa''')
    print('--'*35)
    print('As opções não podem ser acessadas.')
    print('ANTES CADASTRE PELO MENOS UM JOGO.')
    print('--'*35)
    opção1()    
    resp = 'S'
    while resp == 'S':
        print('--'*35)
        print((Back.WHITE + Fore.BLACK + f'{"Menu de Opções":^70}'))
        print('--'*35)
        time.sleep(0.3)
        print('''    1 - Cadastrar mais jogos
    2 - Mostrar jogos cadastrados
    3 - Alterar jogo cadastrado
    4 - Excluir jogo cadastrado
    5 - Executar Programa
    6 - Interromper programa''')
        print('--'*35)
        time.sleep(0.3)
        print('--'*35)
        time.sleep(0.3)
        opção = int(input('    Qual a opção desejada:  '))
        print('--'*35)
        while opção < 1 or opção > 8:
            print('Desculpe a opção digitada não é válida, por favor, refaça.')
            resp = str(input('Deseja continuar? S/N  ')).upper()
            if resp != 'S':
                print(f'Programa finalizado, volte sempre.')
                break
            if resp == 'S':
                time.sleep(0.3)
                print('--'*35)
                print((f'{"Menu de Opções":^70}'))
                print('--'*35)
                print('''
    1 - Cadastrar mais jogos
    2 - Mostrar jogos cadastrados
    3 - Alterar jogo cadastrado
    4 - Excluir jogo cadastrado
    5 - Executar Programa
    6 - Interromper programa''')
            print('--'*35)
            opção = int(input('    Qual a opção desejada:  '))
            print('--'*35)
        
        if opção == 1:
            opção1_menu()
            print(f' Total de {len(jogos_num)} jogos cadastrados')
            
        if opção == 2:
            opção2()   
        
        if opção == 3:
            opção3()

        if opção == 4:
            opção4()   
            
        if opção == 5:
            if len(jogos_num) == 0:
                time.sleep(0.3)
                print(Back.WHITE + 'Você não pode executar o programa.')
                print(Fore.RED + '  * Ainda não foram cadastrados jogos.')
                print(Fore.RED + '  * Volte ao menu anterior')
            else:
                opção5()
        
        if opção == 6:
            print('--'*35)
            print(f'{"Obrigado, volte sempre !":^70} ')
            print(f'{"Programa encerrado com sucesso !":^70}')
            print(f'{"O resultado pode conter erros, não é um programa oficial !":^70}')
            print(f'{"NÃO RASGUE O SEU BILHETE, CONFIRA ANTES NO SITE DA LOTERIA !":^70}')
            print(f'{"O USO DESTE PROGRAMA É DE SUA ÚNICA E EXCLUSIVA RESPONSABILIDADE !":^70}')
            print(f'{"ESTE PROGRAMA É APENAS PARA FINS ACADÊMICOS !":^70}')
            print('--'*35)
            break
                         
menu()