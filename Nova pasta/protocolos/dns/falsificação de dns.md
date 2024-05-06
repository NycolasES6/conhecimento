#protocolo #redes #hacking 

# Falsificação de dns

A falsificação de DNS também é conhecida como envenenamento de cache DNS. Este ataque envolve a alteração de registros DNS legítimos com informações falsas para que possam ser usados ​​para redirecionar o tráfego online para um site fraudulento. Exemplos de caminhos de ataque para envenenamento de cache DNS são os seguintes:

- Um invasor pode interceptar a comunicação entre um usuário e um servidor DNS para encaminhar o usuário para um destino fraudulento em vez de um destino legítimo, realizando um ataque Man-in-the-Middle (`MITM`).
    
- A exploração de uma vulnerabilidade encontrada em um servidor DNS pode gerar o controle do servidor por um invasor para modificar os registros DNS.

## Envenenamento de cache DNS local

Do ponto de vista da rede local, um invasor também pode realizar envenenamento de cache DNS usando ferramentas MITM como [Ettercap](https://www.ettercap-project.org/) ou [Bettercap](https://www.bettercap.org/) .

Para explorar o envenenamento do cache DNS via `Ettercap`, devemos primeiro editar o arquivo `/etc/ettercap/etter.dns` para mapear o nome de domínio de destino (por exemplo, `inlanefreight.com`) que eles desejam falsificar e o endereço IP do invasor (por exemplo, `192.168.225.110`) para o qual desejam redirecionar um usuário:

```shell-session
NycolasES6@htb[/htb]# cat /etc/ettercap/etter.dns

inlanefreight.com      A   192.168.225.110
*.inlanefreight.com    A   192.168.225.110
```

Em seguida, inicie a ferramenta `Ettercap` e procure hosts ativos na rede navegando até `Hosts > Scan for Hosts`. Depois de concluído, adicione o endereço IP de destino (por exemplo, `192.168.152.129`) ao Target1 e adicione um IP de gateway padrão (por exemplo, `192.168.152.2`) ao Target2.

![[target.webp]]

Ative o ataque `dns_spoof` navegando até `Plugins > Manage Plugins`. Isso envia à máquina de destino respostas DNS falsas que serão resolvidas `inlanefreight.com`para o endereço IP `192.168.225.110`:

![[etter_plug.webp]]

Após um ataque de falsificação de DNS bem-sucedido, se um usuário vítima vindo da máquina alvo `192.168.152.129`visitar o domínio `inlanefreight.com` em um navegador da web, ele será redirecionado para uma `Fake page` hospedada em um endereço IP `192.168.225.110`:

![[etter_site.webp]]

Além disso, um ping vindo do endereço IP de destino `192.168.152.129`para `inlanefreight.com` também deve ser resolvido para `192.168.225.110`:

```sh
C:\>ping inlanefreight.com

Pinging inlanefreight.com [192.168.225.110] with 32 bytes of data:
Reply from 192.168.225.110: bytes=32 time<1ms TTL=64
Reply from 192.168.225.110: bytes=32 time<1ms TTL=64
Reply from 192.168.225.110: bytes=32 time<1ms TTL=64
Reply from 192.168.225.110: bytes=32 time<1ms TTL=64

Ping statistics for 192.168.225.110:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
