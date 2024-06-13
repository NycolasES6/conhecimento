#cyber 
# Operação AAA

Uma rede deve ser projetada para controlar quem tem permissão para se conectar a ela e o que eles têm permissão para fazer quando estão conectados. Estes requisitos de design são identificados na política de segurança de rede. A política especifica como administradores de rede, usuários corporativos, usuários remotos, parceiros de negócios e clientes acessam recursos de rede. A política de segurança de rede também pode exigir a implementação de um sistema de contabilidade que rastreia quem iniciou sessão e quando e o que fizeram durante a sessão iniciada. Alguns regulamentos de conformidade podem especificar que o acesso deve ser registrado e os logs mantidos por um determinado período de tempo.

O protocolo AAA (Authentication, Authorization and Accounting) fornece a estrutura necessária para habilitar a segurança de acesso escalável.

As três funções de segurança independentes fornecidas pela estrutura de arquitetura AAA.

### Autenticação

- Os usuários e administradores devem provar quem são.
- A autenticação pode ser estabelecida usando combinações de nome de usuário e senha, perguntas e respostas de desafio, tokens e outros métodos.
- A autenticação AAA fornece uma maneira centralizada de controlar o acesso à rede.

### Autorização

- Após a autenticação do usuário, os serviços de autorização determinam quais recursos o usuário pode acessar e quais operações ele tem permissão para executar.
- Um exemplo é "O usuário 'aluno' pode acessar o servidor host XYZ usando apenas SSH".

### Accounting (Contabilidade)

- O accounting registra o que o usuário faz, incluindo o que é acessado, a quantidade de tempo em que o recurso é acessado e todas as alterações efetuadas.
- O accounting rastreia como os recursos de rede são usados.
- Um exemplo é "O usuário 'aluno' acessou o servidor host XYZ usando SSH por 15 minutos".

---

Esse conceito é semelhante ao uso de um cartão de crédito, conforme indicado na figura. O cartão de crédito identifica quem pode utilizá-lo, estipula um limite de uso e mantém o controle dos itens comprados pelo usuário, como mostrado na figura.

![[Pasted image 20240613134108.png]]