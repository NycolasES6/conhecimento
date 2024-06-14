#Linux
# Linux - Instalação de pacotes de software

O aplicativo de área de trabalho GNOME Software é um front-end para o sistema de gerenciamento de pacotes DNF (antigo YUM). Na linha de comando, o sistema DNF monitora quais softwares estão disponíveis nos repositórios configurados, quais estão instalados no seu sistema e quais atualizações estão disponíveis. Você pode pesquisar aplicativos e comandos da área de trabalho e depois instalá-los e atualizá-los usando o comando `dnf`.

## Listagem de repositórios

A disponibilidade de aplicativos de software é determinada pelos repositórios que estão configurados em seu sistema. Em computadores gerenciados por um departamento de TI corporativo, os repositórios geralmente são configurados para você. Para ver os repositórios configurados no seu sistema, use o comando `dnf repolist`.

![[Pasted image 20240614182924.png]]

## Localização de aplicativos de área de trabalho com Flatpak

O aplicativo GNOME Software facilita a navegação por aplicativos Flatpak criados para a área de trabalho. Explore os aplicativos por categoria ou use a função de pesquisa para localizar aplicativos por nome ou descrição.

## Instalação de aplicativos de área de trabalho com Flatpak

Antes de instalar um aplicativo Flatpak, clique no nome do aplicativo GNOME Software. Leia a descrição do aplicativo com atenção. A descrição de cada aplicativo explica o tamanho da instalação, se o aplicativo tem acesso aos seus dados pessoais ou à rede, qual organização oferece suporte a ele e muito mais. O repositório de origem que fornece o aplicativo é listado no canto superior direito do GNOME Software.

![[Pasted image 20240614183526.png]]

Para instalar um aplicativo como Flatpak, clique em Install.

Depois de concluir a instalação, clique em Open para iniciá-lo. Como alternativa, você pode iniciar o aplicativo em Activities Overview.

