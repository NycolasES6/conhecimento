# Informacoes do sistema

Como trabalharemos com diversos sistemas Linux, precisamos aprender a estrutura e as informações sobre o sistema, seus processos, configurações de rede, usuários, diretórios, configurações de usuário e os parâmetros correspondentes. Aqui está uma lista das ferramentas necessárias que nos ajudarão a obter as informações acima. A maioria deles é instalada por padrão.

``whoami`` - Exibe o nome de usuário atual.

``id`` - Retorna a identidade dos usuários

``hostname`` - Define ou imprime o nome do sistema host atual.

``uname`` - Imprime informações básicas sobre o nome do sistema operacional e o hardware do sistema.

``pwd`` - Retorna o nome do diretório de trabalho.

``ifconfig`` - O utilitário ifconfig é usado para atribuir ou visualizar um endereço para uma interface de rede e/ou configurar parâmetros de interface de rede.

``ip`` - IP é um utilitário para mostrar ou manipular roteamento, dispositivos de rede, interfaces e túneis.

``netstat`` - Mostra o status da rede.

``ss`` - Outro utilitário para investigar soquetes.

``ps`` - Mostra o status do processo.

``who`` - Exibe quem está logado.

``env`` - Imprime o ambiente ou define e executa o comando.

``lsblk`` - Lista dispositivos de bloqueio.

``lsusb`` - Lista dispositivos USB

``lsof`` - Lista os arquivos abertos.

``lspci`` - Lista dispositivos PCI.

`uname -a` - Imprimirá todas as informações sobre a máquina em uma ordem específica: nome do kernel, nome do host, versão do kernel, versão do kernel, nome do hardware da máquina e sistema operacional. O -asinalizador omitirá -p(tipo de processador) e -i(plataforma de hardware) se forem desconhecidos.

`uname -r` - Imprimi a versão do kernel

## Fazendo login via SSH

Secure Shell( SSH) refere-se a um protocolo que permite aos clientes acessar e executar comandos ou ações em computadores remotos. Em hosts e servidores baseados em Linux ou outro sistema operacional semelhante ao Unix, o SSH é uma das ferramentas padrão instaladas permanentemente e é a escolha preferida de muitos administradores para configurar e manter um computador por meio de acesso remoto. É um protocolo mais antigo e muito comprovado que não requer nem oferece uma interface gráfica de usuário (GUI). Por isso funciona de forma muito eficiente e ocupa poucos recursos. Utilizamos este tipo de conexão nas seções seguintes e na maioria dos outros módulos para oferecer a possibilidade de experimentar os comandos e ações aprendidos em um ambiente seguro. Podemos nos conectar aos nossos alvos com o seguinte comando:

`NycolasES6@htb[/htb]$ ssh [username]@[IP address]`
