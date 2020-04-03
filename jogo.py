import os

def verLinhaIgual(matriz):
    count = 0
    soma = 0
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == matriz[i][j-1]:
                count += 1
                soma += matriz[i][j]
            else:
                count += 0
            if count == 3 and soma != 0:
                return True
                exit()
        count = 0
    return False

def verColunaIgual(matriz):
    count = 0
    soma = 0
    for j in range(3):
        for i in range(3):
            if matriz[i][j] == matriz[i-1][j]:
                count += 1
                soma += matriz[i][j]
            else:
                count += 0
            if count == 3 and soma != 0:
                return True
                exit()
        count = 0
    return False

def verDiagonalIgual(matriz):
    count = 0
    soma = 0
    for i in range(3):
        if matriz[i][i] == matriz[i-1][i-1]:
            count += 1
            soma += matriz[i][i]
        else:
            count += 0
        if count == 3 and soma != 0:
            return True
            exit()
    return False

def verDiagonaSeclIgual(matriz):
    count_diag = 0
    num = 2
    for i in range(3):
        for j in range(3):
            if j == num:
                count_diag += matriz[i][j]
                num -= 1
    if count_diag == 30 or count_diag == 3:
        return True
        exit()
    return False

def desenhaTabu(matriz):
    print("")
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 10:
                print("| X |", end="")
            elif matriz[i][j] == 1:
                print("| O |", end="")
            else:
                print("| - |", end="")
        print("")

def menu():
    os.system("cls")
    print("************************************** JOGO DA VELHA **************************************")
    print("******************************** Player 1- O | Player 2 - X *******************************")
    print("*******************************************************************************************")
    print("************************************** COMO JOGAR? ****************************************")
    print("******** Cada jogador deve inserir a coordenada que deve ser inserida cada peça. **********")
    print("*******************************************************************************************")

def verMatriz(matriz):
    if verLinhaIgual(matriz) or verColunaIgual(matriz) or verDiagonalIgual(matriz) or verDiagonalIgual(matriz) or verDiagonaSeclIgual(matriz):
        return True
    else:
        return False

def jogo():
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    menu()

    for ct in range(0, 9):
        if((ct % 2) != 0):
            print("")
            print("Player 2")
            print("")
            p1 = True
            p2 = False
            player = 2
        else:
            print("")
            print("Player 1")
            print("")
            p2 = True
            p1 = False
            player = 1

        try:
            i = int(input("Linha: "))
            j = int(input("Coluna: "))
            print("")

        except ValueError:
            print("Insira um número!")
            i = int(input("Linha: "))
            j = int(input("Coluna: "))
            print("")

        validar = False

        while (validar == False):
            while(i > 2 or i < 0 or j > 2 or j < 0):
                print("Você inseriu um valor abaixo de 0 ou acima de 2. Insira novamente!")
                i = int(input("Linha: "))
                j = int(input("Coluna: "))
                print("")
            if mat[i][j] == 0:
                validar = True
                if p1:
                    mat[i][j] = 10
                else:
                    mat[i][j] = 1
            else:
                print("Você inseriu em cima de outro valor. Insira novamente!")
                i = int(input("Linha: "))
                j = int(input("Coluna: "))
                print("")

        os.system("cls")
        desenhaTabu(mat)

        if ct > 3 and verMatriz(mat):
            print("")
            print("PLAYER {} - WIN!".format(player))
            exit()

    print("\nDRAW!")

jogo()
