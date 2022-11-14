# Sua função receberá 4 valores: TF1 (a taxa fixa da empresa 1), VQR1 (o valor por quilômetro rodado da empresa 1), TF2 (a taxa fixa da empresa 2), VQR2 (o valor por quilômetro rodado da empresa 2), todos em formato string. Seu retorno deve ser uma string em uma das seguintes formas:

# “Tanto faz” - para o caso de o valor das duas empresas para qualquer corrida ser igual
# “Empresa 1” - se o valor da Empresa 1 for sempre menor que o da Empresa 2
# “Empresa 2” - para o caso contrário do citado acima
# “Empresa Xpto quando a distância < N, Tanto faz quando a distância = N, Empresa Ypto quando a distância > N” para o caso de a escolha depender da distância a ser percorrida (onde Xpto e Ypto representa 1 ou 2 e N representa a distância).
# Exemplo:
# TF1 = 2,50
# VQR1 = 1,00
# TF2 = 5,00
# VQR2 = 0,75
# Output:
# “Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0”

def escolhe_taxi(tf1,vqr1,tf2,vqr2):

    tf1 = float(tf1)
    tf2 = float(tf2)
    vqr1 = float(vqr1)
    vqr2 = float(vqr2)

    if tf1 == tf2 and vqr1 == vqr2:
        return "Tanto faz"

    if tf1 < tf2 and vqr1 < vqr2:
        return "Empresa 1"
    if tf1 < tf2 and vqr1 == vqr2:
        return "Empresa 1"
    if tf1 == tf2 and vqr1 < vqr2:
        return "Empresa 1"

    if tf2 < tf1 and vqr2 == vqr1:
        return "Empresa 2"
    if tf2 < tf1 and vqr2 < vqr1:
        return "Empresa 2"
    if tf2 == tf1 and vqr2 < vqr1:
        return "Empresa 2"
    else:
        if vqr1 > vqr2 and tf1 < tf2:
            x = vqr1 - vqr2
            b = tf2 - tf1
            result = b / x
            resultReturn = "Empresa 1 quando a distância <" + str(result) + ", Tanto faz quando a distância =" + str(result) + ", Empresa 2 quando a distância >" + str(result)
            return resultReturn
        else:
            x = vqr2 - vqr1
            b = tf1 - tf2
            result = b / x
            resultReturn = "Empresa 2 quando a distância <" + str(result) + ", Tanto faz quando a distância =" + str(result) + ", Empresa 1 quando a distância >" + str(result)
            return resultReturn
