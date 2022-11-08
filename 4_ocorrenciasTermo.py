# Dada um texto qualquer e um lista de termos de pesquisa (sequencia de caracteres), 
# retorne os primeiros K termos mais recorrentes na string, onde K é um parâmetro configurável.

# Exemplo:

# String: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

# Lista de termos: ["a", "em", "i", "el"]

# K: 2

# Resultado: ["i", "a"]

# Explicação:

# Ocorrências de cada termo,"i": 11, "a": 7, "em": 2, "el": 1, com K = 2, retornamos "i" e "a" 
# ordenados conforme a quantidade de ocorrências de cada termo.

# Obs: Quando houver termos com quantidades iguais, priorizar o retorno de acordo 
# com a ordem de ocorrência do termo na string.

def calcula_top_ocorrencias_de_queries(texto,queries,k):

   termos = queries
   qtdVezes = 0

   arrayQtd = []
   arrayTermos = []
   result = []

   for i in range(len(termos)):
      if termos[i] in texto:
         qtdVezes = texto.count(termos[i])
      else:
         continue
      
      arrayQtd.append(qtdVezes)
      arrayTermos.append(termos[i])

   for a in range(k):
      aux = -1
      for i in range (len(arrayQtd)):
         if arrayQtd[i] > aux:
            aux = arrayQtd[i]
            index = i
         if i == len(arrayQtd) - 1:
            result.append(arrayTermos[index]) 
            arrayQtd[index] = -1
            
   return print(result)
  

calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", ["a", "em", "i", "el"], 2)