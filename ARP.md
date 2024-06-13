#redes 
# ARP

O ARP usa um processo de três etapas para descobrir e armazenar o endereço MAC de um host na rede local quando apenas o endereço IPv4 do host é conhecido.

1. O host remetente cria e envia um quadro destinado ao endereço MAC de broadcast. Incluído no quadro, está uma mensagem com o endereço IPv4 do host do destino a ser alcançado.
2. Cada host na rede recebe o quadro de broadcast e compara o endereço IPv4 na mensagem com o endereço IPv4 configurado. O host com o endereço IPv4 correspondente envia o endereço MAC de volta para o host emissor original.
3. O host emissor recebe a mensagem e armazena informações do endereço IPv4 e do endereço MAC em uma tabela chamada de tabela ARP.

Quando o host emissor tem o endereço MAC do host de destino em sua tabela ARP, ele pode enviar quadros diretamente ao destino sem fazer uma solicitação ARP. Como as mensagens ARP dependem de quadros de broadcast para entregar as solicitações, todos os hosts na rede IPv4 local devem estar no mesmo domínio de broadcast.