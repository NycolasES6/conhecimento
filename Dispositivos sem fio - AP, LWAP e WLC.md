#redes 
# Dispositivos sem fio - AP, LWAP e WLC

Uma implementação comum de dados sem fio permite que dispositivos se conectem sem fio por meio de uma LAN. Em geral, uma LAN sem fio requer pontos de acesso sem fio e clientes que possuem NICs sem fio. Os roteadores sem fio doméstico e de pequenas empresas integram as funções de um roteador, comutador e ponto de acesso em um dispositivo, conforme mostrado na figura. Observe que em redes pequenas, o roteador sem fio pode ser o único AP porque apenas uma área pequena requer cobertura sem fio. Em redes maiores, pode haver muitos APs.

![[Pasted image 20240510112738.png]]

Todas as funções de controle e gerenciamento dos APs em uma rede podem ser centralizadas em um Wireless LAN Controller (WLC). Ao usar uma WLC, os APs não atuam mais de forma autônoma, mas atuam como APs leves (LWAPs). Os LWAPs apenas encaminham dados entre a LAN sem fio e o WLC. Todas as funções de gerenciamento, como definição de SSIDs e autenticação, são conduzidas na WLC centralizada, em vez de em cada AP individual. Um grande benefício da centralização das funções de gerenciamento de AP na WLC é a configuração simplificada e o monitoramento de vários pontos de acesso, entre muitos outros benefícios.



















