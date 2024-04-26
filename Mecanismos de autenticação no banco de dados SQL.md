[[MSSQL]] suporta dois modos de autenticação, o que significa que os usuários podem ser criados no [[Windows]] ou no [[SQL Server]]:

| **Tipo de Autenticação**      | **Descrição**                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Windows authentication mode` | Esse é o padrão, geralmente chamado de segurança integrada porque o modelo de segurança do SQL Server está totalmente integrado ao Windows/Active Directory. Contas específicas de usuários e grupos do Windows são confiáveis ​​para efetuar login no SQL Server. Os usuários do Windows que já foram autenticados não precisam apresentar credenciais adicionais. |
| `Mixed mode`                  | O modo misto oferece suporte à autenticação por contas do Windows/Active Directory e SQL Server. Os pares de nome de usuário e senha são mantidos no SQL Server.                                                                                                                                                                                                    |

[[MySQL]] também suporta diferentes métodos de autenticação , como nome de usuário e senha, bem como autenticação do Windows (é necessário um plugin). Além disso, os administradores podem escolher um modo de autenticação por vários motivos, incluindo compatibilidade, segurança, usabilidade e muito mais. No entanto, dependendo do método implementado, podem ocorrer configurações incorretas.

No passado, havia uma vulnerabilidade CVE-2012-2122 em servidores MySQL 5.6.x, entre outros, que nos permitia ignorar a autenticação usando repetidamente a mesma senha incorreta para uma determinada conta porque a vulnerabilidade de ataque de temporização existia na forma como o MySQL tratou tentativas de autenticação.

Neste ataque de temporização, o MySQL tenta repetidamente se autenticar em um servidor e mede o tempo que leva para o servidor responder a cada tentativa. Medindo o tempo que o servidor leva para responder, podemos determinar quando a senha correta foi encontrada, mesmo que o servidor não indique sucesso ou falha.

No caso do MySQL 5.6.x, o servidor demora mais para responder a uma senha incorreta do que a uma senha correta. Assim, se tentarmos repetidamente autenticar com a mesma senha incorreta, eventualmente receberemos uma resposta indicando que a senha correta foi encontrada, mesmo que não tenha sido.

## Configurações incorretas

A autenticação mal configurada no SQL Server pode nos permitir acessar o serviço sem credenciais se o acesso anônimo estiver habilitado, um usuário sem senha estiver configurado ou qualquer usuário, grupo ou máquina tiver permissão para acessar o SQL Server.

## Privilégios

Dependendo dos privilégios do usuário, poderemos realizar diferentes ações dentro de um SQL Server, como:

- Ler ou alterar o conteúdo de um banco de dados
    
- Ler ou alterar a configuração do servidor
    
- Executar comandos
    
- Ler arquivos locais
    
- Comunique-se com outros bancos de dados
    
- Capture o hash do sistema local
    
- Personificar usuários existentes
    
- Obtenha acesso a outras redes











