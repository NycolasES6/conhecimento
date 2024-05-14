#redes #cyber 

# Ataques ICMP

ICMP foi desenvolvido para transportar mensagens de diagnóstico e relatar condições de erro quando rotas, hosts e portas não estão disponíveis. Mensagens ICMP são geradas por dispositivos quando ocorre um erro de rede ou uma interrupção. O comando ping é uma mensagem ICMP gerada pelo usuário, chamada de solicitação de eco, usada para verificar a conectividade com um destino.

Os agentes de ameaças usam o ICMP para ataques de reconhecimento e varredura. Isso permite que eles lancem ataques de coleta de informações para mapear uma topologia de rede, descobrir quais hosts estão ativos (acessíveis), identificar o sistema operacional do host (impressão digital do sistema operacional) e determinar o estado de um firewall.

Os atores de ameaças também usam ICMP para ataques DoS e DDoS, conforme mostrado no ataque de inundação ICMP na figura.

**Inundação ICMP**

![[Pasted image 20240507124814.png]]

**Nota:** ICMP para IPv4 (ICMPv4) e ICMP para IPv6 (ICMPv6) são suscetíveis a tipos semelhantes de ataques.

Veja a seguir uma lista de mensagens ICMP comuns de interesse para os agentes de ameaças.

- **ICMP solicitação de eco (echo request) e resposta do eco (echo reply)** - Isso é usado para executar verificação de host e ataques de DoS.
- **ICMP inacessível** - Isso é usado para executar ataques de reconhecimento e varredura de rede.
- **Resposta da máscara ICMP** - Isso é usado para mapear uma rede IP interna.
- **ICMP redireciona** - Isso é usado para atrair um host alvo para enviar todo o tráfego através de um dispositivo comprometido e criar um ataque MiTM.
- **Descoberta de rotas ICMP** - Isso é usado para injetar entradas de rota falsas na tabela de roteamento de um host de destino.

As redes devem ter uma filtragem rigorosa da lista de controle de acesso ICMP (ACL) na borda da rede para evitar a sondagem ICMP vindo da Internet. Os analistas de segurança devem ser capazes de detectar ataques relacionados ao ICMP, observando o tráfego capturado e os arquivos de log. No caso de grandes redes, os dispositivos de segurança, como firewalls e sistemas de detecção de intrusão (IDS), devem detectar tais ataques e gerar alertas para os analistas de segurança.













