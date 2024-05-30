#redes 
# Domínios de broadcast e segmentação

Em uma LAN Ethernet, os dispositivos usam broadcast e o Protocolo de Resolução de Endereços (ARP) para localizar outros dispositivos. O ARP envia broadcasts dea Camada 2 para um endereço IPv4 conhecido na rede local para descobrir o endereço MAC associado. Os dispositivos em LANs Ethernet também localizam outros dispositivos usando serviços. Um host normalmente adquire sua configuração de endereço IPv4 usando o protocolo DHCP (Dynamic Host Configuration Protocol) que envia broadcasts na rede local para localizar um servidor DHCP.

Os switches propagam broadcasts por todas as interfaces, exceto a interface em que foram recebidos. Por exemplo, se um switch na figura recebesse um broadcast, ele o encaminharia para os outros switches e os outros usuários conectados na rede.

# Roteadores segmentam domínios de broadcast

![[Pasted image 20240529100602.png]]

Roteadores não propagam broadcasts. Quando um roteador recebe um broadcast, ele não o encaminha por outras interfaces. Por exemplo, quando R1 recebe um broadcast na interface Gigabit Ethernet 0/0, ele não o encaminha por outra interface.

Portanto, cada interface do roteador se conecta a um domínio de broadcast e as transmissões são propagadas apenas dentro desse domínio de broadcast específico.