#linux #comandos

O [[linux]] por ser mais voltado a terminal, tem vários comandos.
# Alguns comandos linux

```sh
 echo JAN > meses
```

Sob escreve o arquivo meses e escreve JAN

```sh
echo FEV >> meses
```

Adiciona FEV ao arquivo

```sh
JAN > meses
```

Cria um arquivo chamado meses escrito JAN

```sh
cp meses meses2
```

Copia o arquivo meses para meses2

```sh
mv meses2 ../
```

Move o arquivo meses2 para uma pasta anterios

```sh
head meses
```

mostra o começo de um arquivo

```sh
head -3 meses
```

Mostra as 3 primeiras linhas

```sh
tails
```

Mostra o final do arquivo

```sh
tail -n4
```

Mostra as 4 últimas linhas

```sh
tail -f meses
```

Abri um arquivo e o deixa em modo aberto

```sh
rm -rf curso/
```

Exclui a pasta curso

- **r** : Recursive
- **f** : Force

## Ganhando tempo com no linux

### grep

```sh
cat /etc/passwd | grep "/bin/bash"
```

Pega o conteúdo do passwd e filtra com o grep

```sh
 grep "/bin/bash" /etc/passwd
```

Retornas as linhas do arquivo "**/etc/passwd**" que contém "**/bin/bash**"

```sh
 grep "/bin/bash" /etc/passwd > temshell
```

Retornas as linhas do arquivo "**/etc/passwd**" que contém "**/bin/bash**", e coloca no arquivo "**temshell**"

```sh
 grep -v "nologin" /etc/passwd 
```

Retorna todas as linhas do arquivo, menos as que tem "**nologin**"

```sh
 egrep -v "nologin|/bin/false" /etc/passwd
```

Retorna todas as linhas do arquivo, menos as que tem "**nologin**" ou "**/bin/false**"

### awk

```sh
awk -F : '{print $1}' temshell
```

Pega o arquivo "**temshell**", separa em colunas pelo caracter "**:**" e printa a coluna 1.

```sh
awk -F : '{print $1,$6}' temshell
```

Pega o arquivo "**temshell**", separa em colunas pelo caracter "**:**" e printa a coluna 1 e 6.

```sh
awk -F : '{print "O usuário "$1 " tem o dir " $6}' temshell
```

### cut

```sh
cut -d : -f1 temshell
```

Pega o arquivo "**temshell**", separa em colunas pelo delimitador "**:**" e printa a coluna 1.

```sh
cut -d : -f1,6 temshell
```

Pega o arquivo "**temshell**", separa em colunas pelo delimitador "**:**" e printa a coluna 1 e 6.

### sed

```sh
sed 's/EVE/FEV' teste.txt
```

Pega o arquivo "**teste.txt**", pega onde estiver escrito "**EVE**" e vai substituir por "**FEV**"





















