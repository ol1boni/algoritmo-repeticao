# menu simples
opcao = 9
print ('Menu Musical :)')
while opcao != 0:
    print("1 - Artistas mais ouvidos | 2 - Acessar sua biblioteca de playlists | 0 - Sair")
    opcao = int(input("Escolha qual você deseja acessar: "))
    if opcao == 1:
        print("Acessando artistas mais ouvidos...")
    elif opcao == 2:
        print("Acessando sua biblioteca de playlists..." \
        "Sua biblioteca foi acessada com sucesso!")
    else:
        print("Programa encerrado.")