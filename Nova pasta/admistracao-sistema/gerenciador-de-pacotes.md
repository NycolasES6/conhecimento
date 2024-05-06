# Gerenciador de pacotes

Seja trabalhndo como admnistrador do sistema, mantendo nossas próprias máquinas em casa ou construind/atualizando/mantendo nossa distribuição de teste de penetração preferida, é crucial ter um conhecimento firme dos, gerenciadores de pacotes Linux disponíveis e das várias maneiras de utlizálos para instalar, atualizar ou remover pacotes. Pacotes são arquivos que contêm bnários de software, arquivos de configuração, informações sobre dependências e acompanham atualizações e upgrades. Os recursos que a maioria dos sistemas de gerenciamento de pacotes oferecem são :

 - Download de pacote.
 - Resolução de dependência.
 - Um formato de pacote binário padrão.
 - Locais comuns de instalação e configuração.
 - Configuração e funcionalidade adicionais relacionadas ao sistema.
 - Controle de qualidade.

Podemos usar muitos sistemas de gerenciamento de pacotes diferentes que cobrem diferentes de arquivos como ".deb", ".rpm" e outros. O requisito de gerenciamento de pacotes é que o software a ser instalado esteja disponível como um pacote correspondente. Normalmente, isso é criado, oferecido e mantido centralmente nas distribuições linux. Desta forma, o software é integrado diretamente no sistema, e seus diversos diretórios são distribuídos por todo o sistema. O siftware de gerenciamento de pacotes recupera as alterações necessárias para a instalação do sistema do próprio pacote e, em seguida, implementa essas alterações para instalar o pacote com êxito. Se o software de gerenciamento de pacotes reconhecer que pacotes adicionais são necessários para o funcionamento adequado do pacote que ainda  não foi instalado, uma dependência será incluída e avisará o administrador ou tentará recarregar o software ausente de um repositório, por exemplo, e instalar isso com antecedência.

Se um software instalado tiver sido excluído, o sistema de gerenciamento de pacotes retoma as informações do pacote, modifica-as com base em sua configuração e exclui os arquivos. Existem diferentes programas de gerenciamento de pacotes que podemos usar para isso. Aqui está uma lista de exemplos de tais programas:

 - `dpkg` - O dpkg é uma ferramenta para instalar, construir, remover e gerenciar pacotes Debian. O front-end principal e mais fácil de usar é o dpkg aptitude.
 - `apt` - Apt fornece uma interface de linha de comando de alto nível para o sistema de gerenciamento de pacotes.
 - `snap` - Instale, configure, atualize e remova pacotes snap. Os Snaps permitem a distribuilçao segura dos aplicativos e utilitário mais recentes para a nuvem, servidores, desktops e IoT.
 - `gem` - Gem é o front-end do RubyGems, o gerenciador de pacotes padrão do Ruby.
 - `pip` - Pip é um instalador de pacotes Python recomendado para instalar pacotes Python que não estão disponíveis no arquivo Debian. Ele pode funcionar com repositórios de controle de versão (atualmente apenas repositórios Git, Mercurial e Bazaar), registra extensivamente a saída e evita instalações parciais baixando todos os requisitos antes de iniciar a instalação.
 - `git` - Git é um sistema de controle de revisão distribuído, rápido e escalável, com um conjunto de comandos excepcionailmente rico que fornece operações de alto nível e acesso total aos componentes internos.

É altamente recomendável configurar nossa máquina virtual (VM) localmente para experimentá-la. Vamos experimentar um pouco em nossa VM local e estendê-la com alguns pacotes adicionais. Primeiro, vamos instalar **git** usando **apt**.

## Gerenciador de pacotes Aançado(APT)

Distribuições Linux baseadas em debian usam o gerenciador de pacotes APT. Um pacote é um arquivo contendo vários arquivos ".deb". O utilitário dpkg é utilizado para instalar programas do arquivo .deb associado. APT facilita a atualização e a instalação de programas porque muitos programas têm dependências. Ao instalar um programa a partir de um arquivo".deb" independente, podemos encontrar problemas de dependências e precisar baixar um ou vários pacotes adicionais. APT torna isoo mais fácil e eficiente ao agrupar todas as dependências necessárias para instalar um programa.

Cada distribuição Linux usa repositórios de software que são atualizados com frequência. Quando atualizamos um programa ou instalamos um novo, o sistema consukta esses repositórios em busca do pacote desejado. Os repositórios podem ser rotulados como estáveis. A maioria das distribuições Linux utiliza o repositório mais estável ou "principal". Isso pode ser verificado visualizando o conteúdo do `etc/apt/sources.list` arquivo. A listade repositórios do Parrot OS est´em `/etc/apt/sources.list.d/parrot.list` .

`cat /etc/apt/sources.list.d/parrot.list`

O APT usa um banco de dados chamado cache do APT. Isto é usado para fornecer informações sobre o pacotes instalados no nosso sistema offiline. Podemos pesquisar no cache do APT, por exemplo, para encontra todos os pacotes Impacket relacionados.

`apt-cache searche impacket`

Podemos então visualizar informações adicionais sobre um pacote.

`apt-cache show impacket-scripts`

Também podemos listar todos os pacotes instalados.

`apt list --installed`

Se estiver faltando algum pacote, podemos procurá-lo e instalá-lo usando o seguinte comando.

`sudo apt install impacket-scripts -y`

## GIT

Agora que instalamos git, podemos usá-lo para baixar ferramentas úteis do Github. Um desses projetos é denominado 'Nishang'. Trataremos e trabalharemos com o projeto em si mais tarde. Primeiro, precisamos navegar até o repositório do projeto e copiar o link do Github antes de usar o git para baixá-lo.

Porém, antes de baixarmos o projeto e seus scripts e listas, devemos criar uma pasta específica.

`mkdir ~/nishang/ && git clone https://github.com/samratashok/nishang.git ~/nishang`

## DPKG

Também podemos baixar os programas e ferramentas dos repositórios separadamente. Neste exemplo, baixamos ‘strace’ para Ubuntu 18.04 LTS.

`wget http://archive.ubuntu.com/ubuntu/pool/main/s/strace/strace_4.21-1ubuntu1_amd64.deb`

Além disso, agora podemos usar ambos apte dpkgpara instalar o pacote. Como já trabalhamos com apt, passaremos dpkgao próximo exemplo.

`sudo dpkg -i strace_4.21-1ubuntu1_amd64.deb`

Com isso, já instalamos a ferramenta e podemos testar se ela funciona corretamente.

`strace -h`







