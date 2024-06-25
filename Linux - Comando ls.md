#Linux #comandos
# Linux - Comando ls

```sh
cry0l1t3@htb[~]$ ls -l

total 32
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 Desktop
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Documents
drwxr-xr-x 3 cry0l1t3 htbacademy 4096 Nov 15 03:26 Downloads
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Music
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Pictures
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Public
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Templates
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Videos
```

Primeiro, vemos a quantidade total de blocos ( `512-byte`) utilizados pelos arquivos e diretórios listados no diretório atual, que indica o tamanho total utilizado. Isso significa que ele usou 32 * 512 bytes = `16384 bytes`de espaço em disco. A seguir, vemos algumas colunas estruturadas da seguinte forma:

| **Conteúdo da coluna** | **Descrição**                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| `drwxr-xr-x`           | Tipo e permissões                                                                          |
| `2`                    | Número de links físicos para o arquivo/diretório                                           |
| `cry0l1t3`             | Proprietário do arquivo/diretório                                                          |
| `htbacademy`           | Proprietário do grupo do arquivo/diretório                                                 |
| `4096`                 | Tamanho do arquivo ou número de blocos usados ​​para armazenar as informações do diretório |
| `Nov 13 17:37`         | Data e hora                                                                                |
| `Desktop`              | Nome do diretório                                                                          |

Porém, não veremos tudo o que está nesta pasta. Um diretório também pode conter arquivos ocultos que começam com um ponto no início de seu nome (por exemplo, `.bashrc`ou `.bash_history`). Portanto, precisamos usar o comando `ls -la`para listar todos arquivos de um diretório:

```sh
cry0l1t3@htb[~]$ ls -la

total 403188
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 .bash_history
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 .bashrc
...SNIP...
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 Desktop
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Documents
drwxr-xr-x 3 cry0l1t3 htbacademy 4096 Nov 15 03:26 Downloads
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Music
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Pictures
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Public
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Templates
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Videos
```

Para listar o conteúdo de um diretório, não precisamos necessariamente navegar até lá primeiro. Também podemos usar “ `ls`” para especificar o caminho onde queremos conhecer o conteúdo.




