def verifi(a, b):
    if primeiro_digito == n13 and segundo_digito == n14:
        print("Seu CPF é válido!")
    else:
        print("Esse CPF é inválido!")


print("Informe seu CPF (Sem caracteres especiais):")
cpf = input()
n1 = int(cpf[0])
n2 = int(cpf[1])
n3 = int(cpf[2])
n4 = int(cpf[3])
n5 = int(cpf[4])
n6 = int(cpf[5])
n7 = int(cpf[6])
n8 = int(cpf[7])
n9 = int(cpf[8])
n10 = int(cpf[9])
n11 = int(cpf[10])

#obtendo 13° digito
primeira_soma = (n1 * 5) + (n2 * 4) + (n3 * 3) + (n4 * 2) + (n5 * 9) + (n6 * 8) + (n7 * 7) + (n8 * 6) + (n9 * 5) + (n10 * 4) + (n11 * 3) + (n12 * 2)
primeiro_digito = primeira_soma % 11
if primeiro_digito < 2:
    primeiro_digito = 0
else:
    primeiro_digito = 11 - primeiro_digito

#obtendo 14° digito
segunda_soma = (n1 * 6) + (n2 * 5) + (n3 * 4) + (n4 * 3) + (n5 * 2) + (n6 * 9) + (n7 * 8) + (n8 * 7) + (n9 * 6) + (n10 * 5) + (n11 * 4) + (n12 * 3) + (primeiro_digito * 2)
segundo_digito = segunda_soma % 11
if segundo_digito < 2:
    segundo_digito = 0
else:
    segundo_digito = 11 - segundo_digito

verifi(primeiro_digito, segundo_digito)
print("Verificação concluída.")

