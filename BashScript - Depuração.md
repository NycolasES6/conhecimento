# BashScript - Depuração

[A depuração Bash](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_03.html) é o processo de remoção de erros (bugs) do nosso código. A depuração pode ser realizada de muitas maneiras diferentes. Por exemplo, podemos usar nosso código para depuração para verificar erros de digitação ou podemos usá-lo para análise de código para rastreá-los e determinar por que erros específicos ocorrem.

Este processo também é usado para encontrar vulnerabilidades em programas. Por exemplo, podemos tentar causar erros usando diferentes tipos de entrada e rastrear seu tratamento na CPU através do assembler, o que pode fornecer uma forma de manipular o tratamento desses erros para inserir nosso próprio código e forçar o sistema a executá-lo.

Este tópico será abordado e discutido em detalhes em outros módulos. Bash nos permite depurar nosso código usando as opções " `-x`" ( `xtrace`) e " `-v`". Agora vamos ver um exemplo com nosso `CIDR.sh`script.

### CIDR.sh - Depuração

```sh
bash -x CIDR.sh

+ '[' 0 -eq 0 ']'
+ echo -e 'You need to specify the target domain.\n'
You need to specify the target domain.

+ echo -e Usage:
Usage:
+ echo -e '\tCIDR.sh <domain>'
	CIDR.sh <domain>
+ exit 1
```

Aqui o Bash nos mostra precisamente qual função ou comando foi executado com quais valores. Isto é indicado pelo sinal de mais ( `+`) no início da linha. Se quisermos ver todo o código de uma função específica, podemos definir a opção "`-v`" que exibe a saída com mais detalhes.

### CIDR.sh - depuração detalhada

```sh
bash -x -v CIDR.sh

#!/bin/bash

# Check for given argument
if [ $# -eq 0 ]
then
	echo -e "You need to specify the target domain.\n"
	echo -e "Usage:"
	echo -e "\t$0 <domain>"
	exit 1
else
	domain=$1
fi
+ '[' 0 -eq 0 ']'
+ echo -e 'You need to specify the target domain.\n'
You need to specify the target domain.

+ echo -e Usage:
Usage:
+ echo -e '\tCIDR.sh <domain>'
	CIDR.sh <domain>
+ exit 1
```

Em comparação com a depuração normal, vemos toda a seção de código que foi processada até agora e, em seguida, as etapas individuais que foram executadas.






























