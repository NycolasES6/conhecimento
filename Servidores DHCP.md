#redes 
# Servidores DHCP

Se você inserir um hotspot sem fio em um aeroporto ou uma lanchonete, o DHCP possibilitará o acesso à Internet. Ao entrar na área, o cliente DHCP de seu laptop entra em contato com o servidor DHCP local via conexão sem fio. O servidor DHCP atribui um endereço IPv4 ao seu notebook.

Vários tipos de dispositivos podem ser servidores DHCP, desde que executem software de serviço DHCP. Na maioria das redes médias a grandes, o servidor DHCP normalmente é um servidor local dedicado baseado em PC.

Nas redes residenciais, é provável que o servidor DHCP esteja localizado no ISP. Um host na rede residencial recebe a configuração IPv4 diretamente do ISP, como mostrado na figura.

![[Pasted image 20240529113628.png]]

Muitas redes de residências e pequenas empresas usam um modem e um roteador sem fio. Nesse caso, o roteador sem fio é tanto servidor como cliente DHCP. O roteador sem fio atua como cliente para receber a configuração de IPv4 do ISP e atua como servidor DHCP para hosts internos na rede local. O roteador recebe o endereço IPv4 público do ISP e, em sua função como servidor DHCP, distribui endereços privados para os hosts internos.

Além de servidores baseados em PC e roteadores sem fio, outros tipos de dispositivos de rede (como roteadores dedicados) podem fornecer serviços DHCP aos clientes, embora isso não seja tão comum.

![[Pasted image 20240610085413.png]]