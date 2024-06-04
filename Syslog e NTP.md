#cyber #redes
# Syslog e NTP

Vários protocolos que geralmente aparecem em redes têm recursos que os tornam de especial interesse no monitoramento de segurança. Por exemplo, syslog e Network Time Protocol (NTP) são essenciais para o trabalho do analista de segurança cibernética.

O padrão syslog é usado para registrar mensagens de eventos de dispositivos de rede e endpoints, conforme mostrado na figura. O padrão permite um meio neutro de sistema de transmissão, armazenamento e análise de mensagens. Muitos tipos de dispositivos de vários fornecedores diferentes podem usar syslog para enviar entradas de log para servidores centrais que executam um daemon syslog. Esta centralização da coleta de logs ajuda a tornar o monitoramento de segurança prático. Os servidores que executam syslog normalmente escutam na porta UDP 514.

Como o syslog é tão importante para o monitoramento de segurança, os servidores syslog podem ser um alvo para atores de ameaças. Algumas explorações, como aquelas que envolvem extração de dados, podem levar muito tempo para serem concluídas. Isso ocorre porque as maneiras pelas quais os dados são roubados secretamente da rede podem ser muito lentos. Alguns atacantes podem tentar ocultar o fato de que a exfiltração está ocorrendo. Eles atacam servidores syslog que contêm as informações que podem levar à detecção da exploração. Os hackers podem tentar bloquear a transferência de dados de clientes de syslog para servidores. Eles podem violar ou destruir dados de log ou o software que cria e transmite mensagens de log. A implementação do syslog de próxima geração (ng), conhecida como syslog-ng, oferece aprimoramentos que podem ajudar a evitar algumas das explorações que visam o syslog.

![[Pasted image 20240604110135.png]]





























