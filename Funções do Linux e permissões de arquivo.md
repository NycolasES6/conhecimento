#Linux #SO 

# Funções do Linux e permissões de arquivo

No Linux, a maioria das entidades do sistema são tratadas como arquivos. Para organizar o sistema e impor limites dentro do computador, o Linux usa permissões de arquivo. As permissões de arquivo são incorporadas à estrutura do sistema de arquivos e fornecem um mecanismo para definir permissões em cada arquivo. Cada arquivo no Linux carrega suas permissões de arquivo, que definem as ações que o proprietário, o grupo e outros podem executar com o arquivo. Os direitos de permissão possíveis são Ler, Gravar e Executar. O comando **ls** com o parâmetro -l lista informações adicionais sobre o arquivo.

Considere o resultado do comando **ls -l** na saída.

```
[analyst@secOps ~]$ ls -l space.txt

-rwxrw-r-- 1 analyst staff 253 May 20 12:49 space.txt

     (1)  (2)  (3)    (4)  (5)     (6)         (7)
```

A saída fornece muitas informações sobre o arquivo **space.txt**

O primeiro campo da saída exibe as permissões associadas a **space.txt (-rwxrw-r--).** As permissões de arquivo são sempre exibidas na ordem Usuário, Grupo e Outro.

O arquivo **space.txt** tem as seguintes permissões:

- O traço (-) significa que este é um arquivo. Para diretórios, o primeiro traço seria um “d”.
- O primeiro conjunto de caracteres é para permissão de usuário (**rwx**). O usuário, **analista**, que possui o arquivo pode **R**ead, **W**rite e e**X**ecute o arquivo.
- O segundo conjunto de caracteres é para permissões de grupo(**rw-**). O grupo, **staff**, que possui o arquivo pode **R**ead e **W**rite no arquivo.
- O terceiro conjunto de caracteres é para quaisquer outras permissões de usuário ou grupo (**r--**). Qualquer outro usuário ou grupo no computador pode apenas ler o arquivo.

O segundo campo define o número de links rígidos para o arquivo (o número 1 após as permissões). Um link rígido cria outro arquivo com um nome diferente vinculado ao mesmo lugar no sistema de arquivos (chamado de inode). Isso está em contraste com um link simbólico, que é discutido na próxima página.

O terceiro e quarto campos exibem o usuário (**analista**) e o grupo (**staff**) que possui o arquivo, respectivamente.

O quinto campo exibe o tamanho do arquivo em bytes. O arquivo **space.txt** tem 253 bytes.

O sexto campo exibe a data e hora da última modificação.

O sétimo campo exibe o nome do arquivo.

A figura mostra uma divisão das permissões de arquivo no Linux.

![[Pasted image 20240515100050.png]]

Use valores octais para definir permissões.

| Binário | Octal | Permissão | Descrição                |
| ------- | ----- | --------- | ------------------------ |
| 000     | 0     | ---       | Sem acesso               |
| 001     | 1     | --x       | Executar apenas          |
| 010     | 2     | -w-       | Somente escrita          |
| 011     | 3     | -wx       | Edição e execução        |
| 100     | 4     | r--       | Somente leitura          |
| 101     | 5     | r-x       | Ler e executar           |
| 110     | 6     | rw-       | Leitura e Escrita        |
| 111     | 7     | rwx       | Ler, escrever e executar |

Permissões de arquivo são uma parte fundamental do Linux e não podem ser quebradas. Um usuário tem apenas os direitos de um arquivo que as permissões de arquivo permitem. O único usuário que pode substituir a permissão de arquivo em um computador Linux é o usuário root. Como o usuário root tem o poder de substituir as permissões de arquivo, o usuário root pode gravar em qualquer arquivo. Como tudo é tratado como um arquivo, o usuário root tem controle total sobre um computador Linux. O acesso como root é muitas vezes necessário antes de realizar tarefas administrativas e de manutenção. Devido ao poder do usuário raiz, as credenciais raiz devem usar senhas fortes e não ser compartilhadas com ninguém além de administradores de sistema e outros usuários de alto nível.

















