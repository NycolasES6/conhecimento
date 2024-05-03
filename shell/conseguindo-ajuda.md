# Getting Help

Sempre tropeçaremos em ferramentas cujos parâmetros opcionais não conhecemos de memória ou em ferramentas que nunca vimos antes. Portanto, é vital saber como podemos nos ajudar a nos familiarizar com essas ferramentas. As duas primeiras formas são as páginas de manual e as funções de ajuda. É sempre uma boa ideia nos familiarizarmos primeiro com a ferramenta que queremos experimentar. Também aprenderemos alguns truques possíveis com algumas das ferramentas que pensávamos não serem possíveis. Nas páginas de manual, encontraremos os manuais detalhados com explicações detalhadas.

## man

### Sintaxe

`NycolasES6@htb[/htb]$ man <tool>`

### Exemplo

`NycolasES6@htb[/htb]$ man curl`

## --help

Depois de ver alguns exemplos, também podemos examinar rapidamente os parâmetros opcionais sem navegar pela documentação completa. Temos várias maneiras de fazer isso.

### Sintaxe

`NycolasES6@htb[/htb]$ <tool> --help`

### Exemplo

`NycolasES6@htb[/htb]$ curl --help`

> O argumento --help pode ser abreviado por -h .

## apropos

Como podemos ver, os resultados entre si não diferem neste exemplo. Outra ferramenta que pode ser útil no início é o apropos. Cada página de manual possui uma breve descrição disponível. Esta ferramenta pesquisa nas descrições instâncias de uma determinada palavra-chave.

### Sintaxe

`NycolasES6@htb[/htb]$ apropos <keyword>`

### Exemplo

`NycolasES6@htb[/htb]$ apropos sudo`
