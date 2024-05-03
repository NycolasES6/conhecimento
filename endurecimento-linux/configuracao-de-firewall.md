# Configuração de firewall

O objetivo principal dos firewalls é fornecer um mecanismo de segurança para controlar e monitorar o tráfego de rede entre diferentes segmentos de rede, como redes internas e externas ou diferentes zonas de rede. Os firewalls desempenham um papel crucial na proteção de redes de computadores contra acesso não autorizado, tráfego malicioso e outras ameaças à segurança. O Linux, sendo um sistema operacional popular usado em servidores e outros dispositivos de rede, fornece recursos de firewall integrados que podem ser usados para controlar o tráfego de rede. Em outras palavras, eles podem filtrar o tráfego de entrada e saída com base em regras, protocolos, portas e outros critérios predefinidos para impedir acesso não autorizado e mitigar ameaças à segurança. O objetivo específico de uma implementação de firewall pode variar dependendo das necessidades específicas da organização, como garantir a confidencialidade, integridade e disponibilidade dos recursos da rede.

Um exemplo da história dos firewalls Linux é o desenvolvimento da ferramenta iptables, que substituiu as ferramentas anteriores ipchains e ipfwadm. O utilitário iptables foi introduzido pela primeira vez no kernel Linux 2.4 em 2000 e forneceu um mecanismo flexível e eficiente para filtrar o tráfego de rede. O iptables se tornou a solução de firewall padrão de fato para sistemas Linux e foi amplamente adotado por muitas organizações e usuários.

O utilitário iptables forneceu uma interface de linha de comando simples, mas poderosa para configurar regras de firewall, que poderia ser usada para filtrar o tráfego com base em vários critérios, como endereços IP, portas, protocolos e muito mais. O iptables foi projetado para ser altamente personalizável e pode ser usado para criar conjuntos de regras de firewall complexos que podem proteger contra várias ameaças à segurança, como ataques de negação de serviço (DoS), varreduras de portas e tentativas de invasão de rede.

No Linux, a funcionalidade do firewall normalmente é implementada usando a estrutura Netfilter, que é parte integrante do kernel. O Netfilter fornece um conjunto de ganchos que podem ser usados para interceptar e modificar o tráfego de rede à medida que ele passa pelo sistema. O utilitário iptables é comumente usado para configurar as regras de firewall em sistemas Linux.

## Iptables

O utilitário iptables fornece um conjunto flexível de regras para filtrar o tráfego de rede com base em vários critérios, como endereços IP de origem e destino, números de porta, protocolos e muito mais. Também existem outras soluções como nftables, ufw e firewalld. Nftablesfornece uma sintaxe mais moderna e desempenho aprimorado em relação ao iptables. No entanto, a sintaxe das regras do nftables não é compatível com o iptables, portanto a migração para o nftables requer algum esforço. UFWsignifica “Firewall Descomplicado” e fornece uma interface simples e amigável para configurar regras de firewall. O UFW é construído sobre a estrutura iptables como o nftables e fornece uma maneira mais fácil de gerenciar regras de firewall. Por fim, o FirewallD fornece uma solução de firewall dinâmica e flexível que pode ser usada para gerenciar configurações complexas de firewall e oferece suporte a um rico conjunto de regras para filtrar o tráfego de rede e pode ser usado para criar zonas e serviços de firewall personalizados. Consiste em vários componentes que trabalham juntos para fornecer uma solução de firewall flexível e poderosa. Os principais componentes do iptables são:

| Componente | Descrção |
| :--------: | :------- |
| Tables  | As tabelas são usadas para organizar e categorizar regras de firewall. |
| Chains  | As cadeias são usadas para agrupar um conjunto de regras de firewall aplicadas a um tipo específico de tráfego de rede. |
| Rules   | As regras definem os critérios para filtrar o tráfego de rede e as ações a serem tomadas para os pacotes que correspondem aos critérios. |
| Matches | As correspondências são usadas para corresponder a critérios específicos de filtragem de tráfego de rede, como endereços IP de origem ou destino, portas, protocolos e muito mais. |
| Targets | Os destinos especificam a ação para pacotes que correspondem a uma regra específica. Por exemplo, os alvos podem ser usados ​​para aceitar, descartar ou rejeitar pacotes ou modificar os pacotes de outra maneira. |

## Tables

Ao trabalhar com firewalls em sistemas Linux, é importante entender como as tabelas funcionam no iptables. As tabelas em iptables são usadas para categorizar e organizar regras de firewall com base no tipo de tráfego para o qual foram projetadas. Essas tabelas são usadas para organizar e categorizar regras de firewall. Cada tabela é responsável por executar um conjunto específico de tarefas.

| Nome da tabela | Descrição | Correntes integradas |
| :-------------: | ------------- | ------- |
|  filter | Usado para filtrar o tráfego de rede com base em endereços IP, portas e protocolos. | INPUT, OUTPUT, FORWARD |
|   nat   | Usado para modificar os endereços IP de origem ou destino dos pacotes de rede. | PREROUTING, POSTROUTING |
|  mangle | Usado para modificar os campos de cabeçalho dos pacotes de rede. | PREROUTING, OUTPUT, INPUT, FORWARD, POSTROUTING |

Além das tabelas integradas, o iptables fornece uma quarta tabela chamada tabela bruta, que é usada para configurar opções especiais de processamento de pacotes. A tabela bruta contém duas cadeias integradas: PREROUTING e OUTPUT.

## Chains

No iptables, as cadeias organizam regras que definem como o tráfego da rede deve ser filtrado ou modificado. Existem dois tipos de cadeias no iptables:

 - Correntes embutidas
 - Cadeias definidas pelo usuário

As cadeias integradas são predefinidas e criadas automaticamente quando uma tabela é criada. Cada tabela possui um conjunto diferente de cadeias integradas. Por exemplo, a tabela de filtros possui três cadeias integradas:

 - INPUT
 - OUTPUT
 - FORWARD

Essas cadeias são usadas para filtrar o tráfego de rede de entrada e saída, bem como o tráfego que está sendo encaminhado entre diferentes interfaces de rede. A tabela nat possui duas cadeias integradas:

 - PREROUTING
 - POSTROUTING

A cadeia PREROUTING é usada para modificar o endereço IP de destino dos pacotes recebidos antes que a tabela de roteamento os processe. A cadeia POSTROUTING é usada para modificar o endereço IP de origem dos pacotes de saída após a tabela de roteamento tê-los processado. A tabela mangle possui cinco cadeias integradas:

 - PREROUTING
 - OUTPUT
 - INPUT
 - FORWARD
 - POSTROUTING

Essas cadeias são usadas para modificar os campos de cabeçalho dos pacotes de entrada e saída e dos pacotes que estão sendo processados pelas cadeias correspondentes.

User-defined chainspode simplificar o gerenciamento de regras agrupando regras de firewall com base em critérios específicos, como endereço IP de origem, porta de destino ou protocolo. Eles podem ser adicionados a qualquer uma das três tabelas principais. Por exemplo, se uma organização tiver vários servidores web que exigem regras de firewall semelhantes, as regras para cada servidor poderão ser agrupadas em uma cadeia definida pelo usuário. Outro exemplo é quando uma cadeia definida pelo usuário pode filtrar o tráfego destinado a uma porta específica, como a porta 80 (HTTP). O usuário poderia então adicionar regras a esta cadeia que filtrassem especificamente o tráfego destinado à porta 80.

## Regras e metas

As regras do Iptables são usadas para definir os critérios de filtragem do tráfego de rede e as ações a serem tomadas para os pacotes que atendem aos critérios. As regras são adicionadas às cadeias usando a -Aopção seguida pelo nome da cadeia e podem ser modificadas ou excluídas usando várias outras opções.

Cada regra consiste em um conjunto de critérios ou correspondências e um alvo especificando a ação para pacotes que correspondam aos critérios. Os critérios ou correspondências correspondem a campos específicos no cabeçalho IP, como endereço IP de origem ou destino, protocolo, origem, número da porta de destino e muito mais. O destino especifica a ação para pacotes que correspondam aos critérios. Eles especificam a ação a ser tomada para pacotes que correspondam a uma regra específica. Por exemplo, os alvos podem aceitar, descartar, rejeitar ou modificar os pacotes. Alguns dos alvos comuns usados nas regras do iptables incluem o seguinte:

| Nome do Alvo | Descrição |
| :--- | :--- |
| ACCEPT | Permite que o pacote passe pelo firewall e continue até seu destino |
| DROP | Descarta o pacote, bloqueando efetivamente sua passagem pelo firewall |
| REJECT | Descarta o pacote e envia uma mensagem de erro de volta ao endereço de origem, notificando-o de que o pacote foi bloqueado |
| LOG | Registra as informações do pacote no log do sistema |
| SNAT | Modifica o endereço IP de origem do pacote, normalmente usado para Network Address Translation (NAT) para traduzir endereços IP privados em endereços IP públicos |
| DNAT | Modifica o endereço IP de destino do pacote, normalmente usado pelo NAT para encaminhar o tráfego de um endereço IP para outro |
| MASQUERADE | Semelhante ao SNAT, mas usado quando o endereço IP de origem não é fixo, como em um cenário de endereço IP dinâmico |
| REDIRECT | Redireciona pacotes para outra porta ou endereço IP |
| MARK | Adiciona ou modifica o valor da marca Netfilter do pacote, que pode ser usado para roteamento avançado ou outros fins |

Vamos ilustrar uma regra e considerar que queremos adicionar uma nova entrada à cadeia INPUT que permita que o tráfego TCP de entrada na porta 22 (SSH) seja aceito. O comando para isso seria parecido com o seguinte:

    `$ sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT`

## Matches

Matches são usados para especificar os critérios que determinam se uma regra de firewall deve ser aplicada a um pacote ou conexão específica. As correspondências são usadas para combinar características específicas do tráfego de rede, como endereço IP de origem ou destino, protocolo, número da porta e muito mais.

| Nome da correspondência | Descrção |
| - | - |
| -p ou --protocol | Especifica o protocolo correspondente (por exemplo, tcp, udp, icmp) |
| --dport | Especifica a porta de destino para corresponder |
| --sport |Especifica a porta de origem para corresponder |
| -s ou --source | Especifica o endereço IP de origem para corresponder |
| -d ou --destination | Especifica o endereço IP de destino para corresponder |
| -m state | Corresponde ao estado de uma conexão (por exemplo, NOVO, ESTABELECIDO, RELACIONADO) |
| -m multiport | Corresponde a várias portas ou intervalos de portas |
| -m tcp | Corresponde a pacotes TCP e inclui opções adicionais específicas de TCP |
| -m udp | Corresponde a pacotes UDP e inclui opções adicionais específicas de UDP |
| -m string | Corresponde a pacotes que contêm uma string específica |
| -m limit | Corresponde pacotes a um limite de taxa especificado |
| -m conntrack | Corresponde pacotes com base em suas informações de rastreamento de conexão |
| -m mark | Corresponde pacotes com base no valor da marca Netfilter |
| -m mac | Corresponde pacotes com base em seu endereço MAC |
| -m iprange | Corresponde pacotes com base em um intervalo de endereços IP |

Em geral, as correspondências são especificadas usando a opção '-m' no iptables. Por exemplo, o comando a seguir adiciona uma regra à cadeia 'INPUT' na tabela 'filter' que corresponde ao tráfego TCP de entrada na porta 80:

    `$ sudo iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT`

Este exemplo de regra corresponde ao tráfego TCP de entrada ( **-p tc**p) na porta 80 ( **--dport 80**) e salta para o destino de aceitação ( **-j ACCEPT**) se a correspondência for bem-sucedida.

1. Inicie um servidor web na porta TCP/8080 do seu destino e use iptables para bloquear o tráfego de entrada nessa porta.
2. Altere as regras do iptables para permitir o tráfego de entrada na porta TCP/8080.
3. Bloqueie o tráfego de um endereço IP específico.
4. Permitir tráfego de um endereço IP específico.
5. Bloqueie o tráfego com base no protocolo.
6. Permitir tráfego com base no protocolo.
7. Crie uma nova cadeia.
8. Encaminhe o tráfego para uma cadeia específica.
9. Exclua uma regra específica.
10. Liste todas as regras existentes.
