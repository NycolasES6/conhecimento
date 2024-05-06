# Protocolos de área remota no linux

Os protocolos de área de trabalho remota são usados ​​no Windows, Linux e macOS para fornecer acesso remoto gráfico a um sistema. Os administradores podem utilizar protocolos de área de trabalho remota em muitos cenários, como solução de problemas, atualização de software ou sistema e administração remota de sistemas. O administrador precisa se conectar ao sistema remoto que administrará remotamente e, portanto, usará o protocolo apropriado de acordo. Além disso, eles podem fazer login usando diferentes protocolos se quiserem instalar um aplicativo em seu sistema remoto. Os protocolos mais comuns para esse uso são RDP (Windows) e VNC (Linux).

## XServer

O XServer é a parte do lado do usuário do X Window System network protocol( X11/ X). O X11é um sistema fixo que consiste em uma coleção de protocolos e aplicativos que nos permitem chamar janelas de aplicativos em displays em uma interface gráfica de usuário. O X11 é predominante em sistemas Unix, mas os servidores X também estão disponíveis para outros sistemas operacionais. Hoje em dia, o XServer faz parte de quase todas as instalações desktop do Ubuntu e seus derivados e não precisa ser instalado separadamente.

Quando um desktop é iniciado em um computador Linux, a comunicação da interface gráfica do usuário com o sistema operacional acontece através de um servidor X. A rede interna do computador é usada, mesmo que o computador não deva estar em uma rede. O aspecto prático do protocolo X é a transparência da rede. Este protocolo usa principalmente TCP/IP como base de transporte, mas também pode ser usado em soquetes Unix puros. As portas utilizadas para o servidor X estão normalmente localizadas no intervalo de TCP/6001-6009, permitindo a comunicação entre o cliente e o servidor. Ao iniciar uma nova sessão de desktop via servidor X, o arquivo será TCP port 6000aberto para a primeira exibição do X. :0Essa faixa de portas permite que o servidor execute suas tarefas, como hospedar aplicativos, bem como fornecer serviços aos clientes. Eles são frequentemente usados para fornecer acesso remoto a um sistema, permitindo que os usuários acessem aplicativos e dados de qualquer lugar do mundo. Além disso, essas portas também são essenciais para o compartilhamento seguro de arquivos e dados, tornando-as parte integrante do Open X Server. Assim, um servidor X não depende do computador local, ele pode ser usado para acessar outros computadores e outros computadores podem usar o servidor X local. Desde que os computadores locais e remotos contenham sistemas Unix/Linux, protocolos adicionais como VNC e RDP são supérfluos. VNC e RDP geram a saída gráfica no computador remoto e a transportam pela rede. Já no X11, ele é renderizado no computador local. Isso economiza tráfego e carga no computador remoto. No entanto, a desvantagem significativa do X11 é a transmissão de dados não criptografada. No entanto, isso pode ser superado através do tunelamento do protocolo SSH.

Para isso, temos que permitir o encaminhamento do X11 no arquivo de configuração SSH ( /etc/ssh/sshd_config) no servidor que fornece a aplicação alterando esta opção para yes.

### Encaminhamento X11

`$ cat /etc/ssh/sshd_config | grep X11Forwarding`

Com isso podemos iniciar uma aplicação do nosso cliente com seguinte comando:

`$ ssh -X htb-student@10.129.23.11 /usr/bin/firefox`

### Segurança X11

O X11 não é um protocolo seguro sem medidas de segurança adequadas, uma vez que a comunicação do X11 é totalmente descriptografada. Um servidor X completamente aberto permite que qualquer pessoa na rede leia o conteúdo de suas janelas, por exemplo, e isso passa despercebido ao usuário sentado à sua frente. Portanto, nem é necessário farejar a rede. Esta funcionalidade padrão do X11 é realizada com ferramentas simples do X11 como **xwd** e **xgrabsc**. Resumindo, como testadores de penetração, poderíamos ler as teclas digitadas pelos usuários, obter capturas de tela, mover o cursor do mouse e enviar as teclas digitadas do servidor pela rede.

Um bom exemplo são várias vulnerabilidades de segurança encontradas no XServer, onde um invasor local pode explorar vulnerabilidades no XServer para executar código arbitrário com privilégios de usuário e obter privilégios de usuário. Os sistemas operacionais afetados por essas vulnerabilidades foram UNIX e Linux, Red Hat Enterprise Linux, Ubuntu Linux e SUSE Linux. Essas vulnerabilidades são conhecidas como CVE-2017-2624, CVE-2017-2625 e CVE-2017-2626.

## XDMCP

Protocolo **X Display Manager Control Protocol** é utilizado pelo **X Display Manager** para comunicação através da porta UDP 117 entre terminais X e computadores em Unix/Linux. Ele é usado para gerenciar sessões remotas do X Window wm outras máquinas e é frequentemente usado por administradores de sistema linus para fornecer acesso a desktops remotos. XDMCP é um procolo inseguro e não deve ser usado em nenhum smbiente que exija um alto nível de segurança.Com isso, é possível redirecionar toda uma interface gráfica de usuário ( GUI) (como KDE ou Gnome) para um cliente correspondente. Para que um sistema Linux atue como um servidor XDMCP, um sistema X com uma GUI deve ser instalado e configurado no servidor. Após iniciar o computador, uma interface gráfica deverá estar disponível localmente para o usuário.

Uma forma potencial de exploração do XDMCP é por meio de um ataque man-in-the-middle. Neste tipo de ataque, um invasor intercepta a comunicação entre o computador remoto e o servidor do X Window System e se faz passar por uma das partes para obter acesso não autorizado ao servidor. O invasor poderá então usar o servidor para executar comandos arbitrários, acessar dados confidenciais ou realizar outras ações que possam comprometer a segurança do sistema.

## VNC

Virtual Network Computing( VNC) é um sistema de compartilhamento remoto de área de trabalho baseado no protocolo RFB que permite aos usuários controlar um computador remotamente. Ele permite que um usuário visualize e interaja com um ambiente de desktop remotamente por meio de uma conexão de rede. O usuário pode controlar o computador remoto como se estivesse sentado na frente dele. Este também é um dos protocolos mais comuns para conexões gráficas remotas para hosts Linux.

O VNC é geralmente considerado seguro. Ele usa criptografia para garantir que os dados estejam seguros durante o trânsito e requer autenticação antes que um usuário possa obter acesso. Os administradores utilizam VNC para acessar computadores que não são fisicamente acessíveis. Isso pode ser usado para solucionar problemas e manter servidores, acessar aplicativos em outros computadores ou fornecer acesso remoto a estações de trabalho. O VNC também pode ser usado para compartilhamento de tela, permitindo que vários usuários colaborem em um projeto ou solucionem um problema.

Existem dois conceitos diferentes para servidores VNC. O servidor normal oferece a tela real do computador host para suporte ao usuário. Como o teclado e o mouse permanecem utilizáveis ​​no computador remoto, recomenda-se um arranjo. O segundo grupo de programas servidores permite o login do usuário em sessões virtuais, semelhante ao conceito de servidor de terminal.

Os programas de servidor e visualizador para VNC estão disponíveis para todos os sistemas operacionais comuns. Portanto, muitos serviços de TI são realizados com VNC. O TeamViewer proprietário e o RDP têm usos semelhantes.

Tradicionalmente, o servidor VNC escuta na porta TCP 5900. Portanto, ele oferece sua porta display 0lá. Outros monitores podem ser oferecidos através de portas adicionais, principalmente 590[x], onde xestá o número do monitor. A adição de múltiplas conexões seria atribuída a uma porta TCP superior, como 5901, 5902, 5903, etc.

Para essas conexões VNC, muitas ferramentas diferentes são usadas. Entre eles estão por exemplo:

 - TigerVNC
 - TightVNC
 - RealVNC
 - UltraVNC

As ferramentas mais utilizadas para esse tipo de conexão são UltraVNC e RealVNC por causa de sua criptografia e maior segurança.

Neste exemplo configuramos um servidor **TigerVNC**, e para isso precisamos, entre outras coisas, também do XFCE4gerenciador de desktop, pois as conexões VNC com GNOME são um tanto instáveis. Portanto precisamos instalar os pacotes necessários e criar uma senha para a conexão VNC.

### Instalação do TigerVNC

`$ sudo apt install  xfce4 xfce4-goodies tigervnc-standalone-server -y`

`$ vncpassword`

Durante a instalação,  uma pasta oculta é criada no diretório inicial chamada **.vnc**. Então, temos que criar dois arquivo adicionais, **xstartup** e **config**. **xstartup** determina como a sessão VNC é criada em conexão com o gerenciador de exibição e **config** de termina as suas configurações.

### Configuração

`$ touch ~/.vnc/xstartup ~/.vnc/config`

`$ cat <<EOT>> ~/.vnc/xstartup`

>#!/bin/bash \
>unset SESSION_MANAGER \
>unset DBUS_SESSION_BUS_ADDRESS \
>/usr/bin/startxfce4 \
>[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup \
>[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources \
>x-window-manager & \
>EOT \

`$ cat <<EOT>> >> ~/.vnc/config`

>geometry=1920x1080 \
>dpi=96 \
>EOT \

Alé disso, o executável **xstartup** precisa de diretirots para ser inciado pelo serviço.

`$ chmod +x ~/.vnc/xstartup`

### Inicie o servidor VNC

`$ vncserver`

Além disso, também podemos exibir sessões inteiras com as portas associadas e o ID do processo.

### Listar sessões

`$ vncserver -list`

### Configurando um túnel SSH

`$ ssh -L 5901:127.0.0.1:5901 -N -f -l htb-student 10.129.14.130`

Finalmente, podemos nos conectar ao servidor através do túnel SSH usando o arquivo xtightvncviewer.

### Se conectando ao servidor VNC

`$ xtightvncviewer localhost:5901`

