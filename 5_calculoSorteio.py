# A chance de uma pessoa ser sorteada é diretamente proporcional às horas de conteúdo que ela assistiu naquele canal. Assim sendo, uma pessoa que ficou 20 horas acompanhando esse streamer tem o dobro de chances de ser sorteado do que uma pessoa que o assistiu durante 10 horas, se ambas não forem assinantes pagos. O número de horas é recebido em minutos e é sempre arredondado para cima, ou seja:

# 181 minutos = 4 horas
# 239 min = 4h
# 180 min = 3h
# Se você possui uma assinatura paga da plataforma, suas chances são dobradas. Assim, no caso acima, se a pessoa que assistiu 10 horas for assinante premium e a que assistiu 20 horas não, ambos terão a mesa chance no sorteio

# Assuma que você vai receber os dados de horas assistidas e de assinaturas em dois vetores, no modelo mostrado abaixo:

# assinante = [True, False, False, False, True, False, True, True, False, False, False]
# minutos_assistidos = [6144, 2742, 330, 30, 1500, 4032, 24036, 3288, 2076, 24540, 4716]
# Considere que as mesmas posições do vetor representam a mesma pessoa. Ex:

# A pessoa número 1 é assinante e viu 103 horas de conteúdo
# A pessoa número 4 não é assinante e viu meia hora de conteúdo
# Escreva um código que retorne um vetor com o percentual de chances de cada uma das pessoas ser sorteada. Retorne os valores arredondados para o inteiro mais próximo.

# Exemplo:
# assinante = [True, False]
# horas_assistidas = [ 60, 120]

# Output:
# [50, 50]

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