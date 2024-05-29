#redes 
# Resumo protocolo IP

## Finalidade do endereço IPv4

O endereço IPv4 é um endereço de rede lógico que identifica um host específico. Ele deve ser configurado corretamente e de forma exclusiva dentro da LAN, para fornecer comunicação local. Também deve ser configurado corretamente e de forma exclusiva no mundo, para fornecer comunicação remota.

Um endereço IPv4 é atribuído à conexão de interface de rede de um host. Essa conexão geralmente é uma placa de interface de rede (NIC) instalada no dispositivo.

Cada pacote enviado pela Internet tem um endereço IPv4 de origem e de destino. Essa informação é necessária para os dispositivos de rede garantirem que os dados cheguem ao destino e que as respostas sejam retornadas à origem.

## A estrutura do endereço IPv4

O endereço lógico IPv4 de 32 bits é hierárquico e contém duas partes, a rede e o host Como exemplo, um host com o endereço IPv4 192.168.5.11 e a máscara de sub-rede 255.255.255.0. Os três primeiros octetos (192.168.5) identificam a porção de rede do endereço e o último octeto (11) identifica o host. Isso é conhecido como endereçamento hierárquico porque a porção de rede indica a rede na qual está localizado cada endereço exclusivo de host.

Os roteadores precisam saber apenas como alcançar cada rede, em vez de precisar saber a localização de cada host individual. Com o endereçamento IPv4, poderão existir diversas redes lógicas em uma rede física se a porção de rede dos endereços de hosts de rede lógica for diferente.