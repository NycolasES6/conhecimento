#bashScript 
# BashScript - Operadores de comparação

Para comparar valores específicos entre si, precisamos de elementos chamados [operadores de comparação](https://www.tldp.org/LDP/abs/html/comparison-ops.html) . Os `comparison operators`são usados ​​para determinar como os valores definidos serão comparados. Para estes operadores, diferenciamos entre:

- operadores de string
- operadores de inteiros
- operadores de arquivos
- operadores de booleanos

## Operadores de string

Se compararmos strings, saberemos o que gostaríamos de ter no valor correspondente.


| Operador | Descrição                             |
| -------- | ------------------------------------- |
| ==       | é igual a                             |
| !=       | não é igual a                         |
| <        | é menor que na ordem alfabética ASCII |
| >        | é maior que na ordem alfabética ASCII |
| -z       | se a string estiver vazia (nulo)      |
| -n       | se a string não for nula              |
|          |                                       |

É importante notar aqui que colocamos a variável para o argumento fornecido ( `$1`) entre aspas duplas ( `"$1"`). Isso diz ao Bash que o conteúdo da variável deve ser tratado como uma string. Caso contrário, receberíamos um erro.

```bash
#!/bin/bash

# Check the given argument
if [ "$1" != "HackTheBox" ]
then
	echo -e "You need to give 'HackTheBox' as argument."
	exit 1

elif [ $# -gt 1 ]
then
	echo -e "Too many arguments given."
	exit 1

else
	domain=$1
	echo -e "Success!"
fi
```

Os operadores de comparação de strings " `<`/ `>`" funcionam apenas entre colchetes duplos `[[ <condition> ]]`. Podemos encontrar a tabela ASCII na Internet ou usando o seguinte comando no terminal. Daremos uma olhada em um exemplo mais tarde.

`ASCII`significa `American Standard Code for Information Interchange`e representa uma codificação de caracteres de 7 bits. Como cada bit pode assumir dois valores, existem `128`diferentes padrões de bits, que também podem ser interpretados como números inteiros decimais `0`- `127`ou em valores hexadecimais `00`- `7F`. Os primeiros 32 códigos de caracteres ASCII são reservados como os chamados [caracteres de controle](https://en.wikipedia.org/wiki/Control_character) .

## Operadores Inteiros

Comparar números inteiros pode ser muito útil para nós se soubermos quais valores queremos comparar. Dessa forma, definimos os próximos passos e comandamos como o script deve tratar o valor correspondente.

| **Operador** | **Descrição**          |
| ------------ | ---------------------- |
| `-eq`        | é igual a              |
| `-ne`        | não é igual a          |
| `-lt`        | é menos do que         |
| `-le`        | é menor ou igual a     |
| `-gt`        | é maior que            |
| `-ge`        | é maior que ou igual a |

```bash
#!/bin/bash

# Check the given argument
if [ $# -lt 1 ]
then
	echo -e "Number of given arguments is less than 1"
	exit 1

elif [ $# -gt 1 ]
then
	echo -e "Number of given arguments is greater than 1"
	exit 1

else
	domain=$1
	echo -e "Number of given arguments equals 1"
fi
```

## Operadores de arquivo

Os operadores de arquivo são úteis se quisermos descobrir permissões específicas ou se elas existem.

|**Operador**|**Descrição**|
|---|---|
|`-e`|se o arquivo existir|
|`-f`|testa se é um arquivo|
|`-d`|testa se é um diretório|
|`-L`|testa se é um link simbólico|
|`-N`|verifica se o arquivo foi modificado após a última leitura|
|`-O`|se o usuário atual possui o arquivo|
|`-G`|se o ID do grupo do arquivo corresponder ao do usuário atual|
|`-s`|testa se o arquivo tem tamanho maior que 0|
|`-r`|testa se o arquivo tem permissão de leitura|
|`-w`|testa se o arquivo tem permissão de gravação|
|`-x`|testa se o arquivo tem permissão de execução|

```bash
#!/bin/bash

# Check if the specified file exists
if [ -e "$1" ]
then
	echo -e "The file exists."
	exit 0

else
	echo -e "The file does not exist."
	exit 2
fi
```

## Operadores Booleanos e Lógicos

Obtemos um valor booleano " `false`" ou " `true`" como resultado com operadores lógicos. Bash nos dá a possibilidade de comparar strings usando colchetes duplos `[[ <condition> ]]`. Para obter esses valores booleanos, podemos usar os operadores de string. Quer a comparação corresponda ou não, obtemos o valor booleano " `false`" ou " `true`".

```bash
#!/bin/bash

# Check the boolean value
if [[ -z $1 ]]
then
	echo -e "Boolean value: True (is null)"
	exit 1

elif [[ $# > 1 ]]
then
	echo -e "Boolean value: True (is greater than)"
	exit 1

else
	domain=$1
	echo -e "Boolean value: False (is equal to)"
fi
```

## Operadores lógicos

Com operadores lógicos, podemos definir diversas condições dentro de uma. Isso significa que todas as condições que definimos devem corresponder antes que o código correspondente possa ser executado.

| **Operador** | **Descrição**         |
| ------------ | --------------------- |
| `!`          | negociação lógica NÃO |
| `&&`         | lógico E              |
| `\|`         | OU lógico             |

```bash
#!/bin/bash

# Check if the specified file exists and if we have read permissions
if [[ -e "$1" && -r "$1" ]]
then
	echo -e "We can read the file that has been specified."
	exit 0

elif [[ ! -e "$1" ]]
then
	echo -e "The specified file does not exist."
	exit 2

elif [[ -e "$1" && ! -r "$1" ]]
then
	echo -e "We don't have read permission for this file."
	exit 1

else
	echo -e "Error occured."
	exit 5
fi
```

## Roteiro de exercícios

```bash
#!/bin/bash

var="8dm7KsjU28B7v621Jls"
value="ERmFRMVZ0U2paTlJYTkxDZz09Cg"

for i in {1..40}
do
        var=$(echo $var | base64)
		
		#<---- If condition here:
done
```

Crie uma condição "If-Else" no loop "For" que verifica se a variável chamada "var" contém o conteúdo da variável chamada "valor". Além disso, a variável “var” deve conter mais de 113.450 caracteres. Se estas condições forem atendidas, o script deverá imprimir os últimos 20 caracteres da variável "var". Envie estes últimos 20 caracteres como resposta.