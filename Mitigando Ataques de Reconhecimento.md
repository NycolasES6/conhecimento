#cyber 

# Mitigando Ataques de Reconhecimento

Os ataques de reconhecimento são tipicamente o precursor de outros ataques que têm a intenção de obter acesso não autorizado a uma rede ou interromper a funcionalidade da rede. Um profissional de segurança de rede pode detectar quando um ataque de reconhecimento está em andamento recebendo notificações de alarmes pré-configurados. Estes alarmes são provocados quando determinados parâmetros são excedidos, tal como o número de pedidos ICMP por segundo. Uma variedade de tecnologias e dispositivos podem ser usados para monitorar esse tipo de atividade e gerar um alarme. A ferramenta de segurança adaptável (ASA) de Cisco fornece a prevenção da intrusão em um dispositivo autônomo. Além disso, os roteadores corporativos, como os Cisco Integrated Services Routers (ISR), oferecem suporte à prevenção contra invasões na rede com software adicional.

Os ataques de reconhecimento podem ser mitigados de várias maneiras, incluindo o seguinte:

- Autenticação de implementação para garantir o acesso adequado.
- Usando a criptografia para renderizar os ataques do Sniffer do pacote.
- Usando ferramentas anti-sniffer para detectar ataques de sniffer de pacotes.
- Implementando uma infraestrutura comutada.
- Usando um firewall e IPS.

O software anti-sniffer e as ferramentas de hardware detectam mudanças no tempo de resposta dos hosts para determinar se os hosts estão processando mais tráfego do que suas próprias cargas de tráfego indicariam. Embora isso não elimine completamente a ameaça, como parte de um sistema geral de mitigação, pode reduzir o número de instâncias de ameaça.

A criptografia também é eficaz para mitigar ataques de sniffer de pacotes. Se o tráfego é criptografado, usar um sniffer de pacote é de pouca utilidade porque os dados capturados não são legíveis.

É impossível mitigar a varredura de portas, mas usar um sistema de prevenção de intrusões (IPS) e firewall pode limitar as informações que podem ser descobertas com um scanner de porta. As varreduras de ping podem ser paradas se o eco ICMP e a resposta de eco estiverem desligados nos roteadores de borda; contudo, quando esses serviços são desligados, os dados de diagnóstico de rede são perdidos. Além disso, as varreduras de porta podem ser executadas sem varreduras de ping completas. As varreduras simplesmente levam mais tempo porque os endereços IP inativos também são verificados.

## Técnicas de Mitigação de Ataque de Reconhecimento

![[Pasted image 20240508175654.png]]

