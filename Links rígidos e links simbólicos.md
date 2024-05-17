#Linux #SO 
# Links rígidos e links simbólicos

Um link rígido é outro arquivo que aponta para o mesmo local que o arquivo original. Use o comando **ln** para criar um link rígido. O primeiro argumento é o arquivo existente e o segundo argumento é o novo arquivo. Como mostrado na saída do comando, o arquivo **space.txt** está vinculado a **space.hard.txt** e o campo de link agora mostra 2.

```sh
[analyst@secOps ~]$ ln space.txt space.hard.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ ls -l space*

-rw-r--r-- 2 analyst analyst 239 May 7 18:18 space.hard.txt

-rw-r--r-- 2 analyst analyst 239 May 7 18:18 space.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ echo "Testing hard link" >> space.hard.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ ls -l space*

-rw-r--r-- 2 analyst analyst 257 May 7 18:19 space.hard.txt

-rw-r--r-- 2 analyst analyst 257 May 7 18:19 space.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ rm space.hard.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ more space.txt

Space... The final frontier…

These are the voyages of the Starship Enterprise. Its continuing mission:

- To explore strange new worlds…

- To seek out new life; new civilizations…

- To boldly go where no one has gone before!

Testing hard link

[analyst@secOps ~]$
```

Ambos os arquivos apontam para o mesmo local no sistema de arquivos. Se você alterar um arquivo, o outro também será alterado. O comando **echo** é usado para adicionar algum texto ao **space.txt.** Observe que o tamanho do arquivo para os dois, **space.txt** e **space.hard.txt** aumentou para 257 bytes . Se você excluir o space.hard.txt com o comando **rm** (remover) , o arquivo **space.txt** ainda existe, conforme verificado com o comando **more space.txt**.

Um link simbólico, também chamado de link simbólico ou link suave, é semelhante a um link rígido em que a aplicação de alterações ao link simbólico também mudará o arquivo original. Como mostrado na saída do comando abaixo, use o comando **ln** com a opção **-s** para criar um link simbólico.

```sh
[analyst@secOps ~]$ echo "Hello World!" > test.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ ln -s test.txt mytest.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ echo "It's a lovely day!" >> mytest.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ more test.txt

Hello World!

It's a lovely day!

[analyst@secOps ~]$

[analyst@secOps ~]$ rm test.txt

[analyst@secOps ~]$

[analyst@secOps ~]$ more mytest.txt

more: stat of mytest.txt failed: No such file or directory

[analyst@secOps ~]$

[analyst@secOps ~]$ ls -l mytest.txt

lrwxrwxrwx 1 analyst analyst 8 May 7 20:17 mytest.txt -> test.txt

[analyst@secOps ~]$
```

Observe que adicionar uma linha de texto ao**test.txt** também adiciona a linha ao **mytest.txt.** No entanto, ao contrário de um link rígido, excluir o arquivo text.txt original significa que agora **mytext.txt** está vinculado a um arquivo que não existe mais, como mostrado com os comandos **mytest.txt** e **ls -l mytest.txt**.

Embora links simbólicos tenham um único ponto de falha (o arquivo subjacente), links simbólicos têm vários benefícios sobre links rígidos:

- Localizar links rígidos é difícil. Os links simbólicos mostram a localização do arquivo original no comando **ls -l**, como mostrado na última linha de saída no comando anterior **(mytest.txt -> test.txt)**.
- Links rígidos são limitados ao sistema de arquivos no qual eles são criados. Links simbólicos podem ser vinculados a um arquivo em outro sistema de arquivos.
- Links rígidos não podem se vincular a um diretório porque o próprio sistema usa links rígidos para definir a hierarquia da estrutura de diretórios. No entanto, links simbólicos podem se vincular a diretórios.






















