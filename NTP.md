#redes 
# NTP

É importante sincronizar a hora em todos os dispositivos da rede porque todos os aspectos de gerenciamento, proteção, solução de problemas e planejamento de redes exigem um registro de data e hora preciso e consistente. Quando a hora não está sincronizada entre os dispositivos, será impossível determinar a ordem dos eventos que ocorreram em diferentes partes da rede.

Normalmente, as configurações de data e hora em um dispositivo de rede podem ser definidas usando um destes dois métodos:

- Configuração manual de data e hora
- Configurando o Network Time Protocol (NTP)

Conforme a rede cresce, torna-se cada vez mais difícil garantir que todos os dispositivos da infraestrutura operem com horário sincronizado. Mesmo em um ambiente de rede menor, o método manual não é o ideal. Se um dispositivo for reinicializado, como ele obterá uma data e um carimbo de hora precisos?

A melhor solução é configurar o NTP na rede. Esse protocolo permite que os roteadores na rede sincronizem as configurações de hora com um servidor NTP. Um grupo de clientes NTP que obtém informações de data e hora de uma única fonte tem configurações de hora mais consistentes. Quando o NTP é implementado na rede, ele pode ser configurado para sincronizar com um relógio mestre privado ou pode ser sincronizado com um servidor NTP disponível publicamente na Internet.

As redes NTP usam um sistema hierárquico de fontes de horário. Cada nível desse sistema hierárquico é denominado stratum. O nível do stratum é definido como o número de contagens de saltos da fonte oficial. O horário sincronizado é distribuído através da rede usando o NTP. A figura exibe uma amostra de uma rede NTP.

## Níveis de estrato NTP

![[Pasted image 20240513112806.png]]

Os servidores NTP são organizados em três níveis conhecidos como estratos:

- **Estrato 0 -** Uma rede NTP obtém o tempo de fontes de tempo confiáveis. Essas fontes, também conhecidas como dispositivos de stratum 0, são dispositivos de pontualidade de alta precisão, com pouco ou nenhum atraso associado a eles.
- **Estrato 1 -** Os dispositivos do estrato 1 estão diretamente conectados às fontes de tempo autorizadas. Eles atuam como o principal padrão de horário da rede.
- **Estrato 2 e estratos inferiores -** Os servidores estrato 2 são conectados aos dispositivos estrato 1 por meio de conexões de rede. Os dispositivos do stratum 2, como os clientes NTP, sincronizam a hora usando os pacotes NTP dos servidores do stratum 1. Eles também podem atuar como servidores dos dispositivos do stratum 3.

Números menores de stratum indicam que o servidor está mais próximo da fonte de horário autorizada, se comparados aos números de strati maiores. Quanto maior o número do stratum, mais baixo seu nível. A valor máximo da contagem de saltos é 15. O Stratum 16, o nível mais baixo de stratum, indica que um dispositivo não está sincronizado. Servidores de horário no mesmo nível de stratum podem ser configurados para agir como pares com outros servidores de horário no mesmo nível de stratum, para finalidades de backup ou verificação da hora.

## SYSLOG

As mensagens do Syslog geralmente são carimbadas de data e hora. Isso permite que mensagens de diferentes fontes sejam organizadas pelo tempo para fornecer uma visão dos processos de comunicação de rede. Como as mensagens podem vir de muitos dispositivos, é importante que os dispositivos compartilhem um timeclock consistente. Uma maneira que isso pode ser alcançado é para os dispositivos usarem o Network Time Protocol (NTP). O NTP usa uma hierarquia de fontes de tempo autoritativas para compartilhar informações de tempo entre dispositivos na rede, conforme mostrado na figura. Dessa forma, as mensagens de dispositivo que compartilham informações de tempo consistentes podem ser enviadas para o servidor syslog. O NTP opera na porta UDP 123.

Como os eventos conectados a uma exploração podem deixar rastros em todos os dispositivos de rede em seu caminho para o sistema de destino, os carimbos de data/hora são essenciais para detecção. Os atores de ameaças podem tentar atacar a infraestrutura NTP para corromper as informações de tempo usadas para correlacionar eventos de rede registrados. Isso pode servir para ofuscar vestígios de explorações em curso. Além disso, os atores de ameaças têm sido conhecidos por usar sistemas NTP para direcionar ataques DDoS por meio de vulnerabilidades no software cliente ou servidor. Embora esses ataques não resultem necessariamente em dados de monitoramento de segurança corrompidos, eles podem interromper a disponibilidade da rede.

![[Pasted image 20240604112055.png]]













