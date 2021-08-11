from time import sleep
print('')
print('-' *70)
print(' '*25 +'Tabela Periódica')
print('-' *70)
print('')
print('H                                                                   He')
print('Li  Be                                          B   C   N   O   F   Ne')
print('Na  Mg                                          Al  Si  P   S   Cl  Ar')
print('K   Ca  Sc  Ti  V   Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr')
print('Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I   Xe')
print('Cs  Ba  ~   Hf  Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn')
print('Fr  Ra  ¬   Rf  Db  Sg  Bh  Hs  Mt')
print('')

elementos = ["Hidrogênio", "Hélio", "Lítio", "Berílio", "Boro", "Carbono", "Nitrogênio", "Oxigênio", "Flúor", 
            "Neônio", "Sódio", "Magnésio", "Alumínio", "Silício", "Fósforo", "Enxofre", "Cloro", "Argônio",
            "Potássio", "Cálcio", "Escândio", "Titânio", "Vanádio", "Cromo", "Manganês", "Ferro", "Cobalto",
            "Níquel", "Cobre", "Zinco", "Gálio", "Germânio", "Arsênio", "Selênio", "Bromo", "Criptônio",
            "Rubídio", "Estrôncio", "ítrio", "Zircônio", "Nióbio", "Molibdênio", "Tecnécio", "Rutênio", 
            "Ródio", "Paládio", "Prata", "Cádmio", "índio", "Estanho", "Antimônio", "Telúrio", "Iodo", 
            "Xenônio", "Césio", "Bário", "Lantanídeos", "Háfnio", "Tântalo", "Tungstênio", "Rênio", "Ósmio",
            "Irídio", "Platina", "Ouro", "Mercúrio", "Tálio", "Chumbo", "Bismuto", "Polônio", "Ástato",
            "Radônio", "Frâncio", "Rádio", "Actinídeos", "Rutherfórdio", "Dúbnio", "Seabórgio", "Bóhrio", 
            "Hássio", "Meitnério", "Darmstádio", "Roentgênio", "Copérnico", "Nihônio", "Fleróvio", "Moscóvio",
            "Livermório", "Tenessino", "Oganessônio"]
siglas = ["h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar",
        "k", "ca", "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br",
        "kr", "rb", "sr", "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te",
        "i", "xe", "cs", "ba", "~", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg", "tl", "pb", "bi",
        "po", "at", "rn", "fr", "ra", "¬", "rf", "db", "sg", "bh", "hs", "mt"]

def finishlines():
    print('-=' *20)


j=0
i=0
while True:
    escolha = str(input('Escolha a sigla do elemento que você quer obter as informações: ')).strip().lower()
    if escolha == '~':
        print('Este espaço é destinado aos Lantanídeos, um grupo composto por 15 elementos')
        finishlines()
        sleep(3)
    elif escolha == '¬':
        print('Este espaço é destinado aos Actinídeos, um grupo composto por 15 elementos')
        finishlines()
        sleep(3)
    elif escolha in siglas:
        while escolha != siglas[j]:
            j += 1
            i += 1
        print(f'A sigla {siglas[j].capitalize()} representa o elemento {elementos[i]}.')
        finishlines()
        sleep(3)
        print('Deseja pesquisar mais algum elemento?')
        print('[1] Sim')
        print('[2] Não')
        resposta = int(input('Digite a opção desejada (1 ou 2): '))
        finishlines()
        i=0
        j=0
        while resposta < 1 or resposta > 2:
            print('Opção inválida.')
            resposta = int(input('Digite a opção desejada (1 ou 2): '))
            finishlines()
        if resposta == 2:
            print('Fim do programa')
            break
    else:
        print('Insira uma sigla válida, de acordo com a tabela periódica apresentada.')
        finishlines()
        sleep(2)