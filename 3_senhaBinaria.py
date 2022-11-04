# A senha é representada por um número binário de 10 dígitos formado pelo dígito predominante de cada coluna. Caso a coluna tenha a mesma quantidade de dígitos 0 e 1, deve se considerar o número 1.

# Exemplo: A primeira coluna da lista tem como dígito predominante o número 1, sendo assim, o primeiro dígito - dos 10 - da senha é 1.

# 0110100000
# 1001011111
# 1110001010
# 0111010101
# 0011100110
# 1010011001
# 1101100100
# 1011010100
# 1001100111
# 1000011000

# Desenvolva um algoritmo que receba um array de valores binários (como o exemplo acima) e retorne a representação decimal da senha.

def calcula_numero_da_senha(senha):
    while True:
        try:
            for i in range(len(senha)):
                senha[i] = list(senha[i])
            zero = [0,0,0,0,0,0,0,0,0,0]
            um = [0,0,0,0,0,0,0,0,0,0]
            password = [0,0,0,0,0,0,0,0,0,0]
           
            for i in range(10):
                for j in range(10):
                    if senha[i][j] == '0':
                        zero[j] += 1
                    else:
                        um[j] += 1

            for i in range(len(zero)):
                if zero[i] == um[i]:
                    password[i] = 1
                elif zero[i] > um[i]:
                    password[i] = 0
                elif zero[i] < um[i]:
                    password[i] = 1

            for i in range(len(password)):
                if password[i] == 1:
                    password[i] = 2**(9-i)

            result = 0
            for i in range(len(password)):
                result += password[i]

            return result
        except EOFError:
            break