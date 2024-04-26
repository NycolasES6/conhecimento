# Executar comandos


`Command execution` é um dos recursos mais desejados ao atacar serviços comuns porque nos permite controlar o sistema operacional. Se tivermos os privilégios apropriados, podemos usar o banco de dados SQL para executar comandos do sistema ou criar os elementos necessários para fazê-lo.

`MSSQL`possui [procedimentos armazenados estendidos](https://docs.microsoft.com/en-us/sql/relational-databases/extended-stored-procedures-programming/database-engine-extended-stored-procedures-programming?view=sql-server-ver15) chamados [xp_cmdshell](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-cmdshell-transact-sql?view=sql-server-ver15) que nos permitem executar comandos do sistema usando SQL. Tenha em mente o seguinte sobre `xp_cmdshell`:

- `xp_cmdshell` é um recurso poderoso e desabilitado por padrão. `xp_cmdshell` pode ser ativado e desativado usando o [Gerenciamento Baseado em Políticas](https://docs.microsoft.com/en-us/sql/relational-databases/security/surface-area-configuration) ou executando [sp_configure](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/xp-cmdshell-server-configuration-option)
- O processo do Windows gerado pelo `xp_cmdshell`tem os mesmos direitos de segurança que a conta de serviço do SQL Server
- `xp_cmdshell`opera de forma síncrona. O controle não é retornado ao chamador até que o comando command-shell seja concluído

Para executar comandos usando a sintaxe SQL no MSSQL, use:

## XP_CMDSHELL

```shell
1> xp_cmdshell 'whoami'
2> GO

output
-----------------------------
no service\mssql$sqlexpress
NULL
(2 rows affected)
```

Se `xp_cmdshell` não estiver habilitado, podemos habilitá-lo, se tivermos os privilégios apropriados, usando o seguinte comando:

```sql
-- To allow advanced options to be changed.  
EXECUTE sp_configure 'show advanced options', 1
GO

-- To update the currently configured value for advanced options.  
RECONFIGURE
GO  

-- To enable the feature.  
EXECUTE sp_configure 'xp_cmdshell', 1
GO  

-- To update the currently configured value for this feature.  
RECONFIGURE
GO
```

Existem outros métodos para obter a execução de comandos, como adicionar [procedimentos armazenados estendidos](https://docs.microsoft.com/en-us/sql/relational-databases/extended-stored-procedures-programming/adding-an-extended-stored-procedure-to-sql-server) , [assemblies CLR](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/introduction-to-sql-server-clr-integration) , [trabalhos do SQL Server Agent](https://docs.microsoft.com/en-us/sql/ssms/agent/schedule-a-job?view=sql-server-ver15) e [scripts externos](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-execute-external-script-transact-sql) . Porém, além desses métodos, existem também funcionalidades adicionais que podem ser utilizadas como o comando `xp_regwrite` que serve para elevar privilégios criando novas entradas no registro do Windows. No entanto, esses métodos estão fora do âmbito deste módulo.

`MySQL` suporta [funções definidas pelo usuário](https://dotnettutorials.net/lesson/user-defined-functions-in-mysql/) que nos permitem executar código C/C++ como uma função dentro do SQL, há uma função definida pelo usuário para execução de comandos neste [repositório GitHub](https://github.com/mysqludf/lib_mysqludf_sys) . Não é comum encontrar uma função definida pelo usuário como esta em um ambiente de produção, mas devemos estar cientes de que poderemos utilizá-la.










