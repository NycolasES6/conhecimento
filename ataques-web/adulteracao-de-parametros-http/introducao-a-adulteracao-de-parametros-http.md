# Introdução ao HTTP Verb Tempering

O protocolo `HTTP`  funciona aceitando vários métodos HTTP como  no início de uma solicitação HTTP. Dependendo da configuração do servidor web, os aplicativos web podem ser programados para aceitar determinados métodos HTTP para suas diversas funcionalidades e executar uma ação específica com base no tipo de solicitação.

Adulteração de método HTTP
-------------------------

Para entender `HTTP Verb Tampering`, devemos primeiro aprender sobre os diferentes métodos aceitos pelo protocolo HTTP. HTTP possui [9 verbos diferentes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) que podem ser aceitos como métodos HTTP por servidores web. Além de `GET`e `POST`, a seguir estão alguns dos verbos HTTP comumente usados:

| Verbo     | Descrição                                                                                           |
|:---------:|:--------------------------------------------------------------------------------------------------- |
| `HEAD`    | Idêntico a uma solicitação GET, mas sua resposta contém apenas o `headers`, sem o corpo da resposta |
| `PUT`     | Grava a carga da solicitação no local especificado                                                  |
| `DELETE`  | Exclui o recurso no local especificado                                                              |
| `OPTIONS` | Mostra diferentes opções aceitas por um servidor web, como verbos HTTP aceitos                      |
| `PATCH`   | Aplicar modificações parciais ao recurso no local especificado                                      |

Como você pode imaginar, alguns dos métodos acima podem executar funcionalidades muito confidenciais, como gravar ( `PUT`) ou excluir ( `DELETE`) arquivos no diretório webroot no servidor back-end. Conforme discutido no módulo [Solicitações Web](https://academy.hackthebox.com/course/preview/web-requests) , se um servidor Web não estiver configurado com segurança para gerenciar esses métodos, podemos usá-los para obter controle sobre o servidor back-end. No entanto, o que torna os ataques de adulteração de verbos HTTP mais comuns (e, portanto, mais críticos) é que eles são causados ​​por uma configuração incorreta no servidor web back-end ou no aplicativo web, qualquer um dos quais pode causar a vulnerabilidade.

Configurações inseguras
-----------------------

Configurações inseguras de servidor web causam o primeiro tipo de vulnerabilidade de adulteração de verbos HTTP. A configuração de autenticação de um servidor web pode ser limitada a métodos HTTP específicos, o que deixaria alguns métodos HTTP acessíveis sem autenticação. Por exemplo, um administrador de sistema pode usar a seguinte configuração para exigir autenticação em uma página web específica:

```xml
<Limit GET POST>
    Require valid-user
</Limit>
```

Como podemos ver, mesmo que a configuração especifique as solicitações `Get` e `POST`para o método de autenticação, um invasor ainda pode usar um método HTTP diferente (como `HEAD`) para ignorar completamente esse mecanismo de autenticação, como veremos na próxima seção. Isso eventualmente leva a um desvio de autenticação e permite que invasores acessem páginas da web e domínios aos quais não deveriam ter acesso.

Codificação Insegura
--------------------

Práticas de codificação inseguras causam outro tipo de vulnerabilidade de adulteração de verbo HTTP (embora alguns possam não considerar isso adulteração de verbo). Isso pode ocorrer quando um desenvolvedor web aplica filtros específicos para mitigar vulnerabilidades específicas, sem cobrir todos os métodos HTTP com esse filtro. Por exemplo, se uma página da Web for considerada vulnerável a uma vulnerabilidade de injeção de SQL e o desenvolvedor back-end atenuar a vulnerabilidade de injeção de SQL aplicando os seguintes filtros de sanitização de entrada:

```php
$pattern = "/^[A-Za-z\s]+$/";

if(preg_match($pattern, $_GET["code"])) {
    $query = "Select * from ports where port_code like '%" . $_REQUEST["code"] . "%'";
    ...SNIP...
}
```

Podemos observar que o filtro de sanitização está sendo testado apenas no parâmetro `GET`. Se as solicitações GET não contiverem caracteres inválidos, a consulta será executada. Porém, quando a consulta é executada, os parâmetros `$_REQUEST["code"]`estão sendo utilizados, que também podem conter o parâmetro `POST` , Levando a uma inconsistência nos parâmetros HTTP. Nesse caso, um invasor pode usar uma solicitação `POST` para realizar injeção de SQL, caso em que os parâmetros `GET` estariam vazios (não incluiriam caracteres inválidos). A solicitação passaria pelo filtro de segurança, o que tornaria a função ainda vulnerável ao SQL Injection.

Embora ambas as vulnerabilidades acima sejam encontradas em público, a segunda é muito mais comum, pois é devido a erros cometidos na codificação, enquanto a primeira é geralmente evitada por configurações seguras de servidores web, como a documentação frequentemente adverte contra isso. Nas próximas seções, veremos exemplos de ambos os tipos e como explorá-los.
















































































































































