def checa_numero_escondido(numero,numero_oculto):
    while True:
        try:
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
        except EOFError:
            break