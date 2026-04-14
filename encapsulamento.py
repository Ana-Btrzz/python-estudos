class Foo:
    def __init__(self, x=None):
        self._x = x
        
    @property
    def x(self):
        return self._x or 0  #retorna o valor de x, se nao tiver valor é 0
    
    # @property = transforma o metodo em atributo  -> assim: obj.x    e nao: obj.x()

    @x.setter    #define em como o valor de x sera alterado
    def x(self, value):
        self._x += value    #define soma
        
    @x.deleter     #reseta o valor para o 0
    def x(self):
        self._x = 0
    

foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)