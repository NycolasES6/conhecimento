#redes 
# Destino na mesma rede

Às vezes, um host deve enviar uma mensagem, mas ele só sabe o endereço IP do dispositivo de destino. O host precisa saber o endereço MAC desse dispositivo, mas como ele pode ser descoberto? É aí que a resolução de endereços se torna crítica.

Dois endereços principais são atribuídos a um dispositivo em uma LAN Ethernet:

- **Endereço físico (o endereço MAC)** - Usado para comunicações de NIC para NIC na mesma rede Ethernet.
- **Endereço lógico (o endereço IP)** – Usado para enviar o pacote do dispositivo de origem para o dispositivo de destino. O endereço IP de destino pode estar na mesma rede IP que a origem ou pode estar em uma rede remota.

Os endereços físicos da camada 2 (ou seja, endereços MAC Ethernet) são usados para entregar o quadro de enlace de dados, contendo o pacote IP encapsulado, a partir de uma NIC para outra NIC que está na mesma rede. Se o endereço IP de destino estiver na mesma rede, o endereço MAC de destino será o do dispositivo de destino.

Considere o exemplo a seguir usando representações de endereço MAC simplificadas.

![[Pasted image 20240610111717.png]]

Neste exemplo, PC1 deseja enviar um pacote para PC2. A figura exibe os endereços MAC de destino e de origem da Camada 2 e o endereçamento IPv4 da Camada 3 que seriam incluídos no pacote enviado a partir do PC1.

O quadro Ethernet da camada 2 contém o seguinte:

- **Endereço MAC de destino** — Este é o endereço MAC simplificado de PC2, 55-55-55.
- **Endereço MAC de origem** — Este é o endereço MAC simplificado da NIC Ethernet em PC1, aa-aa-aa .

O pacote IP da camada 3 contém o seguinte:

- **Endereço IPv4 de origem** — Este é o endereço IPv4 de PC1, 192.168.10.10 .
- **Endereço IPv4 de destino** — Este é o endereço IPv4 de PC2, 192.168.10.11.