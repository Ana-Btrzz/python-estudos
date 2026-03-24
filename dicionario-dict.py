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



#.FROMKEYS   >>cria chaves  >> chaves= identificador para acessar um valor ex: "lala@gmail.com" :

#.GET  >>acessar valores >> acessa chaves:

contatos = {
    "lala@gmail.com": {"nome": "Ana", "tel": "123456"} 
}

#print(contatos[chave]) #keyError
print(contatos.get("chave")) #none
print(contatos.get("chave", {})) #{}

#.ITEMS  >>retorna uma lista de tuplas do dicionario

#.POP >>remove a chave

#.SETDEFAULT

#.UPDATE

#.VALUES

#IN

#DEL