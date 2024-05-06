#redes #protocolo 
# Ethernet

os usuários utilizam um par de fios de cobre trançado para se conectarem a um comutador Ethernet,

O comutador Ethernet, ou uma rede desses comutadores interconectados, é por sua vez conectado à Internet maior. Com o acesso por uma rede Ethernet, os usuários normalmente têm acesso de 100 Mbits/s com o comutador Ethernet, enquanto os servidores possuem um acesso de 1 Gbit/s ou até mesmo 10 Gbits/s.

## Estrutura do protocolo ethernet

![[Pasted image 20240426104909.png]]

- **MAC de destino** - Contém o endereço físico da placa de rede de destino.
- **MAC de origem** - Contém o endereço físico da placa de rede de origem.
- **Tipo** - Código que identifica o tipo de protocolo (0800 = IP / 0806 = [[ARP]]).
- **Payload** - Contém os dados a serem transportados ( outro protocolo ), o tamanho máximo do payload ethernet é de 1500 bytes.

## Exemplo prático

Broadcast é o endereço que indica todo o segmento ethernet (ff:ff:ff:ff:ff:ff)

![[Pasted image 20240426111319.png]]









































