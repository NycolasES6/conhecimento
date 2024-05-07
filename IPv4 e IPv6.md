#redes 

# IPv4 e IPv6

O IP foi projetado como um protocolo sem conexão de Camada 3. Ele fornece as funções necessárias para entregar um pacote de um host de origem a um host de destino por meio de um sistema interconectado de redes. O protocolo não foi projetado para rastrear e gerenciar o fluxo de pacotes. Essas funções, se necessárias, são executadas principalmente pelo TCP na camada 4.

O IP não faz nenhum esforço para validar se o endereço IP de origem contido em um pacote realmente veio dessa origem. Por esse motivo, os agentes de ameaças podem enviar pacotes usando um endereço IP de origem falsificado. Além disso, os agentes da ameaça podem adulterar os outros campos do cabeçalho IP para realizar seus ataques. Portanto, é importante que os analistas de segurança entendam os diferentes campos dos cabeçalhos IPv4 e IPv6.