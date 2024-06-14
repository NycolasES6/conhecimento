#Linux 
# Linux - Configuração do FlatPak

O comando `dnf` requer privilégios administrativos. Como administrador, você pode permitir que os usuários instalem aplicativos sem conceder a eles acesso a privilégios sudo. Como alternativa, você pode ser um usuário em um computador gerenciado por um departamento de TI corporativo e pode não ter permissão para instalar software de fora dos repositórios aprovados. O sistema Flatpak usa contêineres do Linux para instalar aplicativos de área de trabalho com segurança, sem conceder permissões administrativas aos usuários.

Alguns aplicativos estão disponíveis por meio do comando `dnf` e como Flatpak, mas somente Flatpaks estão disponíveis sem o uso de privilégios sudo. O maior repositório de Flatpaks é o Flathub, um projeto open source que serve como um local centralizado para softwares de muitos desenvolvedores diferentes.

Para configurar o sistema Flatpak, abra um navegador, navegue até `https://flathub.org` e clique em Set Up Flathub. Percorra a lista de distribuições, selecione o nome da sua distribuição do Linux e siga as instruções de instalação. Este curso usa o Red Hat Enterprise Linux.

No RHEL, o Flatpak está disponível por DNF e pode já estar instalado. Para instalar o Flatpak, use o comando `dnf install flatpak` com privilégios sudo.

![[Pasted image 20240614183350.png]]

O Flatpak usa repositórios para pesquisar e instalar pacotes. Muitas organizações publicam um repositório Flatpak para distribuir seu software. Para adicionar um repositório Flatpak ao sistema, use o comando `flatpak remote-add`. Se o repositório já existir e você tentar adicioná-lo, o comando falhará. Você pode usar o comando `flatpak remote-add` com a opção `--if-not-exists` para evitar a falha do comando se o repositório já existir.

Neste exemplo, você adiciona o repositório Flathub usando a URL `https://dl.flathub.org/repo/flathub.flatpakrepo`.

![[Pasted image 20240614183417.png]]

Verifique se o repositório Flathub está disponível no sistema local usando o comando `flatpak remotes` para listar os repositórios Flatpak.

![[Pasted image 20240614183429.png]]

Para verificar se os comandos de configuração foram bem-sucedidos e se você adicionou o Flathub como um repositório de software, abra o aplicativo GNOME Software. Clique no menu do aplicativo no canto superior direito e selecione Software Repositories. A caixa de diálogo Software Repositories lista o Flathub como um repositório disponível.

![[Pasted image 20240614183437.png]]

Alguns repositórios Flatpak usam uma string adicional no início da URL para se referir a um registro da Open Container Initiative (OCI). Por exemplo, a URL do repositório Fedora Flatpak é `oci+` `https://registry.fedoraproject.org`, que você pode usar como uma URL normal.

![[Pasted image 20240614183458.png]]

