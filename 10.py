# Sua equipe está trabalhando em um app de streaming de músicas e uma das funcionalidades é criar um embaralhador de músicas. 
# Uma pesquisa feita pela equipe de UX (experiência do usuário) mostrou que essa é uma das funcionalidades mais importantes 
# para os usuários e por isso foi priorizada a criação de um experimento para testar a melhor solução.

# A ideia é criar vários embaralhadores diferentes e realizar um teste com partes dos usuários (chamado de teste A/B), 
# onde cada grupo de usuários selecionado recebe uma versão e através de pesquisas e métricas de utilização 
# saberemos qual terá a maior aceitação.

# Sua tarefa será desenvolver um desses embaralhadores. Você deve criar uma função que receberá uma lista de pesos 
# que representa as músicas mais ouvidas pelo usuário. Sua função deve retornar uma lista organizada intercalando as 
# músicas mais ouvidas com as músicas menos ouvidas. Por exemplo:

# Na situação onde a lista de pesos é: [2, 10, 5, 3] sua função deverá retornar [10, 2, 5, 3]

def shuffle_musicas(musicas_tocadas):

   shuffle = musicas_tocadas

   valor = -1
   for i in range (len(shuffle)):
      if i != len(shuffle) - 1:
         if shuffle[i] < shuffle[i+1]:
            shuffle[i] = shuffle[i+1]
      else:
         continue

   print(shuffle)

shuffle_musicas([2, 10, 5, 3])