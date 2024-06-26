# Linux - Serviços de rede

Não conseguiremos cobrir todos os serviços da rede, mas nos concentraremos e cobriremos os mais importantes. Porque não só do ponto de vista de um administrador e usuário, é de grande benefício, mas também como um testador de penetração para a interação entre outros hosts e nossa máquina.

## SSH

Secure Shell (SSH) é um protocolo de rede que permite a transmissão segura de dados e comandos em uma rede.

Para que haja a comunicação é necessário um cliente SSH e um servidor SSH.

O servidor SSH mais comumente usado é o servidor OpenSSH. Open SSH é uma implementação gratuita e de código aberto do protocolo Secure Shell (SSH) que permite a transmissão segura de dados e comandos em uma rede.

### Instalando o OpenSSH

```sh
sudo apt install openssh-server -y
```

Para verificar se o servidor está funcionando, podemos usar o seguinte comando:

```shell
systemctl status ssh

● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/system/system/ssh.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2023-02-12 21:15:27 GMT; 1min 22s ago
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 7740 (sshd)
      Tasks: 1 (limit: 9458)
     Memory: 2.5M
        CPU: 236ms
     CGroup: /system.slice/ssh.service
             └─7740 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
```

Como pentesters, usamos OpenSSH para acessar sistemas remotos com segurança ao realizar uma auditoria de rede. Para fazer isso, podemos usar o seguinte comando :

### SSH - Login

```sh
ssh cry0l1t3@10.129.17.122
```

O OpenSSH pode ser configurado e personalizado editando o arquivo `/etc/ssh/sshd_config` com um editor de texto.

Aqui podemos ajustar configurações como o número máximo de conexões simultâneas, o uso de senhas ou chaves para logins, verificação de chave de host e muito mais. No entanto, é importante observarmos que as alterações no arquivo de configuração do OpenSSH devem ser feitas com cuidado.

## NFS

Network File System (`NFS`) é um protocolo de rede que nos permite armazenar e gerenciar arquivos em sistemas remotos como se tivessem armazenados no sistema local. Ele permite o gerenciamento fácil e eficiente de arquivos nas redes.

Por exemplo, os administradores usam NFS para armazenar e gerenciar arquivos centralmente (para sistemas Linux e Windows) para permitir fácil colaboração e gerenciamento de dados. Para Linux, existem vários servidores NFS, incluindo NFS-UTILS ( `Ubuntu`), NFS-Ganesha ( `Solaris`) e OpenNFS ( `Redhat Linux`).

Também pode ser usado para compartilhar e gerenciar recursos de forma eficiente, por exemplo, para replicar sistemas de arquivos entre servidores. Ele também oferece recursos como controles de acesso, transferência de arquivos em tempo real e suporte para vários usuários acessando dados simultaneamente. Podemos usar este serviço como o FTP caso não haja nenhum cliente FTP instalado no sistema de destino ou o NFS esteja sendo executado em vez do FTP.

### Instalar o NFS

```sh
sudo apt install nfs-kernel-server -y
```

Para verificar se o servidor está funcionando, podemos usar o seguinte comando:

###  Status do servidor

```sh
systemctl status nfs-kernel-server
```

Podemos configurar o NFS através do arquivo de configuração `/etc/exports`.

Este arquivo especifica quais diretórios devem ser compartilhados e os direitos de acesso para usuários e sistemas.

Também é possível definir configurações como velocidade de transferência e uso de criptografia. Os direitos de acesso NFS determinam quais usuários e sistemas podem acessar os diretórios compartilhados e quais ações eles podem executar. Aqui estão alguns direitos de acesso importantes que podem ser configurados no NFS:

| **Permissões**   | **Descrição**                                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rw`             | Concede aos usuários e sistemas permissões de leitura e gravação no diretório compartilhado.                                                                                                   |
| `ro`             | Fornece aos usuários e sistemas acesso somente leitura ao diretório compartilhado.                                                                                                             |
| `no_root_squash` | Impede que o usuário root no cliente fique restrito aos direitos de um usuário normal.                                                                                                         |
| `root_squash`    | Restringe os direitos do usuário root no cliente aos direitos de um usuário normal.                                                                                                            |
| `sync`           | Sincroniza a transferência de dados para garantir que as alterações sejam transferidas somente após serem salvas no sistema de arquivos.                                                       |
| `async`          | Transfere dados de forma assíncrona, o que torna a transferência mais rápida, mas pode causar inconsistências no sistema de arquivos se as alterações não tiverem sido totalmente confirmadas. |

Podemos criar uma nova pasta e compartilhá-la temporariamente no NFS. Faríamos isso da seguinte maneira:

### Criar compartilhamento NFS

```sh
mkdir nfs_sharing
echo '/home/cry0l1t3/nfs_sharing hostname(rw,sync,no_root_squash)' >> /etc/exports
cat /etc/exports | grep -v "#"
```

Se criamos um compartilhamento NFS e queremos trabalhar com ele no sistema de destino, precisamos montá-lo primeiro. Podemos fazer isso com o seguinte comando:

### Montar compartilhamento NFS

```sh
mkdir ~/target_nfs
mount 10.129.12.17:/home/john/dev/_scripts ~/target_nfs
tree ~/target_nfs
```

Portanto, montamos o compartilhamento NFS ( `dev_scripts`) de nosso destino ( `10.129.12.17`) localmente em nosso sistema no ponto de montagem `target_nfs`pela rede e podemos visualizar o conteúdo como se estivéssemos no sistema de destino. Existem até alguns métodos que podem ser usados ​​em casos específicos para escalar nossos privilégios no sistema remoto usando NFS.

## Servidor WEB

Um servidor web é um tipo de software que fornece dados e documentos ou outros aplicativos e funções pela Internet. Eles usam o protocolo de transferência de hipertexto (HTTP) para enviar dados a clientes, como navegadores da web, e receber solicitações desses clientes. Eles são então renderizados na forma de Hypertext Markup Language (HTML) no navegador do cliente.

O servidor web Apache possui uma variedade de recursos que nos permitem hospedar um aplicativo web seguro e eficiente. Além disso, também podemos configurar o log para obter informações sobre o tráfego em nosso servidor, o que nos ajuda a analisar ataques. Podemos instalar o Apache usando o seguinte comando:

### Instale o servidor web Apache

```sh
sudo apt install apache2 -y
```

Para Apache2, para especificar quais pastas podem ser acessadas, podemos aditar o arquivo `/etc/apache2/apache2.conf` com um editor de texto. Este arquivo contém as configurações globais. Podemos alterar as configurações para especificar quais diretórios podem ser acessados e quais ações podem ser executadas nesses diretórios.

### Configuração Apache

```txt
<Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
</directory>
```

Esta seção especifica que a pasta padrão `/var/www/html`está acessível, que os usuários podem usar as opções `Indexes`e `FollowSymLinks`, que as alterações nos arquivos neste diretório podem ser substituídas por `AllowOverride All`e que `Require all granted`concede a todos os usuários acesso a este diretório.

Por exemplo, se quisermos transferir arquivos para um de nossos sistemas de destino usando um servidor web, podemos colocar os arquivos apropriados na `/var/www/html`pasta e usar `wget`ou `curl`outros aplicativos para baixar esses arquivos no sistema de destino.

Também é possível personalizar configurações individuais no nível do diretório usando o `.htaccess`arquivo, que podemos criar no diretório em questão.

Este arquivo nos permite definir certas configurações em nível de diretório, como controles de acesso, sem precisar personalizar o arquivo de configuração do Apache.
Também podemos adicionar módulos para obter recursos como `mod_rewrite`, `mod_security`e `mod_ssl`que nos ajudam a melhorar a segurança de nosso aplicativo web.

## Instale python e servidor web

```sh
sudo apt install python3 -y
python3 -m http.server
```

Ao executarmos este comando, nosso servidor Web Python será iniciado na porta TCP/8000 e poderemos acessar a pasta em que estamos atualmente.
Também podemos hospedar outra pasta com o seguinte comando:

```sh
python3 -m http.server --directory /home/cry0l1t3/target_files
```

Também podemos hospedar nosso servidor web Python em uma porta diferente da porta padrão usando a opção `-p`:

```sh
python3 -m http.server -p 443
```

Isso hospedará nosso servidor web Python na porta 443 em vez da porta padrão `TCP/8000`. Podemos acessar este servidor web digitando o link em nosso navegador.

## VPN

Rede Privada Virtual ( `VPN`) é uma tecnologia que nos permite conectar-nos com segurança a outra rede como se estivéssemos diretamente nela. Isso é feito criando uma conexão de túnel criptografada entre o cliente e o servidor,

Alguns dos servidores VPN mais populares para servidores Linux são OpenVPN, L2TP/IPsec, PPTP, SSTP e SoftEther.

O OpenVPN nos fornece uma variedade de recursos, incluindo criptografia, tunelamento, modelagem de tráfego, roteamento de rede e a capacidade de se adaptar a redes que mudam dinamicamente.


### Instale o OpenVPN

```bash
sudo apt install openvpn -y
```

OpenVPN pode ser personalizado e configurado editando o arquivo de configuração `/etc/openvpn/server.conf`.

### Conecte-se á VPN

Podemos nos conectar a uma VPN através de um arquivo `.ovpn`

```bash
sudo openvpn --config internal.ovpn
```

Depois que a conexão for estabelecida, podemos nos comunicar com os hosts internos da rede interna.























































































