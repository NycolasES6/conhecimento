# Tuplas

São parecidas com listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis.

## Criando tuplas

### Python

```python
frutas = ("laranja", "pera", "uva",)

letras = tuple([1, 2, 3, 4])
```

## Obtendo valores

### Python

```python
frutas = ("laranja", "pera", "uva",)

frutas[0] # "laranja"
frutas[-1] # "uva"
```

## Tuplas aninhadas

### Python

```python
matriz = (
	(1, "a", 2),
	(3, "h", 7),
	(5, 4, "g")
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-2] # 4
```

## Slice

### Python

```python
tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:]
tupla[:2]
tupla[1:3]
tupla[0:3:2]
tupla[::]
tupla[::-1]
```

## Iteração

### Python

```python
carros = ("gol", "celta", "palio")

for carro in carros:
	print(carro)
```

## Enumeração

### Python

```python
carros = ("gol", "celta", "palio")

for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")
```