#redes 
# O comando ipconfig

Quando um dispositivo não tem um endereço IP ou tem uma configuração de IP incorreta, ele não pode se comunicar na rede local nem acessar a Internet. Em dispositivos do Windows, você pode ver informações de configuração de IP com **o comando ipconfig** no prompt de comando. O **comando ipconfig** tem várias opções úteis, incluindo **/all**, **/release** e **/renew**.

## ipconfig

O **comando ipconfig** é usado para exibir as informações de configuração de IP atuais de um host. A emissão deste comando a partir do prompt de comando exibirá as informações básicas de configuração, incluindo endereço IP, máscara de sub-rede e gateway padrão.

```powershell
C:\> ipconfig

Windows IP Configuration

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected

   Connection-specific DNS Suffix . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix . : lan

   Link-local IPv6 Address . . . . . : fe80 :: a1cc: 4239: d3ab: 2675% 6

   IPv4 Address. . . . . . . . . . . : 10.10.10.130

   Subnet Mask . . . . . . . . . . . : 255.255.255.0

   Default Gateway . . . . . . . . . : 10.10.10.1

C:\>
```

## ipconfig/all

O comando **ipconfig /all** exibe informações adicionais que incluem o endereço MAC, os endereços IP do gateway padrão e os servidores DNS. Ele também indica se o DHCP está ativado, o endereço do servidor DHCP e as informações da concessão.

Como esse utilitário ajuda no processo de solução de problemas? Sem uma configuração de IP apropriada, o host não pode participar da comunicação em uma rede. Se o host não souber o local dos servidores DNS, ele não poderá converter nomes em endereços IP.

```powershell
C:\> ipconfig/all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : your-a9270112e3

   Primary Dns Suffix . . . . . . . :

   Node Type . . . . . . . . . . . . : Hybrid

   IP Routing Enabled. . . . . . . . : Não

   WINS Proxy Enabled. . . . . . . . : Não

   DNS Suffix Search List. . . . . . : lan

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected

   Connection-specific DNS Suffix . :

   Description . . . . . . . . . . . : Realtek PCIe GBE Family Controller

   Physical Address. . . . . . . . . : 00-16-D4-02-5A-EC

   DHCP Enabled. . . . . . . . . . . : Yes

   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix . : lan

   Description . . . . . . . . . . . : Intel (R) banda dupla Wireless-AC 3165

   Physical Address. . . . . . . . . : 00-13-02-47-8C-6A

   DHCP Enabled. . . . . . . . . . . : Yes

   Autoconfiguration Enabled . . . . : Yes

   Link-local IPv6 Address . . . . . : fe80 :: a1cc: 4239: d3ab: 2675% 6 (Preferencial)

   IPv4 Address. . . . . . . . . . . : 10.10.10.130 (preferencial)

   Subnet Mask . . . . . . . . . . . : 255.255.255.0

   Lease Obtained. . . . . . . . . . : Wednesday, September 2, 2020 10:03:43 PM

   Lease Expires . . . . . . . . . . : Friday, September 11, 2020 10:23:36 AM

   Default Gateway . . . . . . . . . : 10.10.10.1

   DHCP Server . . . . . . . . . . . : 10.10.10.1

   DHCPv6 IAID . . . . . . . . . . . : 98604135

   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1E-21-A5-84-44-A8-42-FC-0D-6F

   DNS Servers . . . . . . . . . . . : 10.10.10.1

   NetBIOS over Tcpip. . . . . . . . : Enabled

C:\>
```

## ipconfig/release e ipconfig/renew

Se as informações de endereçamento IP forem atribuídas dinamicamente, o comando **ipconfig /release** liberará as ligações DHCP atuais. **ipconfig /renew** solicitará novas informações de configuração ao servidor DHCP. Um host pode conter informações de configuração de IP desatualizadas ou com falhas. Com uma simples renovação dessas informações, a conectividade pode ser recuperada.

Se, após a liberação da configuração IP o host não puder obter informações atualizadas do servidor DHCP, talvez não haja conectividade de rede. Verifique se a NIC tem uma luz de link acesa, que indica uma conexão física com a rede. Se isso não resolver, talvez exista um problema no servidor DHCP ou nas conexões de rede com o servidor DHCP.

```powershell
C:\> ipconfig/release

Windows IP Configuration

No operation can be performed on Ethernet while it has its media disconnected.

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected

   Connection-specific DNS Suffix . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix . :

   Link-local IPv6 Address . . . . . : fe80 :: a1cc: 4239: d3ab: 2675% 6

   Default Gateway . . . . . . . . . :

C:\> ipconfig/renew

Windows IP Configuration

No operation can be performed on Ethernet while it has its media disconnected.

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected

   Connection-specific DNS Suffix . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix . : lan

   Link-local IPv6 Address . . . . . : fe80 :: a1cc: 4239: d3ab: 2675% 6

   IPv4 Address. . . . . . . . . . . : 10.10.10.130

   Subnet Mask . . . . . . . . . . . : 255.255.255.0

   Default Gateway . . . . . . . . . : 10.10.10.1

C:\>
```









