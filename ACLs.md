#cyber
# ACLs

Muitas tecnologias e protocolos podem ter impacto no monitoramento de segurança. Listas de Controle de Acesso (ACLs) estão entre essas tecnologias. As ACLs podem dar uma falsa sensação de segurança se forem excessivamente confiadas. As ACLs e a filtragem de pacotes em geral são tecnologias que contribuem para um conjunto em evolução de proteções de segurança de rede.

A figura ilustra o uso de ACLs para permitir apenas tipos específicos de tráfego ICMP (Internet Control Message Protocol). O servidor em 192.168.1.10 faz parte da rede interna e tem permissão para enviar solicitações de ping para o host externo em 209.165.201.3. O tráfego ICMP de retorno do host externo é permitido se for uma resposta ICMP, extinção de origem (informa a origem para reduzir o ritmo do tráfego) ou qualquer mensagem ICMP inacessível. Todos os outros tipos de tráfego ICMP são negados. Por exemplo, o host externo não pode iniciar uma solicitação de ping para o host interno. A ACL de saída está permitindo mensagens ICMP que relatam vários problemas. Isso permitirá túneis ICMP e exfiltração de dados.

Os invasores podem determinar quais endereços IP, protocolos e portas são permitidos pelas ACLs. Isso pode ser feito por varredura de portas, testes de penetração ou através de outras formas de reconhecimento. Os atacantes podem criar pacotes que usam endereços IP de origem falsificados. Os aplicativos podem estabelecer conexões em portas arbitrárias. Outros recursos do tráfego de protocolo também podem ser manipulados, como o sinalizador estabelecido em segmentos TCP. As regras não podem ser antecipadas e configuradas para todas as técnicas de manipulação de pacotes emergentes.

Para detectar e reagir à manipulação de pacotes, comportamentos mais sofisticados e medidas baseadas em contexto precisam ser tomadas. Os firewalls de próxima geração da Cisco, o AMP (Advanced Malware Protection) e os appliances de conteúdo de e-mail e Web são capazes de resolver as deficiências das medidas de segurança baseadas em regras.

























