# Desempenho

O desempenho da verificação desempenha um papel significativo quando precisamos verificar uma rede extensa ou quando lidamos com baixa largura de banda da rede. Podemos usar várias opções para dizer Nmap quão rápido ( -T ``<0-5>``), com qual frequência ( ``--min-parallelism <number>``), quais timeouts ( ``--max-rtt-timeout <time>``) os pacotes de teste devem ter, quantos pacotes devem ser enviados simultaneamente ( ``--min-rate <number>``) e com o número de novas tentativas ( ``--max-retries <number>``) para as portas escaneadas. os alvos devem ser escaneados.

## Tempo limite

Quando o Nmap envia um pacote, leva algum tempo (Round-Trip-Time - RTT) para receber uma resposta da porta verificada. Geralmente o [[Nmap]] inicia com um timeout alto (--min-RTT-timeout) de 100ms. Vejamos um exemplo de varredura de toda a rede com 256 hosts, incluindo as 100 principais portas.

### Verificação padrão

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F

    <SNIP>
    Nmap done: 256 IP addresses (10 hosts up) scanned in 39.44 seconds

### RTT otimizado

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F --initial-rtt-timeout 50ms --max-rtt-timeout 100ms

    <SNIP>
    Nmap done: 256 IP addresses (8 hosts up) scanned in 12.29 seconds

| Opções de digitalização | Descrição|
| --- | --- |
| 10.129.2.0/24 | Verifica a rede de destino especificada.|
| -F | Verifica as 100 principais portas.|
| --initial-rtt-timeout 50ms | Define o valor de tempo especificado como tempo limite inicial do RTT.|
| --max-rtt-timeout 100ms | Define o valor de tempo especificado como tempo limite máximo de RTT.|

Ao comparar as duas varreduras, podemos ver que encontramos dois hosts a menos com a varredura otimizada, mas a varredura levou apenas um quarto do tempo. A partir disso, podemos concluir que definir o tempo limite inicial do RTT ( --initial-rtt-timeout) para um período de tempo muito curto pode fazer com que ignoremos os hosts.
## Máximo de tentativas

Outra forma de aumentar a velocidade das varreduras é especificar a taxa de novas tentativas dos pacotes enviados ( --max-retries). O valor padrão para a taxa de novas tentativas é 10, portanto, se Nmapnão receber uma resposta para uma porta, não enviará mais pacotes para a porta e será ignorado.

### Verificação padrão

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F | grep "/tcp" | wc -l

    23

### Novas tentativas reduzidas

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F --max-retries 0 | grep "/tcp" | wc -l

    21

- **--max-retries 0** - Define o número de tentativas que serão realizadas durante a verificação.

Mais uma vez, reconhecemos que a aceleração também pode ter um efeito negativo nos nossos resultados, o que significa que podemos ignorar informações importantes.

## Cotações

Durante um teste de penetração de caixa branca, podemos ser incluídos na lista de permissões dos sistemas de segurança para verificar vulnerabilidades nos sistemas da rede e não apenas testar as medidas de proteção. Se conhecermos a largura de banda da rede, podemos trabalhar com a taxa de pacotes enviados, o que acelera significativamente nossas varreduras com Nmap. Ao definir a taxa mínima ( **--min-rate <number>**) para envio de pacotes, informamos aoNmap para enviar simultaneamente o número especificado de pacotes. Ele tentará manter a taxa de acordo.

## Verificação padrão

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F -oN tnet.default

    <SNIP>
    Nmap done: 256 IP addresses (10 hosts up) scanned in 29.83 seconds

### Verificação otimizada

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F -oN tnet.minrate300 --min-rate 300

    <SNIP>
    Nmap done: 256 IP addresses (10 hosts up) scanned in 8.67 seconds

 - **-oN tnet.minrate300** - Salva os resultados em formatos normais, iniciando o nome de arquivo especificado.
 - **--min-rate 300** - Define o número mínimo de pacotes a serem enviados por segundo.

### Verificação padrão - Portas abertas encontradas

    NycolasES6@htb[/htb]$ cat tnet.default | grep "/tcp" | wc -l

    23

### Varredura otimizada - Portas abertas otimizadas

    NycolasES6@htb[/htb]$ cat tnet.minrate300 | grep "/tcp" | wc -l

    23

## Tempo

Como essas configurações nem sempre podem ser otimizadas manualmente, como em um teste de penetração de caixa preta, o Nmap oferece seis modelos de temporização diferentes ( -T <0-5>) para usarmos. Esses valores ( 0-5) determinam a agressividade de nossas varreduras. Isso também pode ter efeitos negativos se a verificação for muito agressiva e os sistemas de segurança puderem nos bloquear devido ao tráfego de rede produzido. O modelo de tempo padrão usado quando não definimos mais nada é o normal ( -T 3).

 - -T 0/-T paranoid
 - -T 1/-T sneaky
 - -T 2/-T polite
 - -T 3/-T normal
 - -T 4/-T aggressive
 - -T 5/-T insane

Esses modelos contêm opções que também podemos definir manualmente e já vimos algumas delas. Os desenvolvedores determinaram os valores definidos para esses modelos de acordo com seus melhores resultados, facilitando a adaptação de nossas varreduras ao ambiente de rede correspondente.

### Verificação padrão

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F -oN tnet.default

    <SNIP>
    Nmap done: 256 IP addresses (10 hosts up) scanned in 32.44 seconds

### Varredura insana

    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.0/24 -F -oN tnet.T5 -T 5

    <SNIP>
    Nmap done: 256 IP addresses (10 hosts up) scanned in 18.07 seconds

 - **-oN tnet.T5** - Salva os resultados em formatos normais, iniciando o nome de arquivo especificado.
 - **-T 5** - Especifica o modelo de tempo insano.

### Verificação padrão - Portas abertas encontradas

    NycolasES6@htb[/htb]$ cat tnet.default | grep "/tcp" | wc -l

    23

### Varredura Insana - Portas Abertas Encontradas

    NycolasES6@htb[/htb]$ cat tnet.T5 | grep "/tcp" | wc -l

    23


















