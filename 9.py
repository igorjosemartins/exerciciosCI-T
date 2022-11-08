# Ao se comparar se uma string é maior que outra, considera-se a ordem alfabética ou lexicográfica. No caso, “abcd” < “adbc” < “bacd”.

# Escreva uma função que receba uma string A e retorne uma string B, sendo que B é composta pelos mesmos caracteres que A reordenados.

# B deve obedecer às seguintes condições:

# Ser maior que A
# Ser a menor string possível que cumpra as condições acima
# Caso não seja possível encontrar uma string que cumpra as condições, retorne a string “sem resposta”.
# Por exemplo:

# A = “ab”
# Logo, o resultado será “ba”

# A = “abcde”
# Logo, o resultado será “abced”

# A = “ba”
# Nesse caso, o resultado será “sem resposta"



   # transformar a string em um array, separando cada caracter [✅]
   # percorrer o array, *logica* []
   # condição de mesmo elemento (repetição)
   # juntar todos os elementos do array, para formar uma nova string []
   # retornar esta string []


# TESTS: 

# "Qualified" => "Qualiidef"

# "ab" => "ba"

# "nextgen" => "nextgne"

# "ddee" => "dede"

# "ba" => "sem resposta"

# "" => "sem resposta"

def menor_string_maior(name):

   stringB = list(name)
   aux = ""
   
   
   for i in range(len(stringB) + 1):

      if(len(stringB) == 0):
         return print("sem resposta")
      
      elif(len(stringB) == 2 and stringB[i] > stringB[i + 1]):
         return print("sem resposta")
      
      else:
         if i == len(stringB) - 1:
            
            if(stringB[i] == stringB[i - 1]):
               
               aux = stringB[i - 2]
               stringB[i - 2] = stringB[i - 1]
               stringB[i - 1] = aux
            
            else:
               
               aux = stringB[i - 1]
               stringB[i - 1] = stringB[i]
               stringB[i] = aux


   result = ""
   for a in range(len(stringB)):
      result += stringB[a]
   
   return print(stringB), print(result)
   

menor_string_maior("ab")