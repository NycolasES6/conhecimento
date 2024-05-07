#redes 

# DHCP

Os servidores DHCP fornecem dinamicamente informações de configuração de IP aos clientes. A figura mostra a sequência típica de uma troca de mensagens DHCP entre cliente e servidor.

**Operação normal do DHCP**

![[Pasted image 20240507161451.png]]

Na figura, um cliente transmite uma mensagem de descoberta DHCP. O servidor DHCP responde com uma oferta direta (unicast) que inclui informações de endereçamento que o cliente pode usar. O cliente transmite em difusão (broadcast) uma solicitação DHCP para informar ao servidor que aceita a oferta. O servidor responde com uma confirmação de direta (unicast) aceitando a solicitação.






























