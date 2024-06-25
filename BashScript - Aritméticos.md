# BashScript - Aritméticos

## Operadores aritméticos

| **Operador** | **Descrição**                     |
| ------------ | --------------------------------- |
| `+`          | Adição                            |
| `-`          | Subtração                         |
| `*`          | Multiplicação                     |
| `/`          | Divisão                           |
| `%`          | Módulo                            |
| `variable++` | Aumente o valor da variável em 1  |
| `variable--` | Diminuir o valor da variável em 1 |
Podemos resumir todos esses operadores em um pequeno script:

#### script.sh
```bash
#!/bin/bash

increase=1
decrease=1

echo "Addition: 10 + 10 = $((10 + 10))"
echo "Substraction: 10 - 10 = $((10 - 10))"
echo "Multiplication: 10 * 10 = $((10 * 10))"
echo "Division: 10 / 10 = $((10 / 10))"
echo "Modulus: 10 % 4 = $((10 % 4))"

((increase++))
echo "Increase Variable: $increase"

((decrease--))
echo "Decrease Variable: $decrease"
```

A saída deste script é semelhante a esta:

#### script.sh - Em execução

```bash
NycolasES6@htb[/htb]$ ./Arithmetic.sh

Addition: 10 + 10 = 20
Substraction: 10 - 10 = 0
Multiplication: 10 * 10 = 100
Division: 10 / 10 = 1
Modulus: 10 % 4 = 2
Increase Variable: 2
Decrease Variable: 0
```

Também podemos calcular o comprimento da variável. Usando esta função `${#variable}`, cada caractere é contado e obtemos o número total de caracteres na variável.

#### VarLength.sh

```bash
#!/bin/bash

htb="HackTheBox"

echo ${#htb}
```

#### VarLength.sh - Em execução

```bash
NycolasES6@htb[/htb]$ ./VarLength.sh

10
```

Se olharmos nosso script ``CIDR.sh``, veremos que usamos os operadores de ``aumento`` e ``diminuição`` várias vezes. Isso garante que o loop ``while``, que discutiremos mais tarde, execute e execute ``ping`` nos hosts enquanto a variável "``stat``" tenha o valor ``1``. Se o comando ``ping`` terminar com o código ``0`` (bem-sucedido), receberemos uma mensagem de que o host está ``up`` e a variável "``stat``", bem como as variáveis ​​"``hosts_up``" e "``hosts_total``" são alteradas.

#### CIDR.sh

```bash
<SNIP>
	echo -e "\nPinging host(s):"
	for host in $cidr_ips
	do
		stat=1
		while [ $stat -eq 1 ]
		do
			ping -c 2 $host > /dev/null 2>&1
			if [ $? -eq 0 ]
			then
				echo "$host is up."
				((stat--))
				((hosts_up++))
				((hosts_total++))
			else
				echo "$host is down."
				((stat--))
				((hosts_total++))
			fi
		done
	done
<SNIP>
```

















