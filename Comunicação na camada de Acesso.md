#redes 
# Comunicação na camada de Acesso

Em uma rede Ethernet local, uma NIC só aceitará um quadro se o endereço de destino for o endereço MAC de broadcast ou corresponder ao endereço MAC da NIC.

A maioria dos aplicativos de rede, entretanto, baseiam-se no endereço IP lógico de destino para identificar a localização de servidores e clientes. A figura ilustra o problema de um host emissor ter apenas o endereço IP lógico do host de destino. Como o host emissor determina o endereço MAC de destino a ser colocado no quadro?

O host emissor pode usar um protocolo IPv4 chamado ARP (Address Resolution Protocol) para descobrir o endereço MAC de qualquer host na mesma rede local. O IPv6 usa um método semelhante conhecido como Descoberta de Vizinhos (Neighbor Discovery).

![[Pasted image 20240610114624.png]]













