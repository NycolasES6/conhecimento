#Linux 
# Linux - Gestão de serviços e processos

Em geral, existem dois tipos de serviços: internos, os serviços relevantes que são necessários na inicialização do sistema, que, por exemplo, executam tarefas relacionadas ao hardware, e serviços que são instalados pelo usuário, que geralmente incluem todos os serviços do servidor. Esses serviços são executados em segundo plano, sem qualquer interação do usuário. Eles também são chamados `daemons`e identificados pela letra ' `d`' no final do nome do programa, por exemplo, `sshd`ou `systemd`.

A maioria das distribuições Linux agora mudou para `systemd`. Este daemon é `Init process`, iniciado primeiro e, portanto, possui o ID do processo (PID) 1. Este daemon monitora e cuida da inicialização e parada ordenada de outros serviços. Todos os processos possuem um PID atribuído que pode ser visualizado `/proc/` com o número correspondente. Esse processo pode ter um ID de processo pai (PPID) e, nesse caso, é conhecido como processo filho.

Além disso, `systemctl` também podemos usar `update-rc.d` para gerenciar links de script de inicialização SysV. Vejamos alguns exemplos. Usaremos o `OpenSSH` servidor nestes exemplos. Se não o tivermos instalado, instale-o antes de prosseguir para esta seção.

## Sistemactl

Após a instalação `OpenSSH` em nossa VM, podemos iniciar o serviço com o seguinte comando.

```sh
$ systemctl start ssh
```

Depois de iniciarmos o serviço, podemos verificar se ele funciona sem erros.

```sh
$ systemctl status ssh
```

Para adicionar OpenSSH ao script SysV para informar ao sistema para executar este serviço após a inicialização, podemos vinculá-lo com o seguinte comando:

```sh
$ systemctl enable ssh
```

Assim que reiniciarmos o sistema, o servidor OpenSSH será executado automaticamente. Podemos verificar isso com uma ferramenta chamada `ps`.

```sh
$ ps -aux | grep ssh
```

Também podemos usar `systemctl` para listar todos os serviços.

```sh
$ systemctl list-units --type=service
```

É bem possível que os serviços não iniciem devido a um erro. Para ver o problema, podemos usar a ferramenta `journalctl`para visualizar os logs.

```sh
$ journalctl -u ssh.service --no-pager
```

## Mate um processo

Um processo pode estar nos seguintes estados:

- Correndo
- Aguardando (aguardando um evento ou recurso do sistema)
- Parou
- Zumbi (parado, mas ainda possui uma entrada na tabela de processos).

Os processos podem ser controlados usando `kill`, `pkill`, `pgrep`e `killall`. Para interagir com um processo, devemos enviar-lhe um sinal. Podemos visualizar todos os sinais com o seguinte comando:

```sh
$ kill -l

1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

Os mais comumente usados ​​são:

| **Sinal** | **Descrição**                                                                                                                              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `1`       | `SIGHUP`- É enviado a um processo quando o terminal que o controla é fechado.                                                              |
| `2`       | `SIGINT`- Enviado quando um usuário pressiona `[Ctrl] + C`o terminal de controle para interromper um processo.                             |
| `3`       | `SIGQUIT`- Enviado quando um usuário pressiona `[Ctrl] + D`para sair.                                                                      |
| `9`       | `SIGKILL`- Elimine imediatamente um processo sem operações de limpeza.                                                                     |
| `15`      | `SIGTERM`- Encerramento do programa.                                                                                                       |
| `19`      | `SIGSTOP`- Pare o programa. Isso não pode mais ser tratado.                                                                                |
| `20`      | `SIGTSTP`- Enviado quando um usuário pressiona `[Ctrl] + Z`para solicitar a suspensão de um serviço. O usuário pode lidar com isso depois. |

Por exemplo, se um programa travasse, poderíamos forçá-lo a encerrá-lo com o seguinte comando:

```sh
$ kill 9 <PID> 
```

## Antecedentes de um Processo

Às vezes será necessário colocar em segundo plano a varredura ou processo que acabamos de iniciar para continuar usando a sessão atual para interagir com o sistema ou iniciar outros processos. Como já vimos, podemos fazer isso com o atalho `[Ctrl + Z]`. Conforme mencionado acima, enviamos o `SIGTSTP`sinal ao kernel, que suspende o processo.

```sh
$ ping -c 10 www.hackthebox.eu

NycolasES6@htb[/htb]$ vim tmpfile
[Ctrl + Z]
[2]+  Stopped                 vim tmpfile
```

Agora todos os processos em segundo plano podem ser exibidos com o seguinte comando.

```shell-session
$ jobs

[1]+  Stopped                 ping -c 10 www.hackthebox.eu
[2]+  Stopped                 vim tmpfile
```

O atalho `[Ctrl] + Z` suspende os processos e eles não serão mais executados. Para mantê-lo rodando em segundo plano, temos que inserir o comando `bg` para colocar o processo em segundo plano.

```sh
NycolasES6@htb[/htb]$ bg

NycolasES6@htb[/htb]$ 
--- www.hackthebox.eu ping statistics ---
10 packets transmitted, 0 received, 100% packet loss, time 113482ms

[ENTER]
[1]+  Exit 1                  ping -c 10 www.hackthebox.eu
```

Outra opção é definir automaticamente o processo com um sinal AND ( `&`) no final do comando.

```sh
$ ping -c 10 www.hackthebox.eu &

[1] 10825
PING www.hackthebox.eu (172.67.1.1) 56(84) bytes of data.
```

Assim que o processo terminar, veremos os resultados.

```sh
NycolasES6@htb[/htb]$ 

--- www.hackthebox.eu ping statistics ---
10 packets transmitted, 0 received, 100% packet loss, time 9210ms

[ENTER]
[1]+  Exit 1                  ping -c 10 www.hackthebox.eu
```

## Colocar em primeiro plano um processo

Depois disso, podemos usar o `jobs`comando para listar todos os processos em segundo plano. Os processos em segundo plano não requerem interação do usuário e podemos usar a mesma sessão de shell sem esperar até que o processo termine primeiro. Assim que a varredura ou processo terminar seu trabalho, seremos notificados pelo terminal de que o processo foi finalizado

```sh
$ jobs

[1]+  Running                 ping -c 10 www.hackthebox.eu &
```

O comando `fg <ID>` coloca um processo em primeiro plano.

```sh
$ fg 1
ping -c 10 www.hackthebox.eu

--- www.hackthebox.eu ping statistics ---
10 packets transmitted, 0 received, 100% packet loss, time 9206ms
```

## Execute vários comandos

Existem três possibilidades para executar vários comandos, um após o outro. Eles são separados por:

- Ponto e vírgula ( `;` )
- Caracteres `ampersand` duplos ( `&&` )
- Tubos ( `|` )

A diferença entre eles está no tratamento dos processos anteriores e depende se o processo anterior foi concluído com sucesso ou com erros. O ponto e vírgula ( `;` ) é um separador de comandos e executa os comandos ignorando os resultados e erros dos comandos anteriores.

```sh
NycolasES6@htb[/htb]$ echo '1'; echo '2'; echo '3'

1
2
3
```

Por exemplo, se executarmos o mesmo comando, mas substituí-lo em segundo lugar, o comando `ls` por um arquivo que não existe, obteremos um erro e o terceiro comando será executado mesmo assim.

```sh
$ echo '1'; ls MISSING_FILE; echo '3'

1
ls: cannot access 'MISSING_FILE': No such file or directory
3
```

No entanto, parece diferente se usarmos os caracteres AND duplos ( `&&`) para executar os comandos um após o outro. Caso haja erro em um dos comandos, os seguintes não serão mais executados e todo o processo será interrompido.

```sh
NycolasES6@htb[/htb]$ echo '1' && ls MISSING_FILE && echo '3'

1
ls: cannot access 'MISSING_FILE': No such file or directory
```

Pipes ( `|` ) dependem não apenas da operação correta e livre de erros dos processos anteriores, mas também dos resultados dos processos anteriores.
















































