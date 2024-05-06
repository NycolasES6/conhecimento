
# Métodos de classe

Métodos de classe estão ligados á classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.

## Método estático

Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado á classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.

## Métodos de classe X Métodos estáticos

 - Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
 - Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

## Quando utilizar método de classe ou estático

- Geralmente usamos o método de classe para criar métodos de fábrica
- Geralmente usamos métodos estáticos para criar funções utilitárias

## Exemplos

### Python

```python
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p2 = Pessoa.criar_de_nascimento(1995, 8, 31, "João")
print(f"Idade:{p2.idade}\tNome:{p2.nome}")
  
print(Pessoa.e_maior_idade(12))
print(Pessoa.e_maior_idade(18))
```
