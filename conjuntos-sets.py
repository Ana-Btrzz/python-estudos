n = set ([1,2,3,4,1,2,3])
print(n) 

#  >>  não duplica nada, não suporta indexação e nem fatimento.

fruta = set (["abacate", "morango", "abacate"])
print(fruta)

#    >>  converter para acessar um elemento.. mas continua nao duplicando
fruta = list(fruta)
print(fruta[0]) 



#.UNION

conjunto_a = {1, 2}
conjunto_b = {4, 3}

conjunto_a.union(conjunto_b) #{1,2,4,3}


#.INTERSECTION

conjunto_a = {1, 2, 3}
conjunto_b = {4, 3, 2}

conjunto_a.intersection(conjunto_b) #{2,3}


#.DIFFERENCE    

conjunto_a = {1, 2, 3}
conjunto_b = {4, 3, 2}

conjunto_a.difference(conjunto_b) #{1}
conjunto_b.difference(conjunto_a) #{4}


#.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) #{true}  >> todos pertencem a b
conjunto_b.issuperset(conjunto_a) #{false} >> todos nao pertencem a a


#ISDISJOINT

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) #True
conjunto_a.isdisjoint(conjunto_c) #False  >> p tem elemento de a no c

#.ADD

sorteio = {1, 23}

sorteio.add(25) #{1, 23, 25}
sorteio.add(42) #{1, 23, 25, 42}
sorteio.add(25) #{1, 23, 25, 42} >> add numeros, mas nao duplica


#.COPY

#.DISCARD   >> deleta algum elemento do conjunto

#.POP    >> deleta elementos na ordem a partir do 0

#.REMOVE()

#IN