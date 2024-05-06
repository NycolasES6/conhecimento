# Enumeração de serviço

Para nós, é essencial determinar a aplicação e a sua versão com a maior precisão possível. Podemos usar essas informações para procurar vulnerabilidades conhecidas e analisar o código-fonte dessa versão, se a encontrarmos. Um número de versão exato nos permite procurar uma exploração mais precisa que se adapte ao serviço e ao sistema operacional do nosso alvo.

## Detecção de versão de serviço

Recomenda-se realizar primeiro uma varredura rápida de portas, o que nos dá uma pequena visão geral das portas disponíveis. Isto provoca significativamente menos tráfego, o que é vantajoso para nós, pois caso contrário podemos ser descobertos e bloqueados pelos mecanismos de segurança. Podemos lidar com isso primeiro e executar uma varredura de portas em segundo plano, que mostra todas as portas abertas ( -p-). Podemos usar a verificação de versão para verificar portas específicas em busca de serviços e suas versões ( -sV).

Uma verificação completa da porta leva muito tempo. Para visualizar o status da verificação, podemos pressionar [Space Bar]durante a verificação, o que Nmapnos mostrará o status da verificação.



```bash
NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p- -sV

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 19:44 CEST
[Space Bar]
Stats: 0:00:03 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 3.64% done; ETC: 19:45 (0:00:53 remaining)
```



- 10.129.2.28 -- Verifica o destino especificado.
- -p- -- Verifica todas as portas.
- -sV -- Executa a detecção de versão de serviço em portas especificadas.
  
  

Outra opção ( --stats-every=5s) que podemos utilizar é definir por quantos períodos o status deve ser mostrado. Aqui podemos especificar o número de segundos ( s) ou minutos ( m), após os quais queremos obter o status.

Também podemos aumentar o verbosity level( -v/ -vv).

- -v -- Aumenta o detalhamento da verificação, que exibe informações mais detalhadas.

## Banner Grabbing

Assim que a varredura for concluída, veremos todas as portas TCP com o serviço correspondente e suas versões que estão ativas no sistema.

Principalmente, o Nmap olha os banners das portas digitalizadas e os imprime. Se não conseguir identificar as versões através dos banners, o Nmap tenta identificá-las através de um sistema de correspondência baseado em assinaturas, mas isto aumenta significativamente a duração da verificação. Uma desvantagem dos resultados do Nmap apresentados é que a verificação automática pode perder algumas informações porque às vezes o Nmap não sabe como lidar com elas. Vejamos um exemplo disso.



    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p- -sV -Pn -n --disable-arp-ping --packet-trace
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-16 20:10 CEST
    <SNIP>
    NSOCK INFO [0.4200s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [10.129.2.28:25] (35 bytes): 220 inlane ESMTP Postfix (Ubuntu)..
    Service scan match (Probe NULL matched with NULL line 3104): 10.129.2.28:25 is smtp.  Version: |Postfix smtpd|||
    NSOCK INFO [0.4200s] nsock_iod_delete(): nsock_iod_delete (IOD #1)
    Nmap scan report for 10.129.2.28
    Host is up (0.076s latency).
    PORT   STATE SERVICE VERSION
    25/tcp open  smtp    Postfix smtpd
    MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
    Service Info: Host:  inlane
    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    
    Nmap done: 1 IP address (1 host up) scanned in 0.47 seconds



- -Pn -- Desativa solicitações de eco ICMP.
- --disable-arp-ping -- Desativa o ping ARP.
- --packet-trace -- Mostra todos os pacotes enviados e recebidos.
  
  

Se observarmos os resultados de Nmap, podemos ver o status da porta, o nome do serviço e o nome do host. No entanto, vejamos esta linha aqui:

- NSOCK INFO [0.4200s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [10.129.2.28:25] (35 bytes): 220 inlane ESMTP Postfix (Ubuntu)..

Então vemos que o servidor SMTP em nosso destino nos forneceu mais informações do que Nmapnos mostrou. Porque aqui vemos que é a distribuição Linux Ubuntu. Isso acontece porque, após um handshake triplo bem-sucedido, o servidor geralmente envia um banner para identificação. Isso serve para que o cliente saiba com qual serviço está trabalhando. No nível da rede, isso acontece com um sinalizador PSH no cabeçalho TCP. No entanto, pode acontecer que alguns serviços não forneçam imediatamente tais informações. Também é possível remover ou manipular os banners dos respectivos serviços. Se nos conectarmos manualmente ao servidor SMTP usando nc, pegarmos o banner e interceptarmos o tráfego da rede usando tcpdump, poderemos ver o queo Nmap não nos mostrou.

### tcpdump

    NycolasES6@htb[/htb]$ sudo tcpdump -i eth0 host 10.10.14.2 and 10.129.2.28
    
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

### Nc

    NycolasES6@htb[/htb]$  nc -nv 10.129.2.28 25
    
    Connection to 10.129.2.28 port 25 [tcp/*] succeeded!
    220 inlane ESMTP Postfix (Ubuntu)

### TcDump - Tráfego Detectado

    18:28:07.128564 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [S], seq 1798872233, win 65535, options [mss 1460,nop,wscale 6,nop,nop,TS val 331260178 ecr 0,sackOK,eol], length 0
    18:28:07.255151 IP 10.129.2.28.smtp > 10.10.14.2.59618: Flags [S.], seq 1130574379, ack 1798872234, win 65160, options [mss 1460,sackOK,TS val 1800383922 ecr 331260178,nop,wscale 7], length 0
    18:28:07.255281 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [.], ack 1, win 2058, options [nop,nop,TS val 331260304 ecr 1800383922], length 0
    18:28:07.319306 IP 10.129.2.28.smtp > 10.10.14.2.59618: Flags [P.], seq 1:36, ack 1, win 510, options [nop,nop,TS val 1800383985 ecr 331260304], length 35: SMTP: 220 inlane ESMTP Postfix (Ubuntu)
    18:28:07.319426 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [.], ack 36, win 2058, options [nop,nop,TS val 331260368 ecr 1800383985], length 0

As três primeiras linhas nos mostram o aperto de mão triplo.

1. - [SYN]    18:28:07.128564 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [S], <SNIP>
2. - [SYN-ACK]    18:28:07.255151 IP 10.129.2.28.smtp > 10.10.14.2.59618: Flags [S.], <SNIP>
3. - [ACK]    18:28:07.255281 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [.], <SNIP>

Depois disso, o servidor SMTP de destino nos envia um pacote TCP com os sinalizadores PSH e ACK, onde o PSH informa que o servidor de destino está enviando dados para nós e com o ACK nos informa simultaneamente que todos os dados necessários foram enviados.

4. - [PSH-ACK]    18:28:07.319306 IP 10.129.2.28.smtp > 10.10.14.2.59618: Flags [P.], <SNIP>

O último pacote TCP que enviamos confirma o recebimento dos dados com uma extensão ACK.

5. - [ACK]    18:28:07.319426 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [.], <SNIP>




























