#redes 
# Modo de Descoberta Passiva e Ativa

Os dispositivos sem fio devem descobrir e conectar-se a um ponto de acesso ou roteador sem fio. Os clientes sem fio se conectam ao ponto de acesso usando um processo de verificação (verificação). Este processo pode ser passivo ou ativo.

## Modo Passivo

No modo passivo, o ponto de acesso anuncia abertamente seu serviço enviando periodicamente quadros de beacon de transmissão contendo o SSID, padrões suportados e configurações de segurança. O objetivo principal do beacon é permitir que os clientes sem fio aprendam quais redes e pontos de acesso estão disponíveis em uma determinada área. Isso permite que os clientes sem fio escolham qual rede e ponto de acesso usar.

## Modo Ativo

No modo ativo, os clientes sem fio devem saber o nome do SSID. O cliente sem fio inicia o processo transmitindo um quadro de solicitação de análise em vários canais. A solicitação de análise inclui o nome SSID e os padrões suportados. Os pontos de acesso configurados com o SSID enviarão uma resposta do probe que inclui o SSID, os padrões suportados e as configurações de segurança. O modo ativo pode ser necessário se um ponto de acesso ou roteador sem fio estiver configurado para não transmitir quadros de beacon.

Um cliente sem fio também pode enviar uma solicitação de análise sem um nome SSID para descobrir redes WLAN próximas. Os pontos de acesso configurados para transmitir quadros de beacon responderiam ao cliente sem fio com uma resposta do probe e forneceriam o nome SSID. Os pontos de acesso com o recurso SSID de transmissão desativado não respondem.



































