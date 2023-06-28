num_integrantes = int(input())

if num_integrantes >= 1:
    camisas = "1,"  

    if num_integrantes >= 2:
        camisas += " 1"  

        n1 = 1
        n2 = 1
        i = 3
        while i <= num_integrantes:
            n1, n2 = n2, n1 + n2
            camisas += ", " + str(n2)  
            i += 1

    print(f"A sequência de número das camisas do seu time será: {camisas}")
