#cyber #redes 
# Firewalls Baseados em host

Firewalls pessoais baseados em host são programas de software independentes que controlam o tráfego que entra ou sai de um computador. Aplicativos de firewall também estão disponíveis para telefones e tablets Android.

Firewalls baseados em host podem usar um conjunto de políticas predefinidas, ou perfis, para controlar pacotes que vêm e vêm de um computador. Eles também podem ter regras que podem ser diretamente modificadas ou criadas para controlar o acesso com base em endereços, protocolos e portas. Aplicativos de firewall baseados em host também podem ser configurados para emitir alertas aos usuários sobre um comportamento suspeito para detecção. Eles podem então oferecer ao usuário a capacidade de permitir que um aplicativo ofensivo seja executado ou impedido de ser executado no futuro.

O registro varia dependendo do aplicativo de firewall. Normalmente, inclui os dados e a hora do evento, se a conexão foi permitida ou negada, informações sobre os endereços IP de origem ou destino dos pacotes e as portas de origem e destino dos segmentos encapsulados. Além disso, atividades comuns, como pesquisas de DNS e outros eventos de rotina, podem aparecer em logs de firewall baseados em host, portanto, filtragem e outras técnicas de análise são úteis para funcionar grandes detalhes de dados de log.

Uma abordagem para a prevenção de intrusões é o uso de firewalls distribuídos. Os firewalls distribuídos combinam recursos de firewalls baseados em host com gerenciamento centralizado. A função de gerenciamento envia regras para os hosts e também pode aceitar arquivos de log dos hosts.

Independentemente de serem instalados completamente no host ou distribuídos, os firewalls baseados em host são uma camada importante de segurança de rede, juntamente com os firewalls baseados em rede. Aqui estão alguns exemplos de firewalls baseados em host:

## Firewall do Windows Defender

Incluído pela primeira vez no Windows XP, o Firewall do Windows (agora Windows Defender Firewall) usa uma abordagem baseada em perfil para a funcionalidade do firewall. O acesso às redes públicas é atribuído ao perfil restritivo do firewall Público. O perfil Privado é para computadores que estão isolados da Internet por outros dispositivos de segurança, como um roteador doméstico com funcionalidade de firewall. O perfil Domínio é o terceiro perfil disponível. Ele é escolhido para conexões com uma rede confiável, como uma rede de negócios que se propõe ter uma infraestrutura de segurança adequada. O Firewall do Windows tem funcionalidade de registro e pode ser gerenciado centralmente com políticas de segurança de grupo personalizadas a partir de um servidor de gerenciamento, como o System Center 2012 Configuration Manager.

## iptables

Este é um aplicativo que permite aos administradores do sistema Linux configurar regras de acesso à rede que fazem parte dos módulos Netfilter do kernel Linux.

## nftables

O sucessor do iptables, o nftables é um aplicativo de firewall do Linux que usa uma máquina virtual simples no kernel do Linux. O código é executado dentro da máquina virtual que contém pacotes de rede e implementa regras de decisão relacionadas à facilidade de uso e encaminhamento de pacotes.

## wrappers TCP

Este é um sistema de registro e controle de acesso baseado em regras para Linux. A seleção de pacotes é baseada em direções IP e serviços de rede.




















