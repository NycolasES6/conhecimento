#redes
# Broadcast

Transmissão broadcast refere-se a um dispositivo enviando uma mensagem para todos os dispositivos em uma rede, ou seja, comunicação de um para todos.

Um pacote de broadcast possui um endereço IP de destino com todos os (1s) na parte do host ou 32 (um) bits.

**Observação:** O IPv4 usa pacotes de broadcast . No entanto, não há pacotes de broadcast com IPv6.

Um pacote de broadcast deve ser processado por todos os dispositivos no mesmo domínio de broadcast. Um domínio de broadcast identifica todos os hosts no mesmo segmento de rede. Um broadcast pode ser direcionado ou limitado. Um broadcast direcionado é enviado para todos os hosts em uma rede específica. Por exemplo, um host na rede 172.16.4.0/24 envia um pacote para 172.16.4.255. Uma broadcast limitado é enviado para 255.255.255.255. Por padrão, os roteadores não encaminham broadcasts.