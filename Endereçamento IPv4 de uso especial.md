#redes 
# Endereçamento IPv4 de uso especial

Existem determinados endereços, como o endereço de rede e o endereço de broadcast, que não podem ser atribuídos aos hosts. Há também endereços especiais que podem ser atribuídos a hosts, mas com restrições quanto ao modo como interagem na rede.

**Endereços de loopback**

Os endereços de loopback (127.0.0.0 / 8 ou 127.0.0.1 a 127.255.255.254) são comumente identificados apenas como 127.0.0.1. Eles são endereços especiais usados por um host para direcionar tráfego para ele mesmo Por exemplo, o comando **ping** é comumente usado para testar conexões com outros hosts. Mas você também pode usar o comando **ping** para testar a configuração de IP do seu próprio dispositivo, como mostrado na figura.

**Observação:** você aprenderá mais sobre o comando **ping** posteriormente neste curso.

**Endereços locais de link**

Os endereços locais de link (169.254.0.0 / 16 ou 169.254.0.1 a 169.254.255.254) são mais conhecidos como endereços APIPA ( endereçamento IP privado automático ) ou endereços auto-atribuídos. Eles são usados por um cliente Windows para se autoconfigurar caso o cliente não consiga obter um endereçamento IP por outros métodos. Endereços de link local podem ser usados em uma conexão ponto a ponto, mas não são comumente usados para esse fim.