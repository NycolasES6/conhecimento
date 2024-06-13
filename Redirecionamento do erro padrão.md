#linux
# Redirecionamento do erro padrão

A saída padrão e o erro padrão são fluxos de dados distintos. O erro padrão é indicado pelo descritor de arquivo `2`. Use o descritor de arquivo `2` seguido por um ou dois símbolos de maior que para redirecionar apenas o erro padrão.

No exemplo a seguir, você redireciona o erro padrão para o arquivo `example.txt` e lê o conteúdo do arquivo. Esse redirecionamento é muito útil para ver a saída dos comandos sem as mensagens de erro. Posteriormente, você poderá revisar as mensagens de erro conferindo o conteúdo do arquivo.

![[Pasted image 20240612163127.png]]

No exemplo a seguir, você redireciona o erro padrão para o dispositivo `/dev/null`.

![[Pasted image 20240612163143.png]]

O redirecionamento do erro padrão é útil quando você tem uma saída desnecessária, como quando você executa um comando apenas para gerar atividade para testar a CPU. O redirecionamento do erro padrão também é útil quando há uma mensagem de erro conhecida e esperada que você não precisa ver.

