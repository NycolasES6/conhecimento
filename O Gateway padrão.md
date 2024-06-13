#redes 
# O Gateway padrão

O método que um host utiliza para enviar mensagens para um destino em uma rede remota difere da forma como um host envia mensagens na mesma rede local. Quando um host precisa enviar uma mensagem para outro host localizado na mesma rede, ele pode encaminhar a mensagem diretamente. Um host usará o ARP para descobrir o endereço MAC do host de destino. O pacote IPv4 contém o endereço IPv4 de destino, encapsula o pacote em um quadro com o endereço MAC de destino e o encaminha para fora.

Quando um host precisa enviar uma mensagem para uma rede remota, ele deve usar o roteador. O host inclui o endereço IP do host de destino dentro do pacote, exatamente como antes. Entretanto, quando ele encapsula o pacote em um quadro, usa o endereço MAC do roteador como destino do quadro. Dessa forma, o roteador receberá e aceitará o quadro baseado no endereço MAC.

Como o host de origem determina o endereço MAC do roteador? Um host conhece o endereço IPv4 do roteador por meio do endereço de gateway padrão configurado em suas configurações de TCP/IP. O endereço do gateway padrão é o endereço da interface do roteador conectada à mesma rede local do host de origem. Todos os hosts na rede local usam o endereço do gateway padrão para enviar mensagens ao roteador. Quando o host conhece o endereço IPv4 do gateway padrão, ele pode usar o ARP para determinar o endereço MAC. O endereço MAC do roteador é colocado no quadro, destinado a outra rede.

É importante que o gateway padrão correto esteja configurado em cada host na rede local. Se não houver um gateway padrão definido nas configurações TCP/IP do host ou se estiver especificado um gateway padrão incorreto, não será possível entregar as mensagens endereçadas aos hosts nas redes remotas.

![[Pasted image 20240612100820.png]]

|PC|Endereço IPv4|Máscara de Sub-Rede|Gateway Padrão|
|---|---|---|---|
|H1|192.168.1.1|255.255.255.0|192.168.1.254|
|H2|192.168.1.2|255.255.255.0|192.168.1.254|
|H3|192.168.1.3|255.255.255.0|192.168.1.254|
