# Durante a construção desse código tive ajuda e ideias do Canal do Kenji
print('\nSeja Bem vindo ao jogo da forca')
print('====================================================')
print('\nPor-favor,peça ao adversário que vire o rosto')

palavra = []
palavra_a_descobrir = [] # Letra inserida pelo adversário
contador = 10

palavra = input('\nInsira palavra a ser descoberta: ') 
dica = input('\nDê uma dica ao adversário: ')

#Esse comando é para que percorra o vetor é substitua por "-" 
for i in range(0, len(palavra)):
    palavra_a_descobrir.append("-") 
while(contador != 0): 
    letra_descoberta = str(input('\nInsira uma letra: '))
    contador = contador-1 #Quantidade de jogadas que ainda resta.
    print("\nQuantidade de rodadas restante:{}".format(contador))
    for i in range(0, len(palavra)): # Se existir a letra na palavra informada,substituir '-'por a letra  
        if letra_descoberta == palavra[i]:
            palavra_a_descobrir[i] = letra_descoberta
            if "-" in palavra_a_descobrir:
                pass
            else:
                print("\nJogo Finalizado.")
                exit()
        else:
            pass
        print(palavra_a_descobrir[i])
        if contador == 0:
            print('\nJogo finalizado.')
            exit()

for j in range(0, len(palavra_a_descobrir)):
    palavra_a_descobrir[j] == '-'