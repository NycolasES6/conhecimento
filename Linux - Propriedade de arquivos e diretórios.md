#Linux 
# Linux - Propriedade de arquivos e diretórios

No Linux, você compartilha arquivos e diretórios usando grupos. Ao criar um arquivo ou diretório, você é definido como proprietário desse arquivo ou diretório. Se você for membro de um grupo, e esse grupo for proprietário de um diretório, será possível interagir com os arquivos nesse diretório como se fosse o proprietário.

## Alteração de propriedade de arquivo e diretório

ocê pode conferir e atualizar as informações de propriedade de arquivo no aplicativo Files. Navegue até o arquivo ou diretório, clique com o botão direito no item e clique em Properties no menu de contexto.

No exemplo a seguir, o arquivo `mynotes.txt` é de propriedade do usuário conectado `operator1`, desse modo, o rótulo Owner exibe `Me`. A lista suspensa do campo Group exibe `operator1` como proprietário do grupo.

![[Pasted image 20240614163530.png]]

Na linha de comando, use o comando `ls` com a opção `-l` para visualizar as informações de propriedade do arquivo.

No exemplo a seguir, o usuário `operator1` é um membro do grupo `finance`. Os arquivos listados são de propriedade do usuário `operator1`, mas o diretório `Artifacts` é de propriedade do grupo `finance`. Essa configuração permite que o usuário `operator1` crie arquivos no diretório `Artifacts`, mesmo que o diretório `/Projects/Artifacts/` não seja o diretório pessoal do usuário `operator1`.

![[Pasted image 20240614163601.png]]

Você atualiza a propriedade do arquivo usando o comando `chown`. O comando `chown` requer dois argumentos: o novo proprietário (seja um usuário ou um grupo) e o arquivo ou diretório de destino. Você fornece o usuário ou grupo no formato ``_`user`_:_`group`_``. Você deve usar dois pontos (`:`) para separar o usuário do grupo ou para definir somente o grupo.

No exemplo a seguir, dois usuários interagem com um diretório. Observe o nome de usuário no prompt de comando para identificar qual usuário está executando qual comando.

Os usuários `developer1` e `developer2` são membros do grupo `java-devs`. O usuário `developer1` e o grupo `dev1` são proprietários do diretório `/Projects/Java-code`. O diretório tem as permissões necessárias para que os membros do grupo criem arquivos.

![[Pasted image 20240614163715.png]]

O comando a seguir falha porque o usuário `developer2` não é membro do grupo `dev1`.

![[Pasted image 20240614163729.png]]

No comando a seguir, o usuário `developer1` altera o proprietário do grupo do diretório `Java-code` para o grupo `java-devs`. O argumento `developer1:java-devs` define o proprietário do usuário como `developer1` (sem alterações) e o proprietário do grupo como `java-devs`. Essa ação concede acesso ao usuário `developer2` por meio do grupo `java-devs`. O usuário `developer1` ainda é o proprietário do usuário do diretório.

![[Pasted image 20240614163753.png]]

Como o usuário `developer2` é membro do grupo `java-devs`, o usuário `developer2` pode criar um arquivo no diretório `Java-code`.

![[Pasted image 20240614163809.png]]








