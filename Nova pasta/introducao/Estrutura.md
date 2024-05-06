# Estrutura do linux

## Filosofia

O linux segue  5  princípios principais.

### Tudo é um arquivo

Todos os arquivos de configuração dos vários serviços executados no sistema operacional Linux são armazenados em um ou mais arquivos de texto.

### Programas pequenos e de propósito único

O Linux oferece muitas ferramentas diferentes com as quais trabalharemos, que podem ser combinadas para trabalharmos juntas.

### Capacidade de encadear programas para executar tarefas complexas

A integração e combinação de diferentes ferramentas permitem-nos realizar muitas tarefas grandes e complexas, como processar ou filtrar resultados de dados específicos.

### Evitar depender da interface de usuário

O Linux foi projetado para funcionar principalmente com o shell (ou terminal), o que dá ao usuário maior controle sobre o sistema operacional.

### Dados de configuração armazenados em arquivos de texto

Um exemplo desse tipo de arquivo é o ``/etc/passwd`` arquivo que armazena todos os usuários cadastrados no sistema.

## Componentes

### Bootloader

Um trecho de código executado para orientar o processo de inicialização para iniciar o sistema operacional. Parrot Linux usa o carregador de inicialização GRUB.

### OS Kernel

O kernel é o principal componente de um sistema operacional. Ele gerencia os recursos dos dispositivos de E/S do sistema no nível do hardware.

### Daemons

Os serviços em segundo plano são chamados de “daemons” no Linux. Seu objetivo é garantir que funções importantes como agendamento, impressão e multimídia estejam funcionando corretamente. Esses pequenos programas são carregados depois que inicializamos ou fazemos login no computador.

### OS Shell

O shell do sistema operacional ou interpretador de linguagem de comando (também conhecido como linha de comando) é a interface entre o sistema operacional e o usuário. Esta interface permite ao usuário informar ao sistema operacional o que fazer. Os shells mais comumente usados ​​são `Bash, Tcsh/Csh, Ksh, Zsh e Fish`.

### Graphics Server

Isso fornece um subsistema gráfico (servidor) chamado "X" ou "servidor X" que permite que programas gráficos sejam executados local ou remotamente no sistema de janelas X.

### Window Manager

Também conhecida como interface gráfica do usuário (GUI). Existem muitas opções, incluindo GNOME, KDE, MATE, Unity e Cinnamon. Um ambiente de desktop geralmente possui vários aplicativos, incluindo navegadores de arquivos e da web. Eles permitem ao usuário acessar e gerenciar os recursos e serviços essenciais e frequentemente acessados ​​de um sistema operacional.

### Utilities

Aplicativos ou utilitários são programas que executam funções específicas para o usuário ou outro programa.

## Arquitetura Linux

### Hardware

Dispositivos periféricos como RAM do sistema, disco rígido, CPU e outros.

### Kernel

O núcleo do sistema operacional Linux cuja função é virtualizar e controlar recursos comuns de hardware de computador, como CPU, memória alocada, dados acessados, entre outros. O kernel fornece a cada processo seus próprios recursos virtuais e evita/mitiga conflitos entre diferentes processos.

### Shell

Uma interface de linha de comando ( CLI ), também conhecida como shell, na qual um usuário pode inserir comandos para executar as funções do kernel.

### System Utility

Disponibiliza ao usuário todas as funcionalidades do sistema operacional.

## Hierarquia do sistema de arquivos

O sistema operacional Linux é estruturado em uma hierarquia semelhante a uma árvore e está documentado no Filesystem Hierarchy Standard (FHS). O Linux está estruturado com os seguintes diretórios padrão de nível superior:

### /

O diretório de nível superior é o sistema de arquivos raiz e contém todos os arquivos necessários para inicializar o sistema operacional antes que outros sistemas de arquivos sejam montados, bem como os arquivos necessários para inicializar os outros sistemas de arquivos. Após a inicialização, todos os outros sistemas de arquivos são montados em pontos de montagem padrão como subdiretórios da raiz.

### /bin

Contém binários de comando essenciais.

### /boot

Consiste no bootloader estático, no executável do kernel e nos arquivos necessários para inicializar o sistema operacional Linux.

### /dev

Contém arquivos de dispositivos para facilitar o acesso a todos os dispositivos de hardware conectados ao sistema.

### /etc

Arquivos de configuração do sistema local. Os arquivos de configuração dos aplicativos instalados também podem ser salvos aqui.

### /home

Cada usuário no sistema possui um subdiretório aqui para armazenamento.

### /lib

Arquivos de biblioteca compartilhada necessários para inicialização do sistema.

### /media

Dispositivos de mídia removíveis externos, como unidades USB, são montados aqui.

### /mnt

Ponto de montagem temporário para sistemas de arquivos regulares.

### /opt

Arquivos opcionais, como ferramentas de terceiros, podem ser salvos aqui.

### /root

O diretório inicial do usuário root.

### /sbin

Este diretório contém executáveis ​​usados ​​para administração do sistema (arquivos binários do sistema).

### /tmp

O sistema operacional e muitos programas usam esse diretório para armazenar arquivos temporários. Este diretório geralmente é limpo na inicialização do sistema e pode ser excluído em outros momentos sem qualquer aviso.

### /usr

Contém executáveis, bibliotecas, arquivos man, etc.

### /var

Este diretório contém arquivos de dados variáveis, como arquivos de log, caixas de entrada de e-mail, arquivos relacionados a aplicativos da web, arquivos cron e muito mais.

![alt text](./img/hierarquia-sistema-de-arquivos.png)
