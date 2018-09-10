import random

def jogar():    #Define a função do jogo

    print("********************************")
    print("Bem vindo ao jogo de adivinhacao")
    print("********************************")
                 #Boa prática de identação é deixar um espaço da var e o sinal!

    numero_secreto = random.randrange(1,101)  #Gera aleatoriamente um número de 1 à 100.
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")  #Exibe a pergunta
    print("(1) Fácil (2) Médio (3) Difícil")   #Exibe os níveis

    nivel = int(input("Defina o nível: "))  #O usuário insere um número de 1 a 3 escolhendo o nível de dificuldade
    if(nivel == 1):       #Define a qtd de tentativas por nível
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):   #contabiliza a rodada atual com a qdt de tentativas
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))   #exibe, através da interpolação de Strings, a rodada atual e a qtd de tentativas

        chute_str = input("Digite  um número entre 1 e 100: ")  #Declarando valor input(String) a variável
        print("Você digitou ", chute_str)   #Printa o txt and variable
        chute = int(chute_str)   #Converte de String para Int

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue    #Continua com a próxima rodada porque digitou número inválido

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        # compara de o numero é == ao chute printa acertou, se não, errou.
        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))   #Sempre dar um TAB ou 4x espaço nos PRINTS após IF
            break   #Sai do laço quando acerta o número
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto. ")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto. ")
            pontos_perdidos = abs(numero_secreto - chute) #abs deixa o valor absoluto #pontos perdidos da rodada
            pontos = pontos - pontos_perdidos   #subtraindo os pontos perdidos da pontuação total

        print("Fim do jogo! ")
if(__name__ == "__main__"):
    jogar()