#redes 
# Endereçamento classful Legado

Em 1981, os endereços IPv4 foram atribuídos usando o endereço classful, conforme definido na RFC 790 ([https://tools.ietf.org/html/rfc790](https://datatracker.ietf.org/doc/html/rfc790)), Números Atribuídos Os clientes receberam um endereço de rede com base em uma das três classes, A, B ou C. A RFC dividiu os intervalos de unicast em classes específicas da seguinte maneira:

- **Classe A (0.0.0.0/8 to 127.0.0.0/8)** – Projetado para suportar redes extremamente grandes com mais de 16 milhões de endereços de host. A Classe A usou um prefixo fixo /8 com o primeiro octeto para indicar o endereço de rede e os três octetos restantes para endereços de host (mais de 16 milhões de endereços de host por rede).
- **Classe B (128.0.0.0 / 16 - 191.255.0.0 / 16)** - Projetada para oferecer suporte às necessidades de redes de tamanho moderado a grande com até aproximadamente 65.000 endereços de host. A Classe B usou um prefixo fixo /16 com os dois octetos de alta ordem para indicar o endereço de rede e os dois octetos restantes para endereços de host (mais de 65.000 endereços de host por rede).
- **Classe C (192.0.0.0 / 24 - 223.255.255.0 / 24)** - Projetado para oferecer suporte a pequenas redes com no máximo 254 hosts. A Classe C usou um prefixo fixo / 24 com os três primeiros octetos para indicar a rede e o octeto restante para os endereços de host (apenas 254 endereços de host por rede).

**Observação:** Há também um bloco multicast Classe D consistindo de 224.0.0.0 a 239.0.0.0 e um bloco de endereço experimental Classe E consistindo de 240.0.0.0 - 255.0.0.0.

Na época, com um número limitado de computadores usando a internet, o endereçamento clássico era um meio eficaz para alocar endereços. Como mostrado na figura, as redes de classe A e B têm um número muito grande de endereços de host e Classe C tem muito poucos. As redes de classe A representaram 50% das redes IPv4. Isso fez com que a maioria dos endereços IPv4 disponíveis não fossem utilizados.

![[Pasted image 20240529095200.png]]