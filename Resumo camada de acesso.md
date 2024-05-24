#redes #CISCO
# Resumo camada de acesso

## Encapsulamento e o quadro Ethernet

O processo de colocar um formato de mensagem dentro de outro formato de mensagem é chamado de encapsulamento. O desencapsulamento ocorre quando o processo é invertido pelo destinatário e a carta é retirada do envelope. Assim como uma carta é colocada dentro de um envelope para ser entregue, no caso das mensagens de computador, elas são encapsuladas. Uma mensagem enviada por uma rede de computadores segue regras específicas de formato para que seja entregue e processada.

Os padrões do protocolo Ethernet definem muitos aspectos da comunicação de rede, como o formato e o tamanho do quadro, a temporização e a codificação. O formato dos quadros Ethernet especifica a localização dos endereços MAC de destino e de origem e informações adicionais, incluindo preâmbulo para sequenciamento e temporização, início do delimitador de quadro, comprimento e tipo de quadro e sequência de verificação de quadro para detectar erros de transmissão.

## A camada de acesso

É a parte da rede em que as pessoas recebem acesso a outros hosts e a arquivos compartilhados e impressoras. A camada de acesso atua como a primeira linha nos dispositivos de rede que conectam hosts à rede Ethernet com fio. Em uma rede Ethernet, cada host pode se conectar diretamente a um dispositivo de rede da camada de acesso usando um cabo Ethernet. Os hubs Ethernet contêm várias portas que são usadas para conectar hosts à rede. Apenas uma mensagem de cada vez pode ser enviada por um hub Ethernet. Duas ou mais mensagens enviadas ao mesmo tempo causarão um colisão. Como retransmissões excessivas podem congestionar a rede e reduzir o tráfego, os hubs passaram a ser considerados obsoletos e foram substituídos por switches Ethernet.

Um switch Ethernet é um dispositivo usado na camada 2. Quando um host envia uma mensagem para outro host conectado à mesma rede comutada, o switch aceita e decodifica os quadros para ler a parte do endereço MAC da mensagem. Uma tabela no switch, chamada de tabela de endereços MAC, contém uma lista de todas as portas ativas e dos endereços MAC de host conectados a elas. Quando uma mensagem é enviada entre hosts, o switch verifica se o endereço MAC de destino está na tabela. Se estiver, o switch criará uma conexão temporária, chamada de circuito, entre as portas de origem e de destino. Os switches Ethernet também permitem o envio e o recebimento de quadros no mesmo cabo Ethernet simultaneamente. Isso melhora o desempenho da rede eliminando colisões.

Um switch cria a tabela de endereços MAC examinando o endereço MAC de origem de cada quadro enviado entre hosts. Quando um novo host envia uma mensagem ou responde a uma mensagem inundada, o switch descobre imediatamente o endereço MAC e a porta à qual ele está conectado. A tabela é atualizada dinamicamente toda vez que um novo endereço MAC de origem é lido pelo switch.























