#redes 
# Unicast

No tópico anterior, você aprendeu sobre a estrutura de um endereço IPv4; cada um tem uma parte de rede e uma parte de host. Existem diferentes maneiras de enviar um pacote de um dispositivo de origem, e essas transmissões diferentes afetam os endereços IPv4 de destino.

Transmissão unicast refere-se a um dispositivo que envia uma mensagem para outro dispositivo em comunicações um-para-um.

Um pacote unicast tem um endereço IP de destino que é um endereço unicast que vai para um único destinatário. Um endereço IP de origem só pode ser um endereço unicast, porque o pacote só pode originar-se de uma única origem. Isso independentemente de o endereço IP de destino ser unicast, broadcast ou multicast.

Os endereços de host unicast IPv4 estão no intervalo de endereços de 1.1.1.1 a 223.255.255.255. Contudo, dentro desse intervalo há muitos endereços que já são reservados para fins especiais. Esses endereços para fins especiais serão discutidos mais adiante neste módulo.

**Observação:** Na animação, observe que a máscara de sub-rede para 255.255.255.0 é representada usando a notação de barra ou / 24. Isso indica que a máscara de sub-rede tem 24 bits. A máscara de sub-rede 255.255.255.0 em binário é 11111111.11111111.11111111.00000000.





