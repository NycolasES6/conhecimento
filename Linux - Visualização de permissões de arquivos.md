#Linux
# Linux - Visualização de permissões de arquivos

Para visualizar as permissões de um arquivo ou diretório no aplicativo Files, clique com o botão direito do mouse no destino e selecione Properties > Permissions. A lista suspensa Access exibe as permissões definidas no arquivo. A caixa de seleção Execute indica se o arquivo tem permissões de execução.

No exemplo a seguir, o arquivo `Report.docx` tem permissões de leitura e gravação para o usuário, leitura e gravação para o grupo e somente leitura para os outros. A caixa de seleção Execute não está marcada, desse modo, o arquivo não tem permissões de execução.

![[Pasted image 20240614172141.png]]

Na linha de comando, você visualiza a permissão do arquivo usando o comando `ls` com a opção `-l`. A primeira coluna da saída contém três atributos do arquivo: o tipo de arquivo, as permissões do arquivo e os atributos estendidos. O primeiro caractere da string representa o tipo de arquivo, os próximos nove caracteres representam as permissões do arquivo e o último caractere representa os atributos estendidos.

No exemplo a seguir, você examina a propriedade e as permissões do arquivo `Report.docx`. O arquivo `Report.docx` é um arquivo normal, o que é indicado pelo hífen à esquerda, na primeira coluna. O usuário `eprice` tem permissões de leitura, gravação e execução (`rwx`). Membros do grupo `finance` têm permissões de leitura e gravação (`rw-`). Todos os outros usuários têm permissões de leitura (`r--`).

![[Pasted image 20240614172158.png]]

Mesmo que um arquivo tenha permissões de leitura para todos os usuários, você deve ter permissão para visualizar todos os diretórios no caminho do arquivo. Se você não tiver permissão para visualizar um diretório no caminho, não poderá visualizar o arquivo.

















