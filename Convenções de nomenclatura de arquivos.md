#Linux 
# Convenções de nomenclatura de arquivos

No Linux, uma prática recomendada é evitar o uso de espaços em nomes de arquivos, pois o shell usa caracteres de espaço em branco para separar os argumentos de um comando. Os usuários do Linux geralmente usam o terminal para manipular arquivos, e a manipulação de arquivos que contenham um espaço no nome pode causar problemas.

Por exemplo, você pode listar o arquivo `Inventory.xlsx`, mas listar o arquivo `My shopping list` com caracteres de espaço em branco no nome retornará um erro.

![[Pasted image 20240612165344.png]]

O shell interpreta `My`, `shopping` e `list` como argumentos diferentes para o comando `ls`, mas esses arquivos não existem. Os exemplos a seguir mostram como referenciar corretamente o arquivo `My shopping list` usando métodos diferentes.

![[Pasted image 20240612165408.png]]

|   |   |
|---|---|
|[![1](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/1.svg)](https://rha.ole.redhat.com/rha/app/#_conven%C3%A7%C3%B5es_de_nomenclatura_de_arquivos-CO2-1)|Usar o caractere de espace antes do caractere de espaço. O shell pode desativar o significado especial do espaço em branco como separador de palavras e, em vez disso, interpretá-lo como um caractere padrão que faz parte do nome do arquivo. Isso é chamado de _escape_ de um caractere especial. Para fazer escape de um espaço, use o caractere de barra invertida (`\`) antes do espaço.|
|[![2](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/2.svg)](https://rha.ole.redhat.com/rha/app/#_conven%C3%A7%C3%B5es_de_nomenclatura_de_arquivos-CO2-2)|Usar o preenchimento com Tab. Você pode começar a digitar o nome do arquivo e usar o preenchimento com Tab para permitir que o shell conclua o nome do arquivo para você. O shell preenche automaticamente os caracteres de escape necessários. Esse método pode não ser útil quando os arquivos têm nomes semelhantes e talvez você ainda precise fazer o espace do espaço manualmente.|
|[![3](https://rha.ole.redhat.com/rol/static/roc/Common_Content/images/3.svg)](https://rha.ole.redhat.com/rha/app/#_conven%C3%A7%C3%B5es_de_nomenclatura_de_arquivos-CO2-3)|Colocar o nome do arquivo entre aspas. Você pode fazer referência a um nome que contenha espaços colocando o nome completo entre aspas simples ou duplas.|





