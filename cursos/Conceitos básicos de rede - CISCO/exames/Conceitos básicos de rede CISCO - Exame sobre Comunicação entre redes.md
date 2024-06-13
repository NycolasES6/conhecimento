#redes #CISCO #exame #questionario #anki 
# Conceitos básicos de rede CISCO - Exame sobre O protocolo da Internet

#### 1 - Que tipo de endereço pode ser compartilhado por meio de NAT para permitir que dispositivos de uma rede doméstica enviem e recebam dados pela Internet?

- endereço IP público registrado

#### 2 - Um administrador de rede investiga um problema de usuário. O usuário pode acessar hosts na mesma rede, mas não consegue se comunicar com redes remotas. O administrador da rede tenta pingar o endereço do gateway configurado no dispositivo host e não consegue. Qual é a causa mais provável do problema?

- O endereço de gateway padrão está incorreto.

#### 3 - Qual é o resultado se o endereço de gateway padrão for configurado incorretamente em um PC?

- O PC pode se comunicar com dispositivos na mesma rede, mas não com aqueles em redes remotas.

#### 4 - O que ocorrerá se o endereço de gateway padrão estiver incorretamente configurado em um host?

- O host não poderá se comunicar com hosts de outras redes.

#### 5 - Uma rede doméstica está usando NAT no roteador, conectando-a à Internet. Os PCs na rede doméstica recebem endereços IP privados via DHCP. Quando um PC envia um pacote para um servidor web na internet, qual é o endereço IP de origem do cabeçalho do pacote que chega ao servidor web?

- um endereço IP público registrado atribuído à interface externa do roteador

#### 6 - Quando uma LAN está conectada à Internet por meio de um roteador sem fio, como os dispositivos na LAN se comunicam com a Internet usando NAT?

- Todos os dispositivos devem compartilhar um único endereço IPv4 público, atribuído ao roteador sem fio, para se comunicar com a Internet via NAT.

#### 7 - Consulte a figura. Os switches têm uma configuração padrão. O host A precisa se comunicar com o host D, mas o host A não tem o endereço MAC do gateway padrão. Quais dispositivos de rede receberão a solicitação ARP enviada pelo host A?

![[Pasted image 20240612115308.png]]

- somente os hosts B, C e o roteador R1

#### 8 - Um host precisa acessar outro host em uma rede remota, mas o cache ARP não tem entradas de mapeamento. Para qual endereço de destino o host enviará uma solicitação ARP?

- o endereço MAC de broadcast

#### 9 - Qual é o função do ARP em uma rede IPv4?

- obter um endereço MAC específico quando um endereço IP é conhecido

#### 10 - Qual protocolo é usado por um computador para descobrir o endereço MAC do gateway padrão em uma rede Ethernet?

- ARP

#### 11 - Que ação o processo ARP executa quando um host precisa criar um quadro, mas o cache ARP não contém um mapeamento de endereço?

- O processo ARP envia uma solicitação ARP para o endereço de broadcast Ethernet para descobrir o endereço MAC do dispositivo de destino.

#### 12 - A tabela ARP em um switch mapeia quais dois tipos de endereço juntos?

- Endereço de camada 3 para um endereço de camada 2

#### 13 - Qual endereço de destino é usado em um quadro de solicitação ARP?

- FFFF.FFFF.FFFF

#### 14 - Por que é importante que o roteador mantenha uma tabela de roteamento precisa?

- para determinar o melhor caminho para chegar à rede de destino

#### 15 - Quais são as duas funções de um roteador? (Escolha duas.)

- [x] Um roteador conecta várias redes IP.
- [x] Ele determina o melhor caminho para o envio de pacotes
- [ ] Ele controla o fluxo de dados por meio do uso de endereços da Camada 2.
- [ ] Ele cria uma tabela de roteamento com base nas solicitações ARP.
- [ ] Ele proporciona segmentação na Camada 2.

#### 16 - Quando um roteador recebe um pacote, quais informações devem ser analisadas para que o pacote seja encaminhado a um destino remoto?

- Endereço IP destino

#### 17 - Consulte a figura. O que o roteador faz depois de determinar que um pacote de dados da Rede 1 deve ser encaminhado para a Rede 2?

![[Pasted image 20240612115508.png]]

- Ele remonta o quadro com endereços MAC diferentes do quadro original.

#### 18 - Quais duas funções são funções principais de um roteador? (Escolha duas.)

- [x] seleção de caminho
- [x] encaminhamento de pacotes
- [ ] Atribuição de endereço MAC
- [ ] resolução de nomes de domínio

#### 19 - Consulte a figura. Considere a configuração do endereço IP mostrada a partir do PC1. Qual afirmação descreve o endereço de gateway padrão?

![[Pasted image 20240612115554.png]]

- É o endereço IP da interface Router1 conectada à LAN de PC1.

#### 20 - Qual parte do endereço da camada de rede um roteador usa para encaminhar pacotes?

- parte da rede

