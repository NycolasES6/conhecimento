#cyber #anki 
# Modelos de controle de acesso

Uma organização deve implementar controles de acesso adequados para proteger seus recursos de rede, recursos do sistema de informações e informações.

Um analista de segurança deve entender os diferentes modelos básicos de controle de acesso para ter uma melhor compreensão de como os invasores podem quebrar os controles de acesso.

A tabela lista vários tipos de métodos de controle de acesso.

### Discretionary access control (DAC)

- Este é o modelo menos restritivo e permite que os usuários controlem o acesso aos seus dados como proprietários desses dados.
- O DAC pode usar ACLs ou outros métodos para especificar quais usuários ou grupos de usuários têm acesso às informações.

### Controle de acesso obrigatório (MAC)

- Isso aplica o controle de acesso mais rigoroso e é normalmente usado em aplicações militares ou de missão crítica.
- Ele atribui rótulos de nível de segurança às informações e permite que os usuários tenham acesso com base em sua autorização de nível de segurança.

### Controle de acesso baseado em funções (RBAC)

- As decisões de acesso são baseadas nas funções e responsabilidades de um indivíduo dentro da organização.
- Diferentes funções recebem privilégios de segurança e indivíduos são atribuídos ao perfil RBAC para a função.
- As funções podem incluir diferentes posições, classificações de cargo ou grupos de classificações de emprego.
- Também conhecido como um tipo de **controle de acesso não discricionário.**

### Controle de acesso baseado em atributos (ABAC)

O ABAC permite o acesso com base em atributos do objeto (recurso) a ser acessado, o sujeito (usuário) acessando o recurso e fatores ambientais sobre como o objeto deve ser acessado, como a hora do dia.

### Controle de acesso baseado em regras (RBAC)

- A equipe de segurança de rede especifica conjuntos de regras ou condições associadas ao acesso a dados ou sistemas.
- Essas regras podem especificar endereços IP permitidos ou negados, ou determinados protocolos e outras condições.
- Também conhecido como **RBAC Baseado em Regras.**

### Controle de acesso baseado em tempo (TAC)

TAC Permite o acesso a recursos de rede com base na hora e no dia.

---

Outro modelo de controle de acesso é o princípio do privilégio mínimo, que especifica uma abordagem limitada, conforme necessário, para conceder direitos de acesso ao usuário e ao processo a informações e ferramentas específicas. O princípio do privilégio mínimo afirma que os usuários devem receber a quantidade mínima de acesso necessária para desempenhar sua função de trabalho.

Uma exploração comum é conhecida como escalação de privilégios. Nesta exploração, vulnerabilidades em servidores ou sistemas de controle de acesso são exploradas para conceder a um usuário não autorizado, ou processo de software, níveis de privilégio mais altos do que deveriam ter. Depois que o privilégio é concedido, o agente de ameaça pode acessar informações confidenciais ou assumir o controle de um sistema.











