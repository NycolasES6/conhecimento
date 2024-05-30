#cyber 
# Problemas com Domínios de Broadcast Grandes

Um grande domínio de broadcast é uma rede que conecta vários hosts. Um problema desse tipo de domínio é que os hosts podem gerar broadcasts em excesso e afetar a rede de forma negativa. Na figura, a LAN 1 conecta 400 usuários que podem gerar uma quantidade excessiva de tráfego de broadcast. Isso resulta em operações de rede lentas devido à quantidade significativa de tráfego que pode causar e operações de dispositivo lentas porque um dispositivo deve aceitar e processar cada pacote de difusão.

## Um domínio de broadcast Grande

![[Pasted image 20240529100838.png]]

A solução é reduzir o tamanho da rede para criar domínios de broadcast menores em um processo denominado divisão em sub-redes. Os espaços de rede menores são chamados de sub-redes.

Na figura, os 400 usuários da LAN 1 com endereço de rede 172.16.0.0/16 foram divididos em duas sub-redes de 200 usuários cada: 172.16.0.0/24 e 172.16.1.0/24. Os broadcasts são propagados apenas dentro dos domínios de broadcast menores. Portanto, um broadcast em LAN 1 não se propagaria para LAN 2.

## Comunicação entre redes

![[Pasted image 20240529101001.png]]

Observe como o comprimento do prefixo mudou de /16 para /24. Esta é a base da divisão em sub-redes: usar bits de host para criar sub-redes adicionais.

**Observação**: os termos sub-rede e rede costumam ser usados de maneira intercambiável. A maioria das redes são uma sub-rede de um bloco de endereços maior.




























