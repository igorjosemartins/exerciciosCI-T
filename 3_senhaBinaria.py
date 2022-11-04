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