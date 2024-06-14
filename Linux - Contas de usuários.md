#Linux 
# Linux - Contas de usuários

O Linux gerencia o acesso aos recursos do sistema por meio de contas de usuário. Ao fazer login em um sistema Linux, você utiliza um nome de usuário e uma senha para fazer a autenticação. O Linux identifica você de maneira exclusiva e permite que você acesse seus arquivos, diretórios e configurações pessoais. O Linux monitora o que você tem acesso usando um _identificador de usuário_ (_UID_) e um _identificador de grupo_ (_GID_).

##  Identificadores de usuários e usuários do sistema

As contas de usuário têm propriedades que definem algumas características do usuário, como o diretório pessoal ou o shell preferido. A UID é uma propriedade numérica do usuário que identifica exclusivamente um usuário no sistema. O primeiro usuário que você cria no sistema geralmente tem a UID de 1000. A UID é incrementada em um para cada novo usuário.

Os usuários com uma UID inferior a 1000 são conhecidos como _usuários do sistema_. O Linux usa usuários do sistema para executar serviços especiais. O sistema operacional cria vários usuários do sistema durante a instalação, e alguns softwares podem exigir um usuário do sistema para serem operados.

## Linux - Grupos de usuários

Um _grupo_ ou _grupo_ de usuários é uma coleção de usuários que compartilham características, como permissões de arquivo. Quando o Linux cria um usuário, ele também cria um grupo com o mesmo nome dele. Esse grupo é conhecido como o _grupo primário_ do usuário.

Um usuário pode ser membro de muitos grupos. Qualquer grupo diferente do grupo primário é conhecido como grupo _secundário_ ou _suplementar_. A GID do grupo primário geralmente é a mesma que a UID. Semelhante a uma UID, uma GID para um usuário normal começa em 1000.

No exemplo a seguir, o usuário `developer1` tem uma UID de 1020. O usuário `developer1` é membro dos grupos `developer1` e `java-devs`. O grupo `developer1` é o grupo padrão criado pelo sistema e é o grupo primário para esse usuário.

![[Pasted image 20240614163311.png]]

Você usa o comando `id` com a opção `-g` para imprimir a GID do grupo primário de um usuário. Além disso, também é possível usar a opção `--name` para imprimir o nome do grupo em vez do número da ID.

![[Pasted image 20240614163328.png]]

Você também pode visualizar informações de grupo usando o comando `groups`. Por padrão, o comando `groups` mostra a associação de grupo do usuário atual. No exemplo a seguir, você vê a associação de grupo do usuário `developer1`.

![[Pasted image 20240614163341.png]]









