#Linux 
# Linux - Remoção de arquivos e diretórios

Para remover um arquivo ou diretório da área de trabalho GNOME, clique com o botão direito no item no aplicativo Files e selecione Move to Trash no menu de contexto.

![[Pasted image 20240614150339.png]]

Para confirmar que o arquivo foi movido para o Trash ou para recuperá-lo depois de movê-lo por engano para lá, clique no ícone Trash no painel esquerdo da janela Files.

O GNOME Desktop Manager (GDM) usa o diretório `Trash` para manter os diretórios ou arquivos excluídos caso você queira restaurá-los. O GDM cria o diretório `Trash` no diretório oculto `.local` do diretório pessoal do usuário. Na linha de comando, você pode explorar os arquivos enviados para o diretório `Trash` no caminho de arquivo `/home/student/.local/share/Trash/files`.

Para remover um arquivo ou um diretório na linha de comando, você pode usar o comando `rm` ou o comando `mv` para mover itens com segurança para o diretório `Trash`. Depois de remover um arquivo usando o comando `rm`, não há uma maneira fácil de recuperá-lo e nenhuma garantia de que o arquivo possa ser recuperado intacto, mesmo com o software de recuperação.

![[Pasted image 20240614150427.png]]

![[Pasted image 20240614150504.png]]

Um método mais seguro é criar um link para o diretório `Trash` usando o comando `ln`:

![[Pasted image 20240614150518.png]]

Em seguida, use o comando `mv` para mover o arquivo para o diretório `Trash`:

![[Pasted image 20240614150535.png]]

Esse diretório tem o mesmo local do diretório `Trash` que o da sua área de trabalho GNOME.

![[Pasted image 20240614150549.png]]

