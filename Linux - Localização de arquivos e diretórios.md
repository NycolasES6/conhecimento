#Linux 
# Linux - Localização de arquivos e diretórios

Se você não tiver certeza de onde um arquivo está localizado, poderá procurá-lo usando a área de trabalho GNOME ou a linha de comando. Para pesquisar um arquivo ou diretório, abra o aplicativo Files e clique no ícone de Magnifying Glass na barra de ferramentas superior. Digite o nome do arquivo, ou parte dele, no campo de texto e confira os resultados na janela Files.

![[Pasted image 20240614150655.png]]

Na linha de comando, você pode encontrar um arquivo usando o comando `find`. Para encontrar um arquivo pelo nome (ignorando o uso de maiúsculas e minúsculas), use o comando `find`, seguido do caminho que deseja pesquisar e, em seguida, a opção `-iname` juntamente com o nome do arquivo.

![[Pasted image 20240614150727.png]]

Os usuários do Linux normalmente usam o comando `find` com redirecionamento. Essa técnica é útil porque o comando `find` pode produzir uma grande quantidade de saída, mas não separa os resultados esperados dos erros. Usando o redirecionamento, você pode enviar a saída padrão e o erro padrão para arquivos separados. Dessa forma, você pode se concentrar na análise de resultados ou erros ao ver os arquivos resultantes.

![[Pasted image 20240614150747.png]]









