
# Manipulando strings

O tipo [[string]] contém várias formas de ser manipulada para várias ocasiões

## Maiúsculo, minúsculo e título

### Python

```python
curso = "pYtHoN"

print(curso.upper()) # PYTHON

print(curso.lower()) # python

print(curso.title()) # Python
```

## Eliminando espaços em branco

### Python

```python
curso = "   Python   "

print(curso.strip()) # "Python"

print(curso.lstrip()) # "Python   "

print(curso.rstrip()) # "   Python"
```

## Junções e centralização

### Python

```python
curso = "Python"

print(curso.center(10, "#")) # "##Python##"

print(".".join(curso)) # "P.y.t.h.o.n"
```

## Interpolação

### Python

**old school**

```python
nome = "Nycolas"
idade = 23

print("Meu nome é %s e eu tenho %d anos de idade"%(nome, idade))
```

**f strings**

```python
nome = "Nycolas"
idade = 23

print(f"Meu nome é {nome} e eu tenho {idade} anos de idade")
```

```python
PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}") # "Valor de PI:           3.14"
```

**Format**

```python
nome = "Nycolas"
idade = 23

print("Meu nome é {} e eu tenho {} anos de idade".format(nome, idade))
```

```python
nome = "Nycolas"
idade = 23

print("Meu nome é {1} e eu tenho {0} anos de idade".format(idade, nome))
```

```python
nome = "Nycolas"
idade = 23

print("Meu nome é {name} e eu tenho {years} anos de idade".format(name=nome, years=idade))
```

```python
nycolas = {
	"nome" : "Nycolas"
	"idade" : 23
}

print("Meu nome é {nome} e eu tenho {idade} anos de idade".format(**nycolas))
```

## Fatiamento

### Python

```python
nome = "Guilherme Arthur de Carvalho"

nome[0] # "G"

nome[:9] # "Guilherme"

nome[10:] # "Arthur de Carvalho"

nome[10:16] # "Arthur"

nome[10:16:2] # "Atu"

nome[:] # "Guilherme Arthur de Carvalho"

nome[::-1] # "ohlavraC ed ruhtrA emrehliuG"
```

## Strings triplas

```python
nome = "Nycolas"

mensagem = f"""
Olá mundo,
sou o {nome}
"""
# Olá mundo,
# sou o Nycolas
```




















































