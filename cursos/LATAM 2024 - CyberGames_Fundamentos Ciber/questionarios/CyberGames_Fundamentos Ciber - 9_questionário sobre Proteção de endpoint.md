#SO  #Linux  
# CyberGames_Fundamentos Ciber - 9_questionário sobre Proteção de endpoint

### 1 - Qual abordagem de software antimalware pode considerar várias características de arquivos de malware conhecidos para detectar uma ameaça?

- baseado em assinatura

### 2 - Combine o recurso de segurança do sistema da Apple com a finalidade específica.

- permite que apenas software autenticado seja executado - Ports
- armazenamento criptografado - FileVault
- tecnologia antimalware - XProtect
- permite que o disco rígido seja desligado remotamente - Encontre meu Mac

### 3 - Qual dispositivo em uma infraestrutura de LAN é suscetível a ataques de estouro de tabela de endereços MAC e falsificação?

- Switch

### 4 - Na maioria dos pacotes de segurança baseados em host, qual função fornece registro robusto de eventos relacionados à segurança e envio de logs para uma central local?

- Telemetria

### 5 - Qual tecnologia pode aumentar o desafio de segurança para a implementação da IoT em um ambiente empresarial?

- Computação em nuvem

### 6 - Qual declaração descreve a proteção antivírus sem agente?

- As verificações antivírus são realizadas em hosts a partir de um sistema centralizado.

### 7 - Qual HIDS é um produto baseado em código aberto?

- OSSEC

### 8 - Não há Firewall do Windows, quando o perfil de domínio é aplicado?

- quando o host está conectado a uma rede confiável, como uma rede de negócios interna

### 9 - O que é um sistema de detecção de intrusões baseado em host (HIDS)?

- Ele combina funcionalidades de aplicativos antimalware com proteção por firewall.

### 10 - Conforme descrito pelo Instituto SANS, qual superfície de ataque inclui a exploração de vulnerabilidades em protocolos como e sem fio usados ​​por dispositivos IoT?

- Superfície de ataque de rede

### 11 - Qual declaração descreve o termo superfície de ataque?

- É uma soma total de vulnerabilidades em um sistema acessível a um invasor.

### 12 - Conforme descrito pelo Instituto SANS, qual superfície de ataque inclui o uso da engenharia social?

- Superfície de Ataque Humano

### 13 - Qual configuração de segurança de endpoint seria usada por um analista de segurança para determinar se um computador foi configurado para evitar que um determinado aplicativo fosse executado?

- Lista negra

### 14 - O que você pode fazer para garantir que o software operacional de rede permaneça seguro?

- Instale patches e atualizações regularmente

### 15 - Que tipo de tecnologia pode impedir que software mal-intencionado exiba anúncios pop-up indesejados em um dispositivo?

- Proteção contra adware

### 16 - Que tipo de bloqueio é recomendado para proteger a porta do escritório?

- Trava de cifra

## Resumo

## Defesa de sistemas e dispositivos

Para proteger um sistema operacional, os administradores devem remover todos os programas e serviços desnecessários e garantir que as correções de segurança e as atualizações estejam instaladas. Uma empresa deve estabelecer procedimentos para monitorar informações relacionadas à segurança, avaliar atualizações e instalar atualizações usando um plano documentado. Além disso, eles devem identificar possíveis vulnerabilidades ao estabelecer um parâmetro para comparar o desempenho de um sistema.

Malware inclui vírus, worms, cavalos de Troia, keyloggers, spyware, e adware. Todos eles invadem a privacidade, roubam informações, danificam o sistema ou excluem e corrompem os dados. Use software antimalware confiável. Vírus sem arquivo usam linguagens de script como o Windows PowerShell e são difíceis de detectar. Linguagens de script como Python, Bash ou VBA podem ser usadas para criar malware. Remova o software não compatível imediatamente.

Os patches são atualizações de código que os fabricantes fornecem para evitar que um vírus ou um worm recém-descoberto façam um ataque bem-sucedido. Patches e atualizações são frequentemente combinados em um service pack. Uma ferramenta de gerenciamento de patches pode ser usada para gerenciar patches localmente. Também é importante atualizar aplicativos de terceiros, como Adobe Acrobat, Java e Chrome, para lidar com vulnerabilidades. Um firewall baseado em host é executado em um dispositivo para restringir a atividade de rede de entrada e saída desse dispositivo. O software HIDS monitora chamadas e acesso ao sistema de arquivos para detectar solicitações mal-intencionadas. O HIPS monitora um dispositivo em busca de ataques e anomalias. O EDR monitora e coleta continuamente dados de um dispositivo de endpoint e, em seguida, analisa os dados e responde a todas as ameaças. As ferramentas de DLP garantem que dados confidenciais não sejam perdidos ou acessados por usuários não autorizados. O NGFW combina um firewall tradicional com outras funções de filtragem de dispositivos de rede. A criptografia é uma ferramenta usada para proteger os dados usando um algoritmo para transformar dados e torná-los ilegíveis.

O recurso Windows Encrypting File System (EFS) permite que os usuários criptografem arquivos, pastas ou um disco rígido inteiro. A integridade de inicialização garante que o sistema seja confiável e não tenha sido alterado enquanto o sistema operacional é carregado. A inicialização segura é um padrão de segurança para garantir que um dispositivo inicialize usando software confiável. A inicialização medida pode identificar aplicativos não confiáveis que tentam carregar e também permite que o antimalware seja carregado mais cedo.

Os administradores devem ter políticas e contramedidas em vigor para software não corrigido, downloads de usuários não autorizados, malware, dispositivos autônomos, violações de política de uso aceitável e mídia não autorizada. Proteja o equipamento físico com fechaduras de cabo, fechaduras de portas cifradas, gaiolas de Faraday para bloquear campos eletromagnéticos e etiquetas RFID para identificar e rastrear itens. Proteção Antimalware

Os endpoints são hosts na rede que podem acessar ou ser acessados por outros hosts na rede. Com a IoT, outros tipos de dispositivos agora são endpoints. Cada ponto de extremidade é uma forma potencial de software malicioso ter acesso a uma rede. Nem todos os endpoints estão dentro de uma rede. Muitos endpoints se conectam a redes remotamente através de VPN. O perímetro da rede está sempre se expandindo. Vários dispositivos de segurança de rede são necessários para proteger o perímetro da rede contra acesso externo. Muitos ataques são originados de dentro da rede; portanto, proteger uma LAN interna também é importante. Depois que um host interno é infiltrado, ele pode se tornar um ponto de partida para um invasor obter acesso a dispositivos críticos do sistema. Há dois elementos de LAN internos para proteger: endpoints e infra-estrutura de rede.

O Software Antivírus/Antimalware é instalado em um host para detectar e mitigar vírus e malware. Ele faz isso usando três abordagens diferentes, baseadas em assinaturas (usando várias características de arquivos de malware conhecidos), heurística (usando recursos gerais compartilhados por vários tipos de malware) e baseado em comportamento (usando uma análise de comportamento suspeito). Muitos programas antivírus são capazes de fornecer proteção em tempo real analisando dados conforme eles são usados pelo endpoint. Um Firewall baseado em host restringe as conexões de entrada e saída a conexões iniciadas somente por esse host. Alguns softwares de firewall também podem impedir que um host se infecte e impedir que hosts infectados espalhem malware para outros hosts. A maioria dos softwares de segurança baseados em host inclui funcionalidade de registro que é essencial para operações de segurança cibernética. A proteção de endpoints em uma rede sem fronteiras pode ser realizada usando técnicas baseadas em rede, bem como baseadas em host.

### Prevenção de intrusão baseada em host

Firewalls baseados em host podem usar um conjunto de políticas predefinidas, ou perfis, para controlar pacotes que entram e saem de um computador. Eles também podem ter regras que podem ser diretamente modificadas ou criadas para controlar o acesso com base em endereços, protocolos e portas. Eles também podem ser configurados para emitir alertas se um comportamento suspeito for detectado. O registro varia dependendo do aplicativo de firewall. Normalmente, inclui a data e a hora do evento, se a conexão foi permitida ou negada, informações sobre os endereços IP de origem ou destino dos pacotes e as portas de origem e destino dos segmentos encapsulados. (Os firewalls distribuídos combinam recursos de firewalls baseados em host com gerenciamento centralizado.)

Alguns exemplos de firewalls baseados em host incluem Firewall do Windows Defender, iptables, nftables e TCP Wrappers. O HIDS protege os hosts contra malware conhecido e desconhecido. Pode realizar monitoramento e relatórios detalhados sobre a configuração do sistema e a atividade do aplicativo, análise de log, correlação de eventos, verificação de integridade, aplicação de políticas, detecção de rootkit e alertas. Um HIDS incluirá frequentemente um endpoint de servidor de gerenciamento. Como o software HIDS deve ser executado diretamente no host, ele é considerado um sistema baseado em agentes. Um HIDS usa estratégias proativas e reativas. Um HIDS pode impedir intrusões porque utiliza assinaturas para detectar malware conhecido e impedir que infecte um sistema.

As assinaturas não são eficazes contra ameaças novas ou de dia zero. Além disso, algumas famílias de malware exibem polimorfismo. Estratégias adicionais para detectar a possibilidade de sucesso de um ataque, incluem detecção baseada em anomalias e detecção baseada em políticas.

### Segurança de aplicações

Uma superfície de ataque é a soma total das vulnerabilidades em um determinado sistema que é acessível a um invasor. Pode consistir em portas abertas em servidores ou hosts, software que está sendo executado em servidores voltados para a Internet, protocolos de rede sem fio, dispositivos remotos e até mesmo usuários. A superfície de ataque continua a expandir-se. Mais dispositivos estão se conectando a redes através da Internet das Coisas (IoT) e BYOD (Traga seu próprio aparelho).

O Instituto SANS descreve três componentes da superfície de ataque: superfície de ataque de rede, superfície de ataque de software e superfície de ataque humano. Uma maneira de diminuir a superfície de ataque é limitar o acesso a ameaças potenciais criando listas de aplicativos proibidos. As listas brancas são criadas de acordo com uma linha de base de segurança estabelecida por uma organização. Sandboxing é uma técnica que permite que arquivos suspeitos sejam executados e analisados em um ambiente seguro. As sandboxes de análise automatizada de malware oferecem ferramentas que analisam o comportamento do malware. Essas ferramentas observam os efeitos da execução de malware desconhecido para que os recursos do comportamento de malware possam ser determinados e usados para criar defesas contra ele. O malware polimórfico muda com frequência e o novo malware aparece regularmente. O malware entrará na rede apesar dos sistemas de segurança baseados em host e perímetro mais robustos. HIDS e outros sistemas de detecção podem criar alertas sobre suspeita de malware que pode ter entrado na rede e executado em um host.



