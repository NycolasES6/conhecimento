#cyber 
# Políticas de conta no Windows

Na maioria das redes que usam computadores Windows, um administrador configura o Active Directory com domínios em um servidor Windows. Os computadores Windows que ingressam no domínio se tornam membros do domínio.

O administrador configura uma **política de segurança de domínio** que se aplica a todos os computadores que ingressam no domínio. Por exemplo, as políticas de conta são definidas automaticamente quando um usuário faz login no Windows.

Quando um computador não faz parte de um domínio do Active Directory, o usuário configura políticas por meio da Política de Segurança Local do Windows Em todas as versões do Windows exceto na Home Edition, digite secpol. msc no comando Executar para abrir a ferramenta de Política de Segurança Local.

## Políticas de senhas

Um administrador pode configurar políticas de conta de usuário, como políticas de senha e políticas de bloqueio.

No exemplo mostrado, os usuários devem alterar suas senhas a cada 90 dias e usar cada nova senha por pelo menos um dia. As senhas devem conter oito caracteres e três das quatro categorias a seguir: letras maiúsculas, letras minúsculas, números e símbolos. Por último, o usuário pode reutilizar uma senha somente depois de 24 senhas exclusivas. 

Este é apenas um exemplo; É possível definir políticas de senha diferentes, dependendo dos requisitos e das necessidades da empresa.

## Política de bloqueio de conta

Uma política de bloqueio de conta bloqueia uma conta por um período definido quando ocorrem muitas tentativas de login incorretas.

Por exemplo, a política mostrada aqui permite que o usuário digite o nome de usuário e/ou senha errados cinco vezes. Depois de cinco tentativas, a conta é bloqueada por 30 minutos. Depois de 30 minutos, o número de tentativas é redefinido para zero e o usuário pode tentar entrar novamente.

## Política de auditoria

Mais configurações de segurança estão disponíveis selecionando a pasta 'políticas locais' no Windows. Uma política de auditoria cria um arquivo de log de segurança usado para rastrear os seguintes eventos:

- Eventos de login da conta.
- Gestão de contas de auditoria.
- Acesso ao serviço de diretório.
- Acesso a objetos.
- Mudanças de política.
- Privilégio de utilização.
- Acompanhamento de processos.
- Eventos do sistema.



