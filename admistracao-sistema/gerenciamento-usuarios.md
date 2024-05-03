# Gerenciamento de usuários

O gerenciamento de usuários é uma parte essencial da administração do Linux.
Ás vezes precisamos criar novos usuários ou adicionar novos usuários a gruós específicos. Outra possibilidade é executar comandos como um usuário diferente. Afinal, não é raro que usuários de apenas um grupo específico tenham permissões para visualizar ou editar arquivos ou dirertórios específicos. Ista, por sua vez, permite-nos recolher mais informações localmente na mãquina, o que pode ser muito importante. Vamos dar uma olhada no exemplo a seguir de como executar código como un usuário diferente.

### Execução como usuário

`cat /etc/shadow`

### Execução como root

`sudo cat /etc/shadow`

Aqui está uma lista que nos ajudará a entender e lidar melhor com o gerenciamento de usuários.

 - ``sudo`` - Execute o comando como um usuário diferente.
 - ``su`` - O utilitário su solicita credenciais de usuário via PAM e alterna esse ID de usuário (o usuário padrão é o superusuário). Um shell é então executado.
 - ``useradd`` - Cria um novo usuário ou atualiza as informações padrão do novo usuário.
 - ``userdel`` - Exclui uma conta de usuário e arquivos relacinados.
 - ``usermod`` - Modifica uma conta de usuário.
 - ``addgroup`` - Adiciona um grupo ao sistema.
 - ``delgroup`` - Remove um grupo do sistema.
 - ``passwd`` - Altere a senha do usuário.

O gerenciamento de usuários é essencial em qualquer sistema operacional, e amelhor maneira de se familiarizar com ele é experimentar os comandos individuais em conjunto com suas diversas opções.

