# Segurança Linux

Todos os sistemas informáticos apresentam um risco inerente de intrusão. Alguns apresentam mais riscos do que outros, como um servidor web voltado para a Internet que hospeda vários aplicativos web complexos. Os sistemas Linux também são menos propensos a vírus que afetam os sistemas operacionais Windows e não apresentam uma superfície de ataque tão grande quanto os hosts associados ao domínio do Active Directory. Independentemente disso, é essencial ter certos fundamentos para proteger qualquer sistema Linux.

Uma das medidas de segurança mais importantes dos sistemas operacionais Linux é manter o sistema operacional e os pacotes instalados atualizados. Isso pode ser alcançado com um comando como:

`$ apt update && apt dist-upgrade`

Se as regras de firewall não forem definidas adequadamente no nível da rede, podemos usar o firewall do Linux e/ou **iptables** para restringir o tráfego de entrada/saída do host.

Se o SSH estiver aberto no servidor, a configuração deverá ser definida para proibir o login com senha e impedir o login do usuário root via SSH. Também é importante evitar fazer login e administrar o sistema como usuário root sempre que possível e gerenciar adequadamente o controle de acesso. O acesso dos usuários deve ser determinado com base no princípio do menor privilégio. Por exemplo, se um usuário precisar executar um comando como root, esse comando deverá ser especificado na configuração **sudoers** em vez de conceder a ele direitos sudo completos. Outro mecanismo de proteção comum que pode ser usado é o fail2ban. Esta ferramenta conta o número de tentativas de login malsucedidas e, se um usuário atingir o número máximo, o host que tentou se conectar será tratado conforme configurado.

Também é importante auditar periodicamente o sistema para garantir que não existam problemas que possam facilitar o escalonamento de privilégios, como um kernel desatualizado, problemas de permissão do usuário, arquivos graváveis ​​mundialmente e cron jobs mal configurados ou serviços mal configurados. Muitos administradores esquecem a possibilidade de que algumas versões do kernel tenham que ser atualizadas manualmente.

Uma opção para bloquear ainda mais os sistemas Linux é Security-Enhanced Linux( SELinux) ou AppArmor. Este é um módulo de segurança do kernel que pode ser usado para políticas de controle de acesso de segurança. No SELinux, cada processo, arquivo, diretório e objeto do sistema recebe um rótulo. As regras de política são criadas para controlar o acesso entre esses processos e objetos rotulados e são aplicadas pelo kernel. Isso significa que o acesso pode ser configurado para controlar quais usuários e aplicativos podem acessar quais recursos. O SELinux fornece controles de acesso muito granulares, como especificar quem pode anexar ou mover um arquivo.

Além disso, existem diversos aplicativos e serviços como Snort , chkrootkit , rkhunter , Lynis , entre outros que podem contribuir para a segurança do Linux. Além disso, algumas configurações de segurança devem ser feitas, como:

 - Removendo ou desabilitando todos os serviços e softwares desnecessários
 - Removendo todos os serviços que dependem de mecanismos de autenticação não criptografados
 - Certifique-se de que o NTP esteja habilitado e o Syslog esteja em execução
 - Certifique-se de que cada usuário tenha sua própria conta
 - Imponha o uso de senhas fortes
 - Configure a validade da senha e restrinja o uso de senhas anteriores
 - Bloqueio de contas de usuário após falhas de login
 - Desative todos os binários SUID/SGID indesejados

Esta lista está incompleta, pois a segurança não é um produto, mas um processo. Isto significa que devem ser sempre tomadas medidas específicas para proteger melhor os sistemas, e isso depende do quão bem os administradores conhecem os seus sistemas operativos. Quanto melhor os administradores estiverem familiarizados com o sistema e quanto mais treinados forem, melhores e mais seguras serão as suas precauções e medidas de segurança.

## Wrappers TCP

Wrapper TCP é um mecanismo de segurança usado em sistemas Linux que permite ao administrador do sistema controlar quais serviços têm permissão de acesso ao sistema. Funciona restringindo o acesso a determinados serviços com base no nome do host ou endereço IP do usuário que solicita acesso. Quando um cliente tenta se conectar a um serviço, o sistema primeiro consulta as regras definidas nos arquivos de configuração dos wrappers TCP para determinar o endereço IP do cliente. Se o endereço IP corresponder aos critérios especificados nos arquivos de configuração, o sistema concederá ao cliente acesso ao serviço. Porém, caso os critérios não sejam atendidos, a conexão será negada, proporcionando uma camada adicional de segurança ao serviço. Os wrappers TCP usam os seguintes arquivos de configuração:

 - /etc/hosts.allow

 - /etc/hosts.deny

Resumindo, o arquivo **/etc/hosts.allow** especifica quais serviços e hosts têm permissão de acesso ao sistema, enquanto o arquivo **/etc/hosts.deny** especifica quais serviços e hosts não têm permissão de acesso. Esses arquivos podem ser configurados adicionando regras específicas aos arquivos

### /etc/hosts.allow

`$ cat /etc/hosts.allow`

># Allow access to SSH from the local network \
>sshd : 10.129.14.0/24 \
>
># Allow access to FTP from a specific host \
>ftpd : 10.129.14.10 \
>
># Allow access to Telnet from any host in the inlanefreight.local domain \
>telnetd : .inlanefreight.local \

### /etc/hosts.deny

`cat /etc/hosts.deny`

># Deny access to all services from any host in the inlanefreight.com domain \
>ALL : .inlanefreight.com \
>
># Deny access to SSH from a specific host \
>sshd : 10.129.22.22
>
># Deny access to FTP from hosts with IP addresses in the range of 10.129.22.0 to 10.129.22.255 \
>ftpd : 10.129.22.0/24 \

É importante lembrar que a ordem das regras nos arquivos é importante. A primeira regra que corresponder ao serviço e host solicitado é a que será aplicada. Também é importante observar que os wrappers TCP não substituem um firewall, pois são limitados pelo fato de só poderem controlar o acesso aos serviços e não às portas.



