# Varredura de hosts e portas0

É fundamental compreender como funciona a ferramenta que utilizamos e como ela desempenha e processa as diferentes funções. Só compreenderemos os resultados se soubermos o que significam e como são obtidos. Portanto, examinaremos mais de perto e analisaremos alguns dos métodos de digitalização. Depois de descobrirmos que nosso alvo está vivo, queremos obter uma imagem mais precisa do sistema. As informações que precisamos incluem:

- Portas abertas e seus serviços
- Versões de serviços
- Informações dos serviços prestados
- Sistema operacional

Há um total de 6 estados diferentes para uma porta digitalizada que podemos obter:

| Estado             | Descrição                                                                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open               | Isto indica que a conexão com a porta verificada foi estabelecida. Essas conexões podem ser conexões TCP , datagramas UDP e também associações SCTP .                                                                       |
| closed             | Quando a porta é mostrada como fechada, o protocolo TCP indica que o pacote que recebemos de volta contém um RSTsinalizador. Este método de varredura também pode ser usado para determinar se nosso alvo está vivo ou não. |
| filtered           | O Nmap não consegue identificar corretamente se a porta varrida está aberta ou fechada porque nenhuma resposta é retornada do alvo para a porta ou recebemos um código de erro do alvo.                                     |
| unfiltered         | Este estado de uma porta ocorre apenas durante a varredura TCP-ACK e significa que a porta está acessível, mas não pode ser determinado se está aberta ou fechada.                                                          |
| open \| filtered   | Se não obtivermos uma resposta para uma porta específica, Nmapiremos configurá-la para esse estado. Isto indica que um firewall ou filtro de pacotes pode proteger a porta.                                                 |
| closed \| filtered | Este estado ocorre apenas nas varreduras ociosas do IP ID e indica que foi impossível determinar se a porta varrida está fechada ou filtrada por um firewall.                                                               |

## Descobrimos órtas TCP abertas

Por padrão, **Nmap** verifica as 1.000 principais portas TCP com a varredura SYN ( **-sS**). Esta varredura SYN é definida apenas como padrão quando a executamos como root devido às permissões de soquete necessárias para criar pacotes TCP brutos. Caso contrário, a varredura TCP ( **-sT**) será executada por padrão. Isso significa que se não definirmos portas e métodos de varredura, esses parâmetros serão definidos automaticamente.Podemos definir as portas uma por uma ( **-p 22,25,80,139,445**), por intervalo ( **-p 22-445**), pelas portas principais ( **--top-ports=10**) do banco de dados do Nmap que foram assinados como mais frequentes, verificando todas as portas ( **-p-**), mas também definindo uma verificação rápida de portas, que contém as 100 portas principais ( **-F**).

### Verificando as 10 principais portas TCP

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 --top-ports=10
    
    Starting Nmap 7.80 ( https://nmap.org )  at 2020-06-15 15:36 CEST
    Nmap scan report for 10.129.2.28
    Host is up (0.021s latency).
    
    PORT     STATE    SERVICE
    21/tcp   closed   ftp
    22/tcp   open     ssh
    23/tcp   closed   telnet
    25/tcp   open     smtp
    80/tcp   open     http
    110/tcp  open     pop3
    139/tcp  filtered netbios-ssn
    443/tcp  closed   https
    445/tcp  filtered microsoft-ds
    3389/tcp closed   ms-wbt-server
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
    
    Nmap done: 1 IP address (1 host up) scanned in 1.44 seconds

| Opções de digitalização | Descrição                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------- |
| 10.129.2.28             | Verifica o destino especificado.                                                      |
| --top-ports=10          | Verifica as principais portas especificadas que foram definidas como mais frequentes. |

### Nmap - rastreie os pacotes

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p 21 --packet-trace -Pn -n --disable-arp-ping
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:39 CEST
    SENT (0.0429s) TCP 10.10.14.2:63090 > 10.129.2.28:21 S ttl=56 id=57322 iplen=44  seq=1699105818 win=1024 <mss 1460>
    RCVD (0.0573s) TCP 10.129.2.28:21 > 10.10.14.2:63090 RA ttl=64 id=0 iplen=40  seq=0 win=0
    Nmap scan report for 10.11.1.28
    Host is up (0.014s latency).
    
    PORT   STATE  SERVICE
    21/tcp closed ftp
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
    
    Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds

| Opções de digitalização | Descrição                                     |
| ----------------------- | --------------------------------------------- |
| 10.129.2.28             | Verifica o destino especificado.              |
| -p 21                   | Verifica apenas a porta especificada.         |
| --packet-trace          | Mostra todos os pacotes enviados e recebidos. |
| -n                      | Desativa a resolução DNS.                     |
| --disable-arp-ping      | Desativa o ping ARP.                          |

Podemos ver na linha SENT que nós( 10.10.14.2) enviamos um pacote TCP com a flag SYN ( S) para nosso destino ( 10.129.2.28). Na próxima linha do RCVD, podemos ver que o alvo responde com um pacote TCP contendo os sinalizadores RST e ACK( RA). Sinalizadores RST e ACK são usados para confirmar o recebimento do pacote TCP ( ACK) e para encerrar a sessão TCP ( RST).

### Request

| Mensagem                                                  | Descrição                                                                                                |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| SENT (0.0429s)                                            | Indica a operação SENT do Nmap, que envia um pacote ao destino.                                          |
| TCP                                                       | Mostra o protocolo que está sendo usado para interagir com a porta de destino.                           |
| 10.10.14.2:63090 >                                        | Representa nosso endereço IPv4 e a porta de origem, que será utilizada pelo Nmap para enviar os pacotes. |
| 10.129.2.28:21                                            | Mostra o endereço IPv4 de destino e a porta de destino.                                                  |
| S                                                         | Sinalizador SYN do pacote TCP enviado.                                                                   |
| ttl=56 id=57322 iplen=44 seq=1699105818 win=1024 mss 1460 | Parâmetros adicionais do cabeçalho TCP.                                                                  |

### Response

| Mensagem                         | Descrição                                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------- |
| RCVD (0.0573s)                   | Indica um pacote recebido do destino.                                                     |
| TCP                              | Mostra o protocolo que está sendo usado.                                                  |
| 10.129.2.28:21 >                 | Representa o endereço IPv4 de destino e a porta de origem, que será usada para responder. |
| 10.10.14.2:63090                 | Mostra nosso endereço IPv4 e a porta que será respondida.                                 |
| RA                               | Flags RST e ACK do pacote TCP enviado.                                                    |
| ttl=64 id=0 iplen=40 seq=0 win=0 | Parâmetros adicionais do cabeçalho TCP.                                                   |

### Conectar digitalização

O Nmap TCP Connect Scan ( -sT) usa o handshake TCP de três vias para determinar se uma porta específica em um host de destino está aberta ou fechada. A varredura envia um pacote SYN para a porta de destino e aguarda uma resposta. É considerada aberta se a porta alvo responder com um pacote SYN-ACK e fechada se responder com um pacote RST.

A varredura **Connect** é útil porque é a maneira mais precisa de determinar o estado de uma porta e também a mais furtiva. Ao contrário de outros tipos de varredura, como a varredura SYN, a varredura Connect não deixa conexões inacabadas ou pacotes não enviados no host de destino, o que torna menos provável que seja detectado por sistemas de detecção de intrusões (IDS) ou sistemas de prevenção de intrusões (IPS). ). É útil quando queremos mapear a rede e não queremos perturbar os serviços executados por trás dela, causando assim um impacto mínimo e às vezes considerado um método de varredura mais educado.

Também é útil quando o host de destino possui um firewall pessoal que descarta pacotes recebidos, mas permite pacotes enviados. Nesse caso, uma varredura do Connect pode contornar o firewall e determinar com precisão o estado das portas de destino. No entanto, é importante observar que a varredura do Connect é mais lenta do que outros tipos de varredura porque exige que o scanner espere por uma resposta do destino após cada pacote enviado, o que pode levar algum tempo se o alvo estiver ocupado ou sem resposta.

### Conectar digitalização na porta TCP 443

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p 443 --packet-trace --disable-arp-ping -Pn -n --reason -sT
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 16:26 CET
    CONN (0.0385s) TCP localhost > 10.129.2.28:443 => Operation now in progress
    CONN (0.0396s) TCP localhost > 10.129.2.28:443 => Connected
    Nmap scan report for 10.129.2.28
    Host is up, received user-set (0.013s latency).
    
    PORT    STATE SERVICE REASON
    443/tcp open  https   syn-ack
    
    Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds

## Portas filtradas

Quando uma porta é mostrada como filtrada, pode haver vários motivos. Na maioria dos casos, os firewalls possuem certas regras definidas para lidar com conexões específicas. Os pacotes podem ser dropped, ou rejected. Quando um pacote é descartado, o Nmap não recebe resposta de nosso destino e, por padrão, a taxa de novas tentativas ( --max-retries) é definida como 1. Isso significa que o Nmap reenviará a solicitação para a porta de destino para determinar se o pacote anterior não foi acidentalmente maltratado.

Vejamos um exemplo onde o firewall descarta os pacotes TCP enviados para varredura de portas. Portanto verificamos a porta TCP 139 , que já foi mostrada como filtrada. Para poder rastrear como nossos pacotes enviados são tratados, desativamos as solicitações de eco ICMP ( -Pn), a resolução DNS ( -n) e a varredura de ping ARP ( --disable-arp-ping) novamente.


    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p 139 --packet-trace -n --disable-arp-ping -Pn

    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:45 CEST
    SENT (0.0381s) TCP 10.10.14.2:60277 > 10.129.2.28:139 S ttl=47 id=14523 iplen=44  seq=4175236769 win=1024 <mss 1460>
    SENT (1.0411s) TCP 10.10.14.2:60278 > 10.129.2.28:139 S ttl=45 id=7372 iplen=44  seq=4175171232 win=1024 <mss 1460>
    Nmap scan report for 10.129.2.28
    Host is up.
    PORT    STATE    SERVICE
    139/tcp filtered netbios-ssn
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

    Nmap done: 1 IP address (1 host up) scanned in 2.06 seconds

| Opções de digitalização | Descrição                                     |
| ----------------------- | --------------------------------------------- |
| 10.129.2.28             | Verifica o destino especificado.              |
| -p 139                  | Verifica apenas a porta especificada.         |
| --packet-trace          | Mostra todos os pacotes enviados e recebidos. |
| -n                      | Desativa a resolução DNS.                     |
| --disable-arp-ping      | Desativa o ping ARP.                          |
| -Pn                     | Desativa solicitações de eco ICMP.            |

Vemos na última varredura que Nmapenviou dois pacotes TCP com o flag SYN. Pela duração ( 2.06s) da varredura, podemos reconhecer que ela demorou muito mais que as anteriores ( ~0.05s). O caso é diferente se o firewall rejeitar os pacotes. Para isso, olhamos para a porta TCP 445, que é tratada de acordo com essa regra do firewall.
    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p 445 --packet-trace -n --disable-arp-ping -Pn

    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:55 CEST
    SENT (0.0388s) TCP 10.129.2.28:52472 > 10.129.2.28:445 S ttl=49 id=21763 iplen=44  seq=1418633433 win=1024 <mss 1460>
    RCVD (0.0487s) ICMP [10.129.2.28 > 10.129.2.28 Port 445 unreachable (type=3/code=3) ] IP [ttl=64 id=20998 iplen=72 ]
    Nmap scan report for 10.129.2.28
    Host is up (0.0099s latency).
    PORT    STATE    SERVICE
    445/tcp filtered microsoft-ds
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

    Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds

Como resposta, recebemos uma resposta ICMP com type 3 e error code 3, que indica que a porta desejada está inacessível. No entanto, se soubermos que o host está ativo, podemos assumir fortemente que o firewall nesta porta está rejeitando os pacotes, e teremos que examinar esta porta mais de perto mais tarde

## Descobrindo portas UDP abertas

Alguns administradores de sistema ás vezes esquecem de filtrar as portas UDP além das portas TCP. Uma vez que UDP é um **stateless protocol** e não requer um handshake de 3 vias como o TCP.Não recebemos nenhum reconhecimento. Conseqüentemente, o tempo limite é muito maior, tornando o conjunto UDP scan( -sU) muito mais lento que o TCP scan( -sS).

Vejamos um exemplo de como pode ser uma varredura UDP ( -sU) e quais resultados ela nos fornece.

### Varredura de porta UDP

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -F -sU
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 16:01 CEST
    Nmap scan report for 10.129.2.28
    Host is up (0.059s latency).
    Not shown: 95 closed ports
    PORT     STATE         SERVICE
    68/udp   open|filtered dhcpc
    137/udp  open          netbios-ns
    138/udp  open|filtered netbios-dgm
    631/udp  open|filtered ipp
    5353/udp open          zeroconf
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
    
    Nmap done: 1 IP address (1 host up) scanned in 98.07 seconds

| Opções de digitalização                 | Descrição                          |
| --------------------------------------- | ---------------------------------- |
| 10.129.2.28 | Verifica o destino especificado.   |
| -F                                      | Verifica as 100 principais portas. |
| -sU                                     | Executa uma varredura UDP.         |

Outra desvantagem disso é que muitas vezes não obtemos resposta porque Nmap envia datagramas vazios para as portas UDP verificadas e não recebemos nenhuma resposta. Portanto, não podemos determinar se o pacote UDP chegou ou não. Se a porta UDP for open, só obteremos uma resposta se a aplicação estiver configurada para isso.
    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -sU -Pn -n --disable-arp-ping --packet-trace -p 137 --reason

    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 16:15 CEST
    SENT (0.0367s) UDP 10.10.14.2:55478 > 10.129.2.28:137 ttl=57 id=9122 iplen=78
    RCVD (0.0398s) UDP 10.129.2.28:137 > 10.10.14.2:55478 ttl=64 id=13222 iplen=257
    Nmap scan report for 10.129.2.28
    Host is up, received user-set (0.0031s latency).
    PORT    STATE SERVICE    REASON
    137/udp open  netbios-ns udp-response ttl 64
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

    Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds

| Opções de digitalização | Descrição                                                        |
| ----------------------- | ---------------------------------------------------------------- |
| 10.129.2.28             | Verifica o destino especificado.                                 |
| -sU                     | Executa uma varredura UDP.                                       |
| -Pn                     | Desativa solicitações de eco ICMP.                               |
| -n                      | Desativa a resolução DNS.                                        |
| --disable-arp-ping      | Desativa o ping ARP.                                             |
| --packet-trace          | Mostra todos os pacotes enviados e recebidos.                    |
| -p 137                  | Verifica apenas a porta especificada.                            |
| --reason                | Exibe o motivo pelo qual uma porta está em um estado específico. |

Se obtivermos uma resposta ICMP com error code 3(porta inacessível), saberemos que a porta é de fato closed.


    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -sU -Pn -n --disable-arp-ping --packet-trace -p 100 --reason

    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 16:25 CEST
    SENT (0.0445s) UDP 10.10.14.2:63825 > 10.129.2.28:100 ttl=57 id=29925 iplen=28
    RCVD (0.1498s) ICMP [10.129.2.28 > 10.10.14.2 Port unreachable (type=3/code=3) ] IP [ttl=64 id=11903 iplen=56 ]
    Nmap scan report for 10.129.2.28
    Host is up, received user-set (0.11s latency).

    PORT    STATE  SERVICE REASON
    100/udp closed unknown port-unreach ttl 64
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

    Nmap done: 1 IP address (1 host up) scanned in  0.15 seconds



Para todas as outras respostas ICMP, as portas verificadas são marcadas como ( open|filtered).


    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -sU -Pn -n --disable-arp-ping --packet-trace -p 138 --

    reasonStarting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 16:32 CEST
    SENT (0.0380s) UDP 10.10.14.2:52341 > 10.129.2.28:138 ttl=50 id=65159 iplen=28
    SENT (1.0392s) UDP 10.10.14.2:52342 > 10.129.2.28:138 ttl=40 id=24444 iplen=28
    Nmap scan report for 10.129.2.28
    Host is up, received user-set.
    PORT    STATE         SERVICE     REASON
    138/udp open|filtered netbios-dgm no-response
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

    Nmap done: 1 IP address (1 host up) scanned in 2.06 seconds



Outro método útil para verificar portas é a opção **-sV** usada para obter informações adicionais disponíveis nas portas abertas. Este método pode identificar versões, nomes de serviços e detalhes sobre nosso alvo.



## Verificação de versão


    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -Pn -n --disable-arp-ping --packet-trace -p 445 --reason  -sV

    Starting Nmap 7.80 ( https://nmap.org ) at 2022-11-04 11:10 GMT
    SENT (0.3426s) TCP 10.10.14.2:44641 > 10.129.2.28:445 S ttl=55 id=43401 iplen=44  seq=3589068008 win=1024 <mss 1460>
    RCVD (0.3556s) TCP 10.129.2.28:445 > 10.10.14.2:44641 SA ttl=63 id=0 iplen=44  seq=2881527699 win=29200 <mss 1337>
    NSOCK INFO [0.4980s] nsock_iod_new2(): nsock_iod_new (IOD #1)
    NSOCK INFO [0.4980s] nsock_connect_tcp(): TCP connection requested to 10.129.2.28:445 (IOD #1) EID 8
    NSOCK INFO [0.5130s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [10.129.2.28:445]
    Service scan sending probe NULL to 10.129.2.28:445 (tcp)
    NSOCK INFO [0.5130s] nsock_read(): Read request from IOD #1 [10.129.2.28:445] (timeout: 6000ms) EID 18
    NSOCK INFO [6.5190s] nsock_trace_handler_callback(): Callback: READ TIMEOUT for EID 18 [10.129.2.28:445]
    Service scan sending probe SMBProgNeg to 10.129.2.28:445 (tcp)
    NSOCK INFO [6.5190s] nsock_write(): Write request for 168 bytes to IOD #1 EID 27 [10.129.2.28:445]
    NSOCK INFO [6.5190s] nsock_read(): Read request from IOD #1 [10.129.2.28:445] (timeout: 5000ms) EID 34
    NSOCK INFO [6.5190s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 27 [10.129.2.28:445]
    NSOCK INFO [6.5320s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 34 [10.129.2.28:445] (135 bytes)
    Service scan match (Probe SMBProgNeg matched with SMBProgNeg line 13836): 10.129.2.28:445 is netbios-ssn.  Version: |Samba smbd|3.X - 4.X|workgroup: WORKGROUP|
    NSOCK INFO [6.5320s] nsock_iod_delete(): nsock_iod_delete (IOD #1)
    Nmap scan report for 10.129.2.28
    Host is up, received user-set (0.013s latency).

    PORT    STATE SERVICE     REASON         VERSION
    445/tcp open  netbios-ssn syn-ack ttl 63 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    Service Info: Host: Ubuntu

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 6.55 seconds

| Opções de digitalização | Descrição                           |
| ----------------------- | ----------------------------------- |
| -sV                     | Executa uma verificação de serviço. |
