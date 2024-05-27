#Linux #regex
# Expressões regulares no Linux

Expressões regulares ( `RegEx`) são uma arte da linguagem de expressão para pesquisar padrões em textos e arquivos. Eles podem ser usados ​​para localizar e substituir texto, analisar dados, validar entradas, realizar pesquisas e muito mais. Em termos simples, são um critério de filtro que pode ser usado para analisar e manipular strings. Eles estão disponíveis em várias linguagens de programação e programas e são usados ​​de muitas maneiras e funções diferentes.

Uma expressão regular é uma sequência de letras e símbolos que formam um padrão de pesquisa. Além disso, expressões regulares podem ser criadas com padrões chamados metacaracteres. Metacaracteres são símbolos que definem o padrão de pesquisa, mas não têm significado literal. Podemos usá-lo em ferramentas como `grep`,  `sed` ou outras. Freqüentemente, o regex é implementado em aplicativos da web para a validação da entrada do usuário.

## Agrupamento

Entre outras coisas, o regex nos oferece a possibilidade de agrupar os padrões de pesquisa desejados. Basicamente, regex segue três conceitos diferentes, que são diferenciados por três colchetes diferentes:

### Operadores de agrupamento

| **Operadores** | **Descrição** |                                                                                                                                                                                           |
| -------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1              | `(a)`         | Os colchetes são usados ​​para agrupar partes de uma regex. Entre colchetes, você pode definir outros padrões que devem ser processados ​​juntos.                                         |
| 2              | `[a-z]`       | Os colchetes são usados ​​para definir classes de caracteres. Dentro dos colchetes, você pode especificar uma lista de caracteres a serem pesquisados.                                    |
| 3              | `{1,10}`      | As chaves são usadas para definir quantificadores. Dentro dos colchetes, você pode especificar um número ou intervalo que indica com que frequência um padrão anterior deve ser repetido. |
| 4              | `\|`          | Também chamado de operador OR e mostra resultados quando uma das duas expressões corresponde                                                                                              |
| 5              | `.*`          | Também chamado de operador AND e exibe resultados somente se ambas as expressões corresponderem                                                                                           |

Suponha que usemos o operador `OR`. A regex procura um dos parâmetros de pesquisa fornecidos. No próximo exemplo, procuramos linhas que contenham a palavra `my` ou `false`. Para usar esses operadores, você precisa aplicar o regex estendido usando a opção `-E` no grep

## Operador OR

```sh
cry0l1t3@htb:~$ grep -E "(my|false)" /etc/passwd

lxd:x:105:65534::/var/lib/lxd/:/bin/false
pollinate:x:109:1::/var/cache/pollinate:/bin/false
mysql:x:116:120:MySQL Server,,:/nonexistent:/bin/false
```

Como um dos dois parâmetros de pesquisa sempre ocorre nas três linhas, todas as três linhas são exibidas de acordo. Porém, se usarmos o operador `AND`, obteremos um resultado diferente para os mesmos parâmetros de pesquisa.

## Operador AND

```sh
cry0l1t3@htb:~$ grep -E "(my.*false)" /etc/passwd

mysql:x:116:120:MySQL Server,,:/nonexistent:/bin/false
```

Basicamente, o que estamos dizendo com este comando é que estamos procurando uma linha onde queremos ver ambos `my` e `false`. Um exemplo simplificado também seria usar `grep`duas vezes e ficar assim:

```sh
cry0l1t3@htb:~$ grep -E "my" /etc/passwd | grep -E "false"

mysql:x:116:120:MySQL Server,,:/nonexistent:/bin/false
```














































