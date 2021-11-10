list = open("lista.txt").read().split()

a = 0
for nome in list:
    if nome == "Marcel":        
        print ("Encontrei o Marcel")
    else:
        a += 1
              
print ("Encontrei outros ", a, "nomes")

