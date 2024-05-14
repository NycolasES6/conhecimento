#SO #Windows 
# Usuários e Domínios Locais

Quando inicia um novo computador pela primeira vez ou instala o Windows, será pedido para criar uma conta de usuário. Isso é conhecido como um usuário local. Essa conta conterá todas as configurações de personalização, permissões de acesso, locais de arquivos e muitos outros dados específicos do usuário. Há também duas outras contas presentes, o convidado e o administrador. Ambas as contas são desabilitadas por padrão.

Como prática recomendada de segurança, não habilite a conta Administrador e não conceda privilégios administrativos aos usuários padrão. Se um usuário precisar executar qualquer função que exija privilégios administrativos, o sistema solicitará a senha de Administrador e permitirá que somente essa tarefa seja executada como administrador. Exigir a senha de administrador protege o computador impedindo que qualquer software não autorizado instale, execute ou acesse arquivos.

A conta Convidados não deve ser ativada. A conta de convidado não tem uma senha associada a ela porque é criada quando um computador vai ser usado por muitas pessoas diferentes que não têm contas no computador. Cada vez que a conta de convidado faz logon, um ambiente padrão é fornecido a eles com privilégios limitados.

Para facilitar a administração de usuários, o Windows usa grupos. Um grupo terá um nome e um conjunto específico de permissões associadas a ele. Quando um usuário é colocado em um grupo, as permissões desse grupo são dadas a esse usuário. Um usuário pode ser colocado em vários grupos para ser fornecido com muitas permissões diferentes. Quando as permissões se sobrepõem, certas permissões, como “negar explicitamente”, substituirão a permissão fornecida por um grupo diferente. Há muitos grupos de usuários diferentes incorporados no Windows que são usados para tarefas específicas. Por exemplo, o grupo Usuários do Log de Desempenho permite que os membros agendem o log de contadores de desempenho e coletem logs localmente ou remotamente. Os usuários e grupos locais são gerenciados com o miniaplicativo do painel de controle lusrmgr.msc, conforme mostrado na figura.

![[Pasted image 20240514125319.jpg]]

Além dos grupos, o Windows também pode usar domínios para definir permissões. Um domínio é um tipo de serviço de rede onde todos os usuários, grupos, computadores, periféricos e configurações de segurança são armazenados e controlados por um banco de dados. Este banco de dados é armazenado em computadores especiais ou grupos de computadores chamados controladores de domínio (DCs). Cada utilizador e computador no domínio tem de autenticar contra o controlador de domínio para iniciar sessão e acessar os recursos de rede. As configurações de segurança para cada usuário e cada computador são definidas pelo controlador de domínio para cada sessão. Qualquer configuração fornecida pelo controlador de domínio padrão para o computador local ou configuração de conta de usuário.






















