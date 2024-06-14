#Linux 
# Linux - Modificação das permissões de arquivos

No aplicativo Files, visualize as propriedades do arquivo e clique em Permissions. Você pode selecionar a permissão desejada na lista suspensa Access para cada conjunto de usuário.

![[Pasted image 20240614172427.png]]

Na linha de comando, use o comando `chmod` para modificar as permissões do arquivo. O comando `chmod` requer dois argumentos: a definição de nova permissão e o arquivo de destino ou diretório. Semelhante ao comando `chown`, você pode usar a opção `-R` com o comando `chmod` para modificar permissões recursivamente.

No exemplo a seguir, você define permissões para o arquivo `homework.doc`. Você define permissões de leitura e gravação para conjuntos de usuários, e permissões de leitura para os conjuntos de grupo e outros. Esse comando substitui todas as permissões anteriores no arquivo.

![[Pasted image 20240614172443.png]]

No exemplo a seguir, você revisa as permissões de arquivo do script `daily-tasks.sh` e tenta executar o script. Você executa um script do shell fornecendo o caminho do script. Se o script estiver no diretório atual, você poderá usar um ponto seguido por uma barra (`./`) para se referir ao diretório atual. O script `daily-tasks.sh` não tem permissões de execução, por isso, a execução falhou.

![[Pasted image 20240614172455.png]]

Em seguida, você define permissões de execução para o script de shell `daily-tasks.sh`. As permissões `0750` concedem todas as permissões de leitura, gravação e execução ao usuário `aquincy`. Essas permissões também definem permissões de leitura e execução para o grupo `finance`. Nenhuma permissão está definida para o conjunto outros.

![[Pasted image 20240614172510.png]]

Se o script estiver em um diretório diferente, você fornecerá o caminho completo do script para executá-lo. Por exemplo, o comando a seguir executa o script `/usr/local/bin/mytasks.sh`.

![[Pasted image 20240614172529.png]]







