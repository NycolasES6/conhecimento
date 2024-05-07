#redes 

# Serviços TCP

O TCP fornece estes serviços:

- **Entrega confiável -** O TCP incorpora reconhecimentos para garantir a entrega, em vez de depender de protocolos de camada superior para detectar e resolver erros. Se uma confirmação não for recebida à tempo, o remetente retransmitirá os dados. Exigir reconhecimentos dos dados recebidos pode causar atrasos substanciais. Exemplos de protocolos da camada de aplicação que usam a confiabilidade do TCP incluem HTTP, SSL / TLS, FTP, transferências de zona DNS e outros.
- **Controle de fluxo -** TCP implementa controle de fluxo para resolver esse problema. Em vez de reconhecer um segmento de cada vez, vários segmentos podem ser reconhecidos com um único segmento de reconhecimento.
- **Comunicação stateful -** A comunicação com estado do TCP entre duas partes ocorre durante o handshake de três vias do TCP. Antes que os dados possam ser transferidos usando o TCP, um aperto de mãos triplo abre a conexão TCP, conforme mostrado na figura. Se ambos os lados concordarem com a conexão TCP, os dados poderão ser enviados e recebidos por ambas as partes usando o TCP.

**Aperto de mão de três vias TCP**

![[Pasted image 20240507132911.png]]

A conexão TCP é estabelecida em três etapas:

1. O cliente iniciador requisita uma sessão de comunicação cliente-servidor com o servidor.
2. O servidor reconhece a sessão de comunicação cliente-servidor e solicita uma sessão de comunicação servidor-cliente.
3. O cliente inicial reconhece a sessão de comunicação servidor-cliente.












