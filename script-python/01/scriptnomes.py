list = open("lista.txt").read().split()

a = 0
results = 0

for nome in list:
    if nome == "Luiz":
        results += 1
    else:
        a += 1


print("Encontrei ", results, " Luiz")
print("Encontrei outros ", a, "nomes")
