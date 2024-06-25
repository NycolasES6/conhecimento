#bashScript #variaveis
# Variaveis em bashScript
## Variáveis especiais

Variáveis especiais que usam o Separador de Campo Interno (IFS), para identificar quando um argumento termina e o próximo começa. Bash fornece variáveis especiais que auxiliam durante a criação de scripts. Algumas dessas variáveis são:

|**SE**|**Descrição**|
|---|---|
|`$#`|Esta variável contém o número de argumentos passados ​​para o script.|
|`$@`|Esta variável pode ser usada para recuperar a lista de argumentos da linha de comando.|
|`$n`|Cada argumento da linha de comando pode ser recuperado seletivamente usando sua posição. Por exemplo, o primeiro argumento é encontrado em `$1`.|
|`$$`|O ID do processo atualmente em execução.|
|`$?`|O status de saída do script. Esta variável é útil para determinar o sucesso de um comando. O valor 0 representa uma execução bem-sucedida, enquanto 1 é o resultado de uma falha.|

Das mostradas acima, temos 3 dessas variáveis ​​especiais em nossa condição `if-else`.

| **SE** | **Descrição**                                                                                                                                                                                                                                               |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$#`   | Neste caso, precisamos de apenas uma variável que precisa ser atribuída à `domain`variável. Esta variável é usada para especificar o alvo com o qual queremos trabalhar. Se fornecermos apenas um FQDN como argumento, a `$#`variável terá um valor de `1`. |
| `$0`   | A esta variável especial é atribuído o nome do script executado, que é então mostrado no exemplo "`Usage:`".                                                                                                                                                |
| `$1`   | Separado por um espaço, o primeiro argumento é atribuído a essa variável especial.                                                                                                                                                                          |

## Variáveis

Vemos também no final do loop if-else que atribuímos o valor do primeiro argumento à variável chamada " `domain`". A atribuição de variáveis ​​ocorre sem o cifrão ( `$`). O cifrão destina-se apenas a permitir que o valor correspondente desta variável seja usado em outras seções de código. Ao atribuir variáveis, não deve haver espaços entre os nomes e valores.

```bash
<SNIP>
else
	domain=$1
fi
<SNIP>
```

Em contraste com outras linguagens de programação, não há diferenciação e reconhecimento direto entre os tipos de variáveis ​​​​no Bash como " `strings`," " `integers`," e " `boolean`." Todo o conteúdo das variáveis ​​é tratado como caracteres de string. Bash habilita funções aritméticas dependendo se apenas números são atribuídos ou não. É importante observar ao declarar variáveis ​​que elas não tenham `space`. Caso contrário, o nome real da variável será interpretado como uma função interna ou um comando.

#### Declarando uma Variável - Erro

```sh
NycolasES6@htb[/htb]$ variable = "this will result with an error."

command not found: variable
```

#### Declarando uma variável - sem erro

```sh
NycolasES6@htb[/htb]$ variable="Declared without an error."
NycolasES6@htb[/htb]$ echo $variable

Declared without an error.
```
