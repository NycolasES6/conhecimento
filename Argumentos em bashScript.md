#bashScript 
# Argumentos em bashScript

A vantagem dos scripts bash é que podemos passar até 9 argumentos (**$0**-**$9**) para o script sem atribuí-los as variáveis ou definir os requisitos correspondentes para estes. 0 argumentos pois o primeiro (**$0**) já está reservado para o script. Precisamos do **\$** antes do nome da variável, para usá-la na posição especificada.

Ficaria assim:

```
NycolasES6@htb[/htb]$ ./script.sh ARG1 ARG2 ARG3 ... ARG9
       ASSIGNMENTS:       $0      $1   $2   $3 ...   $9
```

```bash
#!/bin/bash

if [ $# -eq 0 ]

then

	echo -e "Please, specift the domain. \n"

    echo -e "Usage:"

    echo -e "\t script.sh <domain>"

    exit 1

else

    domain=$1

    echo "You choose domain $domain "

fi
```

```sh
bash script.sh google.com
```

```
You choose domain google.com
```


## Matrizes.sh

```bash
#!/bin/bash

domains=(www.inlanefreight.com ftp.inlanefreight.com vpn.inlanefreight.com www2.inlanefreight.com)

echo ${domains[0]}
```

```sh
NycolasES6@htb[/htb]$ ./Arrays.sh

www.inlanefreight.com ftp.inlanefreight.com vpn.inlanefreight.com
```












