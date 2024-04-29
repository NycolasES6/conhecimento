#linux #redes 

# gerenciar rede no linux

[[linux]] por ser um sistema mais adaptável, pode ser configurado de maneira rápida

```sh
ifconfig
```

Mostra as configurações do [[adaptador de rede]].

```sh
ifconfig eth0 10.1.1.23 netmask 255.255.255.0
```

Configura uma nova interface temporária, pois quando reiniciar o sistema perde-se esta configuração

```sh
vim /etc/network/interfaces
```

Altera o arquivo das interfaces de rede do sistema;

#### /etc/network /interfaces
```sh
auto eth0
iface eth0 inet static
address 192.168.0.200
netmask 255.255.255.0
gateway 192.168.0.1
```

Assim quando reiniciarmos, ele salvará as configurações da [[interface]]

```sh
service networking restart
```

ou

```sh
/etc/init.d/networking restart
```

Reinicia o [[adaptador de rede]]

```sh
route
```

Mostra a tabela de roteamento

```sh
route -n
```

Vai mostrar o IP do [[gateway ]]

```sh
route del default
```

Deleta o gateway default

```sh
route add default gw 192.168.0.1
```

Assim adicionamos novamente o gateway padrão

```sh
netstat -lt
```

Exibe os serviços executando em porta [[tcp]]

```sh
netstat -lu
```

Exibe os serviços executando em porta [[udp]]

```sh
netstat -lnt
```

**n** : Exibe pelo número da porta

```sh
netstat -lntp
```

**p** : Exibe o nome do programa 














