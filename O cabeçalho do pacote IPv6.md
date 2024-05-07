#redes

# O cabeçalho do pacote IPv6

Há oito campos no cabeçalho do pacote IPv6, como mostrado na figura.

**Cabeçalho do Pacote IPv6**

![[Pasted image 20240507112208.png]]

**Expanda o texto abaixo para saber mais sobre os campos no cabeçalho do pacote IPv6.**

### Versão

- Este campo contém um valor binário de 4 bits definido como 0110 que o identifica como um pacote IPv6.

### Classe te tráfego

- Este campo de 8 bits é equivalente ao campo IPv4 Differentiated Services (DS).

### Rótulo de fluxo

- Este campo de 20 bits sugere que todos os pacotes com o mesmo rótulo de fluxo recebem o mesmo tipo de tratamento pelos roteadores.

### Tamanho da carga

- Este campo de 16 bits indica o comprimento da porção de dados ou carga útil do pacote IPv6.

### Próximo cabeçalho

- Este campo de 8 bits é equivalente ao campo do protocolo IPv4.
- Ele exibe o tipo de carga de dados que o pacote está carregando, permitindo que a camada de rede transfira os dados para o protocolo apropriado das camadas superiores.

### Limite de saltos

- Este campo de 8 bits substitui o campo TTL IPv4.
- Esse valor é subtraído de um por cada roteador que encaminha o pacote.
- Quando o contador chega a 0, o pacote é descartado e uma mensagem ICMPv6 de Tempo Excedido é encaminhada ao host emissor, indicando que o pacote não atingiu seu destino por causa do limite de saltos.

### Endereçamento IPv6 Origem

- Este campo de 128 bits identifica o endereço IPv6 do host de envio.

### Endereçamento IPv4 Destino

- Este campo de 128 bits identifica o endereço IPv6 do host receptor.

Um pacote IPv6 também pode conter cabeçalhos de extensão (EH) que fornecem informações opcionais da camada de rede. Opcionais, os cabeçalhos de extensão ficam posicionados entre o cabeçalho IPv6 e a carga. EHs são usados para fragmentação, segurança, suporte à mobilidade e muito mais.

Ao contrário de IPv4, os roteadores não fragmentam os pacotes IPv6 roteados.













