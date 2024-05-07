#cyber #redes 

# Vulnerabilidades ARP

Os hosts transmitem uma solicitação ARP para outros hosts no segmento de rede para determinar o endereço MAC de um host com um endereço IP específico. Todos os hosts na sub-rede recebem e processam a solicitação ARP. O host com o endereço IP correspondente na solicitação ARP envia uma resposta ARP.

Qualquer cliente pode enviar uma resposta ARP não solicitada denominada "ARP gratuito". Isso geralmente é feito quando um dispositivo é inicializado para informar todos os outros dispositivos na rede local o endereço MAC do novo dispositivo. Quando um host envia um ARP gratuito, outros hosts na sub-rede armazenam o endereço MAC e o endereço IP contidos no ARP gratuito em suas tabelas ARP.

No entanto, esse recurso do ARP também significa que qualquer host pode reivindicar ser o proprietário de qualquer IP / MAC que escolher. Um ator de ameaça pode envenenar o cache ARP de dispositivos na rede local, criando um ataque MiTM para redirecionar o tráfego. O objetivo é associar o endereço MAC do ator de ameaça ao endereço IP do gateway padrão nos caches ARP dos hosts no segmento LAN. Isso posiciona o agente de ameaça entre a vítima e todos os outros sistemas fora da sub-rede local.




























