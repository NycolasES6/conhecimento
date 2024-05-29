#redes 
# Roteamento para a internet

A maioria das redes internas, de grandes empresas a redes domésticas, usa endereços IPv4 privados para endereçar todos os dispositivos internos (intranet), incluindo hosts e roteadores. No entanto, os endereços privados não são globalmente roteáveis.

Na figura, as redes de clientes 1, 2 e 3 estão enviando pacotes fora de suas redes internas. Esses pacotes têm um endereço IPv4 de origem que é um endereço privado e um endereço IPv4 de destino público (globalmente roteável). Os pacotes com um endereço privado devem ser filtrados (descartados) ou traduzidos para um endereço público antes de encaminhar o pacote para um ISP.

### Endereços IPv4 privados e Tradução de Endereços de Rede (NAT)

![[Pasted image 20240529093913.png]]

Antes que o ISP possa encaminhar esse pacote, ele deve traduzir o endereço IPv4 de origem, que é um endereço privado, para um endereço IPv4 público usando a Conversão de Endereços de Rede (NAT). O NAT é usado para converter entre endereços IPv4 privados e IPv4 públicos. Isso geralmente é feito no roteador que conecta a rede interna à rede ISP. Os endereços IPv4 privados na intranet da organização serão traduzidos para endereços IPv4 públicos antes do encaminhamento para a Internet.





















