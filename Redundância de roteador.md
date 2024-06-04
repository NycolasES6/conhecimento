#redes #cyber
# Redundância de roteador

O gateway padrão é normalmente o roteador que proporciona acesso dos dispositivos ao resto da rede ou à Internet. Se houver somente um roteador como gateway padrão, é um ponto único de falha. A empresa pode escolher instalar um roteador de standby adicional.

o roteador de encaminhamento e o roteador standby usam um protocolo de redundância para determinar qual roteador deve assumir o papel ativo na redundância. Cada roteador está configurado com um endereço IP físico e um endereço IP do roteador virtual. Dispositivos finais usam o endereço IP virtual como o gateway padrão.

O roteador de encaminhamento e o roteador standby usam seus endereços IP físicos para trocar mensagens periódicas. O objetivo dessas mensagens é ter certeza de que os dois ainda estão on-line e disponíveis.

Se o roteador em espera parar de receber essas mensagens periódicas do roteador de encaminhamento, ele perceberá que é o único roteador disponível e assumirá a função de encaminhamento. Enquanto isso, como os PCs na rede ainda se comunicam com o roteador virtual em 192.0.2.100, eles permanecem on-line apesar de tudo o que aconteceu, já que o roteador virtual agora encaminha para o que era anteriormente o roteador de espera.

A capacidade de uma rede de se recuperar dinamicamente da falha de um dispositivo que atua como um gateway padrão é conhecida como **redundância de primeiro salto**.







