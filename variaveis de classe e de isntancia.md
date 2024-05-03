
# Variáveis de classe e de instância

Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

## Exemplos

### Python

```python
class Estudante:
	escola = "DIO"
	
	def __init__(self, nome, numero):
		self.nome = nome
		self.numero = numero
	
	def __str__(self) -> str:
		return f"{self.nome} ({self.numero}) - {self.escola}"
	
	def mostrar_valores(*obj):
		for obj in objs:
			print(obj)

aluno_1 = Estudante("Guilherme", 56451)
aluno_2 = Estudante("Giovana", 17323)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
```




















