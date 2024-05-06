tags: #sql 

# Comunique-se com outros bancos de dados com MSSQL

`MSSQL`possui uma opção de configuração chamada [servidores vinculados](https://docs.microsoft.com/en-us/sql/relational-databases/linked-servers/create-linked-servers-sql-server-database-engine) . Os servidores vinculados normalmente são configurados para permitir que o mecanismo de banco de dados execute uma instrução Transact-SQL que inclua tabelas em outra instância do SQL Server ou em outro produto de banco de dados, como Oracle.

Se conseguirmos obter acesso a um SQL Server com um servidor vinculado configurado, poderemos migrar lateralmente para esse servidor de banco de dados. Os administradores podem configurar um servidor vinculado usando credenciais do servidor remoto. Se essas credenciais tiverem privilégios de administrador de sistema, poderemos executar comandos na instância SQL remota. Vamos ver como podemos identificar e executar consultas em servidores vinculados.

## Identifique servidores vinculados em MSSQL

```sh
1> SELECT srvname, isremote FROM sysservers
2> GO

srvname                             isremote
----------------------------------- --------
DESKTOP-MFERMN4\SQLEXPRESS          1
10.0.0.12\SQLEXPRESS                0

(2 rows affected)
```

Como podemos ver na saída da consulta, temos o nome do servidor e a coluna `isremote`, onde `1` significa é um servidor remoto e `0` é um servidor vinculado. Podemos ver [sysservers Transact-SQL](https://docs.microsoft.com/en-us/sql/relational-databases/system-compatibility-views/sys-sysservers-transact-sql) para mais informações.

A seguir, podemos tentar identificar o usuário utilizado para a conexão e seus privilégios. A instrução [EXECUTE](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/execute-transact-sql) pode ser usada para enviar comandos de passagem para servidores vinculados. Adicionamos nosso comando entre parênteses e especificamos o servidor vinculado entre colchetes ( `[ ]` ).

```sh
1> EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]
2> GO

------------------------------ ------------------------------ ------------------------------ -----------
DESKTOP-0L9D4KA\SQLEXPRESS     Microsoft SQL Server 2019 (RTM sa_remote                                1

(1 rows affected)
```

> **Nota:** Se precisarmos usar aspas em nossa consulta ao servidor vinculado, precisaremos usar aspas duplas simples para escapar das aspas simples. Para executar vários comandos de uma vez, podemos dividi-los com ponto e vírgula (;).

Como vimos, agora podemos executar consultas com privilégios de administrador de sistema no servidor vinculado. Como `sysadmin`, controlamos a instância do SQL Server. Podemos ler dados de qualquer banco de dados ou executar comandos do sistema com o `xp_cmdshell`. Esta seção abordou algumas das maneiras mais comuns de atacar bancos de dados SQL Server e MySQL durante testes de penetração. Existem outros métodos para atacar esses tipos de banco de dados e também outros, como [PostGreSQL](https://book.hacktricks.xyz/network-services-pentesting/pentesting-postgresql) , SQLite, Oracle, [Firebase](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/buckets/firebase-database) e [MongoDB](https://book.hacktricks.xyz/network-services-pentesting/27017-27018-mongodb) que serão abordados em outros módulos. Vale a pena dedicar algum tempo para ler sobre essas tecnologias de banco de dados e também sobre algumas das formas comuns de atacá-las.




























