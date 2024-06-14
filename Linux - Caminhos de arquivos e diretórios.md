#Linux 
# Linux - Caminhos de arquivos e diretórios

Você pode expressar o local de qualquer arquivo ou diretório em seu computador usando o design hierárquico de diretórios no Linux. Tudo existe no diretório root, portanto, ao começar com uma única barra, você pode definir todos os passos até o local de um arquivo listando cada diretório pai, separado por uma barra.

Por exemplo, o diretório pessoal `user` neste curso tem o caminho `/home/user` porque o diretório `user` está localizado dentro do diretório `home`, que está localizado dentro do diretório root `/`. Se você fizer download de um arquivo chamado `file.txt` da Internet e seu navegador salvá-lo no disco rígido, o local padrão será `/home/user/Downloads/file.txt`.

Na área de trabalho, você pode ver seu diretório atual na barra superior da janela do aplicativo GNOME Files.

![[Pasted image 20240614142610.png]]

Em um terminal, você pode ver seu diretório de trabalho atual usando o comando `pwd`:

![[Pasted image 20240614142630.png]]

Você pode ver o caminho completo de um arquivo usando o comando `realpath`, seguido do arquivo ao qual deseja que o caminho leve:

![[Pasted image 20240614142646.png]]




















