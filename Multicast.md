#redes 
# Multicast

Transmissão multicast reduz o tráfego, permitindo que um host envie um único pacote para um conjunto de hosts selecionados que participem de um grupo multicast.

Um pacote multicast é um pacote com um endereço IP de destino que é um endereço multicast. O IPv4 reservou os endereços 224.0.0.0 a 239.255.255.255 como intervalo de multicast.

Os hosts que recebem pacotes multicast específicos são chamados de clientes multicast. Os clientes multicast usam serviços solicitados por um programa cliente para se inscrever no grupo multicast.

Cada grupo multicast é representado por um único endereço IPv4 multicast de destino. Quando um host IPv4 se inscreve em um grupo multicast, o host processa pacotes endereçados tanto a esse endereço multicast como a seu endereço unicast alocado exclusivamente.

Protocolos de roteamento, como OSPF, usam transmissões multicast. Por exemplo, os roteadores habilitados com OSPF se comunicam entre si usando o endereço multicast OSPF reservado 224.0.0.5. Somente dispositivos habilitados com OSPF processarão esses pacotes com 224.0.0.5 como endereço IPv4 de destino. Todos os outros dispositivos ignorarão esses pacotes.