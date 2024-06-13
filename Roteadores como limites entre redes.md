#redes 
# Roteadores como limites entre redes

O roteador sem fio atua como servidor DHCP para todos os hosts locais conectados a ele, por cabo de Ethernet ou sem fio. Esses hosts locais estão localizados em uma rede interna. A maioria dos servidores DHCP são configurados para atribuir endereços privados aos hosts na rede interna, em vez de endereços públicos roteáveis da Internet. Isso garante que, por padrão, a rede interna não possa ser acessada diretamente da Internet.

O endereço IPv4 padrão configurado na interface do roteador local sem fio geralmente é o primeiro endereço de host naquela rede. Os hosts internos devem receber endereços dentro da mesma rede do roteador sem fio, sejam eles configurados estaticamente ou através do DHCP. Quando configurado como um servidor DHCP, o roteador sem fio fornece endereços nesse intervalo. Ele também fornece informações de máscara de sub-rede e seu próprio endereço IPv4 da interface como gateway padrão, como mostrado na figura.

Muitos ISPs usam o servidor DHCP para fornecer endereços IPv4 do lado de Internet do roteador sem fio localizado nas instalações de clientes. A rede atribuída ao lado de Internet do roteador sem fio é conhecida como rede externa.

Quando um roteador sem fio está conectado a um ISP, ele atua como um cliente DHCP para receber o endereço IPv4 correto de rede externa para a interface de Internet. Os ISPs normalmente fornecem um endereço roteável pela Internet, o que permite que os hosts conectados ao roteador sem fio tenham acesso à Internet.

O roteador sem fio serve como limite entre a rede interna local e a Internet externa.

![[Pasted image 20240610102505.png]]













