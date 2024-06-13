#cyber 
# Balanceamento de carga

O balanceamento de carga envolve a distribuição do tráfego entre dispositivos ou caminhos de rede para evitar recursos de rede sobrecarregados com muito tráfego. Se existirem recursos redundantes, um algoritmo ou dispositivo de balanceamento de carga funcionará para distribuir o tráfego entre esses recursos, conforme mostrado na figura.

Uma maneira de fazer isso na internet é através de várias técnicas que usam DNS para enviar tráfego para recursos que têm o mesmo nome de domínio, mas vários endereços IP. Em alguns casos, a distribuição pode ser para servidores que são distribuídos geograficamente. Isso pode resultar em uma única transação de Internet sendo representada por vários endereços IP nos pacotes de entrada. Isso pode fazer com que recursos suspeitos apareçam em capturas de pacotes. Além disso, alguns dispositivos do gerenciador de balanceamento de carga (LBM) usam testes para testar o desempenho de diferentes caminhos e a integridade de diferentes dispositivos. Por exemplo, um LBM pode enviar testes para os diferentes servidores para os quais ele está balanceando o tráfego de carga, a fim de detectar que os servidores estão operando. Isso é feito para evitar o envio de tráfego para um recurso que não está disponível. Esses testes podem parecer tráfego suspeito se o analista de segurança cibernética não estiver ciente de que esse tráfego faz parte da operação do LBM.

## Balanceamento de carga com delegação DNS

![[Pasted image 20240611082340.png]]






























