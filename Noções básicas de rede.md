#redes 
# Noções básicas de rede

Uma _rede_ é uma conexão entre dois ou mais computadores. Historicamente, os computadores conectados eram considerados um _servidor_ ou um _cliente_. Um servidor monitorava a comunicação para solicitações de entrada, e um cliente era qualquer computador que fazia solicitações a um servidor. Na computação moderna, essas definições se expandiram. Hoje, qualquer computador preparado para responder a solicitações de entrada pode ser considerado um servidor. Qualquer computador que faz uma solicitação a outro computador pode ser considerado um cliente. Na verdade, o mesmo computador pode atuar como servidor para alguns computadores e como cliente para outros.

#### Infraestrutura

O meio pelo qual a comunicação ocorre.

#### Protocolo

Uma linguagem comum que é usada para a comunicação.

#### Endereços

Um meio de encontrar e identificar outros computadores com os quais se comunicar.

### Infraestrutura

Tradicionalmente, as redes de computadores eram formadas por meio da rede mundial existente de linhas telefônicas. Atualmente, as linhas telefônicas continuam em uso, embora estejam gradualmente sendo suplantadas por cabos de fibra, que usam a luz para enviar dados a taxas mais rápidas do que os fios de cobre das linhas telefônicas. Para redes locais pequenas, as ondas de rádio são um meio de rede comum, chamado de _wi-fi_. Ao ingressar em uma rede wi-fi, você faz isso por meio de um _ponto de acesso_, como um roteador.

### Protocolo TCP/IP

Depois que um computador se conecta a uma rede, ele pode usar o _Transmission Control Protocol_ (_TCP_) e o _Internet Protocol_ (_IP_) para enviar mensagens pela rede. Há outros protocolos de comunicação, como o User Datagram Protocol (UDP) e o Real-time Transport Protocol (RTP), mas o TCP é projetado para confiabilidade. Depois que uma mensagem é enviada por TCP, o computador que recebe os dados envia uma confirmação de que recebeu a mensagem. Se o remetente não receber confirmação dentro de um período específico, o computador enviará os dados novamente.

Os dados são enviados em partes e remontados no lado receptor. O TCP lida com a fragmentação e a montagem de dados. O protocolo Internet Protocol (IP) transporta cada bloco de dados pela rede. Juntos, esses dois protocolos são conhecidos como _TCP/IP_. A combinação TCP/IP funciona como a base tecnológica das redes modernas, incluindo a Internet. A Internet recebeu esse nome devido à junção das palavras "redes interconectadas" (interconnected networks), porque ela conecta pequenas redes locais a uma grande rede.
































