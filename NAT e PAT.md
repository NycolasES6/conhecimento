#cyber 
# NAT e PAT

Conversão de Endereços de Rede (NAT) e Tradução de Endereço de Porta (PAT) podem complicar o monitoramento de segurança. Vários endereços IP são mapeados para um ou mais endereços públicos visíveis na Internet, ocultando os endereços IP individuais que estão dentro da rede (endereços internos).

A figura ilustra a relação entre endereços internos e externos que são usados como endereços de origem (SA) e endereços de destino (DA). Esses endereços internos e externos estão em uma rede que está usando NAT para se comunicar com um destino na Internet. Se o PAT estiver em vigor e todos os endereços IP que saem da rede usarem o endereço global 209.165.200.226 interno para tráfego na Internet, pode ser difícil registrar o dispositivo interno específico que está solicitando e recebendo o tráfego quando ele entra na rede.

Esse problema pode ser especialmente relevante com dados NetFlow. Os fluxos de NetFlow são unidirecionais e são definidos pelos endereços e portas que eles compartilham. O NAT basicamente quebrará um fluxo que passa por um gateway NAT, tornando as informações de fluxo além desse ponto indisponíveis. A Cisco oferece produtos de segurança que irão “costurar” fluir juntos mesmo que os endereços IP tenham sido substituídos pelo NAT.

## Network Address Translation

![[Pasted image 20240611081153.png]]








