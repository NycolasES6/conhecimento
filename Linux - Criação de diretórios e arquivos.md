#Linux 
# Linux - Criação de diretórios e arquivos

## Diretórios

Para criar um diretório na área de trabalho GNOME, abra o aplicativo Files. Clique com o botão direito no fundo da janela e selecione New Folder no menu de contexto. Na caixa de diálogo New Folder que é aberta, digite um nome para o diretório e clique em Create.

![[Pasted image 20240614144248.png]]

Para criar um diretório na linha de comando, use o comando `mkdir` com um nome para o novo diretório.

![[Pasted image 20240614144314.png]]

O terminal interpreta um espaço como o delimitador para um novo argumento ou comando, por isso você deve colocar o nome do diretório entre aspas se quiser incluir espaços.

![[Pasted image 20240614144350.png]]

O comando `mkdir` pode criar vários diretórios com uma linha de comando. Você também pode criar diretórios dentro de outros diretórios.

![[Pasted image 20240614144433.png]]

Crie um diretório com um subdiretório ao mesmo tempo usando o comando `mkdir` com a opção `-p`. No exemplo a seguir, você cria o diretório `July` e o diretório pai `Monthly Reports` no diretório pessoal.

![[Pasted image 20240614144558.png]]

## Arquivos

Para criar um arquivo em um ambiente de área de trabalho, use um aplicativo, como o gedit. Depois de salvar um arquivo no qual você está trabalhando, o aplicativo cria o arquivo. No entanto, na linha de comando, você pode criar um arquivo vazio com o comando `touch`, seguido do caminho do arquivo que pretende criar.

![[Pasted image 20240614144705.png]]

Você também pode criar um arquivo usando o redirecionamento de shell. Ao redirecionar a saída padrão para um arquivo, o shell cria o arquivo se ele ainda não existir.

![[Pasted image 20240614144722.png]]













