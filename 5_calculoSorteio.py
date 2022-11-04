def calcula_porcentagem_sorteio(assinante, minutos_assistidos):

   boolArray = assinante
   numArray = minutos_assistidos

   porcentagem = []
   
   hora = 0

   for i in range (len(boolArray)):
      
      for j in range (len(numArray)):

         hora = float(numArray[i] / 60)

         if(hora.is_integer() == False):
            chance = int(hora + 1)
         else:
            chance = int(hora)
            
         if (boolArray[i] == True):
            chance = chance * 2
            porcentagem.append(chance)
            break
         else:
            chance
            porcentagem.append(chance)
            break
      
   total = 0
   for i in range (len(porcentagem)):
      total += porcentagem[i]

   for i in range (len(porcentagem)):     
      porcentagem[i] = round(porcentagem[i] * 100 / total)
   
   return print(porcentagem)

calcula_porcentagem_sorteio([True, False], [33, 33])