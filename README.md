# Average_Gap_Backtester
Script para backtest e previsões voltadas a trading baseado na interação de médias móveis

Este script tem como objetivo facilitar o backtest aplicado a diversas ações do mercado financeiro, utilizando como
parâmetro de operações o valor da diferença entre uma média móvel de 5 intervalos das ultimas cotações da ação, e
uma média de 20 intervalos das ultimas cotações da mesma ação.

Baseado nisso, o trading system busca operar comprando a ação quando o valor desta diferença, chamada de gap, se 
distancia mais que dois desvios padrão a menos da média dos ultimos 20 intervalos do gap, e busca operar vendendo
a descoberto quando o gap atinge um valor mais alto que 2 desvios padrões acima da média dos 20 ultimos intervalos

Como utilizar:
  
  Basta inserir na pasta DataBase os dados históricos das ações desejadas, em arquivo CSV contendo uma coluna contendo data no 
  formato "DD/MM/YYYY" e nomeada "Data", e o histórico de cotações nomeando a coluna como "Fechamento" (usando ponto como 
  separação de decimais) do período correspondente (recomenda-se no mínimo 1 ano de  histórico), 
  e nomeando o arquivo com o código da ação desejada, (EX.: BOVA11.csv). 
  
  Após executar o script, ele solicitará que você selecione que tipo de operações você deseja simular, sendo as opções:
  
  1 - Para simular tanto operações de compra quanto de venda.
  2 - Para simular apenas operações de compra.
  3 - Para simular apenas operações de venda a descoberto.
  
  Após selecionar o tipo de operação solicidada, o script lhe retornará o retorno histórico deste tipo de operação no período 
  apresentado em comparação ao retorno do Buy and Hold no mesmo período, alem de gerar um gráfico dos retornos históricos de
  ambos em comparação. Também serão gerados dois arquivos de formato CSV para cada ação, um contendo todos os dados processados 
  durante a execução do script, e outro contendo o histórico de retornos dentro do trading system, em comparação ao Buy and Hold 
  do mesmo período.
  
  Recomenda-se o uso deste script em conjunto a um programa de web scrapping para coleta e/ou atualização dos dados em tempo real.
  
  
  ***** ESTE SISTEMA DEVE SER USADO PARA FINS DE ESTUDO ACERCA DO COMPORTAMENTO DOS ATIVOS NO MERCADO FINANCEIRO DE CAPITAIS, OU COMO FERRAMENTA AUXILIAR PARA BACKTEST E CONSTRUÇÃO DE ESTRATÉGIAS QUANTITATIVAS PRÓPRIAS PARA QUEM OS USE, NÃO TENDO PORTANTO QUALQUER FINALIDADE COMO DE RECOMENDAÇÃO DE INVESTIMENTO.

***** A CONSTRUÇÃO E PUBLICAÇÃO DESTE SISTEMA NÃO POSSUI FINS LUCRATIVOS.
