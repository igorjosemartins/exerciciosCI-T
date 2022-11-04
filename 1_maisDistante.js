/*
   Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. 
   No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível.
   E caso não exista posto de gasolina, retornar -1

   A pessoa responsável por fazer a especificação do sistema informou que você terá as seguintes informações: 
   - consumo médio de combustível
   - quantidade de combustível restante no veículo
   - um array contendo distâncias dos postos de gasolinas

   Exemplo:
   Combustivel (em litros): 2
   Consumo médio (km/l): 8
   Postos de Gasolina (km): [2, 15, 22, 10.2]
*/

function ultimaParada(combustivel, consumoMedio, postos) {
  // limite de combustivel
  const limite = combustivel * consumoMedio

  // ordenando crescente
  postos.sort((a, b) => a - b)
  console.log(postos)

  // igualo a variável a -1, pois se não entrar nas condições abaixo, ela retorna -1
  let maisDistante = -1

  for (i = 0; i < postos.length; i++) {
    if (postos[i] > maisDistante && postos[i] <= limite) {
      maisDistante = postos[i]
    }
  }
  return maisDistante
}