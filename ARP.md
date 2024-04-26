#redes #protocolo 

# Protocolo ARP

O ARP tem habilidade de descobrir qual [[endereço físico(Mac address)]] está associado a um determinado [[endereço lógico (IP address)]].

Para fazer isso o ARP utiliza os famosos ARP Request e ARP Reply

ARP Request pergunta quem tem um determinado IP e qual o seu endereço MAC.

ARP Reply é a resposta enviada pelo host que tem o IP requisitado, ao responder ao ARP Request o host envia seu endereço MAC.

O host que recebe a resposta armazena o IP e MAC por um tempo.

```sh
arp -an
```

Mostra a nossa tabela ARP