#cyber 
# Autorização

A autorização controla o que um usuário pode e não pode fazer na rede após a autenticação com sucesso. Depois que um usuário prova sua identidade, o sistema verifica quais recursos de rede o usuário pode acessar e o que pode fazer com os recursos.

## Quando implementar a autorização

A autorização usa um conjunto de atributos que descreve o acesso do usuário à rede para responder à pergunta: "Quais privilégios de leitura, cópia, edição, criação e exclusão esse usuário tem?"

O sistema compara esses atributos com as informações contidas no banco de dados de autenticação, determina um conjunto de restrições para aquele usuário e o entrega ao dispositivo local onde o usuário está conectado.

A autorização é automática e não exige que os usuários executem etapas adicionais após a autenticação. Os administradores do sistema configuraram a rede para implementar a autorização imediatamente após a autenticação do usuário.

## Usando a autorização

Definir as regras de autorização é a primeira etapa no controle de acesso. Uma política de autorização estabelece essas regras.

Uma política de associação baseada em grupo define a autorização com base nos membros de um grupo específico. Todos os funcionários de uma empresa podem ter um cartão de furto, por exemplo, que fornece acesso às instalações, mas pode não permitir o acesso a uma sala do servidor. Pode ser que apenas funcionários de nível sênior e membros da equipe de TI possam acessar a sala do servidor com seus cartões de furto.

Uma política de nível de autoridade define as permissões de acesso com base na posição de um funcionário na organização.




