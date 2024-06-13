#Linux 
# Identificação de arquivos

Em alguns sistemas operacionais, é obrigatório que os arquivos tenham uma extensão, como a extensão `.txt` para um arquivo de texto simples ou a extensão `.exe` para um programa executável. No entanto, o Linux não depende de extensões de arquivo para reconhecer e interagir com arquivos. Em vez disso, os programas leem o _cabeçalho_ do arquivo.

O cabeçalho de um arquivo é um número não específico de linhas na parte superior de um arquivo que atua como um código. Esse código é conhecido como o _número mágico_ de um arquivo. Esse código é comparado internamente a um banco de dados de _padrões mágicos_ para ajudar a determinar o tipo de arquivo. Você pode usar o comando `file` para realizar os testes mágicos necessários e detectar os tipos e formatos de arquivos.

Por exemplo, usar o comando `file` em um arquivo de programa binário, como o arquivo do comando `cat`, retorna `ELF 64-bit LSB shared object` como a descrição. Um arquivo no Executable and Linkable Format (ELF) é um programa binário compilado. O restante da descrição mostra detalhes técnicos sobre como o arquivo foi compilado.

![[Pasted image 20240612165818.png]]

Os arquivos de texto não têm números mágicos, por isso não correspondem às entradas no banco de dados mágico. Nesse caso, o Linux realiza uma série de testes para verificar se o arquivo de texto está em conformidade com algum dos padrões de codificação de caracteres. Se o arquivo de texto estiver em conformidade com um conjunto de caracteres codificados, como ASCII ou UTF-8, o comando `file` imprime o conjunto de caracteres. Os arquivos que não podem ser identificados como um formato binário conhecido ou como um arquivo de texto válido são mostrados como arquivos de dados.

Os exemplos a seguir mostram a saída do comando `file` quando ele é usado com diferentes tipos de arquivos.

![[Pasted image 20240612165913.png]]











