#Linux 
# Linux - Prevenção da expansão

Quando você precisa usar um asterisco (`*`) ou um ponto de interrogação (`?`) como um asterisco ou ponto de interrogação literal, deve colocar um caractere de _escape_ antes deles. Na linha de comando, você pode usar a barra invertida (`\`) como caractere de escape. O terminal sempre trata o caractere imediatamente após o caractere de escape como um caractere literal em vez de um metacaractere.

Nos exemplos a seguir, você usa curingas para corresponder arquivos, mas também usa caracteres de escape para interpretar o ponto de interrogação (`?`) literalmente. Na lista de arquivos a seguir, você deseja listar todos os arquivos que têm um ponto de interrogação (`?`) após a palavra `Linux` no nome.

![[Pasted image 20240614153819.png]]

Você começa listando todos os arquivos que têm a palavra `Linux` no nome:

![[Pasted image 20240614153834.png]]

Em seguida, você lista todos os arquivos que têm a palavra `Linux` no nome e que têm um ponto de interrogação após a palavra. No exemplo a seguir, você não coloca um caractere de escape antes do ponto de interrogação (`?`) para que este seja interpretado como um metacaractere. Devido ao metacaractere ponto de interrogação (`?`), os resultados incluem arquivos com pelo menos um caractere após a palavra `Linux`.

![[Pasted image 20240614153910.png]]

No exemplo a seguir, você coloca um caractere de escape antes do ponto de interrogação (`?`) para que este seja interpretado literalmente.

![[Pasted image 20240614153922.png]]





