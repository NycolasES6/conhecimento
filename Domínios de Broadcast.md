#redes 
# Domínios de Broadcast

Quando um host recebe uma mensagem endereçada ao endereço de broadcast, ele aceita e processa a mensagem como se ela tivesse sido endereçada diretamente a ele. Quando um host envia uma mensagem de broadcast, os switches encaminham a mensagem para cada host conectado na mesma rede local. Por esse motivo, uma rede local (ou seja, uma rede com um ou mais switches Ethernet) também é conhecida como domínio de broadcast.

Se muitos hosts estiverem conectados ao mesmo domínio de broadcast, o tráfego de broadcast poderá ficar excessivo. O número de hosts e a quantidade de tráfego de rede que pode ser suportada na rede local são limitados pelos recursos dos switches usados para conectá-los. À medida que a rede cresce e mais hosts são adicionados, o tráfego de rede aumenta, inclusive o tráfego de broadcast. Para melhorar o desempenho, geralmente é necessário dividir uma rede local em várias redes (ou seja, domínios de broadcast), como mostrado na figura. Os roteadores são usados para dividir a rede em vários domínios de broadcast.

![[Pasted image 20240610114400.png]]










