#portugol
// 6. Versão em Portugol (VisualG / Portugol Studio)
algoritmo "exercicio_integrador"
var
   nomes: vetor[1..100] de cadeia
   unicos: vetor[1..100] de cadeia
   i, j, qtd, total_unicos: inteiro
   aux, primeiro, ultimo: cadeia
   repetido: logico
inicio
   // 1. Criar lista (vetor) de nomes
   escreva("Quantos nomes deseja digitar? ")
   leia(qtd)
   
   para i de 1 ate qtd faca
      escreva("Digite o ", i, "º nome: ")
      leia(nomes[i])
   fimpara

   // 2. Remover duplicatas
   total_unicos <- 0
   para i de 1 ate qtd faca
      repetido <- falso
      para j de 1 ate i - 1 faca
         se nomes[i] = nomes[j] entao
            repetido <- verdadeiro
         fimse
      fimpara
      
      se nao repetido entao
         total_unicos <- total_unicos + 1
         unicos[total_unicos] <- nomes[i]
      fimse
   fimpara

   // 3. Ordenar alfabeticamente (Método da Bolha)
   para i de 1 ate total_unicos - 1 faca
      para j de 1 ate total_unicos - i faca
         se unicos[j] > unicos[j + 1] entao
            aux <- unicos[j]
            unicos[j] <- unicos[j + 1]
            unicos[j + 1] <- aux
         fimse
      fimpara
   fimpara

   // 4. Criar tupla (Simulado com variáveis)
   primeiro <- unicos[1]
   ultimo <- unicos[total_unicos]

   // 5. Exibir relatório final
   escreval("")
   escreval("--- RELATÓRIO FINAL ---")
   escreval("Total digitados: ", qtd)
   escreval("Total de únicos: ", total_unicos)
   
   escreva("Lista ordenada: [")
   para i de 1 ate total_unicos faca
      escreva(unicos[i])
      se i < total_unicos entao
         escreva(", ")
      fimse
   fimpara
   escreval("]")
   
   escreval("Tupla (primeiro, último): (", primeiro, ", ", ultimo, ")")
fimalgoritmo