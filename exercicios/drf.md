```
(config) # vlan 20
```
cria vlan com id de 20


```
# show vlan
```
mostra as vlans


## VTP SERVER

### sw vtp server
vtp mode server
vtp domain vtpserver.com

vlan 10
name VLAN10

interface range fastEthernet 0/23-24
switchport mode trunk

vtpServer#show vlan brief

vtpServer#show interfaces trunk











https://www.cisco.com/c/pt_br/support/docs/lan-switching/vtp/10558-21.html


https://www.cisco.com/c/pt_br/support/docs/lan-switching/vtp/98154-conf-vlan.html


https://harrymaq.medium.com/l2-mock-lab-vtp-dhcp-server-intervlan-routing-wan-failover-ipsla-2fe9e6f684f8



