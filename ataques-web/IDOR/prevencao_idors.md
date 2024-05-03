# Prevenção de IDORs

Aprendemos várias maneiras de identificar e explorar vulnerabilidades IDOR em páginas da web, funções da web e chamadas de API. Até agora, já deveríamos ter entendido que as vulnerabilidades do IDOR são causadas principalmente por controle de acesso inadequado nos servidores back-end. Para evitar tais vulnerabilidades, primeiro temos que construir um sistema de controle de acesso em nível de objeto e depois usar referências seguras para nossos objetos ao armazená-los e chamá-los.

## Controle de acesso em nível de objeto

Um sistema de controle de acesso deve estar no centro de qualquer aplicação web, pois pode afetar todo o seu design e estrutura. Para controlar adequadamente cada área da aplicação web, seu design deve suportar a segmentação de funções e permissões de forma centralizada. No entanto, o Controlo de Acessos é um tema vasto, pelo que nos concentraremos apenas no seu papel nas vulnerabilidades IDOR, representadas nos mecanismos de controlo de acessos do `Object-Level`.

As funções e permissões dos usuários são uma parte vital de qualquer sistema de controle de acesso, que é totalmente realizado em um sistema de controle de acesso baseado em funções (RBAC). Para evitar a exploração das vulnerabilidades do IDOR, devemos mapear o RBAC para todos os objetos e recursos. O servidor back-end pode permitir ou negar todas as solicitações, dependendo se a função do solicitante tem privilégios suficientes para acessar o objeto ou o recurso.

Depois que um RBAC for implementado, cada usuário receberá uma função com determinados privilégios. A cada solicitação feita pelo usuário, suas funções e privilégios seriam testados para verificar se ele tem acesso ao objeto que está solicitando. Eles só teriam permissão para acessá-lo se tivessem o direito de fazê-lo.

Há muitas maneiras de implementar um sistema RBAC e mapeá-lo para os objetos e recursos da aplicação web, e projetá-lo no centro da estrutura da aplicação web é uma arte a ser aperfeiçoada. A seguir está um exemplo de código de como um aplicativo da web pode comparar funções de usuário a objetos para permitir ou negar controle de acesso:

```javascript
match /api/profile/{userId} {
    allow read, write: if user.isAuth == true
    && (user.uid == userId || user.roles == 'admin');
}
```

Embora o principal problema do IDOR esteja no controle de acesso quebrado (Inseguro), ter acesso a referências diretas a objetos (Referência Direta de Objeto) torna possível enumerar e explorar essas vulnerabilidades de controle de acesso. Ainda podemos usar referências diretas, mas apenas se tivermos um sistema sólido de controle de acesso implementado.

Mesmo depois de construir um sistema de controle de acesso sólido, nunca devemos usar referências de objetos em texto não criptografado ou padrões simples (por exemplo, uid=1). Devemos sempre usar referências fortes e únicas, como hashes salgados ou UUIDs. Por exemplo, podemos usar UUID V4 para gerar um ID fortemente aleatório para qualquer elemento, que se parece com (89c9b29b-d19f-4515-b2dd-abb6e693eb20). Então, podemos mapear esse UUID para o objeto ao qual ele está referenciando no banco de dados back-end e sempre que esse UUID for chamado, o banco de dados back-end saberá qual objeto retornar. O exemplo de código PHP a seguir nos mostra como isso pode funcionar:

```php
$uid = intval($_REQUEST['uid']);
$query = "SELECT url FROM documents where uid=" . $uid;
$result = mysqli_query($conn, $query);
$row = mysqli_fetch_array($result));
echo "<a href='" . $row['url'] . "' target='_blank'></a>";
```

Além disso, como vimos anteriormente no módulo, nunca devemos calcular hashes no front-end. Devemos gerá-los quando um objeto for criado e armazená-los no banco de dados back-end. Então, devemos criar mapas de banco de dados para permitir rápida referência cruzada de objetos e referências.

Finalmente, devemos observar que o uso de UUIDs pode permitir que as vulnerabilidades do IDOR passem despercebidas, pois torna mais desafiador testar as vulnerabilidades do IDOR. É por isso que a referência forte a objetos é sempre o segundo passo após a implementação de um sistema de controle de acesso forte. Além disso, algumas das técnicas que aprendemos neste módulo funcionariam mesmo com referências únicas se o sistema de controle de acesso fosse quebrado, como repetir a solicitação de um usuário com a sessão de outro usuário, como vimos anteriormente.

Se implementarmos ambos os mecanismos de segurança, estaremos relativamente seguros contra as vulnerabilidades do IDOR.









