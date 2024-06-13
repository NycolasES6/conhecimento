#Linux 
# Exibição de arquivos de texto

Você pode ver o conteúdo dos arquivos de texto abrindo o arquivo com um editor de texto. Você também pode ver o conteúdo de um arquivo de texto na linha de comando usando utilitários de texto de linha de comando, como o comando `cat`. O exemplo a seguir mostra o conteúdo do arquivo de texto `dictionary`.

![[Pasted image 20240612170047.png]]

Para ver o conteúdo de vários arquivos, adicione os nomes dos arquivos ao comando `cat` como argumentos.

![[Pasted image 20240612170102.png]]

O comando `cat` mostra todo o conteúdo do arquivo, mesmo para arquivos com milhares de linhas de texto. Para ver esses arquivos grandes, use o comando `less`. Diferentemente do comando `cat`, o comando `less` pagina a saída para que ela se adapte ao tamanho da sua janela de terminal.

A paginação é interrompida no final das linhas exibidas na janela, e você deve fornecer informações para continuar nas próximas linhas. O comando `less` também fornece opções para navegação de arquivos para frente e para trás. Você pode pular diretamente para qualquer linha usando um código de linha ou pesquisar uma palavra ou pressionamentos de teclas no início ou no final de um arquivo.

![[Pasted image 20240612170145.png]]

Use as teclas de **UpArrow** e **DownArrow** para rolar para cima e para baixo. Pressione **h** para a página de ajuda e **q** para sair do comando.

Você pode usar o comando `head` para ver as primeiras linhas de um arquivo. O comando `head` exibe as primeiras 10 linhas do arquivo por padrão, mas você pode usar a opção `-n` para especificar um número diferente de linhas. O comando `tail` exibe as últimas linhas de um arquivo especificado, da mesma forma que o comando `head` retorna as primeiras linhas.

![[Pasted image 20240612170217.png]]

Em alguns cenários, talvez você queira saber quantas linhas ou palavras existem em um arquivo de texto. Você pode usar o comando `wc` para ver o número de linhas, palavras e caracteres em um arquivo. Use as opções `-l`, `-w` ou `-c` para exibir apenas as linhas, as palavras ou os caracteres determinados.

![[Pasted image 20240612170246.png]]






