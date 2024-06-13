#Linux 
# Uso da entrada padrão para comandos

Ao inserir um comando na linha de comando, você instrui o shell sobre qual programa iniciar. O _interpretador de comandos_ recebe entradas interativas do usuário e inicia o programa. Às vezes, um comando usa um argumento que indica um objeto a ser manipulado, como um arquivo que você deseja referenciar ou alterar. Por exemplo, ao usar o comando `cat`, você pode especificar um arquivo como um argumento:

![[Pasted image 20240612162112.png]]

Você também pode fornecer opções de comando para ajustar o comportamento de um programa. Por exemplo, quando você usa a opção `--number` com o comando `cat`, o comando `cat` adiciona um número de linha a cada linha do arquivo que você está visualizando:

![[Pasted image 20240612162136.png]]

Alguns comandos entram em um modo interativo quando são fornecidos sem argumentos. No modo interativo, um comando é executado e aguarda os dados na entrada padrão. Por exemplo, o comando `cat` normalmente exibe o conteúdo de um arquivo de texto. No entanto, quando você não fornece o comando com um arquivo, o comando `cat` exibe o texto da entrada padrão.

![[Pasted image 20240612162213.png]]

Sem entrada padrão, o comando `cat` é executado, mas parece não fazer nada.



