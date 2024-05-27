# Composição de um protocolo de rede

A maioria dos protocolos de rede sçao compostos por um cabeçalho e uma área de dados.

![[Pasted image 20240527185506.png]]

**Header** - Cada header tem uma estrutura específica.
**Payload** - Contém as informações que o protocolo carrega

## Modelos de referência

### OSI

| OSI          |
| ------------ |
| Aplicação    |
| Apresentação |
| Sessão       |
| Transporte   |
| Rede         |
| Enlace       |
| Física       |

### TCP/IP

| TCP/IP        |
| ------------- |
| Aplicação     |
| Transporte    |
| Internet      |
| Acesso a rede |

## Exemplo de encapsulamento

Um **frame** ethernet contém um **pacote** IP que contém um segmento **TCP** que contém os **dados** com o protocolo http.


| PROTOCOLO HTTP |
| -------------- |

| Header TCP | Payload TCP |
| ---------- | ----------- |

| Header IP | Payload TCP |
| --------- | ----------- |

| Header IP | Payload IP |
| --------- | ---------- |

| Header Ethernet | Payload Ethernet |
| --------------- | ---------------- |

## Exemplo

Para que uma simples comunicação abaix






















