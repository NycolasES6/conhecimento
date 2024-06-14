#Linux 
# Linux- Permissões de arquivos

### Permissões de arquivos

As permissões de arquivo são uma parte importante do modelo de segurança do Linux. A propriedade e as permissões de arquivo gerenciam o acesso do usuário aos recursos do arquivo. As permissões de arquivo definidas em um arquivo ou diretório determinam quem pode acessá-lo e como esse usuário pode interagir com o arquivo.

#### Interpretação das permissões de arquivos

No Linux, três tipos de permissões de arquivo determinam o acesso para três conjuntos de usuários: usuário, grupo e outros.

O conjunto _usuário_, também conhecido como _proprietário_, refere-se a apenas um usuário: o usuário que é proprietário do arquivo. Por padrão, esse usuário é o usuário que cria o arquivo. O conjunto _grupo_ refere-se a todos os usuários que são membros do grupo proprietário do arquivo. Por padrão, esse grupo geralmente é o grupo primário do usuário que cria o arquivo. O conjunto _outros_ refere-se a qualquer usuário que não seja membro do grupo nem seja o usuário proprietário do arquivo.

Cada conjunto de usuários pode ter permissões para ler, gravar ou executar um arquivo ou diretório. Essas permissões são representadas por letras ou valores octais.

leitura (`r`)

A permissão de _leitura_ é a permissão mais básica em um arquivo. A permissão de leitura permite que o conjunto de usuário visualize o arquivo, mas não modifique seu conteúdo. Em um diretório, a permissão de leitura permite que o usuário liste o conteúdo desse diretório.

gravação (`w`)

A permissão de _gravação_ permite a um conjunto de usuário modificar o conteúdo do arquivo. Em um diretório, a permissão de gravação permite que o conjunto de usuário crie arquivos dentro desse diretório. A permissão de leitura está implícita na permissão de gravação.

execução (`x`)

A permissão de _execução_ permite a um conjunto de usuário executar o arquivo. _Executar_ ou _rodar_ um arquivo significa que o sistema executa uma lista de tarefas codificadas no arquivo executado. No Linux, você normalmente executa _scripts de shell_. Esses scripts de shell são arquivos de texto simples que contêm uma lista de comandos. Em um diretório, a permissão de execução permite que o usuário navegue até o diretório. A permissão de leitura está implícita na permissão de execução. A permissão de gravação não está implícita na permissão de execução.

Um conjunto de permissões é uma string de nove caracteres. Por exemplo, a string `rwxrw-r--` representa as permissões de um arquivo. Para interpretar as permissões, divida a string em três conjuntos de três caracteres cada. O primeiro conjunto corresponde a permissões de usuário, o segundo conjunto corresponde a permissões de grupo e o terceiro conjunto corresponde a permissões para outros.

![[Pasted image 20240614171935.png]]

|   |   |
|---|---|
|[![1](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/1.svg)](https://rha.ole.redhat.com/rha/app/#_interpreta%C3%A7%C3%A3o_das_permiss%C3%B5es_de_arquivos-CO5-1)|A string `rwx` representa as três permissões: leitura, gravação e execução.|
|[![2](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/2.svg)](https://rha.ole.redhat.com/rha/app/#_interpreta%C3%A7%C3%A3o_das_permiss%C3%B5es_de_arquivos-CO5-2)|A string `rw-` representa as permissões de leitura e gravação. O hífen (`-`) representa a ausência da permissão de execução.|
|[![3](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/3.svg)](https://rha.ole.redhat.com/rha/app/#_interpreta%C3%A7%C3%A3o_das_permiss%C3%B5es_de_arquivos-CO5-3)|A string `r--` representa as permissões somente leitura.|

As permissões de arquivo também podem ser representadas por números octais, que é um sistema numérico que usa um intervalo de oito dígitos (0 a 7). Um conjunto completo de permissões octais é representado por quatro números. O primeiro número representa permissões especiais. Um zero à esquerda em números octais representa que não há permissões especiais. Os próximos três números são os números de permissão para cada conjunto de usuários. A permissão de leitura é representada pelo número quatro, a de gravação é representada por um dois e a de execução é representada por um.

No exemplo anterior, a string `rwxrw-r--` é representada como `0761` em números octais:

- O primeiro número (`0`) representa que não há permissões especiais.
    
- O segundo número (`7`) representa o proprietário de usuário e é equivalente à string `rwx`. O número `7` resulta da adição das permissões de leitura (`4` em valor octal), gravação (`2` em valor octal) e execução (`1` em valor octal).
    
- O terceiro número (`6`) representa o usuário proprietário e é equivalente à string `rw-`. O número `6` resulta da adição das permissões de leitura (`4` em valor octal) e gravação (`2` em valor octal).
    
- O quarto número (`1`) representa o conjunto outros e é equivalente à string `r--`. O número `1` representa a permissão de execução em valor octal.
    

A permissão de arquivo padrão definida para um novo diretório é `rwxrwxr-x`, que pode ser representada como o número octal `0775`.
