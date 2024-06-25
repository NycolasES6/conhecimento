#Linux #shell 
# Gerenciamento de permissões

No Linux, as permissões são atribuídas a usuários e grupos. Cada usuário pode ser membro de grupos diferentes, e a associação a esses grupos fornece ao usuário permissões adicionais específicas. Cada arquivo e diretório pertence a um usuário específico e a um grupo específico. Assim as permissões para usuários e grupos que definiram um arquivo também são definidas para os respectivos proprietários. Quando criamos novos arquivos ou diretórios, eles pertencem ao grupo ao qual pertencemos e a nós.

Quando um usuário deseja acessar o conteúdo de um diretório Linux, ele deve primeiro percorrer o diretório, o que significa navegar até esse diretório, exigindo que o usuário tenha permissões de `execução` no diretório. Sem esta permissão, o usuário não poderá acessar o conteúdo do diretório e, em vez disso, receberá uma mensagem de erro “`Permission Denied`".

```sh
cry0l1t3@htb[/htb]$ ls -l

drw-rw-r-- 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:30 scripts


cry0l1t3@htb[/htb]$ ls -al mydirectory/

ls: cannot access 'mydirectory/script.sh': Permission denied
ls: cannot access 'mydirectory/..': Permission denied
ls: cannot access 'mydirectory/subdirectory': Permission denied
ls: cannot access 'mydirectory/.': Permission denied
total 0
d????????? ? ? ? ?            ? .
d????????? ? ? ? ?            ? ..
-????????? ? ? ? ?            ? script.sh
d????????? ? ? ? ?            ? subdirectory
```

é importante perceber que são necessárias permissões de execução para percorrer um diretório, independentemente do nível de acesso do usuário. Além disso, as permissões em um diretório não permitem que um usuário execute ou modifique quaisquer arquivos ou conteúdos dentro do diretório, apenas percorrer e acessar o conteúdo do diretório.

Para executar arquivos dentro do diretório, um usuário precisa de permissões no arquivo correspondente. Para modificar o conteúdo de um diretório (criar, excluir ou renomear arquivos e subdiretórios), o usuário precisa de permissões de escrita no diretório.

Todo sistema de permissões em sistemas Linux é baseado no sistema de números octais e, basicamente, existem três tipos diferentes de permissões que podem ser atribuídas a um arquivo ou diretório:

- ( `r` ) - Ler
- ( `w` ) - Escrever
- ( `x` ) - Executar

As permissões podem ser definidas para `owner`, `group`e `others` como apresentado no próximo exemplo com suas permissões correspondentes.

```sh
cry0l1t3@htb[/htb]$ ls -l /etc/passwd

- rwx rw- r--   1 root root 1641 May  4 23:42 /etc/passwd
- --- --- ---   |  |    |    |   |__________|
|  |   |   |    |  |    |    |        |_ Date
|  |   |   |    |  |    |    |__________ File Size
|  |   |   |    |  |    |_______________ Group
|  |   |   |    |  |____________________ User
|  |   |   |    |_______________________ Number of hard links
|  |   |   |_ Permission of others (read)
|  |   |_____ Permissions of the group (read, write)
|  |_________ Permissions of the owner (read, write, execute)
|____________ File type (- = File, d = Directory, l = Link, ... )
```

## Alterar permissões

Podemos modificar as permissões usando o comando `chmod`, referências de grupo de permissões ( `u`- proprietário, `g`- Grupo, `o`- outros, `a`- Todos os usuários) e um \[`+`] ou um \[`-`] para adicionar e remover as permissões designadas. No exemplo a seguir, vamos supor que temos um arquivo chamado `shell`e queremos alterar as permissões dele para que esse script de propriedade desse usuário se torne não executável e definido com permissões de leitura/gravação para todos os usuários.

```shell-session
cry0l1t3@htb[/htb]$ ls -l shell

-rwxr-x--x   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```

Podemos então aplicar permissões `read` para todos os usuários e ver o resultado.

```sh
cry0l1t3@htb[/htb]$ chmod a+r shell && ls -l shell

-rwxr-xr-x   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```

Também podemos definir as permissões `read` para todos os outros usuários usando apenas a atribuição de valor octal.

```sh
cry0l1t3@htb[/htb]$ chmod 754 shell && ls -l shell

-rwxr-xr--   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```

Vejamos todas as representações associadas a ele para entender melhor como a atribuição de permissão é calculada.

```shell-session
Binary Notation:                4 2 1  |  4 2 1  |  4 2 1
----------------------------------------------------------
Binary Representation:          1 1 1  |  1 0 1  |  1 0 0
----------------------------------------------------------
Octal Value:                      7    |    5    |    4
----------------------------------------------------------
Permission Representation:      r w x  |  r - x  |  r - -
```

Se somarmos os bits definidos da Representação Binária atribuídos aos valores da Notação Binária, obteremos o Valor Octal. A Representação de Permissão representa os bits definidos na Representação Binária usando os três caracteres, que apenas reconhecem mais facilmente as permissões definidas.

## Alterar proprietário

Para alterar o proprietário e/ou as atribuições de grupo de um arquivo ou diretório, podemos usar o comando `chown`. A sintáxe é a seguinte:

### Sintaxe - chown

```sh
cry0l1t3@htb[/htb]$ chown <user>:<group> <file/directory>
```

Neste exemplo, “shell” pode ser substituído por qualquer arquivo ou pasta arbitrária.

```sh
cry0l1t3@htb[/htb]$ chown root:root shell && ls -l shell

-rwxr-xr--   1 root root 0 May  4 22:12 shell
```

## SUID e SGID

Além de atribuir permissões diretas a usuários e grupos, também podemos configurar permissões especiais para arquivos definindo os bits `Set User ID`( `SUID`) e `Set Group ID`( `SGID`). Esses bits `SUID`/ `SGID`permitem, por exemplo, que usuários executem programas com os direitos de outro usuário. Os administradores costumam usar isso para conceder aos usuários direitos especiais para determinados aplicativos ou arquivos. A letra " `s`" é usada em vez de " `x`". Ao executar tal programa, o SUID/SGID do proprietário do arquivo é usado.

Muitas vezes acontece que os administradores não estão familiarizados com os aplicativos, mas ainda assim atribuem os bits SUID/SGID, o que leva a um alto risco de segurança. Tais programas podem conter funções que permitem a execução de um shell a partir do pager, como a aplicação " `journalctl`."

Se o administrador definir o bit SUID como " `journalctl`," qualquer usuário com acesso a este aplicativo poderá executar um shell como `root`. Mais informações sobre este e outros aplicativos podem ser encontradas em [GTFObins](https://gtfobins.github.io/gtfobins/journalctl/) .

## Sticky Bit

Sticky bits são um tipo de permissão de arquivo no Linux que pode ser definida em diretórios. Este tipo de permissão fornece uma camada extra de segurança ao controlar a exclusão e renomeação de arquivos dentro de um diretório. Geralmente é usado em diretórios compartilhados por vários usuários para evitar que um usuário exclua ou renomeie acidentalmente arquivos que são importantes para outros.

Por exemplo, em um diretório inicial compartilhado, onde vários usuários têm acesso ao mesmo diretório, um administrador do sistema pode definir o sticky bit no diretório para garantir que apenas o proprietário do arquivo, o proprietário do diretório ou o usuário root pode excluir ou renomear arquivos dentro do diretório. Isso significa que outros usuários não podem excluir ou renomear arquivos no diretório porque não possuem as permissões necessárias. Isso fornece uma camada adicional de segurança para proteger arquivos importantes, pois somente aqueles com o acesso necessário podem excluir ou renomear arquivos. Definir o sticky bit em um diretório garante que apenas o proprietário, o proprietário do diretório ou o usuário root possam alterar os arquivos dentro do diretório.

Quando um sticky bit é definido em um diretório, ele é representado pela letra “ `t`" na permissão de execução das permissões do diretório. Por exemplo, se um diretório tiver permissões “ `rwxrwxrwt`", significa que o sticky bit está definido, dando o extra nível de segurança para que ninguém além do proprietário ou usuário root possa excluir ou renomear os arquivos ou pastas no diretório.

```shell-session
cry0l1t3@htb[/htb]$ ls -l

drw-rw-r-t 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:30 scripts
drw-rw-r-T 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:32 reports
```

Neste exemplo, vemos que ambos os diretórios têm o sticky bit definido. No entanto, a pasta `reports` tem letras maiúsculas `T` e a pasta `scripts` tem letras minúsculas `t`.

Se o sticky bit estiver maiúsculo ( `T`), isso significa que todos os outros usuários não têm permissões `execute`( `x`) e, portanto, não podem ver o conteúdo da pasta nem executar nenhum programa a partir dela. O sticky bit minúsculo ( `t`) é o bit sticky onde as permissões `execute`( `x`) foram definidas.











