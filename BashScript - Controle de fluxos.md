# BashScript - Controle de fluxos

Cada estrutura de controle é uma `branch` ou uma `loop`. Expressões lógicas de valores booleanos geralmente controlam a execução de uma estrutura de controle. Essas estruturas de controle incluem:

- **Branches**:
	- Condições `if-else`
	- Declarações `case`
- **Loops**:
	- Loops `for`
	- Loops `while`
	- Loops `until`

## Loop for

O `For` loop é executado em cada passagem para exatamente um parâmetro, que o shell obtém de uma lista, calcula a partir de um incremento ou obtém de outra fonte de dados. O loop for é executado enquanto encontra os dados correspondentes. Este tipo de loop pode ser estruturado e definido de diferentes maneiras.

Por exemplo, os loops for são frequentemente usados ​​quando precisamos trabalhar com muitos valores diferentes de um array. Isso pode ser usado para verificar diferentes hosts ou portas. Também podemos usá-lo para executar comandos específicos para portas conhecidas e seus serviços para acelerar nosso processo de enumeração. A sintaxe para isso pode ser a seguinte:

### Sintaxe

#### exemplo-1.sh
```bash
for variable in 1 2 3 4
do
	echo $variable
done
```

#### exemplo-2.sh
```bash
for variable in file1 file2 file3
do
	echo $variable
done
```

#### exemplo-3.sh
```bash
for ip in "10.10.10.170 10.10.10.174 10.10.10.175"
do
	ping -c 1 $ip
done
```

Claro, também podemos escrever esses comandos em uma única linha. Esse comando ficaria assim:

```bash
NycolasES6@htb[/htb]$ for ip in 10.10.10.170 10.10.10.174;do ping -c 1 $ip;done

#PING 10.10.10.170 (10.10.10.170): 56 data bytes
#64 bytes from 10.10.10.170: icmp_seq=0 ttl=63 time=42.106 ms

#--- 10.10.10.170 ping statistics ---
#1 packets transmitted, 1 packets received, 0.0% packet loss
#round-trip min/avg/max/stddev = 42.106/42.106/42.106/0.000 ms
#PING 10.10.10.174 (10.10.10.174): 56 data bytes
#64 bytes from 10.10.10.174: icmp_seq=0 ttl=63 time=45.700 ms

#--- 10.10.10.174 ping statistics ---
#1 packets transmitted, 1 packets received, 0.0% packet loss
#round-trip min/avg/max/stddev = 45.700/45.700/45.700/0.000 ms
```

Vamos dar uma outra olhada em nosso script `CIDR.sh`. Adicionamos vários loops for ao script, mas vamos ficar com esta pequena seção de código.

#### CIDR.sh
```bash
<SNIP>

# Identify Network range for the specified IP address(es)
function network_range {
	for ip in $ipaddr
	do
		netrange=$(whois $ip | grep "NetRange\|CIDR" | tee -a CIDR.txt)
		cidr=$(whois $ip | grep "CIDR" | awk '{print $2}')
		cidr_ips=$(prips $cidr)
		echo -e "\nNetRange for $ip:"
		echo -e "$netrange"
	done
}

<SNIP>
```

Como no exemplo anterior, para cada endereço IP do array " `ipaddr`" fazemos uma solicitação "`whois` ", cuja saída é filtrada por " `NetRange`" e " `CIDR`." Isso nos ajuda a determinar em qual intervalo de endereços nosso alvo está localizado. Podemos usar essas informações para procurar hosts adicionais durante um teste de penetração `if approved by the client`. Os resultados que recebemos são exibidos de acordo e armazenados no arquivo " `CIDR.txt`."

## Loop While

O loop `while` é conceitualmente simples e segue o seguinte princípio:

- Uma instrução é executada desde que uma condição seja atendida (`true`)

Também podemos combinar loops e mesclar sua execução com valores diferentes. É importante observar que a combinação excessiva de vários loops entre si pode tornar o código muito confuso e levar a erros que podem ser difíceis de encontrar e seguir. Essa combinação pode parecer em nosso script `CIDR.sh`.

#### CIDR.sh

```bash
<SNIP>
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
<SNIP>
```

Os `while`loops também funcionam com condições como `if-else`. Um loop while precisa de algum tipo de contador para se orientar quando precisa parar de executar os comandos que contém. 

Caso contrário, isso leva a um loop infinito. Esse contador pode ser uma variável que declaramos com um valor específico ou um valor booleano. `While`os loops são executados enquanto o valor booleano é " `True`".

Além do contador, também podemos utilizar o comando " `break`," que interrompe o loop ao chegar a este comando como no exemplo a seguir:

#### whileBreak.sh
```bash
#!/bin/bash

counter=0

while [ $counter -lt 10 ]
do
  # Increase $counter by 1
  ((counter++))
  echo "Counter: $counter"

  if [ $counter == 2 ]
  then
    continue
  elif [ $counter == 4 ]
  then
    break
  fi
done
```

## Loop until

Há também o loop `until`, que é relativamente raro. No entanto, o loop `until`funciona exatamente como o `while`loop, mas com a diferença:

- O código dentro de um loop `until` é executado enquanto a condição específica for `false`.

A outra maneira é deixar o loop rodar até que o valor desejado seja alcançado. Os loops "`until`" são muito adequados para isso. Este tipo de loop funciona de forma semelhante ao loop "`while`" mas, como já mencionado, com a diferença de que funciona até que o valor booleano seja " `False`."

```bash
#!/bin/bash

counter=0

until [ $counter -eq 10 ]
do
    ((counter++))
    echo "Counter: $counter"
done
```

