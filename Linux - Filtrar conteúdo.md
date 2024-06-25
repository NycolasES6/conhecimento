#Linux #SO 
# Filtrar conteúdo no Linux

Existem duas ferramentas chamadas `more`e `less`, que são muito idênticas. São fundamentais `pagers`que nos permitem percorrer o arquivo de forma interativa. Vejamos alguns exemplos.

### more

```sh
NycolasES6@htb[/htb]$ more /etc/passwd
```

Saímos quando saímos permanece no terminal

### less

```sh
NycolasES6@htb[/htb]$ less /etc/passwd
```

Quando saimos ele não aparece no terminal

### head

Às vezes estaremos interessados ​​apenas em questões específicas no início ou no final do arquivo. Se quisermos apenas obter as `first`linhas do arquivo, podemos usar a ferramenta `head`.

```sh
NycolasES6@htb[/htb]$ head /etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
```

### tail

```shell-session
NycolasES6@htb[/htb]$ tail /etc/passwd

miredo:x:115:65534::/var/run/miredo:/usr/sbin/nologin
usbmux:x:116:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:117:119:RealtimeKit,,,:/proc:/usr/sbin/nologin
nm-openvpn:x:118:120:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:119:121:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
pulse:x:120:122:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
beef-xss:x:121:124::/var/lib/beef-xss:/usr/sbin/nologin
lightdm:x:122:125:Light Display Manager:/var/lib/lightdm:/bin/false
do-agent:x:998:998::/home/do-agent:/bin/false
user6:x:1000:1000:,,,:/home/user6:/bin/bash
```

### sort

Dependendo de quais resultados e arquivos são tratados, eles raramente são classificados. Muitas vezes é necessário ordenar os resultados desejados em ordem alfabética ou numérica para obter uma melhor visão geral. Para isso, podemos utilizar uma ferramenta chamada `sort`.

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | sort

_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
cry0l1t3:x:1001:1001::/home/cry0l1t3:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
dovecot:x:114:117:Dovecot mail server,,,:/usr/lib/dovecot:/usr/sbin/nologin
dovenull:x:115:118:Dovecot login user,,,:/nonexistent:/usr/sbin/nologin
ftp:x:113:65534::/srv/ftp:/usr/sbin/nologin
games:x:5:60:games:/usr/games:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
htb-student:x:1002:1002::/home/htb-student:/bin/bash
<SNIP>
```


### grep

Mais frequentemente, procuraremos apenas resultados específicos que contenham padrões que definimos. Uma das ferramentas mais utilizadas para isso é o `grep`, que oferece diversos recursos. Assim, podemos procurar usuários que tenham o shell padrão " `/bin/bash`" definido como exemplo.

```shell
NycolasES6@htb[/htb]$ cat /etc/passwd | grep "/bin/bash"

root:x:0:0:root:/root:/bin/bash
mrb3n:x:1000:1000:mrb3n:/home/mrb3n:/bin/bash
cry0l1t3:x:1001:1001::/home/cry0l1t3:/bin/bash
htb-student:x:1002:1002::/home/htb-student:/bin/bash
```

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | grep "/bin/bash"

root:x:0:0:root:/root:/bin/bash
mrb3n:x:1000:1000:mrb3n:/home/mrb3n:/bin/bash
cry0l1t3:x:1001:1001::/home/cry0l1t3:/bin/bash
htb-student:x:1002:1002::/home/htb-student:/bin/bash
```

Outra possibilidade é excluir resultados específicos. Para isso, `utiliza-se a opção " ge" com `grep`. No próximo exemplo, excluímos todos os usuários que desabilitaram o shell padrão com o nome " `/bin/false`" ou " `/usr/bin/nologin`".

```shell
NycolasES6@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin"

root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
postgres:x:111:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
user6:x:1000:1000:,,,:/home/user6:/bin/bash
```


## Cut

Resultados específicos com caracteres diferentes podem ser separados como delimitadores. Aqui é útil saber como remover delimitadores específicos e mostrar as palavras em uma linha em uma posição especificada. Uma das ferramentas que podem ser utilizadas para isso é o `cut`. Portanto usamos a opção " `-d`" e definimos o delimitador para o caractere de dois pontos ( `:`) e definimos com a opção " `-f`" a posição na linha que queremos gerar.

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin" | cut -d":" -f1

root
sync
mrb3n
cry0l1t3
htb-student
```


## Tr

Outra possibilidade de substituir determinados caracteres de uma linha por caracteres definidos por nós é a ferramenta `tr`. Como primeira opção definimos qual caractere queremos substituir e, como segunda opção, definimos o caracter pelo qual queremos substituí-lo. No próximo exemplo, substituímos o caractere dois pontos por espaço.

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin" | tr ":" " "

root x 0 0 root /root /bin/bash
sync x 4 65534 sync /bin /bin/sync
mrb3n x 1000 1000 mrb3n /home/mrb3n /bin/bash
cry0l1t3 x 1001 1001  /home/cry0l1t3 /bin/bash
htb-student x 1002 1002  /home/htb-student /bin/bash
```

## Column

Como os resultados da pesquisa muitas vezes podem ter uma representação pouco clara, a ferramenta `column` é adequada para exibir esses resultados em formato tabular usando o " `-t`."

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | column -t

root         x  0     0      root               /root        /bin/bash
sync         x  4     65534  sync               /bin         /bin/sync
mrb3n        x  1000  1000   mrb3n              /home/mrb3n  /bin/bash
cry0l1t3     x  1001  1001   /home/cry0l1t3     /bin/bash
htb-student  x  1002  1002   /home/htb-student  /bin/bash
```

## Awk

Como podemos ter notado, o usuário " `postgres`" tem uma linha a mais. Para manter a classificação de tais resultados o mais simples possível, a programação ( `g`) `awk` é benéfica, que nos permite exibir o primeiro ( `$1`) e o último ( `$NF`) resultado da linha.

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}'

root /bin/bash
sync /bin/sync
mrb3n /bin/bash
cry0l1t3 /bin/bash
htb-student /bin/bash
```

## Sed

Haverá momentos em que desejaremos alterar nomes específicos em todo o arquivo ou na entrada padrão. Uma das ferramentas que podemos usar para isso é o editor de stream chamado `sed`. Um dos usos mais comuns disso é a substituição de texto. Aqui, `sed` procura padrões que definimos na forma de expressões regulares (regex) e os substituímos por outro padrão que também definimos. Vamos nos ater aos últimos resultados e dizer que queremos substituir a palavra " `bin`" por " `HTB`."

O sinalizador "`s`" no início representa o comando substituto. Em seguida, especificamos o padrão que queremos substituir. Após a barra (`/`), inserimos o padrão que queremos usar como substituto na terceira posição. Por fim, usamos a  flag "`g`", que significa substituir todas as correspondências.

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | sed 's/bin/HTB/g'

root /HTB/bash
sync /HTB/sync
mrb3n /HTB/bash
cry0l1t3 /HTB/bash
htb-student /HTB/bash
```

## Wc

Por último, mas não menos importante, muitas vezes será útil saber quantas partidas bem-sucedidas temos. Para evitar a contagem manual de linhas ou caracteres, podemos usar a ferramenta `wc`. Com a opção "`-l`", especificamos que apenas as linhas são contadas.

```sh
NycolasES6@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | wc -l

5
```




