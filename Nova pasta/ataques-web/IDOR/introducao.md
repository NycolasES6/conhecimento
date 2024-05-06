# Introdução ao IDOR

Vulnerabilidades  `Insecure Direct Object References (IDOR)` estão entre as vulnerabilidades da web mais comuns e podem impactar significativamente o aplicativo da web vulnerável. As vulnerabilidades IDOR ocorrem quando uma aplicação web expõe uma referência direta a um objeto, como um arquivo ou recurso de banco de dados, que o usuário final pode controlar diretamente para obter acesso a outros objetos semelhantes. Se algum usuário puder acessar qualquer recurso devido à falta de um sistema sólido de controle de acesso, o sistema será considerado vulnerável.

Construir um sistema de controle de acesso sólido é muito desafiador, e é por isso que as vulnerabilidades do IDOR são generalizadas. Além disso, automatizar o processo de identificação de fragilidades nos sistemas de controle de acesso também é bastante difícil, o que pode fazer com que essas vulnerabilidades fiquem sem identificação até chegarem à produção.

Por exemplo, se os usuários solicitarem acesso a um arquivo que carregaram recentemente, eles poderão receber um link para ele, como ( `download.php?file_id=123`). Então, como o link faz referência direta ao arquivo com ( `file_id=123`), o que aconteceria se tentássemos acessar outro arquivo (que pode não nos pertencer) com ( `download.php?file_id=124`)? Se a aplicação web não tiver um sistema de controle de acesso adequado no back-end, poderemos acessar qualquer arquivo enviando uma solicitação com sua extensão `file_id`. Em muitos casos, podemos descobrir que o `id` é facilmente adivinhado, tornando possível recuperar muitos arquivos ou recursos aos quais não deveríamos ter acesso com base em nossas permissões.

O que torna uma vulnerabilidade IDOR
------------------------------------

Apenas expor uma referência direta a um objeto ou recurso interno não é uma vulnerabilidade em si. No entanto, isso pode tornar possível explorar outra vulnerabilidade: um arquivo com sistema de controle de acesso fraco. Muitos aplicativos da web restringem o acesso dos usuários aos recursos, restringindo-os de acessar as páginas, funções e APIs que podem recuperar esses recursos. No entanto, o que aconteceria se um usuário de alguma forma conseguisse acesso a essas páginas (por exemplo, através de um link compartilhado/adivinhado)? Eles ainda conseguiriam acessar os mesmos recursos simplesmente tendo o link para acessá-los? Se o aplicativo da web não tivesse um sistema de controle de acesso no back-end que comparasse a autenticação do usuário com a lista de acesso do recurso, eles poderiam conseguir.

Existem muitas maneiras de implementar um sistema de controle de acesso sólido para aplicações web, como ter um sistema de controle de acesso baseado em funções ( [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) ). A principal lição é essa , um IDOR existe principalmente pela falta de controle de acesso no back-end. Se um usuário tivesse referências diretas a objetos em uma aplicação web sem controle de acesso, seria possível que invasores visualizassem ou modificassem os dados de outros usuários.




