#Linux #comandos
# Linux - Encontre arquivos e diretórios

## which

Uma das ferramentas comuns é `which`. Esta ferramenta retorna o caminho do arquivo ou link que deve ser executado. Isso nos permite determinar se programas específicos, como **cURL** , **netcat** , **wget** , **python** , **gcc** , estão disponíveis no sistema operacional. Vamos usá-lo para procurar Python em nossa instância interativa.

```sh
NycolasES6@htb[/htb]$ which python

/usr/bin/python
```

## find

Outra ferramenta útil é `find`. Além da função de localizar arquivos e pastas, esta ferramenta também contém a função de filtrar os resultados. Podemos usar parâmetros de filtro como o tamanho do arquivo ou a data. Também podemos especificar se procuramos apenas arquivos ou pastas.

### sintaxe

```sh
NycolasES6@htb[/htb]$ find <location> <options>
```

```sh
NycolasES6@htb[/htb]$ find / -type f -name *.conf -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null

-rw-r--r-- 1 root root 136392 Apr 25 20:29 /usr/src/linux-headers-5.5.0-1parrot1-amd64/include/config/auto.conf
-rw-r--r-- 1 root root 82290 Apr 25 20:29 /usr/src/linux-headers-5.5.0-1parrot1-amd64/include/config/tristate.conf
-rw-r--r-- 1 root root 95813 May  7 14:33 /usr/share/metasploit-framework/data/jtr/repeats32.conf
-rw-r--r-- 1 root root 60346 May  7 14:33 /usr/share/metasploit-framework/data/jtr/dynamic.conf
-rw-r--r-- 1 root root 96249 May  7 14:33 /usr/share/metasploit-framework/data/jtr/dumb32.conf
-rw-r--r-- 1 root root 54755 May  7 14:33 /usr/share/metasploit-framework/data/jtr/repeats16.conf
-rw-r--r-- 1 root root 22635 May  7 14:33 /usr/share/metasploit-framework/data/jtr/korelogic.conf
-rwxr-xr-x 1 root root 108534 May  7 14:33 /usr/share/metasploit-framework/data/jtr/john.conf
-rw-r--r-- 1 root root 55285 May  7 14:33 /usr/share/metasploit-framework/data/jtr/dumb16.conf
-rw-r--r-- 1 root root 21254 May  2 11:59 /usr/share/doc/sqlmap/examples/sqlmap.conf
-rw-r--r-- 1 root root 25086 Mar  4 22:04 /etc/dnsmasq.conf
-rw-r--r-- 1 root root 21254 May  2 11:59 /etc/sqlmap/sqlmap.conf
```

Essas são algumas opções do comando **find**

| **Opção**             | **Descrição**                                                                                                                                                                                                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-type f`             | Assim, definimos o tipo do objeto pesquisado. Neste caso, ' `f`' significa ' `file`'.                                                                                                                                                                                                  |
| `-name *.conf`        | Com ' `-name`', indicamos o nome do arquivo que procuramos. O asterisco ( `*`) significa 'todos' os arquivos com a extensão `.conf` ''.                                                                                                                                                |
| `-user root`          | Esta opção filtra todos os arquivos cujo proprietário é o usuário root.                                                                                                                                                                                                                |
| `-size +20k`          | Podemos então filtrar todos os arquivos localizados e especificar que queremos ver apenas os arquivos maiores que 20 KiB.                                                                                                                                                              |
| `-newermt 2020-03-03` | Com esta opção, definimos a data. Somente arquivos mais recentes que a data especificada serão apresentados.                                                                                                                                                                           |
| `-exec ls -al {} \;`  | Esta opção executa o comando especificado, usando chaves como espaços reservados para cada resultado. A barra invertida evita que o próximo caractere seja interpretado pelo shell porque, caso contrário, o ponto e vírgula encerraria o comando e não alcançaria o redirecionamento. |
| `2>/dev/null`         | Este é um redirecionamento `STDERR` para o ' `null device`', ao qual voltaremos na próxima seção. Este redirecionamento garante que nenhum erro seja exibido no terminal. Este redirecionamento não deve ser uma opção do comando ‘find’.                                              |






























