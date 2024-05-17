#Linux 
# Instalando e executando aplicativos em um host Linux

Muitos aplicativos de usuário final são programas complexos escritos em linguagens compiladas. Para ajudar no processo de instalação, o Linux geralmente inclui programas chamados gerenciadores de pacotes. Um pacote é o termo usado para se referir a um programa e todos os seus arquivos de suporte. Ao usar um gerenciador de pacotes para instalar um pacote, todos os arquivos necessários são colocados no local correto do sistema de arquivos.

Os gerenciadores de pacotes variam dependendo das distribuições do Linux. Por exemplo, **pacman** é usado pelo Arch Linux enquanto **dpkg** (pacote Debian) e **apt** (Advanced Packaging Tool) são usados em distribuições Debian e Ubuntu Linux.

A saída do comando mostra a saída de alguns comandos **apt-get** usados nas distribuições Debian.

```
analyst@cuckoo:~$ sudo apt-get update

[sudo] password for analyst:

Hit:l http://us.archive.ubuntu.com/ubuntu xenial InRelease

Get:2 http://us.archive.ubuntu.com/ubuntu xenial-updates InRelease [102 kB]

Get:3 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]

Get:4 http://us.archive.ubuntu.com/ubuntu xenial-backports InRelease [102 kB]

Get:5 http://us.archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [534 kB]

Fetched 4,613 kB in 4s (1,003 kB/s)

Reading package lists... Done

analyst@cuckoo:~$

analyst@cuckoo:~$ sudo apt-get upgrade

Reading package lists Done

Building dependency tree

Reading state information... Done

Calculating upgrade... Done

The following packages have been kept back:

linux-generic-hwe-16.04 linux-headers-generic-hwe-16.04

linux-image-generic-hwe-16.04

The following packages will be upgraded:

firefox firefox-locale-en girl.2-javascriptcoregtk-4.0 girl.2-webkit2-4.0 libjavascriptcoregtk-4.0-18

libwebkit2gtk-4.0-37 libwebkit2gtk-4.0-37-gtk2 libxen-4.6 libxenstore3.0 linux-libc-dev logrotate

openssh-client

qemu-block-extra qerau-kvm qemu-system-common qemu-system-x86 qemu-utils
```

O comando **apt-get update** é usado para obter a lista de pacotes do repositório de pacotes e atualizar o banco de dados de pacotes local. O comando **apt-get upgrade** é usado para atualizar todos os pacotes atualmente instalados para suas versões mais recentes.










