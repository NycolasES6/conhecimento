# Identificando IDORs

## Parâmetros de URL e APIS

A primeira etapa para explorar vulnerabilidades IDOR é identificar referências diretas a objetos. Sempre que recebermos um arquivo ou recurso específico, devemos estudar as solicitações HTTP para procurar parâmetros de URL ou APIs com referência de objeto (ex. `?uid=1`ou `?filename=file_1.pdf`). Eles são encontrados principalmente em parâmetros de URL ou APIs, mas também podem ser encontrados em outros cabeçalhos HTTP, como cookies.

Nos casos mais básicos, podemos tentar incrementar os valores das referências do objeto para recuperar outros dados, como ( `?uid=2`) ou ( `?filename=file_2.pdf`). Também podemos usar um aplicativo fuzzing para testar milhares de variações e ver se elas retornam algum dado. Qualquer acesso bem-sucedido a arquivos que não sejam nossos indicaria uma vulnerabilidade IDOR.

## Chamadas AJAX

Também podemos identificar parâmetros ou APIs não utilizados no código front-end na forma de chamadas JavaScript AJAX. Alguns aplicativos da web desenvolvidos em estruturas JavaScript podem colocar todas as chamadas de função no front-end de forma insegura e usar as apropriadas com base na função do usuário.

Por exemplo, se não tivéssemos uma conta de administrador, apenas as funções de nível de usuário seriam usadas, enquanto as funções de administrador seriam desativadas. No entanto, ainda poderemos encontrar as funções administrativas se examinarmos o código JavaScript front-end e identificarmos chamadas AJAX para terminais ou APIs específicos que contêm referências diretas a objetos. Se identificarmos referências diretas a objetos no código JavaScript, poderemos testá-las em busca de vulnerabilidades IDOR.

Isso não é exclusivo das funções administrativas, é claro, mas também pode ser qualquer função ou chamada que não possa ser encontrada por meio do monitoramento de solicitações HTTP. O exemplo a seguir mostra um exemplo básico de uma chamada AJAX:

```js
function changeUserPassword() {
    $.ajax({
        url:"change_password.php",
        type: "post",
        dataType: "json",
        data: {uid: user.uid, password: user.password, is_admin: is_admin},
        success:function(result){
            //
        }
    });
}
```

A função acima nunca pode ser chamada quando usamos o aplicativo da web como um usuário não administrador. Porém, se o localizarmos no código front-end, poderemos testá-lo de diferentes maneiras para ver se podemos chamá-lo para realizar alterações, o que indicaria que ele é vulnerável ao IDOR. Podemos fazer o mesmo com código back-end se tivermos acesso a ele (por exemplo, aplicativos web de código aberto).

## Entenda hash/codificação

Suponha que a referência foi codificada com um codificador comum (por exemplo, `base64`). Nesse caso, poderíamos decodificá-lo e visualizar o texto simples da referência do objeto, alterar seu valor e então codificá-lo novamente para acessar outros dados. Por exemplo, se virmos uma referência como ( `?filename=ZmlsZV8xMjMucGRm`), podemos adivinhar imediatamente que o nome do arquivo está `base64`codificado (a partir de seu conjunto de caracteres), que podemos decodificar para obter a referência do objeto original de ( `file_123.pdf`). Então, podemos tentar codificar uma referência de objeto diferente (por exemplo, `file_124.pdf`) e tentar acessá-la com a referência de objeto codificado ( `?filename=ZmlsZV8xMjQucGRm`), o que pode revelar uma vulnerabilidade IDOR se conseguirmos recuperar quaisquer dados.

Por outro lado, a referência do objeto pode ser hash, como ( `download.php?filename=c81e728d9d4c2f636f067f89cc14862c`). À primeira vista, podemos pensar que esta é uma referência de objeto segura, pois não utiliza nenhum texto simples ou codificação fácil. No entanto, se olharmos o código-fonte, poderemos ver o que está sendo hash antes da chamada da API ser feita:

```javascript
$.ajax({
    url:"download.php",
    type: "post",
    dataType: "json",
    data: {filename: CryptoJS.MD5('file_1.pdf').toString()},
    success:function(result){
        //
    }
});
```

Nesse caso, podemos ver que o código usa the `filename`e hash com `CryptoJS.MD5`, facilitando o cálculo de `filename`para outros arquivos potenciais. Caso contrário, podemos tentar identificar manualmente o algoritmo de hash que está sendo usado (por exemplo, com ferramentas de identificação de hash) e então fazer o hash do nome do arquivo para ver se ele corresponde ao hash usado. Assim que pudermos calcular hashes para outros arquivos, podemos tentar baixá-los, o que pode revelar uma vulnerabilidade IDOR se pudermos baixar arquivos que não nos pertencem.

## Compare funções de usuário

Se quisermos realizar ataques IDOR mais avançados, poderemos precisar registrar vários usuários e comparar suas solicitações HTTP e referências de objetos. Isso pode nos permitir entender como os parâmetros de URL e identificadores exclusivos estão sendo calculados e depois calculá-los para que outros usuários coletem seus dados.

Por exemplo, se tivéssemos acesso a dois usuários diferentes, um deles poderia visualizar seu salário após fazer a seguinte chamada de API:

```json
{
  "attributes" : 
    {
      "type" : "salary",
      "url" : "/services/data/salaries/users/1"
    },
  "Id" : "1",
  "Name" : "User1"

}
```

O segundo usuário pode não ter todos esses parâmetros de API para replicar a chamada e não poderá fazer a mesma chamada que `User1`. No entanto, com esses detalhes em mãos, podemos tentar repetir a mesma chamada de API enquanto estivermos logados para `User2`ver se a aplicação web retorna alguma coisa. Esses casos podem funcionar se o aplicativo Web exigir apenas uma sessão de login válida para fazer a chamada à API, mas não tiver controle de acesso no back-end para comparar a sessão do chamador com os dados que estão sendo chamados.

Se for esse o caso, e pudermos calcular os parâmetros da API para outros usuários, isso seria uma vulnerabilidade IDOR. Mesmo que não pudéssemos calcular os parâmetros da API para outros usuários, ainda teríamos identificado uma vulnerabilidade no sistema de controle de acesso back-end e poderíamos começar a procurar outras referências de objetos para explorar.
