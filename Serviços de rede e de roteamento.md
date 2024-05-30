#cyber #redes 
# Serviços de rede e de roteamento

Os criminosos usam serviços de rede vulneráveis para atacar um dispositivo ou usá-lo como parte do ataque. Para verificar os serviços de rede não protegidos, verifique se um dispositivo tem portas abertas usando um scanner de porta. Um scanner de porta envia uma mensagem para cada porta e espera por uma resposta, indicando como a porta é usada e se está aberta.

Os criminosos virtuais também irão usar scanners de porta pelo mesmo motivo. Proteger os serviços de rede garante que somente as portas necessárias estejam expostas e disponíveis.

## Protocolo de Configuração Dinâmica de Host (DHCP)

O DHCP usa um servidor para atribuir um endereço IP e outras informações de configuração automaticamente aos dispositivos de rede. Na realidade, o dispositivo está obtendo uma permissão do servidor DHCP para usar a rede. Os invasores podem direcionar servidores DHCP para negar o acesso a dispositivos na rede, mas medidas de segurança como rastreamento de DHCP impedem que servidores DHCP invasores forneçam endereços IP para clientes ao validar mensagens de fontes que não são confiáveis.

A Figura 1 fornece uma lista de verificação de segurança para DHCP:

- Proteja fisicamente o servidor DHCP.
- Aplique as correções de software.
- Localize o servidor DHCP atrás de um firewall.
- Monitore a atividade do DHCP analisando os registros do DHCP.
- Mantenha uma solução antivírus forte.
- Desinstale qualquer serviço e aplicação não utilizado.
- Feche as portas não utilizadas.

## Domain Name System (DNS)

O DNS converte um URL ou endereço de site, como www.cisco.com, em um endereço IP numérico. Quando os usuários digitam um endereço da Web na barra de endereços, o servidor DNS reconhece o endereço IP. Os invasores podem direcionar os servidores DNS para negar o acesso aos recursos da rede ou redirecionar o tráfego para sites falsos. Use serviço e autenticação seguros entre servidores DNS para protegê-los contra esses ataques.

As DNS Security Extensions (DNSSEC) usam assinaturas digitais para fortalecer a autenticação e proteger contra ameaças ao DNS.

Uma checklist de segurança para DNS:

- Manter softwares DNS atualizados.
- Impeça que a string de versão revele informações.
- Separe os servidores DNS internos e externos.
- Restrinja as transações permitidas pelo endereço IP do cliente.
- Use assinaturas de transação para autenticar transações.
- Desative ou restrinja as transferências de zona e as atualizações dinâmicas o máximo possível.
- Habilitar o log e analisar logs.
- Use Domain Name System Security Extensions (DNSSEC).
- Assine zonas.

## Protocolo de mensagens de controle da Internet (ICMP)

Dispositivos de rede usam ICMP para enviar mensagens de erro como quando um serviço solicitado não está disponível ou se o host não pode acessar o roteador.

O comando ping é um utilitário de rede que usa o ICMP para testar a acessibilidade de um host em uma rede. O ping envia mensagens ICMP para o host e aguarda uma resposta. Os criminosos digitais podem alterar o uso do ICMP para executar ataques de canal secreto e reconhecimento, negação de serviço (DoS). Muitas redes filtram solicitações de ICMP para evitar esses ataques.

## Routing Information Protocol (RIP)

O RIP limita o número de saltos permitidos em um caminho em uma rede do dispositivo de origem para o destino. O número máximo de saltos permitidos para o RIP é 15. O RIP é um protocolo de roteamento usado para trocar informações de roteamento sobre quais redes cada roteador pode acessar e a que distância estão essas redes.

O RIP calcula a melhor rota com base na contagem de saltos, mas os criminosos digitais também podem direcionar roteadores e o protocolo RIP. Esses ataques a serviços de roteamento podem afetar o desempenho e a disponibilidade; alguns ataques podem até resultar em redirecionamento de tráfego. Use os serviços seguros com autenticação e implemente patches e atualizações de sistema para proteger serviços de roteamento como o RIP.

## Network Time Protocol (NTP)

Ter o tempo correto nas redes é importante. Carimbos de data e hora corretos são necessários para rastrear com precisão os eventos da rede, como as violações de segurança. Além disso, a sincronização do relógio é fundamental para a interpretação correta dos eventos nos arquivos de dados syslog, bem como para os certificados digitais.

O NTP (Network Time Protocol, Protocolo de tempo de rede) é um protocolo que sincroniza os relógios de sistemas de computadores em redes de dados. O NTP permite que os dispositivos de rede sincronizem as configurações de hora com um servidor NTP. Os criminosos virtuais atacam servidores de tempo para interromper a comunicação segura que depende de certificados digitais e esconder informações do ataque, como carimbos de data e hora. Use a autenticação NTP para verificar se o servidor é confiável.



