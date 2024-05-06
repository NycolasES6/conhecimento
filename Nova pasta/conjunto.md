# Conjunto

Conjuntos não podem ter elementos repetidos

Não suportam indexação e nem fatiamento

Caso queira alterar seus valores, tem de converter o conjunto para [[lista]], muito utilizado em [[Java]]

## Declaração

### Python

```python
numeros = set([1, 2, 3, 4, 2, 3]) # {1, 2, 3, 4}

letras = set("abacaxi") # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"} # {"java", "python"}
```

## Acessar valores

### Python

```python
numeros = {1, 2, 3, 2} # {1, 3, 2}

numeros = list(numeros)

print(numeros[0]) # 1
```

## Iteração

### Python

```python
numeros = {1, 2, 3, 2} # {1, 3, 2}

for numero in numeros:
	print(numero)
```

## Enumeração

### Python

```python
numeros = {1, 2, 3, 2} # {1, 3, 2}

for indice, numero in enumerate(numeros):
	print(f"{indice}: {numero}")
```

## União

### Python

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
```

## Interseção

### Python

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}
```

## Diferença

### Python

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}
```

## Diferença simétrica

### Python

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}
```

## {}.issubset

### Python

```python
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False
```

## {}.issuperset

### Python

```python
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True
```

## {}.isdisjoint

### Python

```python
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4}
conjunto_c = {4, 5, 6}

conjunto_a.isdisjoint(conjunto_b) # False
conjunto_b.isdisjoint(conjunto_c) # True
```

## Adicionar

### Python

```python
sorteio = {1, 4, 3}

sorteio.add(45) # {1, 4, 3, 45}
```

## Copiar

### Python

```python
sorteio = {1, 4, 3}

sorteio.copy() # {1, 4, 3}
```

## Limpar

### Python

```python
sorteio = {1, 4, 3}

sorteio.clear() # { }
```

## Descartar elemento

### Python

```python
sorteio = {1, 4, 3}

sorteio.discard(4) # {1, 3}
```

## Remover primeiro elemento

### Python

```python
sorteio = {1, 4, 3}

sorteio.pop() # {4, 3}
sorteio.pop() # {3}
```

## Remover elemento

### Python

```python
sorteio = {1, 4, 3}

sorteio.pop(3) # {1, 4}
```

## Tamanho

### Python

```python
sorteio = {1, 4, 3}

sorteio.len() # 3
```

## Verificar se contém

### Python

```python
sorteio = {1, 4, 3}
1 in sorteio # True
10 in sorteio # alse
```






















































