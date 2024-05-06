# Configuração de rede

Uma das principais tarefas de configuração de rede é configurar interfaces de rede. Isso inclui a atribuição de endereços IP, a configuração de dispositivos de rede, coomo roteadores e switches, e a configuração de protocolos de rede. É essencial compreender completamente os protocolos de rede e seus casos de uso específicos, como TCP/IP, DNS, DHCP E FTP. Além disso, devemos estar familiarizados com diferentes interfaces de rede, incluindo conexões sem fio, e ser capazes de solucionar problemas de conectividade.

O controle de acesso á rede é outro componente crítico da configuração da rede. Como testadores de penetração, devemos estar familiarizados com a importância do NAC para a segurança da rede e com as diferentes tecnologias NAC disponíveis. Esses incluem:

 - Controle de acesso discricionário (DAC)
 - Controle de acesso obrigatório (MAC)
 - Controle de acesso baseado em função (RBAC)

Devemos também compreender os diferentes mecanismos de aplicação do NAC e saber como configurar dispositivos de rede Linux para NAC. Isso inclui configurar políticas SELinux, configurar perfis AppArmor e usar wrappers TCP para controlar o acesso.

O monitoramento do tráfego de rede também é uma parte essencial da configuração da rede. Portanto, devemos saber como configurar o monitoramento e o registro da rede e ser capazes de analisar o tráfego da rede para fins de segurança. Ferramentas como syslog, rsyslog, ss, lsof e pilha ELK podem ser usadas para monitorar o tráfego de rede e identificar problemas de segurança.

Além disso, um bom conhecimento das ferramentas de solução de problemas de rede é crucial para identificar vulnerabilidades e interagir com outras redes e hosts. Além das ferramentas que mencionamos, podemos usar ping, nslookup e nmap para diagnosticar e enumerar redes. Essas ferramentas podem fornecer informações valiosas sobre o tráfego de rede, perda de pacotes, latência, resolução de DNS, etc. Ao compreender como usar essas ferramentas de maneira eficaz, podemos identificar rapidamente a causa raiz de qualquer problema de rede e tomar as medidas necessárias para resolvê-lo.

## Configurando interfaces de rede

Ao trabalhar com o Ubuntu, você pode configurar interfaces de rede locais usando o comando ifconfigou ip. Esses comandos poderosos nos permitem visualizar e configurar as interfaces de rede do nosso sistema. Quer pretendamos fazer alterações em nossa configuração de rede existente ou verificar o status de nossas interfaces, esses comandos podem simplificar bastante o processo. Além disso, desenvolver uma compreensão sólida das complexidades das interfaces de rede é uma capacidade essencial no mundo moderno e interligado. Com o rápido avanço da tecnologia e a crescente dependência da comunicação digital, ter um conhecimento abrangente de como trabalhar com interfaces de rede pode permitir que você navegue de forma eficaz na diversificada gama de redes que existem hoje em dia.

Uma forma de obter informações sobre interfaces de rede, como endereços IP, máscaras de rede e status, é usando o comando **ifconfig**. Ao executar este comando, podemos visualizar as interfaces de rede disponíveis e seus respectivos atributos de forma clara e organizada. Essas informações podem ser particularmente úteis ao solucionar problemas de conectividade de rede ou definir uma nova configuração de rede. Deve-se observar que o comando **ifconfig** foi descontinuado nas versões mais recentes do Linux e substituído pelo comando **ip**, que oferece recursos mais avançados. No entanto, o comando **ifconfig** ainda é amplamente utilizado em muitas distribuições Linux e continua a ser uma ferramenta confiável para gerenciamento de rede.

## Configurações de rede

`$ ifconfig`

`$ ip addr`

Quando se trata de ativar as interfaces de rede, os comandos **ifconfig** e **ip** são duas ferramentas comumente usadas. Esses comandos permitem que os usuários modifiquem e ativem comfigurações para uma interface específica, como **eth0**. Podemos ajustar as configurações de rede para atender ás nossas necessidades usando a sintáxe apropriada e especificando o nome da interface.

## Ativar a interfac

`$ sudo ifconfig eth0 up`

ou

`$ sudo ip link set eth0 up`

Uma maneira de alocar um endereço IP para uma interface de rede é utiliando o comando **ifconfig**. Devemos especificar o nome da interface e o endereço IP como argumentos para fazer isso. Esta é uma etapa crucial na configuração de uma conxão de rede. O endereço IP serve como identificador exclusivo para interface e permite a comunicação entre dispositivos na rede.

## Atribuir endereço IP a uma interface

`$ sudo ifconfig eth0 192.168.1.2`

Para definir a máscara de rede para uma interface de rede, podemos executar o seguinte comando com o nome da interface e a máscara de rede:

## Atribuir uma máscara de rede a uma interface

`$ sudo ifconfig eth0 netmask 255.255.255.0`

Quando quisermos definir o gateway padrão para uma interface de rede, podemos usar o comando **route** com a opção **add**. Isto permite-nos Isto permite-nos especificar o endereço IP do gateway e a interface de rede à qual deve ser aplicado. Ao definir o gateway padrão, estamos designando o endereço IP do roteador que será usado para enviar tráfego para destinos fora da rede local. Garantir que o gateway padrão esteja configurado corretamente é importante, pois a configuração incorreta pode levar a problemas de conectividade.

## Atribuir a rota a uma interface

`$ sudo route add default gw 192.168.1.1 eth0`

Ao configurar uma interface de rede, muitas vezes é necessário configurar servidores de Sistema de Nomes de Domínio (**DNS**) para garantir a funcionalidade adequada da rede. Os servidores DNS traduzem nomes df domínio em endereços IP, permitindo que os dispositivos se conectem entre si na Internet. Ao configurá-los, podemos garantir que seus dispositivos possam se comunicar com outros dispositivos e acessar sites e outros recursos online. Sem a configuração adequada do servidor DNS, os dispositivos podem enfrentar problemas de conectividade de rede e não conseguir acessar determinados recursos online. Isto pode ser conseguido atualizando o arquivo **/etc/resolv.conf** com as informações apropriadas do servidor DNS. O arquivo **/etc/resolv.conf** é um arquivo de texto simples que contém as informações de DNS do sistema. O sistema pode resolver adequadamente nomes de domínio em endereços IP adicionando os servidores DNS necessários a este arquivo. É importante observar que quaisquer alterações feitas neste arquivo serão aplicadas apenas à sessão atual e deverão ser atualizadas caso o sistema seja reiniciado ou a configuração da rede seja alterada.

## Editando configurações de DNS

`$ sudo vim /etc/resolv/conf`

## /etc/resolv.conf

código: txt

>nameserver 8.8.8.8 \
>nameserver 8.8.4.4

Depois de concluir as modificações necessárias na configuração da rede, é essencial garantir que essas alterações sejam salvas para persistirem durante as reinicializações. Isto pode ser conseguido editando o arquivo **/etc/network/interfaces**, que define interfaces de rede para sistemas operacionais baseados em Linux. Portanto, é vital salvar todas as alterações feitas neste arquivo para evitar possíveis problemas de conectividade de rede.

## Editando interfaces

`$ sudo vim /etc/network/interfaces`

Isso abrirá o aqruivo interfaces no editro vim. Poemod adicionar as configurações de rede ao arquivo assim:

## /etc/rede/interfaces

código: txt

>auto eth0 \
>iface eth0 inet static \
>    address 192.168.1.2 \
>    netmask 255.255.255.0 \
>    gateway 192.168.1.1 \
>    dns-nameservers 8.8.8.8 8.8.4.4

Ao configurar a interface de rede **eth0** para usar um endereço IP estático de **192.168.1.2**, com uma máscara de rede **255.255.255.0** e um gateway padrão de **192.168.1.1**, podemos garantir que sua conexão de rede permaneça estável e confiável. Além disso, ao especificar os servidores DNS de **8.8.8.8** e **8.8.4.4**, podemos garantir que nosso computador possa acessar facilmente a Internet e resolver nomes de domínio. Depois de fazer essas alterações no arquivo de configuração, é importante salvar o arquivo e sair do editor. Depois disso, devemos reiniciar o serviço de rede para aplicar as alterações.

## Reinicie o serviço de rede

`$ sudo systemctl restart networking`

## Controle de acesso à rede

O controle de acesso à rede (NAC) é um componente crucial da segurança da rede, especialmente na era atual de crescentes ameaças cibernéticas. Como testador de penetração, é vital compreender a importância do NAC na proteção da rede e nas diversas tecnologias NAC que podem ser utilizadas para aprimorar as medidas de segurança. NAC é um sistema de segurança que garante que apenas dispositivos autorizados e em conformidade tenham acesso à rede, evitando acesso não autorizado, violações de dados e outras ameaças à segurança. Ao implementar o NAC, as organizações podem ter confiança na sua capacidade de proteger os seus activos e dados contra cibercriminosos que procuram sempre explorar vulnerabilidades do sistema. A seguir estão as diferentes tecnologias NAC que podem ser usadas para melhorar as medidas de segurança:

 - Controle de acesso discricionário (DAC)
 - Controle de acesso obrigatório (MAC)
 - Controle de acesso baseado em função (RBAC)

Essas tecnologias são projetadas para fornecer diferentes níveis de controle de acesso e segurança. Cada tecnologia tem características únicas e é adequada para diferentes casos de uso. Como testador de penetração, é essencial compreender essas tecnologias e seus casos de uso específicos para testar e avaliar a segurança da rede de forma eficaz.

## Controle de acesso discricionário

O DAC é um componente crucial dos sistemas de segurança modernos, pois ajuda as organizações a fornecer acesso aos seus recursos enquanto gerenciam os riscos associados ao acesso não autorizado. É um sistema de controle de acesso amplamente utilizado que permite aos usuários gerenciar o acesso aos seus recursos, concedendo aos proprietários dos recursos a responsabilidade de controlar as permissões de acesso aos seus recursos. Isto significa que os utilizadores e grupos que possuem um recurso específico podem decidir quem tem acesso aos seus recursos e que ações estão autorizados a executar. Essas permissões podem ser definidas para leitura, gravação, execução ou exclusão do recurso.

## Controle de acesso obrigatório

O MAC é usado em infraestrutura que fornece controle mais refinado sobre o acesso a recursos do que os sistemas DAC. Esses sistemas definem regras que determinam o acesso aos recursos com base no nível de segurança do recurso e no nível de segurança do usuário ou processo que solicita acesso. Cada recurso recebe um rótulo de segurança que identifica seu nível de segurança, e cada usuário ou processo recebe uma autorização de segurança que identifica seu nível de segurança. O acesso a um recurso só é concedido se o nível de segurança do usuário ou processo for igual ou superior ao nível de segurança do recurso. O MAC é frequentemente usado em sistemas operacionais e aplicativos que exigem um alto nível de segurança, como sistemas militares ou governamentais, sistemas financeiros e sistemas de saúde. Os sistemas MAC são projetados para impedir o acesso não autorizado aos recursos e minimizar o impacto das violações de segurança.

## Controle de acesso baseado em função

O RBAC atribui permissões aos usuários com base em suas funções dentro de uma organização. Os usuários recebem funções com base em suas responsabilidades profissionais ou outros critérios, e cada função recebe um conjunto de permissões que determinam as ações que eles podem executar. O RBAC simplifica o gerenciamento de permissões de acesso, reduz o risco de erros e garante que os usuários possam acessar apenas os recursos necessários para desempenhar suas funções de trabalho. Pode restringir o acesso a recursos e dados confidenciais, limitar o impacto de violações de segurança e garantir a conformidade com os requisitos regulamentares. Comparado aos sistemas de Controle de Acesso Discricionário (DAC), o RBAC oferece uma abordagem mais flexível e escalável para gerenciar o acesso a recursos. Em um sistema RBAC, cada usuário recebe uma ou mais funções, e cada função recebe um conjunto de permissões que definem as ações do usuário. O acesso ao recurso é concedido com base na função atribuída ao usuário, e não na identidade ou propriedade do recurso. Os sistemas RBAC são normalmente usados ​​em ambientes com muitos usuários e recursos, como grandes organizações, agências governamentais e instituições financeiras.

## Monitoramento

O monitoramento de rede envolve capturar, analisar e interpretar o tráfego de rede para identificar ameaças à segurança, problemas de desempenho e comportamento suspeito. O objetivo principal da análise e monitoramento do tráfego de rede é identificar ameaças e vulnerabilidades à segurança. Por exemplo, como testadores de penetração, podemos capturar credenciais quando alguém usa uma conexão não criptografada e tenta fazer login em um servidor FTP. Como resultado, obteremos as credenciais desse usuário que podem nos ajudar a nos infiltrar ainda mais na rede ou a aumentar nossos privilégios para um nível superior. Resumindo, ao analisar o tráfego da rede, podemos obter insights sobre o comportamento da rede e identificar padrões que podem indicar ameaças à segurança. Essa análise inclui a detecção de atividades suspeitas na rede, a identificação de tráfego malicioso e a identificação de possíveis riscos de segurança. No entanto, abordamos este vasto tópico no módulo Introdução à Análise de Tráfego de Rede , onde usamos diversas ferramentas para monitoramento de rede em sistemas Linux como Ubuntu e sistemas Windows, como Wireshark, tshark e Tcpdump.

## Solução de problemas

A solução de problemas de rede é um processo essencial que envolve o diagnóstico e a resolução de problemas de rede que podem afetar adversamente o desempenho e a confiabilidade da rede. Este processo é fundamental para garantir o funcionamento ideal da rede e evitar interrupções que possam afetar as operações comerciais durante os nossos testes de penetração. Também envolve identificar, analisar e implementar soluções para resolver problemas. Esses problemas incluem problemas de conectividade, velocidades de rede lentas e erros de rede. Várias ferramentas podem nos ajudar a identificar e resolver problemas relacionados à solução de problemas de rede em sistemas Linux. Algumas das ferramentas mais comumente usadas incluem:

1. Ping
2. Traceroute
3. Netstat
4. tcpdump
5. Wireshark
6. Nmap

Ao usar essas ferramentas e outras semelhantes, podemos entender melhor como a rede funciona e diagnosticar rapidamente quaisquer problemas que possam surgir. Por exemplo, **ping** é uma ferramenta de linha de comando usada para testar a conectividade entre dois dispositivos. Ele envia pacotes para um host remoto e mede o tempo para devolvê-los. Para usar **ping**, podemos inserir o seguinte comando:

## Ping

`$ ping <remote_host>`

Por exemplo, fazer ping no servidor DNS do Google enviará pacotes ICMP ao servidor DNS do Google e exibirá os tempos de resposta.

`$ ping 8.8.8.8`

Outra ferramenta é o **traceroute**, que rastreia a rota que os pacotes seguem para chegar a um host remoto. Ele envia pacotes com valores crescentes de Time-to-Live (TTL) para um host remoto e exibe os endereços IP dos dispositivos pelos quais os pacotes passam. Por exemplo, para rastrear a rota até o servidor DNS do Google, inseriríamos o seguinte comando:

`$ traceroute www.inlanefreight.com`

Isso exibirá os endereços IP dos dispositivos pelos quais os pacotes passam para chegar ao servidor DNS do Google. A saída de um comando traceroute mostra como ele é usado para rastrear o caminho dos pacotes até o site www.inlanefreight.com , que possui um endereço IP 134.209.24.248. Cada linha da saída contém informações valiosas.

Ao configurar uma conexão de rede, é importante especificar o host de destino e o endereço IP. Neste exemplo, o host de destino é 134.209.24.248 e o número máximo de saltos permitido é 30. Isso garante que a conexão seja estabelecida de forma eficiente e confiável. Ao fornecer essas informações, o sistema pode encaminhar o tráfego para o destino correto e limitar o número de paradas intermediárias que os dados precisam fazer.

A segunda linha mostra o primeiro salto no traceroute, que é o gateway da rede local com o endereço IP 10.80.71.5, seguida pelas próximas três colunas mostram o tempo que cada um dos três pacotes enviados levou para chegar ao gateway em milissegundos ( 2,716 ms, 2,700 ms e 2,730 ms).

A seguir, vemos o segundo salto no traceroute. No entanto, não houve resposta do dispositivo naquele salto, indicado pelos três asteriscos em vez do endereço IP. Isso pode significar que o dispositivo está inativo, bloqueando o tráfego ICMP ou que um problema de rede causou a queda dos pacotes.

Na quarta linha, podemos ver o terceiro salto no traceroute, composto por dois dispositivos com endereços IP 10.80.68.175 e 10.80.68.161, e novamente as próximas três colunas mostram o tempo que cada um dos três pacotes levou para chegar ao primeiro dispositivo (7,147 ms, 7,132 ms e 7,393 ms).

## Netstat

**Netstaté** usado para exibir conexões de rede ativas e suas portas associadas. Ele pode ser usado para identificar o tráfego de rede e solucionar problemas de conectividade. Para usar **netstat**, podemos inserir o seguinte comando:
`$ netstat -a`

Podemos esperar receber informações detalhadas sobre cada conexão ao usar esta ferramenta. Isso inclui o protocolo usado, o número de bytes recebidos e enviados, endereços IP, números de porta de dispositivos locais e remotos e o estado atual da conexão. A saída fornece informações valiosas sobre a atividade de rede no sistema, destacando quatro conexões específicas atualmente ativas e escutando em portas específicas. Essas conexões incluem o software de desktop remoto VNC, o serviço Sun Remote Procedure Call, o protocolo HTTP para tráfego da web e o protocolo SSH para acesso remoto seguro ao shell. Ao saber quais portas são usadas por quais serviços, os usuários podem identificar rapidamente quaisquer problemas de rede e solucioná-los adequadamente. Os problemas de rede mais comuns que encontraremos durante nossos testes de penetração incluem o seguinte:

 - Problemas de conectividade de rede
 - Problemas de resolução de DNS (é sempre DNS)
 - Perda de pacotes
 - Problemas de desempenho de rede

Cada problema, juntamente com causas comuns que podem incluir firewalls ou roteadores mal configurados, cabos ou conectores de rede danificados, configurações de rede incorretas, falha de hardware, configurações incorretas de servidor DNS, falha de servidor DNS, registros DNS mal configurados, congestionamento de rede, hardware de rede desatualizado, configuração incorreta configurações de rede, software ou firmware sem patch e falta de controles de segurança adequados. Compreender esses problemas comuns de rede e suas causas é importante para identificar e explorar com eficácia vulnerabilidades em sistemas de rede durante nossos testes.

## Hardening

Vários mecanismos são altamente eficazes na proteção de sistemas Linux, mantendo os dados de nossas empresas e de outras empresas seguros. Três desses mecanismos são SELinux, AppArmor e TCP wrappers. Essas ferramentas são projetadas para proteger os sistemas Linux contra diversas ameaças à segurança, desde acesso não autorizado a ataques maliciosos, especialmente durante a realização de testes de penetração. Quase não há cenário pior do que quando uma empresa é comprometida devido a um teste de penetração. Ao implementar estas medidas de segurança e garantir que configuramos a proteção correspondente contra potenciais atacantes, podemos reduzir significativamente o risco de fugas de dados e garantir que os nossos sistemas permanecem seguros. Embora essas ferramentas compartilhem algumas semelhanças, elas também apresentam diferenças importantes.

SELinux é um sistema MAC integrado ao kernel Linux. Ele foi projetado para fornecer controle de acesso refinado sobre recursos e aplicativos do sistema. O SELinux funciona aplicando uma política que define os controles de acesso para cada processo e arquivo no sistema. Ele fornece um nível mais alto de segurança, limitando os danos que um processo comprometido pode causar.

AppArmor também é um sistema MAC que fornece um nível semelhante de controle sobre recursos e aplicativos do sistema, mas funciona de maneira um pouco diferente. O AppArmor é implementado como um Módulo de Segurança Linux (LSM) e usa perfis de aplicativos para definir os recursos que um aplicativo pode acessar. O AppArmor normalmente é mais fácil de usar e configurar do que o SELinux, mas pode não fornecer o mesmo nível de controle refinado.

Wrappers TCP são um mecanismo de controle de acesso à rede baseado em host que pode ser usado para restringir o acesso a serviços de rede com base no endereço IP do sistema cliente. Funciona interceptando solicitações de rede recebidas e comparando o endereço IP do sistema cliente com as regras de controle de acesso. Eles são úteis para limitar o acesso a serviços de rede por parte de sistemas não autorizados.

No que diz respeito às semelhanças, os três mecanismos de segurança compartilham o objetivo comum de garantir a segurança dos sistemas Linux. Além de fornecerem proteção extra, podem restringir o acesso a recursos e serviços, reduzindo assim o risco de acessos não autorizados e violações de dados. Também é importante notar que esses mecanismos estão prontamente disponíveis como parte da maioria das distribuições Linux, tornando-os acessíveis para aumentar a segurança de seus sistemas. Além disso, esses mecanismos podem ser facilmente customizados e configurados usando ferramentas e utilitários padrão, tornando-os uma escolha conveniente para usuários de Linux.

Em termos de diferenças, SELinux e AppArmor são sistemas MAC que fornecem controle de acesso refinado sobre os recursos do sistema, mas funcionam de maneiras diferentes. O SELinux é integrado ao kernel e é mais complexo de configurar e usar, enquanto o AppArmor é implementado como um módulo e normalmente é mais fácil de usar. Por outro lado, os wrappers TCP são um mecanismo de controle de acesso à rede baseado em host, projetado para restringir o acesso aos serviços de rede com base no endereço IP do sistema cliente. É um mecanismo mais simples que o SELinux e o AppArmor, mas é útil para limitar o acesso a serviços de rede de sistemas não autorizados.

## Configurando

À medida que navegamos no mundo do Linux, inevitavelmente encontramos uma ampla gama de tecnologias, aplicativos e serviços com os quais precisamos nos familiarizar. Esta é uma competência crucial, especialmente se trabalharmos com segurança cibernética e nos esforçarmos para melhorar continuamente os nossos conhecimentos. Por esse motivo, é altamente recomendável dedicar algum tempo para aprender como configurar medidas de segurança importantes, como SELinux, AppArmore TCP wrapperspor conta própria. Ao aceitar este desafio (opcional, mas altamente eficiente), você aprofundará sua compreensão dessas tecnologias, desenvolverá suas habilidades de resolução de problemas e ganhará uma experiência valiosa que será útil para você no futuro. É altamente recomendável usar uma VM pessoal e fazer snapshots antes de fazer alterações.

Quando se trata de implementar medidas de segurança cibernética, não existe uma abordagem única para todos. É importante considerar as informações específicas que você deseja proteger e as ferramentas que usará para fazer isso. No entanto, você pode praticar e implementar diversas tarefas opcionais com outras pessoas no canal Discord para aumentar seus conhecimentos e habilidades nesta área. Aproveitando a ajuda de outras pessoas e compartilhando sua própria experiência, você pode aprofundar sua compreensão sobre segurança cibernética e ajudar outras pessoas a fazerem o mesmo. Lembre-se de que explicar conceitos a outras pessoas é essencial para o ensino e a aprendizagem.













