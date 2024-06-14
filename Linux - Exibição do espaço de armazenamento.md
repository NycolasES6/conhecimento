#Linux
# Linux - Exibição do espaço de armazenamento

Para ver a quantidade de espaço de armazenamento disponível no seu sistema Linux, você pode usar o aplicativo Disk Usage Analyzer na área de trabalho GNOME. Abra o aplicativo Disk Usage Analyzer na Activities Overview.

O Disk Usage Analyzer exibe cada dispositivo de armazenamento anexado ao seu computador e ao seu diretório pessoal. Nos computadores de laboratório usados neste curso, os dispositivos incluem um disco rígido e uma unidade ótica. O espaço disponível da unidade de disco é exibido no lado direito da janela.

![[Pasted image 20240614155052.png]]

O sistema operacional usa espaço em disco para o kernel, pacotes e outros arquivos. O espaço em disco usado pelo sistema operacional é incluído nas métricas para o dispositivo de disco primário. Você pode ver o espaço em disco usado por seus arquivos clicando em Home Folder.

Ao exibir os detalhes de um diretório ou dispositivo, o Disk Usage Analyzer lista os diretórios que usam a maior quantidade de espaço em ordem decrescente. No painel direito, o Disk Usage Analyzer mostra um mapa interativo do uso do disco. O anel mais interno do gráfico representa diretórios em seu diretório pessoal, com subdiretórios nos anéis externos. O tamanho dos segmentos em cada anel corresponde ao tamanho relativo do diretório.

Você pode clicar em qualquer segmento de qualquer anel para entrar nesse diretório e ver um gráfico de seu conteúdo. Clique com o botão direito em um segmento e clique em Open Folder para abrir o local no aplicativo Files. Também é possível clicar em Move to Trash para remover o diretório do sistema.

![[Pasted image 20240614155153.png]]

Para ver o espaço em disco disponível usando a linha de comando, use o comando `df` com a opção `-h` para tornar a saída legível.

![[Pasted image 20240614155211.png]]

Para obter um relatório detalhado sobre quais arquivos estão usando espaço na sua unidade, use o comando `du` com a opção `-h`.

![[Pasted image 20240614155225.png]]


