# BashScript - Funções

Se usarmos as mesmas rotinas várias vezes no script, o tamanho do script aumentará de acordo.

Nesses casos, `functions`são a solução que melhora muitas vezes tanto o tamanho quanto a clareza do roteiro.

Combinamos vários comandos em um bloco entre chaves ( `{`... `}`) e os chamamos com um nome de função definido por nós com `functions`.

É importante observar que as funções devem sempre ser definidas logicamente `before`na primeira chamada, pois um script também é processado de cima para baixo.

Existem dois métodos para definir as funções:

### Método 1

```bash
function name {
	<commands>
}
```

### Método 2

```bash
name() {
	<commands>
}
```

Podemos escolher o método para definir uma função que nos seja mais confortável.

Em nosso script `CIDR.sh`, usamos o primeiro método porque é mais fácil de ler com a palavra-chave " `function`.

### CIDR.sh

```bash
<SNIP>

# Identfy Network range for the specified IP address(es)

function network_range {
	for ip in $ipaddr
	do
		netrange=$(whois $ip | grep "NetRange\|CIDR" | tee -a CIDR.txt)
		cidr=$(whois $ip | grep "CIDR" | awk '{print $2}')

		echo -e "\nNetRange for $ip:"
		echo -e "$netrange"
	done
}

<SNIP>

```

A função é chamada apenas chamando o nome especificado da função, como vimos na instrução ``case``.

### Execução da Função - CIDR.sh

```bash
<SNIP>

case $opt in
	"1") network_range ;;
	"2") ping_host ;;
	"3") network_range && ping_host ;;
	"*") exit 0 ;;
esac
```

## Passagem de parâmetros

Tais funções devem ser projetadas de forma que possam ser utilizadas com uma estrutura fixa de valores ou pelo menos apenas com um formato fixo.

Como já vimos em nosso `CIDR.sh`script, utilizamos o formato de um endereço IP para a função " `network_range`".

Os parâmetros são opcionais e, portanto, podemos chamar a função sem parâmetros. Em princípio, o mesmo se aplica aos parâmetros passados ​​e aos parâmetros passados ​​para um script de shell.

Estes são `$1`- `$9`( `${n}`), ou `$variable`como já vimos. Cada função possui seu próprio conjunto de parâmetros. Portanto, eles não colidem com os de outras funções ou com os parâmetros do shell script.

Uma diferença importante entre scripts bash e outras linguagens de programação é que todas as variáveis ​​definidas são sempre processadas, `globally`a menos que seja declarado de outra forma por " [local](https://www.tldp.org/LDP/abs/html/localvar.html) ". Isso significa que na primeira vez que definirmos uma variável em uma função, iremos chamá-la em nosso script principal (fora da função). A passagem dos parâmetros para as funções é feita da mesma forma que passamos os argumentos para o nosso script e fica assim:

### ImprimirPars.sh

```bash
#!/bin/bash

function print_pars {
	echo $1 $2 $3
}

one="First parameter."
two="Second parameter."
three="Third parameter."

print_pars "$one" "$two" "$three"
```

```sh
./PrintPars.sh

First parameter Second parameter Third parameter

```


## Valores de retorno

Quando iniciamos um novo processo, cada um `child process`(por exemplo, a `function`no script executado) retorna a `return code`para o `parent process`( `bash shell`através do qual executamos o script) ao seu término, informando-o do status da execução.

Essas informações são usadas para determinar se o processo foi executado com êxito ou se ocorreram erros específicos. Com base nesta informação, o `parent process`pode decidir sobre o fluxo adicional do programa.

| **Código de retorno** | **Descrição**                              |
| --------------------- | ------------------------------------------ |
| `1`                   | Erros gerais                               |
| `2`                   | Uso indevido de recursos internos do shell |
| `126`                 | O comando invocado não pode ser executado  |
| `127`                 | Comando não encontrado                     |
| `128`                 | Argumento inválido para sair               |
| `128+n`               | Sinal de erro fatal " `n`"                 |
| `130`                 | Script finalizado por Control-C            |
| `255\*`               | Status de saída fora do intervalo          |

Para recuperar o valor de uma função, podemos usar vários métodos como `return`, `echo`ou a `variable`. No próximo exemplo, veremos como usar " `$?`" para ler o " " `return code`, como passar os argumentos para a função e como atribuir o resultado a uma variável.

### Retorno.sh

```bash
#!/bin/bash

function given_args {

        if [ $# -lt 1 ]
        then
                echo -e "Number of arguments: $#"
                return 1
        else
                echo -e "Number of arguments: $#"
                return 0
        fi
}

# No arguments given
given_args
echo -e "Function status code: $?\n"

# One argument given
given_args "argument"
echo -e "Function status code: $?\n"

# Pass the results of the funtion into a variable
content=$(given_args "argument")

echo -e "Content of the variable: \n\t$content"
```

### Return.sh - Execução

```sh
./Return.sh

	Number of arguments: 0
	Function status code: 1

	Number of arguments: 1
	Function status code: 0

	Content of the variable:
    Number of arguments: 1
```








































