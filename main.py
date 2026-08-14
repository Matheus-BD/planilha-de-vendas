vendas = [
    [1200, 1500, 1100], 
    [1000, 1300, 1400], 
    [900, 1700, 1600,8000]
    ]

atual = 0
for i in vendas:
    atual +=1
    for j in range(len(i)):
            print(f"O {atual} vendedor vendeu no {j+1} mês R${i[j]}")

for i in range(len(vendas)):
    print(f"A soma das vendas do {i+1} vendedor é {sum(vendas[i])}")

maior = 0
for ver in vendas:
    if maior < len(ver):
        maior = len(ver)

for j in range(maior):
    mes_tol = 0
    for i in vendas:
        if j < len(i):
            mes_tol += i[j]
    print(f"No {j+1} mẽs o total de vendas foi de: R${mes_tol}")

total = 0
for i in vendas:
    total += sum(i) 
print(f"O total das vendas da empresa é R${total}")

maiorvenda = 0
melhor = 0

for i in range(len(vendas)):
    if maiorvenda < sum(vendas[i]):
        maiorvenda = sum(vendas[i])
        melhor = 1 + i   
print(f"O melhor vendedor e o {melhor} com o total de: R${maiorvenda}")

