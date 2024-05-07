#redes #cyber 
# Ataques DHCP

### Ataque de falsificação de DHCP

Um ataque de spoofing de DHCP ocorre quando um servidor DHCP invasor está conectado à rede e fornece falsos parâmetros de configuração IP aos clientes legítimos. Um servidor não autorizado pode fornecer uma variedade de informações enganosas:

- **Gateway padrão errado -** O ator da ameaça fornece um gateway inválido ou o endereço IP de seu host para criar um ataque MiTM. Isso pode não ser totalmente detectado, pois o invasor intercepta o fluxo de dados pela rede.
- **Servidor DNS errado -** O agente de ameaças fornece um endereço de servidor DNS incorreto, apontando o usuário para um site malicioso.
- **Endereço IP errado -** O agente de ameaças fornece um endereço IP inválido, um endereço IP de gateway padrão inválido ou ambos. O agente de ameaça cria um ataque de negação de serviço no cliente DHCP.

Suponha que um agente de ameaça tenha conectado com êxito um servidor DHCP não autorizado a uma porta de switch na mesma sub-rede que os clientes de destino. O objetivo do servidor não autorizado é fornecer aos clientes informações falsas de configuração de IP.

#### Cliente transmite mensagens de descoberta DHCP

Na figura, um cliente legítimo se conecta à rede e requer parâmetros de configuração de IP. O cliente transmite uma solicitação de descoberta de DHCP procurando uma resposta de um servidor DHCP. Ambos os servidores recebem a mensagem.

![[Pasted image 20240507162151.png]]

#### Servidor DHCP respondem com ofertas

A figura mostra como os servidores DHCP legítimos e o não autorizado, respondem com parâmetros de configuração de IP válidos. O cliente responde à primeira oferta recebida.

![[Pasted image 20240507162246.png]]

#### Cliente aceita solicitação DHCP não autorizada

Nesse cenário, o cliente recebeu a oferta não autorizada primeiro. Ele transmite uma solicitação DHCP, aceitando os parâmetros do servidor não autorizado, conforme mostrado na figura. Cada servidor legítimo e não autorizado recebem a solicitação.

![[Pasted image 20240507162350.png]]

#### DHCP não autorizado confirma a solicitação

No entanto, apenas o servidor não autorizado envia uma resposta ao cliente para confirmar sua solicitação, conforme mostrado na figura. O servidor legítimo para de se comunicar com o cliente porque a solicitação já foi confirmada.

![[Pasted image 20240507162440.png]]











