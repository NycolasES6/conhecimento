#redes #CISCO #questionario
# Conceitos básicos de rede CISCO - 11_questionário sobre Endereçamento dinâmico com DHCP

#### 1 - Faça a correspondência de cada descrição com um endereço IP apropriado.

- um cliente inicia uma mensagem para encontrar um servidor DHCP - DHCP DISCOVER
- O cliente aceita o endereço IP fornecido pelo servidor DHCP - DHCP REQUEST
- um servidor DHCP responde à solicitação inicial de um cliente - DHCP OFFER
- O servidor DHCP confirma que a concessão de endereço foi aceita - DHCP ACK

#### 2 - Quais são os dois motivos que geralmente tornam o DHCP o método preferido de atribuição de endereços IP a hosts em redes grandes? (Escolha duas.)

- Ele elimina a maioria dos erros de configuração de endereço
- Isso reduz a carga sobre a equipe de suporte de rede.

#### 3 - Qual mensagem um host IPv4 usa para responder quando recebe uma mensagem DHCPOFFER de um servidor DHCP?

- DHCP REQUEST

#### 4 - Qual endereço IPv4 destino é usado pelo cliente DHCPv4 para enviar o pacote DHCP Discover inicial quando o cliente está procurando um servidor DHCP?

- 255.255.255.255

#### 5 - Que tipo de pacote é enviado por um servidor DHCP após receber uma mensagem de DHCP Discover?

- DHCP OFFER

#### 6 - Qual é a vantagem de usar o DHCP para atribuir endereços a dispositivos móveis?

- As concessões de endereço são temporárias e retornam ao pool quando o dispositivo é desligado.

#### 7 - Consulte a figura. O roteador doméstico está configurado como um servidor DHCP. A faixa de endereços IP está configurado para ser 192.168.0.100 - 149.  Qual endereço IP será atribuído automaticamente ao primeiro dispositivo que se conecta ao roteador sem fio?

![[Pasted image 20240610090747.png]]

 - 192.168.0.100

#### 8 - Consulte a figura. PC1 foi configurado para obter um endereço IP dinâmico de um servidor DHCP O PC1 foi desligado por duas semanas. Quando o PC1 inicializa e tenta solicitar um endereço IP disponível, qual endereço IP de destino o PC1 colocará no cabeçalho IP?

![[Pasted image 20240610090824.png]]

- 255.255.255.255

#### 9 - Que tipo de servidor atribui dinamicamente um endereço IP a um host?

- DHCP

#### 10 - Quais das três instruções descrevem uma mensagem de descoberta de DHCP? (Escolha três.)

- O endereço IP de destino é 255.255.255.255
- Todos os hosts recebem a mensagem, mas apenas um servidor DHCP responde.
- A mensagem vem de um cliente que procura um endereço IP.

#### 11 - Um PC está tentando conceder um endereço através do DHCP. Que mensagem é enviada pelo servidor para que o cliente saiba que é capaz de usar as informações de IP fornecidas?

- DHCP ACK
