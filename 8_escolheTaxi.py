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
