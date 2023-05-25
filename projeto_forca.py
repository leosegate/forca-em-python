import random

def limpa():
     print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']


lista_palavras = {
     'teste': ['hello'],
     'animais':{
          'facil':['abelha','cachorro','cavalo','coruja'],
          'medio':['bufalo','camelo','castor','crocodilo'],
          'dificil':['bisonte','biablotim','dromedario','esturjao']
     },
     'frutas':{
          'facil':['mamao','uva','maça','limao','goiaba'],
          'medio':['lixia','carambola','cereja','melancia'],
          'dificil':['roma','pitaya','tamarindo','jabuticaba']
     },
     'paises':{
          'facil':['russia','alemanha','brasil','espanha'],
          'medio':['italia','Grecia','Franca','dinamarca'],
          'dificil':['turcomenitao','cazaquistao','tunisia','finlandia']
     },
     'profissoes':{
          'facil':['animador','chef','ator','advogado'],
          'medio':['programador','administrador','fotografo','professor'],
          'dificil':['biotecnologo','geofisico','zootecnologo','arquivologista']
     }
}

limpa()
print('Bem vindo(a) ao jogo da forca!')
jogar = input("Desejar jogar? (sim/nao): ").lower()

while(jogar=='sim'): 

     limpa()
     print('Opcoes: animais, frutas, paises e profissoes')
     opcao = input("Qual voce deseja?: ").lower()

     if opcao in lista_palavras:
          dificuldade = input('Selecione o grau de dificuldade: facil, medio ou dificil: ')
          escolha_computador = random.choice(lista_palavras[opcao][dificuldade])
          resposta = len(escolha_computador)*'_'
          i=0
          while(i<len(des_forca)):
               letra = input("Digite a letra: ").lower()
               if letra in escolha_computador:
                    pos=0
                    while(pos<len(escolha_computador)):
                         if(letra==escolha_computador[pos]):
                              print('Voce achou uma letra!')
                              print(des_forca[i])
                              resposta = list(resposta)
                              resposta[pos] = letra
                              print(''.join(resposta))
                              pos+=1
                         else:
                              pos+=1
                         if('_' not in resposta):
                              limpa()
                              print(f'Parabens voce ganhou! Total de erros: {i}')
                              print(f'A palavra era: {escolha_computador}')
                              i=1000
                              break
               else:
                    i+=1
                    limpa()
                    print(f"Nao tem '{letra}'.")
                    print(f"Tentativas restantes: {(len(des_forca)-1)-i}")
                    print(des_forca[i])
                    print(''.join(resposta))
                    if((len(des_forca)-1)-i == 0):
                         print('Voce nao conseguiu!!')
                         print(f'A palavra era: {escolha_computador}')
                         i=1000
                         break

     else:
          print("Nao existe essa opcao.")
     jogar = input('Deseja jogar denovo? (sim/nao): ')