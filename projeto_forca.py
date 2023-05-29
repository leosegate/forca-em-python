import random

def limpa():
     print("\n"*20)

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
          limpa()
          escolha_computador = random.choice(lista_palavras[opcao][dificuldade])
          resposta = len(escolha_computador)*'_'
          resposta = list(resposta)
          tried_letters = []
          i = 0
          num_dicas = 0
          num_dicas_max = 0
          if(len(escolha_computador)<5):
               num_dicas_max = 1
          elif(len(escolha_computador)<7):
               num_dicas_max = 2
          elif(len(escolha_computador)>9):
               num_dicas_max = 3
          while(i<len(des_forca)):
               print(f"Letras ja usadas: {','.join(tried_letters)}")
               letra = input("Digite a letra: ").lower()
               while(letra in tried_letters):
                    limpa()
                    print(f"Letras ja usadas: {','.join(tried_letters)}")
                    letra = input(f'Voce ja tentou essa letra ("{letra}"), tente novamente: ').lower()
               if (letra in escolha_computador):
                    pos=0
                    while(pos<len(escolha_computador)):
                         if(letra==escolha_computador[pos]):
                              print('Voce achou uma letra!')
                              print(des_forca[i])
                              resposta[pos] = letra
                              print(''.join(resposta))
                              pos+=1
                         else:
                              pos+=1
                    tried_letters.append(letra)
               else:
                    i+=1
                    limpa()
                    tried_letters.append(letra)
                    print(f"Nao tem '{letra}'.")
                    print(f"Tentativas restantes: {(len(des_forca)-1)-i}")
                    print(des_forca[i])
                    print(''.join(resposta))
                    if((len(des_forca)-1)-i == 0):
                         print('Voce nao conseguiu!!')
                         print(f'A palavra era: {escolha_computador}')
                         i=1000
                         break
               
               if('_' not in resposta):
                    limpa()
                    print(f'Parabens voce ganhou! Total de erros: {i}')
                    print(f'A palavra era: {escolha_computador}')
                    break

               if(len(escolha_computador) > 4 and num_dicas < num_dicas_max):
                    print(f'Deseja usar a dica? numero de dicas restantes: {num_dicas_max - num_dicas}')
                    dica = input("(sim/nao): ")
                    limpa()
                    if(dica == 'sim'):
                              l = list(escolha_computador) 
                              index = random.randrange(len(l))
                              while(resposta[index]=='_'):
                                   if(resposta[index]=='_'):
                                        resposta[index] = l[index]
                                        print(''.join(resposta))
                                        num_dicas += 1
                                        break;
                                   else:
                                        index = random.randrange(len(l))
     else:
          print("Nao existe essa opcao.")
     jogar = input('Deseja jogar denovo? (sim/nao): ')
