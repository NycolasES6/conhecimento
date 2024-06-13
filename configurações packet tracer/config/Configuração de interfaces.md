```
Router#>show ip interface brief

Interface IP-Address OK? Method Status Protocol

GigabitEthernet0/0 unassigned YES unset administratively down down

GigabitEthernet0/1 unassigned YES unset administratively down down

GigabitEthernet0/2 unassigned YES unset administratively down down

Vlan1 unassigned YES unset administratively down down
```
Mostra as interfaces de rede

```
Router (config) #interface GigabitEthernet0/0
```
Diz que queremos configurar esta interface. Vai entrar no modo de configuração de interface

```
Router (config-if) #no shutdown
```
Habilita a interface

```
Router (config-if) #ip address 10.0.0.1 255.255.255.0
```
Atribui um endereço ip e uma máscara para a interface
















