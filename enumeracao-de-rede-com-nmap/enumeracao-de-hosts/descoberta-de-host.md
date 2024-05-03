# Ddescoberta de host

Quando precisamos realizar um teste de penetração interno para toda a rede de uma empresa, por exemplo, então devemos, antes de mais nada, ter uma visão geral de quais sistemas estão online com os quais podemos trabalhar. Para descobrir ativamente esses sistemas na rede, podemos usar várias opções do **Nmap** de descoberta de host. Existem muitas opções do **Nmap** para determinar se nosso alvo está vivo ou não. O método de descoberta de host mais eficaz é usar solicitações de eco ICMP , que examinaremos.

É sempre recomendado armazenar cada digitalização. Posteriormente, isso pode ser usado para comparação, documentação e relatórios. Afinal, ferramentas diferentes podem produzir resultados diferentes. Portanto, pode ser benéfico distinguir qual ferramenta produz quais resultados.



```bash
$ sudo nmap 10.129.2.0/24 -sn -oA tnet | grep for | cut -d" " -f5

10.129.2.4
10.129.2.10
10.129.2.11
10.129.2.18
10.129.2.19
10.129.2.20
10.129.2.28
```

| Opções de digitação | Descrição                                                                |
| ------------------- | ------------------------------------------------------------------------ |
| 10.129.2.0/24       | Intervalo de rede alvo                                                   |
| -sn                 | Desativa a verificação de rotas                                          |
| oA tnet             | Armazena os resultados em todos os formatos começando com o nome 'tnet'. |

Este método de verificação funciona apenas se os firewalls dos hosts permitirem. Caso contrário, podemos usar outras técnicas de varredura para descobrir se os hosts estão ativos ou não. Examinaremos essas técnicas mais de perto em " **Firewall and IDS Evasion**".

## Digitalizar lista de IP

Durante um teste de penetração interno, não é incomum recebermos uma lista de IPs com os hosts que precisamos testar. Nmap também nos dá a opção de trabalhar com listas e ler os hosts dessa lista em vez de defini-los ou digitá-los manualmente.
    

```bash
$ cat hosts.lst

10.129.2.4
10.129.2.10
10.129.2.11
10.129.2.18
10.129.2.19
10.129.2.20
10.129.2.28
```

Se usarmos a mesma técnica de varredura na lista predefinida, o comando ficará assim:



```bash
$ sudo nmap -sn -oA tnet -iL hosts.lst | grep for | cut -d" " -f5

10.129.2.18
10.129.2.19
10.129.2.20
```

| Opções de digitalização | Descrição                                                                |
| ----------------------- | ------------------------------------------------------------------------ |
| -sn                     | Desativa a verificação de portas                                         |
| -oA tnet                | Armazena os resultados em todos os formatos começando com o nome 'tnet'. |
| -iL                     | Executa varreduras definidas em alvos na lista 'hosts.lst' fornecida.    |

Neste exemplo, vemos que apenas 3 dos 7 hosts que estão ativos. Lembre-se, isso pode significar que os outros hosts ignoram as **solicitações de eco ICMP** padrão devido às suas configurações de firewall. Como Nmap não recebe resposta, marca esses hosts como inativos.

## Digitalize vários IPs

Também pode acontecer que precisemos apenas digitalizar uma pequena parte de uma rede. Uma alternativa ao método que usamos da última vez é especificar vários endereços IP.



```bash
$ sudo nmap -sn -oA tnet 10.129.2.18 10.129.2.19 10.129.2.20 | grep for | cut -d" " -f5

10.129.2.18
10.129.2.19
10.129.2.20
```

Se esses endereços IP estiverem próximos um do outro, também podemos definir o intervalo no respectivo octeto.



    $ sudo nmap -sn -oA tnet 10.129.2.18-20| grep for | cut -d" " -f5
    
    10.129.2.18
    10.129.2.19
    10.129.2.20

## Digitalizar IP único

Antes de verificarmos um único host em busca de portas abertas e seus serviços, primeiro precisamos determinar se ele está ativo ou não. Para isso, podemos usar o mesmo método de antes.
    $ sudo nmap 10.129.2.18 -sn -oA host

    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-14 23:59 CEST
    Nmap scan report for 10.129.2.18
    Host is up (0.087s latency).
    MAC Address: DE:AD:00:00:BE:EF
    Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds

| Opções de digitalização | Descrição                                                               |
| ----------------------- | ----------------------------------------------------------------------- |
| 10.129.2.18             | Executa varreduras definidas no destino.                                |
| -sn                     | Desativa a verificação de portas.                                       |
| -oA host                | Armazena os resultados em todos os formatos começando com o nome 'host' |

Se desabilitarmos a varredura de porta ( **-sn**), o Nmap fará ping automaticamente na varredura com ICMP Echo Requests( **-PE**). Depois que tal solicitação é enviada, geralmente esperamos uma mensagem ICMP replyse o host que executa o ping estiver ativo. O fato mais interessante é que nossas varreduras anteriores não fizeram isso porque antes que o Nmap pudesse enviar uma solicitação de eco ICMP, enviaria um ping ARP resultando em uma resposta ARP. Podemos confirmar isso com a opção **--packet-trace**. Para garantir que as solicitações de eco ICMP sejam enviadas, também definimos a opção (**-PE**) para isso.
    $ sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace

    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 00:08 CEST
    SENT (0.0074s) ARP who-has 10.129.2.18 tell 10.10.14.2
    RCVD (0.0309s) ARP reply 10.129.2.18 is-at DE:AD:00:00:BE:EF
    Nmap scan report for 10.129.2.18
    Host is up (0.023s latency).
    MAC Address: DE:AD:00:00:BE:EF
    Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds

| Opções de digitalização | Descrição                                                                   |
| ----------------------- | --------------------------------------------------------------------------- |
| 10.129.2.18             | Executa varreduras definidas no destino.                                    |
| -sn                     | Desativa a verificação de portas.                                           |
| -oA host                | Armazena os resultados em todos os formatos começando com o nome 'host'.    |
| -PE                     | Executa a verificação de ping usando 'solicitações de eco ICMP' no destino. |
| --packet-trace          | Mostra todos os pacotes enviados e recebidos                                |

Outra maneira de determinar por que o Nmap tem nosso alvo marcado como “vivo” é com a opção **--reason**.



    $ sudo nmap 10.129.2.18 -sn -oA host -PE --reason
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 00:10 CEST
    SENT (0.0074s) ARP who-has 10.129.2.18 tell 10.10.14.1
    RCVD (0.0309s) ARP reply 10.129.2.18 is-at DE:AD:00:00:BE:EF
    Nmap scan report for 10.129.2.18
    Host is up, received arp-response (0.028s latency).
    MAC Address: DE:AD:00:00:BE:EF
    Nmap done: 1 IP address (1 host up) scanned in 0.03 seconds

| Opções de digitalização | Descrição                                                                   |
| ----------------------- | --------------------------------------------------------------------------- |
| 10.129.2.18             | Executa varreduras definidas no destino.                                    |
| -sn                     | Desativa a verificação de portas.                                           |
| -oA host                | Armazena os resultados em todos os formatos começando com o nome 'host'.    |
| -PE                     | Executa a verificação de ping usando 'solicitações de eco ICMP' no destino. |
| --reason                | Exibe o motivo do resultado específico.                                     |

Vemos aqui que Nmap de fato detecta se o hospedeiro está vivo ou não através da solicitação ARP e requisição ARP somente. Para desabilitar solicitações ARP e escanear nosso alvo com o desejado ICMP echo requests, podemos desabilitar pings ARP configurando a opção **--disable-arp-ping**. Então podemos escanear nosso alvo novamente e observar os pacotes enviados e recebidos.



    $ sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace --disable-arp-ping
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 00:12 CEST
    SENT (0.0107s) ICMP [10.10.14.2 > 10.129.2.18 Echo request (type=8/code=0) id=13607 seq=0] IP [ttl=255 id=23541 iplen=28 ]
    RCVD (0.0152s) ICMP [10.129.2.18 > 10.10.14.2 Echo reply (type=0/code=0) id=13607 seq=0] IP [ttl=128 id=40622 iplen=28 ]
    Nmap scan report for 10.129.2.18
    Host is up (0.086s latency).
    MAC Address: DE:AD:00:00:BE:EF
    Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds

Já mencionamos no " Learning Process," e no início deste módulo é fundamental estar atento aos detalhes. Um **ICMP echo request** pode nos ajudar a determinar se nosso alvo está vivo e identificar seu sistema. Mais estratégias sobre descoberta de host podem ser encontradas em:
