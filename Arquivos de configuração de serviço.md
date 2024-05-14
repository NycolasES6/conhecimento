#server 
# Arquivos de configuração de serviço

No Linux, os serviços são gerenciados usando arquivos de configuração. As opções comuns nos arquivos de configuração são o número da porta, a localização dos recursos hospedados e os detalhes da autorização do cliente. Quando o serviço é iniciado, ele procura seus arquivos de configuração, carrega-os na memória e se ajusta de acordo com as configurações nos arquivos. As modificações do arquivo de configuração geralmente exigem a reinicialização do serviço antes que as alterações entrem em vigor.

Como os serviços geralmente exigem privilégios de superusuário para serem executados, os arquivos de configuração de serviço geralmente exigem privilégios de superusuário para editar.

A saída do comando mostra uma parte do arquivo de configuração do Nginx, que é um servidor web leve para Linux.

```txt
[analyst@secOps ~]$ cat /etc/nginx/nginx.conf

#user html;

worker_processes  1;

#error_log  logs/error.log;

#error_log  logs/error.log  notice;

#error_log  logs/error.log  info;

#pid        logs/nginx.pid;

events {

    worker_connections 1024;

}

http {

   include      mime.types;

   default_type  application/octet-stream;

   #log_format main '$remote_addr - $remote_user [$time_local] "$request"'

   #                  '$status $body_bytes_sent "$http_referer"'

   #                  '"$http_user_agent" "$http_x_forwarded_for"';

   #access_log logs/access.log main;
```

A próxima saída do comando mostra o arquivo de configuração para o protocolo de tempo de rede (NTP).

```txt
[analyst@secOps ~]$ cat /etc/ntp.conf

# Please consider joining the pool:

#

#        http://www.pool.ntp.org/join.html

#

# For additional information see:

# - https://wiki.archlinux.org/index.php/Network_Time_Protocol_daemon

# - http://support.ntp.org/bin/view/Support/GettingStarted

# - the ntp.conf man page

# Associate to Arch's NTP pool

server 0.arch.pool.ntp.org

server 1.arch.pool.ntp.org

server 2.arch.pool.ntp.org

server 3.arch.pool.ntp.org

# By default, the server allows:

# - all queries from the local host

# - only time queries from remote hosts, protected by rate limiting and kod

restrict default kod limited nomodify nopeer noquery notrap

restrict 127.0.0.1

restrict ::1

# Location of drift file

[analyst@secOps ~]$
```

A saída do último comando mostra o arquivo de configuração do Snort, um sistema de detecção de intrusões (IDS) baseado em Linux.

```txt
[analyst@secOps ~]$ cat /etc/snort/snort.conf

#--------------------------------------------------

#   VRT Rule Packages Snort.conf

#

#   For more information visit us at:

#      http://www.snort.org                 Snort Website

#       http://vrt-blog.snort.org/          Sourcefire VRT Blog

#

#      Mailing list Contact:    snort-sigs@lists.sourceforge.net

#      False Positive reports:  fp@sourcefire.com

#      Snort bugs:              bugs@snort.org

#

#      Compatible with Snort Versions:

#      VERSIONS :2.9.9.0

#

#      Snort build options:

#      OPTIONS : --enable-gre --enable-mpls --enable-targetbased --enable-ppm --enable-perfprofiling --

enable-zlib --enable-active-response --enable-normalizer --enable-reload --enable-react --enable-

flexresp3

###################################################

# Step #1: Set the network variables. For more information, see README.variables

###################################################

# Setup the network addresses you are protecting

###ipvar HOME_NET any

###ipvar HOME_NET [192.168.0.0/24,192.168.1.0/24]

ipvar HOME_NET [209.165.200.224/27]

# Set up the external network addresses. Leave as "any" in most situations

ipvar EXTERNAL_NET any
```

Não há regra para um formato de arquivo de configuração; é a escolha do desenvolvedor do serviço. No entanto, o formato **opção = valor** é frequentemente usada. Por exemplo, na última saída do comando, a variável **ipvar** é configurada com várias opções. A primeira opção, HOME_NET, tem o valor 209.165.200.224/27. O caractere hash **(#)** é usado para indicar comentários.






