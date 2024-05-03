#redes #protocolo 

# Definição de RDP

[O Remote Desktop Protocol (RDP)](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol) é um protocolo proprietário desenvolvido pela Microsoft que fornece ao usuário uma interface gráfica para se conectar a outro computador por meio de uma conexão de rede. É também uma das ferramentas de administração mais populares, permitindo que os administradores de sistema controlem centralmente seus sistemas remotos com a mesma funcionalidade como se estivessem no local. Além disso, os provedores de serviços gerenciados (MSPs) costumam usar a ferramenta para gerenciar centenas de redes e sistemas de clientes. Infelizmente, embora o RDP facilite muito a administração remota de sistemas de TI distribuídos, ele também cria outra porta de entrada para ataques.

Por padrão, o RDP usa porta `TCP/3389`. Usando `Nmap`, podemos identificar o serviço RDP disponível no host de destino:

```bash
NycolasES6@htb[/htb] nmap -Pn -p3389 192.168.2.143 

Host discovery disabled (-Pn). All addresses will be marked 'up', and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-25 04:20 BST
Nmap scan report for 192.168.2.143
Host is up (0.00037s latency).

PORT     STATE    SERVICE
3389/tcp open ms-wbt-server
```














