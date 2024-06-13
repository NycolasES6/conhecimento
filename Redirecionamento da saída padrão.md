#Linux 
# Redirecionamento da saída padrão

Você pode alterar o destino da saída padrão usando _redirecionamento_. Por exemplo, você pode redirecionar a saída padrão para um arquivo usando um símbolo de maior que (`>`). Um único símbolo de maior que (`>`) substitui todo o texto em um arquivo com os dados que são enviados para a saída padrão.

![[Pasted image 20240612162455.png]]

Dois símbolos maiores que (`>>`) anexam dados de texto da saída padrão ao final de um arquivo.

![[Pasted image 20240612162514.png]]

Você também pode redirecionar fluxos usando um descritor de arquivo numérico e um ou dois símbolos de maior que. O descritor de arquivo designado para a saída padrão é `1`. A saída padrão é o fluxo padrão para redirecionamento, por isso não precisa ser especificada.

Nos exemplos a seguir, o primeiro comando usa um descritor de arquivo e o segundo comando não. Ambos os comandos são equivalentes.

![[Pasted image 20240612162550.png]]

Você pode redirecionar a saída padrão para um dispositivo em vez de um arquivo. O dispositivo `/dev/null` é um dispositivo virtual projetado para descartar bits. Quando você envia dados para o dispositivo `/dev/null`, ele os descarta silenciosamente.

No exemplo a seguir, você redireciona a saída padrão para o dispositivo `/dev/null` para não ver nenhuma saída na tela.

![[Pasted image 20240612162708.png]]

Você pode redirecionar a saída padrão para um dispositivo em vez de um arquivo. O dispositivo `/dev/null` é um dispositivo virtual projetado para descartar bits. Quando você envia dados para o dispositivo `/dev/null`, ele os descarta silenciosamente.

No exemplo a seguir, você redireciona a saída padrão para o dispositivo `/dev/null` para não ver nenhuma saída na tela.

![[Pasted image 20240612162750.png]]

O redirecionamento da saída padrão é útil quando você usa comandos que podem ter muitas saídas. Em vez de revisar a saída longa rolando no terminal, você pode revisar a saída do comando no arquivo resultante usando o comando `less` para paginação, o comando `wc` para contagem de caracteres e assim por diante.