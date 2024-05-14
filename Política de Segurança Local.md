#Windows #SO 

# Política de Segurança Local

Uma política de segurança é um conjunto de objetivos que garante a segurança de uma rede, dos dados e dos sistemas de computador em uma organização. A política de segurança é um documento em constante desenvolvimento, baseado em mudanças na tecnologia, nos negócios e nas necessidades dos funcionários.

Na maioria das redes que usam computadores Windows, o Active Directory é configurado com domínios em um servidor Windows. Computadores Windows ingressam no domínio. O administrador configura uma Política de Segurança de Domínio que se aplica a todos os computadores que ingressam no domínio. As políticas de conta são definidas automaticamente quando um usuário efetua login em um computador que é membro de um domínio. A Política de Segurança Local do Windows, mostrada na figura, pode ser usada para computadores autônomos que não fazem parte de um domínio do Active Directory. Para abrir o aplicativo Política de Segurança Local, procure Política de Segurança Local e clique no programa.

![[Pasted image 20240514151559.jpg]]

As diretrizes de senha são um componente importante de uma política de segurança. Qualquer usuário que fizer logon em um computador ou se conectar a um recurso de rede deve ter uma senha. As senhas ajudam a evitar roubo de dados e atos mal-intencionados. As senhas também ajudam a confirmar se o registro de eventos é válido, garantindo que o usuário seja quem diz ser. Na Política de Segurança Local, a Política de Palavra-passe é encontrada em Políticas de Conta e define os critérios para as palavras-passe para todos os utilizadores no computador local.

Use a Diretiva de Bloqueio de Conta em Diretivas de Conta, para impedir tentativas de login por força bruta. Por exemplo, você pode definir a política para permitir que o usuário insira um nome de usuário e / ou senha incorretos cinco vezes. Após cinco tentativas, a conta é bloqueada por 30 minutos. Depois de 30 minutos, o número de tentativas é redefinido para zero e o usuário pode tentar entrar novamente.

É importante garantir que os computadores estejam seguros, quando os usuários estiverem ausentes. Uma política de segurança deve conter uma regra sobre a necessidade de se bloquear um computador, quando a proteção de tela for iniciada. Isso garantirá que, depois de um curto período de tempo longe do computador, a proteção de tela será iniciada e o computador não poderá ser usado, até que o usuário faça login novamente.

Se a política de segurança local em cada computador autônomo for a mesma, use o recurso Exportar política. Salve a diretiva com um nome, como workstation.inf. Copie o arquivo de política para uma mídia externa ou unidade de rede para usar em outros computadores independentes. Isso é particularmente útil quando o administrador precisa configurar diretivas locais abrangentes para direitos de usuário e opções de segurança.

O miniaplicativo Diretiva de Segurança Local contém muitas outras configurações de segurança que se aplicam especificamente ao computador local. Você pode configurar Direitos de Usuário, Regras de Firewall e até mesmo a capacidade de restringir os arquivos que os usuários ou grupos têm permissão para executar com o AppLocker.



























