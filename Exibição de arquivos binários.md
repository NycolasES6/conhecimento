#linux
# Exibição de arquivos binários

Você não pode ver ou editar diretamente arquivos binários usando ferramentas de texto, como os comandos `cat` ou `less`. Tentar usar ferramentas de texto em um arquivo binário pode exibir o conteúdo binário do arquivo, o que raramente é útil. Os arquivos binários são lidos e modificados somente por seus programas compatíveis.

Se você abrir um arquivo binário com um visualizador de texto, poderá fazer com que a janela de terminal pare de funcionar. Nessa situação, um terminal pode parar de exibir os caracteres que você digita. O comando `stty` pode ver e modificar as configurações do terminal e pode resolver esse problema. Você pode usar o comando `stty` com o argumento `sane` para redefinir os atributos do terminal para os valores de trabalho padrão.

Para restaurar a funcionalidade do terminal, primeiro saia da ferramenta de texto que causou o mau funcionamento do terminal. Se a ferramenta usar paginação, pressione **q** para sair da ferramenta; caso contrário, pressione **Ctrl**+**C** para interromper e forçar o encerramento da ferramenta. Em seguida, pressione **Enter** para solicitar um novo prompt de comando. Ignore qualquer saída de erro exibida. Se o terminal imprimir outro prompt de comando, seu terminal será funcional.

Se o terminal continuar inoperante, digite o comando `stty sane`. Se o terminal ainda não imprimir outro prompt de comando, feche a guia ou janela do terminal com defeito e inicie outro terminal.

![[Pasted image 20240612170738.png]]

|   |   |
|---|---|
|[![1](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/1.svg)](https://rha.ole.redhat.com/rha/app/#_exibi%C3%A7%C3%A3o_de_arquivos_bin%C3%A1rios-CO3-1)|Se o terminal parar de funcionar, você não poderá mais ver o que digita. Tente **q** ou **Ctrl**+**C**.|
|[![2](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/2.svg)](https://rha.ole.redhat.com/rha/app/#_exibi%C3%A7%C3%A3o_de_arquivos_bin%C3%A1rios-CO3-2)|Pressione **Enter** e digite `stty sane`. Os caracteres que você digita podem não ecoar no terminal.|
|[![3](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/3.svg)](https://rha.ole.redhat.com/rha/app/#_exibi%C3%A7%C3%A3o_de_arquivos_bin%C3%A1rios-CO3-3)|Seu prompt de comando deve retornar. Caso contrário, feche a janela e abra outra.|








