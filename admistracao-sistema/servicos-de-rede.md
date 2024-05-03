# Serviços de rede

Não conseguiremos cobrir todos os serviços da rede, mas nos concentraremos e cobriremos os mais importantes. Porque não só do ponto de vista de um administrador e usuário, é de grande benefício, mas também como um testador de penetração para a interação entre outros hosts e nossa máquina.

## SSH

Secure Shell (SSH) é um protocolo de rede que permite a transmissão segura de dados e comandos em uma rede. É amplamente utilizado para gerenciar sistemas remotos com segurança e acessar sistemas remotos com segurança para executar comando ou tranferir arquivos. Para se conectar ao nosso host Linux remoto via SSH, um servidor SSH correspondente deve estar disponível e em execução.

O servidor SSH mais comumente usado é o servidor OpenSSH. OpenSSH é uma implementação gratuita de código aberto em uma rede.

Os administradores usam OpenSSH para gerenciar sistemas remotos com segurança, estabelecendo uma conexão criptografada com um host remoto. Com o OpenSSH, os administradores podem executar comandos em sistemas remotos, tranferir arquivos com segurança e estabelecer uma conexão remota sem que a transmissão de dados e comandos seja interpretada por terceiros.

### Instale o OpenSSH

`$ sudo apt install openssh-server -y`

Para verificar se o servidor está funcionando, podemos usar o seguinte comando:
### Status do servidor

`systemctl status ssh`

Como testadores de penetração, usamos OpenSSH para acessar sistemas remotos com segurança ao realizar uma auditoria de rede. Para fazer isso, podemos usar o seguinte comando:

### SSH - LOGIN

`$ cry0l1t3@10.129.17.122`

O OpenSSH pode ser configurado e personalizado editando o arquivo **/ect/ssh/sshd_config** com um editor de texto. Aqui podemos ajustar configurações com o número máximo de conexões simultâneas, o uso de senhas ou chaves para login, verificação de chave de host e muito mais. No entanto, é importante observarmos que as alterações no arquivo de configuração do OpenSSH devem ser feitas com cuidado.

Por exemplo, podemos usar SSH para fazer login com segurança em um sistema remoto e executar comandos ou usar tunelamento e encaminhamento de porta para encapsular dados por meio de uma conexão criptografada para verificar as configurações de rede e outras configurações do sistema sem a possibilidade de terceiros interceptarem a transmissão de dados e comandos.

## NFS

Network File System ( NFS) é um protocolo de rede que nos permite armazenar e gerenciar arquivos em sistemas remotos como se estivessem armazenados no sistema local. Ele permite o gerenciamento fácil e eficiente de arquivos nas redes. Por exemplo, os administradores usam NFS para armazenar e gerenciar arquivos centralmente (para sistemas Linux e Windows) para permitir fácil colaboração e gerenciamento de dados. Para Linux, existem vários servidores NFS, incluindo NFS-UTILS ( Ubuntu), NFS-Ganesha ( Solaris) e OpenNFS ( Redhat Linux).

Também pode ser usado para compartilhar e gerenciar recursos de forma eficiente, por exemplo, para replicar sistemas de arquivos entre servidores. Ele também oferece recursos como controles de acesso, transferência de arquivos em tempo real e suporte para vários usuários acessando dados simultaneamente. Podemos usar este serviço como o FTP caso não haja nenhum cliente FTP instalado no sistema de destino ou o NFS esteja sendo executado em vez do FTP.

Podemos instalar o NFS no Linux com o seguinte comando:

### Instalar NFS

`$ sudo apt install nfs-kernel-server -y`

Para verificar se o servidor está funcionando, podemos usar o seguinte comando:
### Status do servidor

`$ systemctl status nfs-kernel-server`

Podemos configurar o NFS através do arquivo de configuração **/etc/exports**. Este arquivo especifica quais diretórios devem ser compartilhados e os direitos de acesso para usuários e sistemas. Também é possível definir configurações como velocidade de transferência e uso de criptografia. Os direitos de acesso NFS determinam quais usuários e sistemas podem acessar os diretórios compartilhados e quais ações eles podem executar. Aqui estão alguns direitos de acesso importantes que podem  ser configurados no NFS:

|  Permissões   | Description |
| ------------- |     ---     |
|      `rw`     | Concede aos usuários e sistemas permissões de leitura e gravação no diretório compartilhado. |
|      `ro`     | Fornece aos usuários e sistemas acesso somente leitura ao diretório compartilhado. |
| `no_root_squash` | Impede que o usuário root no cliente fique restrito aos direitos de um usuário normal. |
| `root_squash` |Restringe os direitos do usuário root no cliente aos direitos de um usuário normal.  |
|     `sync`    | Sincroniza a transferência de dados para garantir que as alterações sejam transferidas somente após serem salvas no sistema de arquivos. |
|    `async`    | Transfere dados de forma assíncrona, o que torna a transferência mais rápida, mas pode causar inconsistências no sistema de arquivos se as alterações não tiverem sido totalmente confirmadas. |













