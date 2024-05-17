#Linux
# Processos e forks

Um processo é uma instância em execução de um programa de computador. Os sistemas operacionais multitarefa podem executar muitos processos ao mesmo tempo.

A bifurcação é um método que o kernel usa para permitir que um processo crie uma cópia de si mesmo. Os processos precisam de uma maneira de criar novos processos em sistemas operacionais multitarefa. A operação bifurcação (fork) é a única maneira de fazer isso no Linux.

A bifurcação (fork) é importante por muitos motivos. Um deles está relacionado à escalabilidade do processo. Apache, um servidor web popular, é um bom exemplo. Ao se bifurcar, o Apache é capaz de atender a um grande número de solicitações com menos recursos do sistema do que um servidor baseado em processo único.

Quando um processo é bifurcado (fork), o processo do chamador se torna o processo pai, com o processo recém-criado referido como seu filho. Depois da bifurcação, os processos são, até certo ponto, processos independentes; eles têm IDs de processo diferentes, mas executam o mesmo código de programa.

A tabela lista três comandos usados para gerenciar processos.

| Comando | Descrição                                                                                                                                                                                                                                                                                                                            |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ps      | - Usado para listar os processos em execução no computador no momento em que ele é chamado.<br>- Ele pode ser instruído a exibir processos em execução que pertencem ao usuário atual ou a outros usuários.<br>- Embora listar processos não exija privilégios de root, eliminar ou modificar os processos de outros usuários exige. |
| top     | - Usado para listar processos em execução, mas ao contrário do ps, top continua exibindo processos em execução dinamicamente.<br>- Pressione q para sair do top.                                                                                                                                                                     |
| kill    | - Usado para modificar o comportamento de um processo específico.<br>- Dependendo dos parâmetros, kill removerá, reiniciará ou pausará um processo.<br>- Em muitos casos, o usuário executará ps ou top antes de executar kill.<br>- Isso é feito para que o usuário possa aprender o PID de um processo antes de executar kill.     |

A saída do comando mostra a saída do comando top em um computador Linux.

```sh
[analyst@secOps ~]$ top

top - 11:29:16 up 0 min, 1 user, load average: 1.09, 0.31, 0.11

Tasks: 119 total, 1 running, 118 sleeping, 0 stopped, 0 zombie

%Cpu(s): 5.4 us, 2.0 sy, 0.0 ni, 87.4 id, 2.7 wa, 1.4 hi, 1.0 si, 0.0 st

MiB Mem :        982.8 total,        67.9 free,        765.8 used,        149.1 buff/cache

MiB Swap :        0.0 total,        0.0 free,        0.0 used.        39.3 avail Mem

        PID USER        PR NI  VIRT  RES  SHR S  %CPU  %MEM        TIME+ COMMAND

        729 analyst        20  0  2652376  284472  61076 S  2.7  28.3  0:06.75 Web Con+

        570 analyst        20  0  2691388  215728  62404 S  2.0  21.4  0:06.99 firefox

        357 root        20  0  267972   91960  18468 S  1.3  9.1  0:01.63 Xorg

        461 analyst        20  0  322208  21000  7480 S  1.3  2.1  0:00.67 xfce4-p+

        121 root        20  0  0  0  0 S  0.7  0.0  0:00.43 kswapd0

        1 root        20  0  174376  4196   1688 S  0.3  0.4  0:00.66 systemd

        294        root 20  0  245036  11876  868 S  0.3  1.2  0:00.34 python2+

        539 analyst        20  0  150824  660  0 S  0.3  .1  0:00.02VBoxCli+

        800 analyst        200  477768  18968  9800 S  0.3  1.9  0:00.30 xfce4-t+

        2 root        20  0        0        0        0 S    0.0    0.0    0:00.00    kthreadd

        3 root        0  -20        0        0        0 I    0.0    0.0    0:00.00 rcu_gp

        4 root        0  -20        0        0        0.0    0.0    0:00.00    rcu_par+

        5 root        20  0        0        0        0 I    0.0    0.0    0:00.00 kworker+

        6 root        0  -20        0        0        0 I    0.0    0.0    0:00.00    kworker+

        7 root        20  0        0        0        0 I    0.0    0.0    0:00.00 kworker+

        8 root        0  -20        0        0        0 I    0.0    0.0    0:00.00 mm_perc+

        9 root        20  0        0        0        0 S    0.0    0.0    0:00.02 ksoftir+

[analyst@secOps ~]$
```