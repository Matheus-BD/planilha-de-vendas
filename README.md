## planilha-de-vendas

# Vendedor e a Venda do Mẽs
Foi usando variavel atual para saber qual e o vendedor que está sendo citado, dois laços for um para separar um vetor dentro da matriz e outro para percorrer esse vetor para buscar as informações necessárias para informar o vendedor e a venda que ele vez em cada mẽs.

# Total de Vendas de Cada Vendedor 
Foi usando for para podemos navegar por cada linha e depois fazemos a soma de tudo na linha com a função sum, assim podemos descobrir quanto cada vendedor vendeu.

# Total de Vendas no Mẽs 
Primeiro descobrimos qual é a maior quantidade de meses existente na matriz. Depois percorremos mês por mês e, para cada mês, percorremos todos os vendedores. Antes de somar, verificamos se aquele vendedor possui dados para o mês. Dessa forma, conseguimos somar as vendas de cada mês sem depender de uma quantidade fixa de meses e sem tentar acessar posições que não existem.

# Total de Vendas da empresa
Aqui usamos um for para podemos somar cada valor das linhas que existem na matriz e ai adcionar o valor em uma variavel que a cada vez que passa pelo loop e somanda com o valor anterior 

# Melhor Vendedor 
Aqui usamos 2 variaveis para armazenar qual o melhor vendedor e para armazenar qual foi o valor da venda, aonde foi usando a logica do loop para saber o total de vendas de cada vendedor mas colocamos um if para saber se a soma da venda dos vendedor sendo verificado maior do que a armazenada na variavel do maior valor caso seja e trocado o antigo valor pelo novo