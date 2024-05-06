# Prevenção de adulteração de verbos

Depois de ver algumas maneiras de explorar vulnerabilidades de adulteração de verbos, vamos ver como podemos nos proteger contra esses tipos de ataques, evitando a adulteração de verbos. Configurações inseguras e codificação insegura são o que geralmente introduz vulnerabilidades de adulteração de verbos. Nesta seção, veremos exemplos de códigos e configurações vulneráveis ​​e discutiremos como podemos corrigi-los.

## Configuração insegura

Vulnerabilidades de adulteração de verbos HTTP podem ocorrer na maioria dos servidores web modernos, incluindo Apache, Tomcat, e ASP.NET. A vulnerabilidade geralmente acontece quando limitamos a autorização de uma página a um determinado conjunto de verbos/métodos HTTP, o que deixa os demais métodos restantes desprotegidos.

A seguir está um exemplo de configuração vulnerável para um servidor web Apache, que está localizado no arquivo de configuração do site (por exemplo, `000-default.conf`) ou em um arquivo `.htaccess` de configuração de página web:

```xml
<security-constraint>
    <web-resource-collection>
        <url-pattern>/admin/*</url-pattern>
        <http-method>GET</http-method>
    </web-resource-collection>
    <auth-constraint>
        <role-name>admin</role-name>
    </auth-constraint>
</security-constraint>
```

Podemos perceber que a autorização está sendo limitada apenas ao método `GET` com `http-method`, o que deixa a página acessível através de outros métodos HTTP.

Por fim, segue um exemplo de configuração `ASP.NET` encontrada no arquivo `web.config` de uma aplicação web:

```xml
<system.web>
    <authorization>
        <allow verbs="GET" roles="admin">
            <deny verbs="GET" users="*">
        </deny>
        </allow>
    </authorization>
</system.web>
```

Outra vez, os escopos `allow` e `deny` estão limitando o método `GET`, o que deixa a aplicação web acessível através de outros métodos HTTP.

Os exemplos acima mostram que não é seguro limitar a configuração de autorização a um verbo HTTP específico. É por isso que devemos sempre evitar restringir a autorização a um método HTTP específico e sempre permitir/negar todos os verbos e métodos HTTP.

Se quisermos especificar um único método, podemos usar palavras-chave seguras, como `LimitExcept` no Apache, `http-method-omission` no Tomcat e `add`/`remove` no ASP.NET, que cobrem todos os verbos, exceto os especificados.

Finalmente, para evitar ataques semelhantes, devemos geralmente, considere desabilitar/negar todas requisições `HEAD` a menos que seja especificamente exigido pela aplicação web.

## Codificação insegura

Embora identificar e corrigir configurações de servidores web inseguros seja relativamente fácil, fazer o mesmo para códigos inseguros é muito mais desafiador. Isso ocorre porque, para identificar essa vulnerabilidade no código, precisamos encontrar inconsistências no uso de parâmetros HTTP entre funções, pois em alguns casos isso pode levar a funcionalidades e filtros desprotegidos.

Vamos considerar o seguinte PHPcódigo do nosso exercício `File Manager`:

```php
if (isset($_REQUEST['filename'])) {
    if (!preg_match('/[^A-Za-z0-9. _-]/', $_POST['filename'])) {
        system("touch " . $_REQUEST['filename']);
    } else {
        echo "Malicious Request Denied!";
    }
}
```

Se estivéssemos considerando apenas as vulnerabilidades de injeção de comando, diríamos que isso está codificado com segurança. A função `preg_match` procura corretamente caracteres especiais indesejados e não permite que a entrada entre no comando se algum caractere especial for encontrado. No entanto, o erro fatal cometido neste caso não é devido às injeções de comando, mas sim ao arquivo de uso inconsistente de métodos HTTP.

Vemos que o filtro `preg_match` verifica apenas caracteres especiais em parâmetros `POST` com `$_POST['filename']`. No entanto, o comando final `system` usa a variável `$_REQUEST['filename']`, que abrange os parâmetros `GET` e `POST`. Portanto, na seção anterior, quando estávamos enviando nossa entrada maliciosa por meio de uma solicitação `GET`, ela não foi interrompida pela função `preg_match`, pois os parâmetros `POST` estavam vazios e, portanto, não continham nenhum caractere especial. Assim que chegamos à função `system`, entretanto, ela usou todos os parâmetros encontrados na solicitação, e nossos parâmetros `GET` foram usados ​​no comando, eventualmente levando à Injeção de Comando.

Este exemplo básico nos mostra como pequenas inconsistências no uso de métodos HTTP podem levar a vulnerabilidades críticas. Em um aplicativo Web de produção, esses tipos de vulnerabilidades não serão tão óbvios. Eles provavelmente estariam espalhados por todo o aplicativo da web e não em duas linhas consecutivas como temos aqui. Em vez disso, o aplicativo da web provavelmente terá uma função especial para verificar injeções e uma função diferente para criar arquivos. Essa separação de código torna difícil detectar esses tipos de inconsistências e, portanto, elas podem sobreviver à produção.

Para evitar vulnerabilidades de adulteração de verbos HTTP em nosso código devemos ser consistentes em nosso uso com métodos HTTP e garantir que o mesmo método seja sempre usado para qualquer funcionalidade específica no aplicativo da web. É sempre aconselhável expandir o escopo de teste em filtros de segurança e testar todos os parâmetros da solicitação. Isso pode ser feito com as seguintes funções e variáveis:

| Linguagem | Função |
| --- | --- |
| PHP | `$_REQUEST['param']` |
| Java | `request.getParameter('param')` |
| C# | `Request['param']` |

Se nosso escopo em funções relacionadas à segurança abranger todos os métodos, devemos evitar tais vulnerabilidades ou ignorar filtros.
