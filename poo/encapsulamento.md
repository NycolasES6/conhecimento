#programação #POO 

# Encapsulamento

Encapsulamento é mais um conceito da programação orientada a objeto, como [[herança]] e [[polimorfismo]].

## Definição

O encapsulamento é um dos conceitos fundamentais em POO. Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impõe restrições ao acesso direto a variáveis e métodos, podendo evitar a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

 - **Público**: Pode ser acessado de fora da classe
 - **Privado**: Só pode ser acessado pela classe

## Modificadores de acesso

Em linguagens como Java e C++, existem palavras reservadas pada definir o nível de acesso aos atributos e métodos da classe. 

### Python

Em python não temos o nome do recurso, porém usamos convenções no nome do recurso, para definir se a variável é pública ou privada. 

```python
_saldo_cliente
```

Todos os recursos são públicos, a menos que o nome inicie com underline. Ou seja, o interpretador Python não irá garantir a proteção do recurso, mas por ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por underline, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar o método fora do escopo da classe.

```python
class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        pass

    def sacar(self, valor):
        pass


conta = Conta(100)
print(conta._saldo)
```

#### Propriedades

Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

```python
class Foo:
    def __init__(self, x):
        self._x = x
	
    @property
    def x(self):
        return self._x
	
    @x.setter
    def x(self, value):
        _x = self._x
        _value = value
        self._x = _x + _value
	
    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(20)
print(foo.x)
foo.x = 40
print(foo.x)
del foo.x
print(foo.x)
```






























