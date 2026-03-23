dados = {"nome": "Ana", "idade": 25, "cidade": "Barueri"}
print(dados["nome"]) #Ana
print(dados["idade"]) #25
print(dados["cidade"]) #Barueri

dados["cidade"] = "Osasco"
print(dados) #{'nome': 'Ana', 'idade': 25, 'cidade': 'Osasco'}


#DICIONARIO ANINHADOS:

contatos = {
    "anahsgsdyg@gmail.com": {"nome": "Ana", "idade": 25, "cidade": "Barueri"},    
    "lolg@gmail.com": {"nome": "lol", "idade": 23, "cidade": "Barueri"}, 
    "anag@gmail.com": {"nome": "Ana", "idade": 25, "cidade": "lalallal"},    
}

print(contatos["anag@gmail.com"]["cidade"]) #lalallal


#INTERANDO DICIONARIO
for chave in contatos:
    print(chave, contatos[chave]) #retorna todos os itens de contatos


#.CLEAR    >>limpa o dicionario.. zera

#.COPY

#.FROMKEYS   >>cria chaves

#.GET  >>acessar valores >> acessa chaves:
contatos = {
    "lala@gmail.com"}
