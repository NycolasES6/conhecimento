# Logs do sistema

Os logs do sistema no Linux são um conjunto de arquivos que contêm informações sobre o sistema e as atividades que ocorrem nele. Esses logs são importantes para monitorar e solucionar problemas do sistema, pois podem fornecer insights sobre o comportamento do sistema, a atividade do aplicativo e os eventos de segurança. Esses logs do sistema também podem ser uma fonte valiosa de informações para identificar possíveis pontos fracos e vulnerabilidades de segurança em um sistema Linux. Ao analisar os logs em nossos sistemas de destino, podemos obter insights sobre o comportamento do sistema, a atividade da rede e a atividade do usuário e podemos usar essas informações para identificar qualquer atividade anormal, como logins não autorizados, tentativas de ataques, credenciais de texto não criptografado ou arquivos incomuns. acesso, o que pode indicar uma possível violação de segurança.

Nós, como testadores de penetração, também podemos usar logs do sistema para monitorar a eficácia de nossas atividades de testes de segurança. Ao revisar os logs após realizar testes de segurança, podemos determinar se nossas atividades desencadearam algum evento de segurança, como alertas de detecção de intrusão ou avisos do sistema. Essas informações podem nos ajudar a refinar nossas estratégias de testes e melhorar a segurança geral do sistema.

Para garantir a segurança de um sistema Linux, é importante configurar os logs do sistema corretamente. Isso inclui definir os níveis de log apropriados, configurar a rotação de logs para evitar que os arquivos de log fiquem muito grandes e garantir que os logs sejam armazenados com segurança e protegidos contra acesso não autorizado. Além disso, é importante rever e analisar regularmente os registos para identificar potenciais riscos de segurança e responder a quaisquer eventos de segurança em tempo útil. Existem vários tipos diferentes de logs do sistema no Linux, incluindo:

 - logs do kernel
 - logs do sistema
 - logs de autenticação
 - logs de aplicativos
 - logs de segurança

## Logs do kernel

Esses logs contêm informações sobre o kernel do sistema, incluindo drivers de hardware, chamadas do sistema e eventos do kernel. Eles são armazenados no arquivo **/var/log/kern.log**. Por exemplo, os logs do kernel podem revelar a presença de drivers vulneráveis ou desatualizados que podem ser alvo de invasores para obter acesso ao sistema. Eles também podem fornecer insights sobre falhas no sistema, limitações de recursos e outros eventos que podem levar à negação de serviço ou a outros problemas de segurança. Além disso, os logs do kernel podem nos ajudar a identificar chamadas de sistema suspeitas ou outras atividades que possam indicar a presença de malware ou outro software malicioso no sistema. Ao monitorar o arquivo **/var/log/kern.log**, podemos detectar qualquer comportamento incomum e tomar as medidas adequadas para evitar maiores danos ao sistema.

## Logs do sistema

Esses logs contêm informações sobre eventos no nível do sistema, como inícios e paradas de serviços, tentativas de login e reinicializações do sistema. Eles são armazenados no arquivo **/var/log/syslog**. Ao analisar tentativas de login, inícios e paradas de serviços e outros eventos no nível do sistema, podemos detectar quaisquer possíveis acessos ou atividades no sistema. Isso pode nos ajudar a identificar quaisquer vulnerabilidades que possam ser exploradas e a recomendar medidas de segurança para mitigar esses riscos. Além disso, podemos usar o syslogpara identificar possíveis problemas que possam afetar a disponibilidade ou o desempenho do sistema, como falha na inicialização do serviço ou na reinicialização do sistema. Aqui está um exemplo de como esse arquivo **syslog** poderia ser:

### Logs do sistema

    Feb 28 2023 15:00:01 server CRON[2715]: (root) CMD (/usr/local/bin/backup.sh)
    Feb 28 2023 15:04:22 server sshd[3010]: Failed password for htb-student from 10.14.15.2 port 50223 ssh2
    Feb 28 2023 15:05:02 server kernel: [  138.303596] ata3.00: exception Emask 0x0 SAct 0x0 SErr 0x0 action 0x6 frozen
    Feb 28 2023 15:06:43 server apache2[2904]: 127.0.0.1 - - [28/Feb/2023:15:06:43 +0000] "GET /index.html HTTP/1.1" 200 13484 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    Feb 28 2023 15:07:19 server sshd[3010]: Accepted password for htb-student from 10.14.15.2 port 50223 ssh2
    Feb 28 2023 15:09:54 server kernel: [  367.543975] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro
    Feb 28 2023 15:12:07 server systemd[1]: Started Clean PHP session files.

### logs de autenticação

Esses logs contêm informações sobre tentativas de autenticação do usuário, incluindo tentativas bem-sucedidas e mal sucedidas. Eles são armazenados no arquivo**/var/log/auth.log**. É importante observar que, embora o arquivo **/var/log/syslog** possa conter informações de login semelhantes, o arquivo **/var/log/auth.log** se concentra especificamente nas tentativas de autenticação do usuário, tornando-o um recurso mais valioso para identificar possíveis ameaças à segurança. Portanto, é essencial que os testadores de penetração revisem os logs armazenados no arquivo **/var/log/auth.log** para garantir que o sistema esteja seguro e não tenha sido comprometido.

### Auth.log

    Feb 28 2023 18:15:01 sshd[5678]: Accepted publickey for admin from 10.14.15.2 port 43210 ssh2: RSA SHA256:+KjEzN2cVhIW/5uJpVX9n5OB5zVJ92FtCZxVzzcKjw
    Feb 28 2023 18:15:03 sudo:   admin : TTY=pts/1 ; PWD=/home/admin ; USER=root ; COMMAND=/bin/bash
    Feb 28 2023 18:15:05 sudo:   admin : TTY=pts/1 ; PWD=/home/admin ; USER=root ; COMMAND=/usr/bin/apt-get install netcat-traditional
    Feb 28 2023 18:15:08 sshd[5678]: Disconnected from 10.14.15.2 port 43210 [preauth]
    Feb 28 2023 18:15:12 kernel: [  778.941871] firewall: unexpected traffic allowed on port 22
    Feb 28 2023 18:15:15 auditd[9876]: Audit daemon started successfully
    Feb 28 2023 18:15:18 systemd-logind[1234]: New session 4321 of user admin.
    Feb 28 2023 18:15:21 CRON[2345]: pam_unix(cron:session): session opened for user root by (uid=0)
    Feb 28 2023 18:15:24 CRON[2345]: pam_unix(cron:session): session closed for user root

Neste exemplo, podemos ver na primeira linha que uma chave pública bem-sucedida foi usada para autenticação do usuário admin. Além disso, podemos ver que este usuário está no grupo **sudoers** porque ele pode executar comandos usando **sudo**. A mensagem do kernel indica que foi permitido tráfego inesperado na porta 22, o que pode indicar uma possível violação de segurança. Depois disso, vemos que uma nova sessão foi criada para o usuário “admin” prlo **systemd-login** e que uma sessão **cron** foi aberta e fechada para o usuário root.

## Logs de aplicativos

Esses logs contêm informações sobre as atividades de aplicativos específicos em execução no sistema. Eles geralmente são armazenados em seus próprios arquivos, como **/var/log/apache2/error.log** no servidor web Apache ou **/var/log/mysql/error.log** no servidor de banco de dados MySQL. Esses logs são particularmente importantes quando visamos aplicativos específicos, como servidores web ou bancos de dados, pois podem fornecer insights sobre como esses aplicativos estão processando e manipulando dados. Ao examinar esses logs, podemos identificar possíveis vulnerabilidades ou configurações incorretas. Por exemplo, os logs de acesso podem ser usados para rastrear solicitações feitas a um servidor web, enquanto os logs de auditoria podem ser usados para rastrear alterações feitas no sistema ou em arquivos específicos. Esses registros podem ser usados para identificar tentativas de acesso não autorizado, exfiltração de dados ou outras atividades suspeitas.

Além disso, os logs de acesso e auditoria são logs críticos que registram informações sobre as ações dos usuários e processos no sistema. Eles são cruciais para fins de segurança e conformidade e podemos usá-los para identificar possíveis problemas de segurança e vetores de ataque.

Por exemplo, **access logs** mantém um registro das atividades de usuários e processos no sistema, incluindo tentativas de login, acessos a arquivos e conexões de rede. **Audit logs** registra informações sobre eventos relevantes para a segurança no sistema, como modificações nos arquivos de configuração do sistema ou tentativas de modificar arquivos ou configurações do sistema. Esses registros ajudam a rastrear possíveis ataques e atividades ou a identificar violações de segurança ou outros problemas. Um exemplo de entrada em um arquivo de log de acesso pode ser semelhante ao seguinte:

### Entrada de log de acesso

    2023-03-07T10:15:23+00:00 servername privileged.sh: htb-student accessed /root/hidden/api-keys.txt

Nesta entrada de log, podemos ver que o usuário **htb-student** utilizou o script **privileged.sh** para acessar o arquivo **api-keys.txt** no /root/hidden/diretório. Em sistemas Linux, os serviços mais comuns possuem locais padrão para logs de acesso:

| Serviço | Descrição |
| :--- | :--- |
| Apache | Os logs de acesso são armazenados no arquivo /var/log/apache2/access.log (ou similar, dependendo da distribuição). |
| Ngnix | Os logs de acesso são armazenados no arquivo /var/log/nginx/access.log (ou similar). |
| OpenSSH | Os logs de acesso são armazenados no arquivo /var/log/auth.log no Ubuntu e em /var/log/secure no CentOS/RHEL. |
| MySQL | Os logs de acesso são armazenados no arquivo /var/log/mysql/mysql.log. |
| PostgreSQL | Os logs de acesso são armazenados no arquivo /var/log/postgresql/postgresql-version-main.log. |
| Systemd | Os logs de acesso são armazenados no diretório /var/log/journal/. |

## Logs de segurança

Esses logs de segurança e seus eventos geralmente são registrados em vários arquivos de log, dependendo do aplicativo ou ferramenta de segurança pecífica em uso. Por exemplo, o aplicativo Fail2ban registra tentativas de login mal sucedidas no arquivo **/var/log/auth.log**, enquanto o firewall UFW registra atividades no arquivo **/var/log/ufw.log**. Outros eventos relacionados á segurança, como alterações nos arquivos ou configurações do sistema, podem ser registrados em registros mais gerais do sistema, como **/var/log/syslog** ou **/var/log/auth.log**. Como testadores de penetração, podemos usar ferramentas e técnicas de análise de log para procurar eventos ou padrões de atividade específicos que possam indicar um problema de segurança e usar essas informações para testar ainda mais o sistema em busca de vulnerabilidades ou possíveis vetores de ataque.

É importante estar familiarizado com os locais padrão para logs de acesso e outros arquivos de log em sistemas Linux, pois essas informações podem ser úteis ao realizar uma avaliação de segurança ou teste de penetração. Ao compreender como os eventos relacionados à segurança são registrados e armazenados, podemos analisar de forma mais eficaz os dados de log e identificar possíveis problemas de segurança.

Todos esses logs podem ser acessados e analisados usando uma variedade de ferramentas, incluindo os visualizadores de arquivos de log integrados na maioria dos ambientes de desktop Linux, bem como ferramentas de linha de comando, como od comandos **tail**, **grep** e **sed**. A análise adequada dos logs do sistema pode ajudar a identificar e solucionar problemas do sistema, bem como detectar violações de segurança e outros eventos de interesse.

