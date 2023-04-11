# exercício de while que gere um retorno assim --> 
# *G*e*i*l*a* *M*a*r*t*i*n*s
nome = 'Geila Martins'
indice = 0
novo_nome =''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
print(novo_nome)