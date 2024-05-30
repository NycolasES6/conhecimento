# introdução a redes TCP IP

Redes de computadores pode ser definida como a comunicação entre dois ou mais computadores

- **Host** - Nome atribuído a um computador na rede, pode ser um host cliente ou um host servidor
- **Servidor** - Fornece algum serviço a rede
- **Cliente** - Consome algum serviço oferecido por um servidor

## Protocolos

Garantem que diferentes computadores usando diferentes hardwares e softwares consigam se comunicar

Exemplo de protocolo de rede: TCP/IP

A comunicação só ocorre pois existe um protocolo, no qual, ambos os lados compreendem.

## Endereços Físicos e Lógicos e Portas

Endereço físico é conhecido como MAC Address e vem definido de fábrica.

Endereço lógico é atribuído ao adaptador de rede de acordo com a rede.

Cada serviço ativo usa uma porta de identificação

#### Cliente

- Endereço MAC: a4:5e:60:b8:c1:af (placa de rede)
- Endereço IP: 192.168.0.192
- Porta: 50234

#### Servidor (WEB)

- Endereço MAC: 00:0C:29:76:43:E1
- Endereço IP: 192.168.0.200
- Porta: 80

## Endereço Físico (MAC Address)

Formado por uma sequência de 6 bytes

A4:5E:60:B8:C1:AF -> A4:5E:60 **-** B8:C1:AF

## IP Lógico (IP address)

O endereço IP é formado por 4 octetos representados de forma decimal.

Existem várias classificações de endereços IP e cada uma serve para definir o uso em uma rede de acordo com a necessidade.

![[Pasted image 20240527183210.png]]

- Exemplo de máscara de rede: 255.255.255.0

#### 192.168.0.200

- **rede** - 192.168.0
- **host** - 200

## Roteamento

Redes diferentes só se enxergam através do roteamento de rede, para isso precisam definir um gateway.

![[Pasted image 20240527183547.png]]

## Portas

As portas vão de 0 até 65535 e normalmente são utilizadas com os protocolos TCP e  UDP.

![[Pasted image 20240527183745.png]]

#### Socket
**IP**:PORTA
**192.168.0.200**:8080















