# Introdução ao XXE

As vulnerabilidades de injeção de entidade externa XML (XXE) ocorrem quando os dados XML são obtidos de uma entrada controlada pelo usuário sem higienizá-los adequadamente ou analisá-los com segurança, o que pode nos permitir usar recursos XML para executar ações maliciosas. As vulnerabilidades XXE podem causar danos consideráveis a uma aplicação web e ao seu servidor back-end, desde a divulgação de ficheiros sensíveis até ao encerramento do servidor back-end, razão pela qual é considerada um dos 10 principais riscos de segurança web pela OWASP.

## XML

Extensible Markup Language (XML) é uma linguagem de marcação comum (semelhante a HTML e SGML) projetada para transferência e armazenamento flexível de dados e documentos em vários tipos de aplicativos. XML não se concentra na exibição de dados, mas principalmente no armazenamento de dados de documentos e na representação de estruturas de dados. Os documentos XML são formados por árvores de elementos, onde cada elemento é essencialmente denotado por uma tag, e o primeiro elemento é chamado de elemento raiz, enquanto os outros elementos são elementos filhos.

Aqui vemos um exemplo básico de um documento XML representando uma estrutura de documento de e-mail:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<email>
  <date>01-01-2022</date>
  <time>10:00 am UTC</time>
  <sender>john@inlanefreight.com</sender>
  <recipients>
    <to>HR@inlanefreight.com</to>
    <cc>
        <to>billing@inlanefreight.com</to>
        <to>payslips@inlanefreight.com</to>
    </cc>
  </recipients>
  <body>
  Hello,
      Kindly share with me the invoice for the payment made on January 1, 2022.
  Regards,
  John
  </body> 
</email>
```
O exemplo acima mostra alguns dos elementos-chave de um documento XML, como:

| Chave | Definição | Exemplo |
| - | - | - |
|Tag | As chaves de um documento XML, geralmente agrupadas com caracteres ( </ ).> | ``<date>`` |
|Entity | Variáveis ​​XML, geralmente agrupadas com caracteres ( &/; ). | ``&lt;`` |
|Element | O elemento raiz ou qualquer um de seus elementos filhos e seu valor são armazenados entre uma tag inicial e uma tag final. | ``<date>01-01-2022</date>`` |
|Attribute | Especificações opcionais para qualquer elemento armazenado nas tags, que podem ser utilizadas pelo analisador XML. | ``version="1.0"/encoding="UTF-8"`` |
| Declaration | Geralmente a primeira linha de um documento XML e define a versão XML e a codificação a ser usada ao analisá-lo. | ``<?xml version="1.0" encoding="UTF-8"?>`` |

Além disso, alguns caracteres são usados ​​como parte de uma estrutura de documento XML, como ``<``,`` >``, ``&``, ou ``"``. Portanto, se precisarmos usá-los em um documento XML, devemos substituí-los pelas referências de entidade correspondentes (por exemplo, &lt; , &gt;, &amp;, &quot;). Finalmente, podemos escrever comentários em documentos XML entre ``<!--`` e ``-->``, semelhante a documentos HTML.

## DTD XML

XML Document Type Definition (DTD)permite a validação de um documento XML em relação a uma estrutura de documento predefinida. A estrutura pré-definida do documento pode ser definida no próprio documento ou em um arquivo externo. A seguir está um exemplo de DTD para o documento XML que vimos anteriormente:

```xml
<!DOCTYPE email [
  <!ELEMENT email (date, time, sender, recipients, body)>
  <!ELEMENT recipients (to, cc?)>
  <!ELEMENT cc (to*)>
  <!ELEMENT date (#PCDATA)>
  <!ELEMENT time (#PCDATA)>
  <!ELEMENT sender (#PCDATA)>
  <!ELEMENT to  (#PCDATA)>
  <!ELEMENT body (#PCDATA)>
]>
```

Como podemos ver, o DTD está declarando o elemento raiz email com a declaração do tipo ELEMENT e então denotando seus elementos filhos. Depois disso, cada um dos elementos filhos também é declarado, onde alguns deles também possuem elementos filhos, enquanto outros podem conter apenas dados brutos (conforme indicado por PCDATA).

A DTD acima pode ser colocada dentro do próprio documento XML, logo após a Declaração XML na primeira linha. Caso contrário, ele pode ser armazenado em um arquivo externo (por exemplo, email.dtd) e depois referenciado no documento XML com a palavra-chave SYSTEM, como segue:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email SYSTEM "email.dtd">
```

Também é possível referenciar um DTD através de uma URL, como segue:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email SYSTEM "http://inlanefreight.com/email.dtd">
```

Isso é relativamente semelhante ao modo como os documentos HTML definem e fazem referência a scripts JavaScript e CSS.

## Entidades XML

Também podemos definir entidades personalizadas (ou seja, variáveis ​​XML) em DTDs XML, para permitir a refatoração de variáveis ​​e reduzir dados repetitivos. Isso pode ser feito com o uso da palavra-chave `ENTITY`, que é seguida do nome da entidade e seu valor, conforme segue:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [
  <!ENTITY company "Inlane Freight">
]>
```

Depois de definirmos uma entidade, ela pode ser referenciada em um documento XML entre um e comercial ``&`` e um ponto e vírgula ``;`` (por exemplo, ``&company;``). Sempre que uma entidade for referenciada, ela será substituída pelo seu valor pelo analisador XML. O mais interessante, entretanto, é que podemos fazer referência a Entidades XML Externas com a palavra-chave ``SYSTEM``, que é seguida pelo caminho da entidade externa, como segue:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [
  <!ENTITY company SYSTEM "http://localhost/company.txt">
  <!ENTITY signature SYSTEM "file:///var/www/html/signature.txt">
```

> Nota: Também podemos usar a palavra-chave ``PUBLIC`` em vez de ``SYSTEM`` para carregar recursos externos, que é usada com entidades e padrões declarados publicamente, como um código de idioma (``lang="en"``). Neste módulo, usaremos ``SYSTEM``, mas poderemos usar qualquer um deles na maioria dos casos.

Isso funciona de forma semelhante às entidades XML internas definidas nos documentos. Quando referenciamos uma entidade externa (por exemplo, ``&signature;``), o analisador substituirá a entidade pelo seu valor armazenado no arquivo externo (por exemplo, ``signature.txt``). Quando o arquivo XML é analisado no lado do servidor, em casos como APIs SOAP (XML) ou formulários web, uma entidade pode fazer referência a um arquivo armazenado no servidor back-end, que pode eventualmente ser divulgado para nós quando fizermos referência ao entidade.

Na próxima seção, veremos como podemos usar Entidades XML Externas para ler arquivos locais ou até mesmo realizar mais ações maliciosas.

