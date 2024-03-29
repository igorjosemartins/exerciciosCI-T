# /* 
#    Dizemos que um número natural X esconde o Y quando, ao apagar alguns algarismos de X, o número Y aparece. 
#    Por exemplo, o número 12345 esconde o número 235, uma vez que pode ser obtido ao apagar os números 1 e 4. 
#    Por outro lado, ele não esconde o número 154.
#    Escreva um código que recebe dois números e que retorna um booleano dizendo se o primeiro esconde o segundo.
# */

def checa_numero_escondido(numero,numero_oculto):
    
    number1 = str(numero)
    numberOculto = str(numero_oculto)
    
    arrayNumber1 = list(number1)
    arrayOculto = list(numberOculto)
    
    result = []
    index = 0
    
    for x in range(len(arrayOculto)):
        result.append(None)

    for i in range(len(arrayOculto)):
        for j in range(len(arrayNumber1)):
            if arrayOculto[i] == arrayNumber1[j]:
                result[index] = arrayNumber1[j]
                index += 1
                break
            else:
                arrayNumber1[j] = 'X'

    if result == arrayOculto:
        return True
    else:
        return False
