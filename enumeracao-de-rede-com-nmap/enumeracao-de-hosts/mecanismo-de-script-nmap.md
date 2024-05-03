# Mecanismo de script Nmap

O Nmap Scripting Engine ( NSE) é outro recurso útil do Nmap. Ele nos oferece a possibilidade de criar scripts em Lua para interação com determinados serviços. Há um total de 14 categorias nas quais esses scripts podem ser divididos:

| Categoria | Descrição                                                                                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auth      | Determinação de credenciais de autenticação.                                                                                                              |
| broadcast | Os scripts, que são usados para descoberta de host por transmissão e os hosts descobertos, podem ser adicionados automaticamente às varreduras restantes. |
| brute     | Executa scripts que tentam fazer login no respectivo serviço por força bruta com credenciais.                                                             |
| default   | Scripts padrão executados usando a opção -sC .                                                                                                            |
| discovery | Avaliação de serviços acessíveis.                                                                                                                         |
| dos       | Esses scripts são usados para verificar serviços em busca de vulnerabilidades de negação de serviço e são menos usados, pois prejudicam os serviços.      |
| exploit   | Esta categoria de scripts tenta explorar vulnerabilidades conhecidas na porta verificada.                                                                 |
| external  | Scripts que usam serviços externos para processamento adicional.                                                                                          |
| fuzzer    | Isso usa scripts para identificar vulnerabilidades e manipulação inesperada de pacotes, enviando diferentes campos, o que pode levar muito tempo.         |
| intrusive | Scripts intrusivos que podem afetar negativamente o sistema de destino.                                                                                   |
| malware   | Verifica se algum malware infecta o sistema de destino.                                                                                                   |
| safe      | Scripts defensivos que não realizam acessos intrusivos e destrutivos.                                                                                     |
| version   | Extensão para detecção de serviço.                                                                                                                        |
| vuln      | Identificação de vulnerabilidades específicas.                                                                                                            |

Temos diversas maneiras de definir os scripts desejados em Nmap.

### Scripts padrão

    NycolasES6@htb[/htb]$ sudo nmap <target> -sC

### Categoria de scripts específicos

    NycolasES6@htb[/htb]$ sudo nmap <target> --script <category>

### Scripts definidos

    NycolasES6@htb[/htb]$ sudo nmap <target> --script <script-name>,<script-name>,...

Por exemplo, vamos continuar trabalhando com a porta SMTP de destino e ver os resultados que obtemos com dois scripts definidos.

### Nmap - Especificando Scripts

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p 25 --script banner,smtp-commands
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-16 23:21 CEST
    Nmap scan report for 10.129.2.28
    Host is up (0.050s latency).
    
    PORT   STATE SERVICE
    25/tcp open  smtp
    |_banner: 220 inlane ESMTP Postfix (Ubuntu)
    |_smtp-commands: inlane, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8,
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

- **--script banner,smtp-commands** - Usa scripts NSE especificados.

Vemos que podemos reconhecer a distribuição Ubuntu do Linux usando o script 'banner'. O script smtp-commands nos mostra quais comandos podemos usar ao interagir com o servidor SMTP de destino. Neste exemplo, tais informações podem nos ajudar a descobrir os usuários existentes no alvo. Nmap também nos dá a habilidade de escanear nosso alvo com a opção agressiva ( -A). Isso verifica o destino com várias opções como detecção de serviço ( -sV), detecção de sistema operacional ( -O), traceroute ( --traceroute) e com os scripts NSE padrão ( -sC).

### Nmap - verificação agressiva

```bash
NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p 80 -A

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-17 01:38 CEST
Nmap scan report for 10.129.2.28
 Host is up (0.012s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: WordPress 5.3.4
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: blog.inlanefreight.com
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 (96%), Linux 3.2 - 4.9 (96%), Linux 2.6.32 - 3.10 (96%), Linux 3.4 - 3.10 (95%), Linux 3.1 (95%), Linux 3.2 (95%),
AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Synology DiskStation Manager 5.2-5644 (94%), Netgear RAIDiator 4.2.28 (94%),
Linux 2.6.32 - 2.6.35 (94%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

TRACEROUTE
HOP RTT      ADDRESS
1   11.91 ms 10.129.2.28

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.36 seconds
```

- -A - Executa detecção de serviço, detecção de sistema operacional, traceroute e usa scripts padrão para verificar o alvo.

Com a ajuda da opção de verificação usada ( -A), descobrimos que tipo de servidor web ( Apache 2.4.29) está sendo executado no sistema, qual aplicativo web ( WordPress 5.3.4) é usado e o título(blog.inlanefreight.com) da página web. Além disso, o Nmap mostra que é provável que o sistema operacional seja Linux( 96%).

## Avaliação de vulnerabilidade

Agora vamos passar para a porta HTTP 80 e ver quais informações e vulnerabilidades podemos encontrar usando a categoria vuln de NSE.

### Nmap - Categoria Vuln

```bash
NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p 80 -sV --script vuln

Nmap scan report for 10.129.2.28
Host is up (0.036s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-enum:
|   /wp-login.php: Possible admin folder
|   /readme.html: Wordpress version: 2
|   /: WordPress version: 5.3.4
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|_  /readme.html: Interesting, a readme.
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-wordpress-users:
| Username found: admin
|_Search stopped at ID #25. Increase the upper limit if necessary with 'http-wordpress-users.limit'
| vulners:
|   cpe:/a:apache:http_server:2.4.29:
|         CVE-2019-0211    7.2    https://vulners.com/cve/CVE-2019-0211
|         CVE-2018-1312    6.8    https://vulners.com/cve/CVE-2018-1312
|         CVE-2017-15715    6.8    https://vulners.com/cve/CVE-2017-15715
<SNIP>
```

- --script vuln - Usa todos os scripts relacionados da categoria especificada.

Os scripts usados para a última varredura interagem com o servidor web e sua aplicação web para descobrir mais informações sobre suas versões e verificar vários bancos de dados para ver se há vulnerabilidades conhecidas.






















