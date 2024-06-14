#Linux 
# Linux - Privilégios de usuário

No Linux, um usuário normal não pode alterar a configuração do sistema, instalar software ou adicionar dispositivos (como impressoras ou dispositivos USB). Usuários regulares também estão impedidos de criar arquivos fora de seu diretório pessoal. Essas restrições ajudam a manter o sistema protegido contra acesso não autorizado e uso indevido acidental. Mas, em alguns cenários, um usuário comum pode precisar executar essas tarefas.

## Representação de um usuário com privilégios

Em vez de fornecer credenciais administrativas ao usuário comum, você pode conceder a esse usuário privilégios granulares para realizar as tarefas necessárias. Esses privilégios são concedidos pela representação de um usuário com privilégios, geralmente o usuário `root`. Ao _representar_ um usuário, você usa um comando como se fosse o usuário representado. Esse privilégio é comumente conhecido como _privilégio sudo_ ou _acesso sudo_. O termo _sudo_ significa "superusuário faz" ou "usuário substituto faz".

Para usar um privilégio sudo, use o comando `sudo`. É necessário definir o comando `sudo` antes do comando que exige privilégios escalonados. O comando `sudo` solicita uma senha, que geralmente é a senha do usuário comum.

No exemplo a seguir, você usa o comando `sudo` para alterar apenas o proprietário do grupo do diretório `/Finance/Sales` para o grupo `sales-team`. Como sua conta de usuário tem privilégio sudo, você usa o comando `sudo` para representar o usuário `root`. Caso contrário, não será possível alterar as permissões no diretório porque você não é o proprietário.

![[Pasted image 20240614164150.png]]

Você pode usar o comando `sudo -l` para listar seus privilégios sudo.

![[Pasted image 20240614164203.png]]

Alterar a propriedade de arquivos e diretórios é especialmente útil quando você usa privilégios sudo para manipular arquivos. Por exemplo, se você usar privilégios sudo para copiar um diretório, o proprietário do diretório será o usuário `root`. Talvez você queira alterar o proprietário do diretório para sua conta de usuário comum. Nesses casos, você pode usar o comando `chown` com a opção `-R` para atualizar recursivamente o proprietário de todo o conteúdo do diretório.