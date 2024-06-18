# Protocolo - ICMP
O protocolo ICMP é um protocolo de alertas por mensagens, ele emite avisos sobre a situação da rede.

A estrutura básica do ICMP é simples, composta de tipos e códigos, cada um coma sua função

![[Pasted image 20240618114014.png]]

## Tipos e códigos ICMP

Existem vários tipos e códigos, mas vamos nos concentrar nos principais.

![[Pasted image 20240618114041.png]]

## A importância do ICMP

No exemplo abaixo temos o host cliente utilizando o protocolo UDP tentando se comunicar por uma porta fechada no host servidor.

Lembrando que o protocolo UDP não possui nenhum tipo de controle, dessa forma o protocolo UDP sozinho não tem capacidade de avisar sobre o que acontece na comunicação.

![[Pasted image 20240618115018.png]]