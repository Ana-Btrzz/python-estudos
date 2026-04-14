#     git pull   =   atualiza


class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    # __init__ = construtor da classe  -> executa quando cria um objeto, trazendo a quantidade de patas.

    # __str__ = define como o objeto vai aparecer quando fizer um print(animal)

    # self.__dict__.items() = pega todos os atributos e transforma em dicionario -> ex: {'nro_patas': 4}

    # no fim o __str__ forma : nro_patas=4


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(
            **kw
        )  # super = chama a classe pai(animal) e **kw = pega os parametros


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
  pass

# pass = faz nada.. -> herda tudo da classe mamifero e afins, mas n faz nada por ele agora

# para definir os atributos do gato:

gato = Gato(nro_patas=4, cor_pelo="Creme")
print(gato)