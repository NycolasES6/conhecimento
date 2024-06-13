#redes 
# Roteadores como gateway

O roteador fornece um gateway pelo qual os hosts de uma rede podem se comunicar com hosts de diferentes redes. Cada interface em um roteador está conectada a uma rede separada.

O endereço IPv4 atribuído à interface identifica a rede local que está diretamente conectada a ele.

Todo host de uma rede deve usar o roteador como um gateway para outras redes. Portanto, cada host deve conhecer o endereço IPv4 da interface do roteador conectada à rede na qual o host está conectado. Esse endereço é conhecido como endereço de gateway padrão. Ele pode ser configurado estaticamente no host ou recebido dinamicamente por DHCP.

Quando um roteador sem fio está configurado para ser um servidor DHCP da rede local, ele envia automaticamente o endereço IPv4 correto da interface para os hosts como o endereço de gateway padrão. Dessa forma, todos os hosts na rede podem usar o endereço IPv4 para encaminhar mensagens aos hosts localizados no ISP e obter acesso a hosts na Internet. Os roteadores sem fio geralmente são definidos para serem servidores DHCP por padrão.

O endereço IPv4 dessa interface do roteador local passa a ser o endereço de gateway padrão para a configuração do host. O gateway padrão é fornecido estaticamente ou por DHCP.

Quando um roteador sem fio está configurado como servidor DHCP, ele fornece seu próprio endereço IPv4 interno como gateway padrão aos clientes DHCP. Também fornece a eles seu endereço IPv4 e sua máscara de sub-rede, como mostrado na figura.

![[Pasted image 20240610102207.png]]













