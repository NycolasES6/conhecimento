# Arquivo e diretorios

A principal diferença entre trabalhar com arquivos no Linux e no Windows é a forma como podemos acessar os arquivos. Por exemplo, normalmente temos que abrir o Explorer para localizar e editar arquivos no Windows. Já no Linux, temos um terminal onde podemos acessar e editar arquivos por meio de comandos. Além disso, podemos até editar os arquivos de forma interativa sem usar um editor, como ``vim`` ou ``nano``.`

O terminal no Linux é uma ferramenta mais eficiente e rápida porque você pode acessar os arquivos diretamente com alguns comandos e editá-los e modificá-los seletivamente com expressões regulares ( ``regex``). Você também pode executar vários comandos simultaneamente e redirecionar a saída para um arquivo. Isso economiza tempo e é muito útil quando queremos editar muitos arquivos de uma vez.

## Criar, mover e copiar

A seguir, vamos trabalhar com arquivos e diretórios e aprender como criar, renomear, mover, copiar e excluir. Primeiro, vamos criar um arquivo vazio e um diretório. Podemos usar ``touch`` para criar um arquivo vazio e ``mkdir`` para criar um diretório.

### Sintaxe - touch

``NycolasES6@htb[/htb]$ touch <name>``

### Sintaxe - mkdir

``NycolasES6@htb[/htb]$ mkdir <name>``

Neste exemplo, nomeamos o arquivo info.txt e o diretório Storage. Para criá-los, seguimos os comandos e sua sintaxe mostrados acima.

### Crie um arquivo vazis

`NycolasES6@htb[/htb]$ touch info.txt`

### Crie um diretório

``NycolasES6@htb[/htb]$ mkdir Storage``

Podemos querer ter diretórios específicos no diretório e seria muito demorado criar este comando para cada diretório. O comando ``mkdir`` tem uma opção marcada ``-p`` para adicionar diretórios pais.

``NycolasES6@htb[/htb]$ mkdir -p Storage/local/user/documents``

Podemos observar toda a estrutura após criar os diretórios pais com a ferramenta tree.

``NycolasES6@htb[/htb]$ tree .``

![alt text](img/tree01.png)

Com o comando ``mv`` podemos mover e também renomear arquivos e diretórios. A sintaxe para isso é semelhante a esta:

``NycolasES6@htb[/htb]$ mv <file/directory> <renamed file/directory>``

### Mover arquivos para um diretório específico

``NycolasES6@htb[/htb]$ mv information.txt readme.txt Storage/``

Vamos supor que queremos ter o readme.txtno local/diretório. Então podemos copiá-los para lá com os caminhos especificados.

``NycolasES6@htb[/htb]$ cp Storage/readme.txt Storage/local/``
