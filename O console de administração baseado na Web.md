#Linux 
# O console de administração baseado na Web

No Linux, uma prática recomendada é limitar o acesso de um usuário apenas aos recursos necessários para concluir uma tarefa. Da mesma forma, pode haver cenários em que o acesso a uma máquina seja limitado por motivos de segurança. No entanto, a comunicação HTTP geralmente está habilitada e amplamente disponível.

Nestes cenários, você pode usar o console de administração baseado na web chamado Cockpit. Cockpit é uma ferramenta de administração com módulos para interagir com o sistema subjacente. Cockpit é patrocinado pela Red Hat e é instalado por padrão em muitas distribuições Linux.

O Cockpit usa contas de usuário existentes para autenticar e cria uma sessão como usuário logado. Se você fizer login como um usuário sem privilégios ou se seu usuário não tiver privilégios de escalonamento, algumas tarefas serão restritas, mas você poderá visualizar informações do sistema, atualizar sua senha, instalar aplicativos e assim por diante.

Para fazer login no Cockpit, abra um navegador da web e navegue até o `https://localhost:9090`site. A `localhost`string instrui o navegador da web a procurar o serviço na máquina local e a `:9090`string instrui o navegador da web a procurar o serviço na porta 9090.

O navegador exibe um aviso de certificado porque o Cockpit usa um certificado autoassinado. Confirme a exceção de segurança e autentique usando seu usuário e senha.

![[Pasted image 20240612150748.png]]

Após o login, o Cockpit exibe um painel com informações do sistema.


