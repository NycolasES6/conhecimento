#Linux 
# Linux - Agendamento de tarefas

Ele permite que administradores e usuários executem tarefas em horários específicos ou em frequências específicas, sem precisar iniciá-las manualmente.

Os exemplos incluem atualização automática de software, execução de scripts, limpeza de bancos de dados e automação de backups.

## Systemd

Systemd é um serviço usado em sistemas Linux como Ubuntu, Redhat Linux e Solaris para iniciar processos e scripts em um horário específico.

Podemos configurar processos e scripts para serem executados em um horário ou intervalo de tempo específico e também especificar eventos e gatilhos específicos que irão acionar uma tarefa específica.

Mas precisamos tomar algumas medidas e cuidados antes que nossos scripts ou processos sejam executados automaticamente pelo sistema.

1. Crie um cronômetro
2. Crie um serviço
3. Ative o cronômetro

### Crie um cronômetro

Para criar um ``timer`` para o `systemd`, precisamos criar um diretório onde o script do timer será armazenado.

```sh
sudo mkdir /etc/systemd/system/mytimer.timer.d
sudo vim /etc/systemd/system/mytimer.timer
```

A seguir precisamos criar um script de configuração do cronômetro.

Ele deve conter as seguintes opções: "**Unit**", "**Timer**" e "**Install**".

- **Unit** - Especifica uma descrição para o contador.
- **Timer** - Especifica quando iniciar o cronômetro e quando ativá-lo.
- **Install** - Especifica onde instalar o temporizador.

```txt
[Unit]
Description=My Timer

[Timer]
OnBootSec=3min
OnUnitActiveSec=1hour

[Install]
WantedBy=timers.target
```

Aqui depende de como queremos usar nosso script. Por exemplo, se quisermos executar nosso script apenas uma vez após a inicialização do sistema, devemos usar a configuração `OnBootSec` em `Timer`.

No entanto, se quisermos que nosso script seja executado regularmente, devemos usar o `OnUnitActiveSec` para que o sistema execute o script em intervalos regulares. Em seguida, precisamos criar nosso arquivo `service`.

### Crie um serviço

```sh
sudo vim /etc/systemd/system/mytimer.service
```

Aqui definimos uma descrição e especificamos o caminho completo para o script que queremos executar. O "multi-user.target" é o sistema de unidades que é ativado ao iniciar um modo multiusuário normal. Ele define os serviços que devem ser iniciados na inicialização normal do sistema.

```txt
[Unit]
Description=My Service

[Service]
ExecStart=/full/path/to/my/script.sh

[Install]
WantedBy=multi-user.target
```

Depois disso, temos que deixar o `systemd` ler as pastas novamente para incluir as alterações.

### Recarregar o Systemd

```sh
sudo systemctl daemon-reload
```

Depois disto, podemos usar o `systemctl` para `iniciar` o serviço manualmente e habilitar o `autostart`.

### Iniciar o cronômetro e o serviço

```sh
sudo systemctl start mytimer.service
sudo systemctl enable mytimer.service
```

## Cron

Ele permite que usuários e administradores executem tarefas em horários específicos ou em intervalos específicos.

Para os exemplos acima, também podemos usar o Cron para automatizar as mesmas tarefas. Precisamos apenas criar um script e então dizer ao ``daemon`` ``cron`` para chamá-lo em um horário específico.

O processo de configuração do ``daemon`` Cron é um pouco diferente do ``Systemd``.

Para configurar o ``daemon`` ``cron``, precisamos armazenar as tarefas em um arquivo chamado `crontab` e então informar ao ``daemon`` quando executar as tarefas.

### Iniciando o cron

- `crontab -e` - Abre o arquivo de configurações do cron
- `crontab -l` - Lista as tarefas agendadas


A estrutura do Cron consiste nos seguintes componentes:

| **Prazo**            | **Descrição**                                                 |
| -------------------- | ------------------------------------------------------------- |
| Minutos (0-59)       | Especifica em que minuto a tarefa deve ser executada.         |
| Horas (0-23)         | Especifica em que hora a tarefa deve ser executada.           |
| Dias do mês (1-31)   | Especifica em qual dia do mês a tarefa deve ser executada.    |
| Meses (1-12)         | Especifica em qual mês a tarefa deve ser executada.           |
| Dias da semana (0-7) | Especifica em qual dia da semana a tarefa deve ser executada. |

Por exemplo, esse crontab poderia ser assim:

```txt
# System Update
* */6 * * /path/to/update_software.sh

# Execute scripts
0 0 1 * * /path/to/scripts/run_scripts.sh

# Cleanup DB
0 0 * * 0 /path/to/scripts/clean_database.sh

# Backups
0 0 * * 7 /path/to/scripts/backup.sh
```

A “Atualização do Sistema” deve ser executada a cada seis horas. Isto é indicado pela entrada `*/6`na coluna da hora. A tarefa é executada pelo script `update_software.sh`, cujo caminho é fornecido na última coluna.

A tarefa `execute scripts`deve ser executada todo primeiro dia do mês à meia-noite. Isto é indicado pelas entradas `0`e `0`nas colunas de minutos e horas e `1`na coluna de dias do mês. A tarefa é executada pelo `run_scripts.sh`script, cujo caminho é fornecido na última coluna.

A terceira tarefa, `Cleanup DB`, deve ser executada todos os domingos à meia-noite. Isto é especificado pelas entradas `0`e `0`nas colunas de minutos e horas e `0`na coluna de dias da semana. A tarefa é executada pelo `clean_database.sh`script, cujo caminho é fornecido na última coluna.

A quarta tarefa, `backups`, deve ser executada todos os domingos à meia-noite. Isto é indicado pelas entradas `0`e `0`nas colunas de minutos e horas e `7`na coluna de dias da semana. A tarefa é executada pelo `backup.sh`script, cujo caminho é fornecido na última coluna.

Também é possível receber notificações quando uma tarefa é executada com ou sem sucesso. Além disso, podemos criar logs para monitorar a execução das tarefas.






























