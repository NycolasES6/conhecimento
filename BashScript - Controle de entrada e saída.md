# BashScript - Controle de entrada e saída

  
Precisamos estar familiarizados com como fazer com que um script em execução aguarde nossas instruções. Se olharmos novamente para nosso script ``CIDR.sh``, veremos que adicionamos essa chamada para decidir as próximas etapas.

#### CIDR.sh
```bash
# Available options
<SNIP>
echo -e "Additional options available:"
echo -e "\t1) Identify the corresponding network range of target domain."
echo -e "\t2) Ping discovered hosts."
echo -e "\t3) All checks."
echo -e "\t*) Exit.\n"

read -p "Select your option: " opt

case $opt in
	"1") network_range ;;
	"2") ping_host ;;
	"3") network_range && ping_host ;;
	"*") exit 0 ;;
esac
```

As primeiras linhas `echo` servem como menu de exibição das opções disponíveis. Com o comando `read`, a linha com " `Select your option:`" é exibida, e a opção adicional `-p` garante que nossa entrada permaneça na mesma linha. Nossa entrada é armazenada na variável `opt`, que então usamos para executar as funções correspondentes com a instrução `case`, que veremos mais tarde. Dependendo do número que inserimos, a instrução `case` determina quais funções serão executadas.

## Controle de saída

Um problema com os redirecionamentos é que não obtemos nenhuma saída do respectivo comando. Ele será redirecionado para o arquivo apropriado.

Se nossos scripts se tornarem mais complicados posteriormente, eles poderão levar muito mais tempo do que apenas alguns segundos. Para evitar ficar inativo esperando pelos resultados do nosso script, podemos usar o utilitário [tee](https://man7.org/linux/man-pages/man1/tee.1.html) .

Ele garante que vejamos os resultados obtidos imediatamente e que eles sejam armazenados nos arquivos correspondentes. Em nosso script `CIDR.sh`, usamos esse utilitário duas vezes de maneiras diferentes.

#### CIDR.sh
```sh
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

# Identify IP address of the specified domain
hosts=$(host $domain | grep "has address" | cut -d" " -f4 | tee discovered_hosts.txt)

<SNIP>
```

Ao usar `tee`, transferimos a saída recebida e usamos o pipe( `|`) para encaminhá-la para `tee`. O parâmetro " `-a`/ `--append`" garante que o arquivo especificado não seja sobrescrito, mas complementado com os novos resultados. Ao mesmo tempo, mostra-nos os resultados e como eles serão encontrados no arquivo.

```sh
NycolasES6@htb[/htb]$ cat discovered_hosts.txt CIDR.txt

165.22.119.202
NetRange:       165.22.0.0 - 165.22.255.255
CIDR:           165.22.0.0/16
```
















