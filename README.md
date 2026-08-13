1. Declaramos as variaveis num_vendedor = len(vendas) e num_mes = len(vendas[0]) para podemos ter um controle da quantidade de colunas e de linhas na nossa matriz
2. depois usamos 2 for para podemos percorrer toda lista para informar o vendedor e a quantidade da venda do mes 
3. depois um for com objetivo de apenas separar a linha para podemos usar um sum nas 3 linhas para descobrir a soma do total de vendas de cada vendedor 
4. depois usamos a mesma lógica que usamos para exibir o vendedor e a quantidade da venda do mes mas acontrario para podemos somar as vendas do mes
5. depois usamos outro for que tem o mesmo objetivo do 3 iten da lista de separar as linhas para podemos somar o total de todos o o lucro da empresa 
6. e por ultimo crimos 2 variaveis maiorvenda = 0 para armazenar a maior venda e melhor = 0 para armazenar qual vendedor vez ela, pegamos a informação usando um if verificando se o valor da variavel maior venda e a mesma da soma da venda do vendedor atual do loop for 