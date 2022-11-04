/* 
   Dizemos que um número natural X esconde o Y quando, ao apagar alguns algarismos de X, o número Y aparece. 
   Por exemplo, o número 12345 esconde o número 235, uma vez que pode ser obtido ao apagar os números 1 e 4. 
   Por outro lado, ele não esconde o número 154.
   Escreva um código que recebe dois números e que retorna um booleano dizendo se o primeiro esconde o segundo.
*/

function checaNumeroEscondido(numero, numeroOculto) {
  // Cria um array vazio para adicionar os números encontrados
  let numeroEncontrado = []

  // Cria uma variável para controlar o último valor do index onde o elemento foi encontrado
  let ultimoIndex = 0

  // Converte o número base em um array de strings
  let arrayNumero = ("" + numero).split("")

  // Converte o número oculto em um array de strings
  let arraynumeroOculto = ("" + numeroOculto).split("")

  // Itera sobre o número oculto que agora é um array e pergunta para o array
  // se os elementos do número oculto estão presentes no array
  arraynumeroOculto.forEach(function (item) {
    // O indexOf retorna -1 se não encontrar o elemento
    // a busca é sempre da esquerda para a direita
    arrayNumero = arrayNumero.slice(ultimoIndex)
    let index = arrayNumero.indexOf(item)

    // verifica se encontrou o elemento no arraynumeroOculto no arrayNumero
    if (index !== -1) {
      // Se o número foi encontrado adiciona ao numeroEncontrado
      numeroEncontrado.push(item)

      // o ultimoIndex recebe o valor de index + o seu valor atual para não
      // permitir valores invertidos
      ultimoIndex = index
    }
  })

  // Fora do loop converte o array em uma string e em seguida em um inteiro
  let resultado = parseInt(numeroEncontrado.join(""))

  // Se o valor de resultado for igual ao de numeroEncontrado o resultado é true
  // senão é sempre falso
  return resultado === parseInt(numeroOculto)
}