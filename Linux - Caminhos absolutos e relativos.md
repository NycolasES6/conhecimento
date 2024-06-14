#Linux 
# Linux - Caminhos absolutos e relativos

Um _caminho absoluto_ é um caminho de arquivo que inicia no diretório root. O caminho absoluto é uma expressão explícita da localização precisa de um arquivo ou diretório. Cada arquivo no seu computador tem um caminho absoluto que começa com um caractere de barra (`/`). Por exemplo, o caminho absoluto para o diretório `Documents` em seu diretório pessoal é `/home/user/Documents`, não apenas `Documents`.

Um _caminho relativo_ é um caminho de arquivo que começa a partir do seu diretório de trabalho atual. Um caminho relativo nunca começa com um caractere de barra (`/`). Em vez disso, um caminho relativo começa com um ponto (`.`), dois pontos (`..`) ou o nome de um arquivo ou diretório.

Quando um caminho relativo começa com um nome (de um arquivo ou diretório) ou um ponto, o recurso está em seu diretório atual. Um nome ou um ponto são instruções para procurar o arquivo no diretório atual ou em um subdiretório. Por exemplo, um arquivo chamado `example.txt` no diretório `Documents` pode ser expresso como `./example.txt` ou apenas `example.txt` quando seu diretório de trabalho atual é `Documents`.

![[Pasted image 20240614142844.png]]

Dois pontos indicam um diretório pai. Dois pontos (`..`) são uma instrução para mover "para cima" na árvore de arquivos e procurar um arquivo ou diretório a partir desse local. Por exemplo, o caminho relativo do diretório `Downloads` para o arquivo `Documents/example.txt` é `../Documents/example.txt` porque você deve sair do diretório `Downloads` e entrar no diretório `Documents` para ficar no mesmo local que o arquivo `example.txt`.

Uma vantagem de conhecer o caminho de um arquivo é que você pode fazer referência a um arquivo ou diretório de qualquer lugar do sistema sem precisar estar no mesmo diretório. Por exemplo, para ver o conteúdo de um arquivo, você pode se referir a esse arquivo por seu caminho absoluto ou relativo completo, independentemente do seu diretório de trabalho atual.

![[Pasted image 20240614142913.png]]










