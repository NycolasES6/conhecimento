#Linux 
# Linux - Criação de atalhos para arquivos e diretórios

Você pode armazenar um arquivo ou diretório em dois locais diferentes ao mesmo tempo criando um _link_. Por padrão, os links estão desabilitados no aplicativo GNOME Files. Para habilitar os links, clique no menu principal no canto superior direito da janela Files e clique em Preferences. Na janela Preferences, defina Create Link como on.

![[Pasted image 20240614150210.png]]

Na janela Files, clique com o botão direito em um diretório e selecione Create Link. Um link, ou um atalho, para o diretório selecionado é exibido na mesma janela.

![[Pasted image 20240614150225.png]]

Você pode criar atalhos para arquivos da mesma maneira. Ao abrir um atalho para um arquivo, você abre o arquivo vinculado.

Para criar um link para um arquivo ou diretório na linha de comando, use o comando `ln` com a opção `--symbolic`. O comando exige um item que exista, seguido pelo atalho que você pretende criar.

![[Pasted image 20240614150239.png]]

Semelhante a um ponteiro na programação, um link é um recurso que ajuda você a acessar rapidamente um arquivo ou diretório. Usar links pode ser útil para acessar diretórios com caminhos longos ou itens com nomes longos ou complicados.

Você pode confirmar se um arquivo é um link usando o comando `file` ou `tree`.

![[Pasted image 20240614150258.png]]




