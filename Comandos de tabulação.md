#Linux #SO #shell 
# Comandos de tabulação

Embora as ferramentas de linha de comando geralmente sejam projetadas para executar uma tarefa específica e bem definida, muitos comandos podem ser combinados para executar tarefas mais complexas por uma técnica conhecida como tubulação. Nomeado após seu caractere definidor, o pipe (|), tubulação consiste em encadear comandos juntos, alimentando a saída de um comando na entrada de outro.

Por exemplo, o comando ls é usado para exibir todos os arquivos e diretórios de um determinado diretório. O comando **grep** compara pesquisas através de um arquivo ou texto procurando a string especificada. Se encontrado, **grep** exibe todo o conteúdo da pasta onde a string foi encontrada.

Os dois comandos, **ls** e **grep,** podem ser canalizado juntos para filtrar a saída de**ls.** Isto é mostrado na saída do comando **ls -l | grep host** e do comando **ls -l | grep file**.

```sh
[analyst@secOps ~]$ ls -ltotal 40drwxr-xr-x 2 analyst analyst    4096 Mar  22  2018 Desktopdrwxr-xr-x 3 analyst analyst    4096 April 2 14:44 Downloads-rw-r--r-- 1 analyst analyst    9 May 20 10:51 hostfile1.txt-rw-r--r-- 1 analyst analyst    9 May 20 10:51 hostfile2.txt-rw-r--r-- 1 analyst analyst    9 May 20 10:52 hostfile3.txtdrwxr-xr-x 9 analyst analyst    4096 Jul 19 2018 lab.support.files-rw-r--r-- 1 analyst analyst    19 May 20 10:53 mytest.com-rw-r--r-- 1 analyst analyst    228844 May 20 10:54 rkhunter-1.4.6-1-any.pkg.tar.xzdrwxr-xr-x 2 analyst analyst     4096 Mar 21 2018 second_drive-rw-r--r-- 1 analyst analyst    257 May 20 10:52 space.txt[analyst@secOps ~]$[analyst@secOps ~]$ ls -l | grep host-rw-r--r-- 1 analyst analyst    9 May 20 10:51 hostfile1.txt-rw-r--r-- 1 analyst analyst    9 May 20 10:51 hostfile2.txt-rw-r--r-- 1 analyst analyst    9 May 20 10:52 hostfile3.txt[analyst@secOps ~]$[analyst@secOps ~]$ ls -l | grep file-rw-r--r-- 1 analyst analyst    9 May 20 10:51 hostfile1.txt-rw-r--r-- 1 analyst analyst    9 May 20 10:51 hostfile2.txt-rw-r--r-- 1 analyst analyst    9 May 20 10:52 hostfile3.txtdrwxr-xr-x 9 analyst analyst  4096 Jul 19 2018 lab.support.files[analyst@secOps ~]$
```