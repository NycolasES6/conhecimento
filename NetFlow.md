#redes 
# NetFlow

NetFlow é uma tecnologia CISCO IOS que fornece estatísticas em pacotes que passam por meio de um switch multicamadas ou de um roteador da Cisco. Enquanto o SNMP tenta fornecer uma ampla gama de recursos e opções de gerenciamento de rede, o NetFlow está focado em fornecer estatísticas sobre pacotes IP que fluem através de dispositivos de rede.

O NetFlow fornece dados para permitir monitoramento de rede e segurança, planejamento de rede, análise de tráfego para incluir identificação de gargalos de rede e contabilidade IP para fins de faturamento. Por exemplo, na figura, o PC 1 se conecta ao PC 2 usando um aplicativo como HTTPS.

**NetFlow na rede**

![[Pasted image 20240513111233.png]]

O NetFlow pode monitorar essa conexão de aplicativo, rastreando contagens de bytes e pacotes para esse fluxo de aplicativo individual. Em seguida, envia as estatísticas para um servidor externo chamado coletor NetFlow.

A tecnologia NetFlow tem visto várias gerações que oferecem mais sofisticação na definição de fluxos de tráfego, mas fluxos “NetFlow original” diferenciados usando uma combinação de sete campos. Caso um desses campos varie em valor de outro pacote, os pacotes podem ser determinados com segurança como sendo de fluxos diferentes:

- Endereço IP de origem
- Endereço IP de destino
- Número da porta de origem
- Número da porta de destino
- Tipo de protocolo da camada 3
- Marcação de tipo de serviço (ToS)
- Interface lógica de entrada

Os quatro primeiros campos que o NetFlow usa para identificar um fluxo devem ser familiares. Os endereços IP de origem e destino, além das portas de origem e destino, identificam a conexão entre o aplicativo de origem e de destino. O tipo de protocolo da Camada 3 identifica o tipo de cabeçalho que segue o cabeçalho IP (geralmente TCP ou UDP, mas outras opções incluem ICMP). O byte ToS no cabeçalho IPv4 contém informações sobre como os dispositivos devem aplicar regras de qualidade de serviço (QoS) aos pacotes nesse fluxo.

















