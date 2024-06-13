#SO  #Linux  
# CyberGames_Fundamentos Ciber - 19_questionário sobre Tecnologias e Protocolos

#### 1 - Como os cibercriminosos fazem uso de um iFrame malicioso?

- O iFrame permite que o navegador carregue uma página da Web de outra fonte.

#### 2 - De que forma o uso do HTTPS aumenta os desafios de monitoramento de segurança nas redes empresariais?

- O tráfego HTTPS permite a criptografia de ponta a ponta.

#### 3 - Qual serviço de rede sincroniza a hora em todos os dispositivos na rede?

- NTP

#### 4 - Que tipo de daemon de servidor aceita mensagens enviadas por dispositivos de rede para criar uma coleção de entradas de log?

- syslog

#### 5 - Qual número de porta seria usado se um ator de ameaça estivesse usando NTP para direcionar ataques DDoS?

- 123

#### 6 - Qual protocolo é usado para enviar mensagens de email entre dois servidores que estão em domínios de email diferentes?

- SMTP

#### 7 - Com que tipo de servidor os agentes ameaçadores podem usar o DNS para se comunicar?

- CNC

#### 8 - Que tipo de servidor seria compatível com os protocolos SMTP, POP e IMAP?

- e-mail

#### 9 - Qual método permite que o tráfego VPN permaneça confidencial?

- criptografia

#### 10 - Para facilitar o processo de solução de problemas, qual mensagem ICMP de entrada deve ser permitida em uma interface externa?

- echo reply

#### 11 - Qual instrução descreve a função fornecida pela rede Tor?

- Ele permite que os usuários naveguem na Internet anonimamente.

#### 12 - Como a NAT/PAT pode complicar o monitoramento da segurança da rede se o NetFlow estiver sendo usado?

- Ele oculta endereços IP internos, permitindo que eles compartilhem um ou alguns endereços IP externos.

#### 13 - Um analista cibernético está revisando uma ACL de ponto de entrada. Que três tipos de tráfego ICMP devem ter permissão para acessar uma rede interna a partir da Internet? (Escolha três.)

- reply
- Destino inalcançável
- Squelch

#### 14 - Uma empresa decide comprar um dispositivo capaz de gerenciar o balanceamento de carga para que o tráfego seja distribuído entre seus servidores. O que poderia ser um problema potencial ao usar o novo dispositivo na rede?

- As mensagens de teste do LBM podem aparecer como tráfego suspeito.

## Resumo

### Monitorando protocolos comuns

Muitos tipos de dispositivos de vários fornecedores diferentes podem usar syslog para enviar entradas de log para servidores centrais que executam um daemon syslog. Esta centralização da coleta de logs ajuda a tornar o monitoramento de segurança prático. Como o syslog é tão importante para o monitoramento de segurança, os servidores syslog podem ser um alvo para atores de ameaças. Os hackers podem tentar bloquear a transferência de dados de clientes syslog para servidores, adulterar ou destruir dados de log ou adulterar software que cria e transmite mensagens de log. As mensagens do Syslog geralmente são carimbadas de data e hora. Como as mensagens podem vir de muitos dispositivos, é importante que os dispositivos compartilhem um timeclock consistente. Uma maneira que isso pode ser alcançado é para os dispositivos usarem o Network Time Protocol (NTP). Como os eventos conectados a uma exploração podem deixar rastros em todos os dispositivos de rede em seu caminho para o sistema de destino, os carimbos de data/hora são essenciais para detecção. Os atores de ameaças podem tentar atacar a infraestrutura NTP para corromper informações de tempo usadas para correlacionar eventos de rede registrados ou usar sistemas NTP para direcionar ataques DDoS por meio de vulnerabilidades no software cliente ou servidor.

Os invasores geralmente encapsulam diferentes protocolos de rede no DNS para evitar dispositivos de segurança. O DNS agora é usado por muitos tipos de malware. Algumas variedades de malware usam DNS para se comunicar com servidores de comando e controle (CNC) e para exfiltrar dados no tráfego disfarçados como consultas DNS normais. Vários tipos de codificação podem ser usados para camuflar os dados e evitar medidas básicas de prevenção de perda de dados (DLP). É provável que a parte do subdomínio de tais consultas seria muito mais longa do que as solicitações habituais.

O Hypertext Transfer Protocol (HTTP) é o protocolo de backbone da World Wide Web. O HTTP não protege os dados contra alteração ou interceptação por partes mal-intencionadas, o que é uma séria ameaça à privacidade, identidade e segurança das informações. Uma exploração comum de HTTP é chamada de injeção iFrame (quadro inline). Um agente de ameaça compromete um servidor da Web e planta código malicioso que cria um iFrame invisível em uma página da Web comumente visitada. Quando o iFrame é carregado, o malware é baixado. Para lidar com a alteração ou interceptação de dados confidenciais, muitas organizações comerciais adotaram HTTPS ou implementaram políticas somente HTTPS para proteger os visitantes de seus sites e serviços. HTTPS adiciona uma camada de criptografia ao protocolo HTTP usando SSL (Secure Socket Layer), tornando os dados HTTP ilegíveis à medida que deixa o computador de origem até chegar ao servidor. Infelizmente, o tráfego HTTPS criptografado complica o monitoramento de segurança de rede. Alguns dispositivos de segurança incluem descriptografia e inspeção SSL; no entanto, isso pode apresentar problemas de processamento e privacidade. Além disso, o HTTPS adiciona complexidade às capturas de pacotes devido às mensagens adicionais envolvidas no estabelecimento da conexão criptografada.

Protocolos de e-mail como SMTP, POP3 e IMAP podem ser usados por atores de ameaças para espalhar malware, exfiltrar dados ou fornecer canais para servidores CNC de malware. SMTP envia dados de um host para um servidor de email e entre servidores de email. Como há muito tráfego SMTP, ele nem sempre é monitorado. No entanto, o SMTP foi usado no passado por malware para exfiltrar dados da rede. O monitoramento de segurança pode revelar esse tipo de tráfego com base nos recursos da mensagem de email. IMAP e POP3 são usados para baixar mensagens de email de um servidor de email para o computador host. O monitoramento de segurança pode identificar quando um anexo de e-mail de malware entrou na rede e qual host ele infectou pela primeira vez. A análise retrospectiva pode então rastrear o comportamento do malware a partir desse ponto em diante.

A funcionalidade ICMP tem sido usada para criar vários tipos de explorações. O ICMP pode ser usado para identificar hosts em uma rede, a estrutura de uma rede e determinar os sistemas operacionais em uso na rede. Ele também pode ser usado como um veículo para vários tipos de ataques DoS. Ele também pode ser usado para exfiltração de dados. Devido à preocupação de que o ICMP possa ser usado para vigiar ou negar o serviço de fora da rede, o tráfego ICMP de dentro da rede às vezes é ignorado. No entanto, algumas variedades de malware usam pacotes ICMP criados para transferir arquivos de hosts infectados para agentes ameaçadores usando esse método, conhecido como tunelamento ICMP.

### Tecnologias de segurança

As ACLs podem dar uma falsa sensação de segurança se forem excessivamente confiadas. Os invasores podem determinar quais endereços IP, protocolos e portas são permitidos pelas ACLs. Isso pode ser feito por varredura de portas ou testes de penetração, ou através de outras formas de reconhecimento. Os atacantes podem criar pacotes que usam endereços IP de origem falsificados. Os aplicativos podem estabelecer conexões em portas arbitrárias. Outros recursos do tráfego de protocolo também podem ser manipulados, como o sinalizador estabelecido em segmentos TCP. As regras não podem ser antecipadas e configuradas para todas as técnicas de manipulação de pacotes emergentes.

Conversão de Endereços de Rede (NAT) e Tradução de Endereço de Porta (PAT) podem complicar o monitoramento de segurança. Vários endereços IP são mapeados para um ou mais endereços públicos visíveis na Internet, ocultando os endereços IP individuais que estão dentro da rede (endereços internos). Esse problema pode ser especialmente relevante com dados NetFlow. Os fluxos de NetFlow são unidirecionais e são definidos pelos endereços e portas que eles compartilham. O NAT basicamente quebrará um fluxo que passa por um gateway NAT, tornando as informações de fluxo além desse ponto indisponíveis.

A criptografia pode apresentar desafios para o monitoramento de segurança tornando os detalhes do pacote ilegíveis. A criptografia faz parte das tecnologias VPN. Nas VPNs, um protocolo comum, como IP, é usado para transportar tráfego criptografado. O tráfego criptografado essencialmente estabelece uma conexão virtual ponto a ponto entre redes através de instalações públicas. A criptografia torna o tráfego ilegível para outros dispositivos, exceto os endpoints VPN. Uma tecnologia semelhante pode ser usada para criar uma conexão virtual ponto a ponto entre um host interno e dispositivos de atores de ameaças. O malware pode estabelecer um túnel criptografado que usa um protocolo comum e confiável e usá-lo para exfiltrar dados da rede.

Na rede ponto a ponto (P2P), os hosts podem operar em funções de cliente e servidor. Existem três tipos de aplicativos P2P: compartilhamento de arquivos, compartilhamento de processadores e mensagens instantâneas. No compartilhamento de arquivos P2P, os arquivos em uma máquina participante são compartilhados com membros da rede P2P. Sempre que os usuários desconhecidos recebem acesso aos recursos de rede, a segurança é uma preocupação. Aplicativos P2P de compartilhamento de arquivos não devem ser permitidos em redes corporativas. A atividade da rede P2P pode contornar as proteções de firewall e é um vetor comum para a propagação de malware. P2P é inerentemente dinâmico. Arquivos compartilhados são frequentemente infectados com malware, e os atores de ameaças podem posicionar seu malware em clientes P2P para distribuição a outros usuários.

Tor é uma plataforma de software e rede de hosts P2P que funcionam como roteadores de internet na rede Tor. Isso permite que os usuários naveguem na internet anonimamente. Os usuários acessam a rede Tor usando um navegador especial. O navegador constrói um caminho de ponta a ponta em camadas na rede do servidor Tor que é criptografado. Cada camada criptografada é “removida” como as camadas de uma cebola (portanto, “onion routing”) à medida que o tráfego atravessa um retransmissor do Tor. As camadas contêm informações criptografadas do próximo salto que só podem ser lidas pelo roteador que precisa ler as informações. Quando o tráfego é retornado à origem, um caminho criptografado em camadas é construído novamente. Tor apresenta uma série de desafios aos analistas de segurança cibernética. Primeiro, o Tor é amplamente utilizado por organizações criminosas na “Dark Net”. Além disso, Tor tem sido usado como um canal de comunicação para malware CNC. Como o endereço IP de destino do tráfego Tor é ofuscado pela criptografia, com apenas o nó Tor de próximo salto conhecido, o tráfego Tor evita listas negras configuradas em dispositivos de segurança.

O balanceamento de carga envolve a distribuição do tráfego entre dispositivos ou caminhos de rede para evitar recursos de rede sobrecarregados com muito tráfego. Uma maneira de fazer isso na internet é através de várias técnicas que usam DNS para enviar tráfego para recursos que têm o mesmo nome de domínio, mas vários endereços IP. Isso pode resultar em uma única transação de Internet sendo representada por vários endereços IP nos pacotes de entrada, o que pode fazer com que recursos suspeitos apareçam em capturas de pacotes. Alguns dispositivos do gerenciador de balanceamento de carga (LBM) usam testes para testar o desempenho de diferentes caminhos e a integridade de diferentes dispositivos. Esses testes podem parecer tráfego suspeito se o analista de segurança cibernética não estiver ciente de que esse tráfego faz parte da operação do LBM.

































