#Linux 
# Pipelines

Você pode redirecionar a saída padrão para a entrada padrão usando um pipe (`|`). O redirecionamento da saída padrão usando um pipe é uma forma de comunicação entre processos e usa a saída de um comando como a entrada de outro. Um uso comum para os pipes é manipular a saída do comando por uma série de comandos para apresentá-la em um determinado formato. Você pode usar mais de um pipe para processar a saída do comando.

Neste exemplo, o comando `date` envia a data para a entrada padrão do comando `rev`, que inverte as strings:

![[Pasted image 20240612163303.png]]

No exemplo a seguir, você usa dois pipes para manipular o comando `timedatectl`. O comando `grep` filtra as linhas que contêm a string `time`. Em seguida, o comando `sort` classifica as linhas em ordem alfabética. A opção `sort` do comando `-b` ignora os espaços em branco à esquerda.

![[Pasted image 20240612163320.png]]

Usando o comando `tee`, você pode ver a saída padrão e redirecioná-la ao mesmo tempo.

![[Pasted image 20240612163331.png]]

O uso de pipes é útil para localizar ou formatar texto específico de grandes quantidades de saída. Em alguns cenários, em vez de usar pipes em uma saída de comando, talvez você queira redirecionar a saída de comando para um arquivo de texto. Em seguida, você poderá ver o arquivo resultante e usar pipes para manipular a saída. Ao salvar a saída em um arquivo primeiro, você evita a execução de um comando longo ou lento várias vezes.




