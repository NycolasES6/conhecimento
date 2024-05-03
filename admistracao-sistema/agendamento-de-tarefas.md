# Agendamento de tarefas

O agendamento de tarefas é um recurso dos sistemas Linux que permite aos usuários agendar e automatizar tarefas. Ele permite que administradores e usuários executem tarefas em horários específicos ou em frequências específicas, sem precisar iniciá-las manualmente. Ele pode ser usado em sistemas Linux como Ubuntu, Redhat Linux e Solaris para gerenciar uma variedade de tarefas. Os exemplos incluem atualização automática de software, execução de scripts, limpeza de bancos de dados e automação de backups. Isso também permite que os usuários agendem tarefas regulares e repetitivas para garantir que sejam executadas regularmente. Além disso, alertas podem ser configurados para serem exibidos quando determinados eventos ocorrerem ou para entrar em contato com administradores ou usuários. Existem muitos casos de uso diferentes para automação desse tipo, mas estes abrangem a maioria dos casos.

## Sistema

Systemd é um serviço usado em sistemas linux com Ubuntu, Solaris e Redhatpara iniciar processo e scripts em um horário específico. Com ele, podemos configurar processos e scripts para serem executados em um horário ou intervalo de tempo especófico e também especificar eventos e gatilhos específicos que irão acionar uma tarefa específica. Para fazer isso, precisamos tomar algumas medidas e cuidados antes que nossos scripts ou processos sejam executados automaticamente pelo sistema.

1. Crie um cronômetro
2. Crie um serviço
3. Ative o cronômetro

## Crie um cronômetro

Para criar um timer para o systemd, precisamos criar um diretório onde o script do timer será armazenado.

#### `$ sudo mkdir /etc/systemd/system/mytimer.timer.d`

#### `$ sudo vim /etc/systemd/system/mytimer.timer`

A seguir, precisamos criar um script que configure o cronômetro. O script deve conter as seguintes opções: "Unit", "Timer" e "install". A opção "Uint" especifica uma descrição para o temporizador. A opção "Timer" especifica quando iniciar o cronômetro e quando ativá-lo. Finalmente, a opção "install" específica onde instalar o temporizador.

### mytimer.timer

[Unit]<br/>
Description=My Timer

[Timer]<br/>
OnBootSec=3min<br/>
OnUnitActiveSec=1hour

[Install]<br/>
WantedBy=timers.target

Aqui depende de como queremos criar o nosso script. Por exmplo, se quisermos executar nosso script apenas uma vez após a inicialização do sistema, devemos usar a configuração **OnBootSec** em **Timer**. No entanto, se quisermos que nosso script seja executado regularmente, devemos usar o **OnUnitActiveSec** para queo sistema execute o script em intervalos regulares. Em seguida, precisamos criar nosso **service**.

## Crie um serviço

#### `$ sudo vim /etc/systemd/system/mytimer.service`

Aqui definimos uma descrição e especificamos o caminho completo para o script que queremos executar. O "multi-user.target" é o sistema de unidades que é ativado ao iniciar um modo multiusuário normal. Ele define os serviços que devem ser iniciados na inicialização normal do sistema.

### mytimer.service

[Unit]<br/>
Description=My Service

[Service]<br/>
ExecStart=/full/path/to/my/script.sh

[Install]<br/>
WantedBy=multi-user.target

<br/>

Depois disso, temos que deixar o **systemd** ler as pastas novamente para incluir as alterações.

### Recarregar o systemd

#### `$ sudo systemctl daemon-reload`

Depois disso, podemos utilizar o systemctl para iniciar  o serviço manualmente e ativar a inicialização automática.

### Inicie o cronômetro e serviço

#### `$ sudo systemctl start mytimer.service`

#### `$ sudo systemctl enable mytimer.service`

## Cron

Cron é outra ferramenta que pode ser usada em sistemas linux para agendar e automatizar processos. Ele permite que usuários e administradores executem tarefas em horários ou em intervalos específicos. Para os exemplos acima, também podemos usar o Cron para automatizar as mesmas tarefas. Precisamos apenas criar um script e então dizer ao daemon cron para chamálo em um horário específico.

Com o Cron, podemos automatizar as mesmas tarefas, mas o processo de configuração do daemon Cron é um pouco diferente do Systemd. Para configurar o daemon cron, precisamos armazenar as tarefas em um arquivo chamado crontabe então informar ao daemon quando executar as tarefas. Então podemos agendar e automatizar as tarefas configurando o daemon cron adequadamente. A estrutura do Cron consiste nos seguintes componentes:

| Prazo         | Descrição |
| ------------- | --------- |
|  Minutos ( 0 - 59 )       | Especifica em que minuto a tarefa deve ser executada.|
|  Horas ( 0 - 23 )         | Especifica em que hora a tarefa deve ser executada.|
|  Dias do mês ( 1 - 31 )   | Especifica em qual dia do mês a tarefa deve ser executada.|
|  Meses ( 1 - 12 )         | Especifica em qual mês a tarefa deve ser executada.|
|  Dias da semana ( 0 - 7 ) | Especifica em qual dia da semana a tarefa deve ser executada.|

### Por exemplo, esse crontab poderia ser assim :

\# System Update <br/>
\* */6 * * /path/to/update_software.sh

\# Execute scripts<br/>
0 0 1 * * /path/to/scripts/run_scripts.sh

\# Cleanup DB<br/>
0 0 * * 0 /path/to/scripts/clean_database.sh

\# Backups<br/>
0 0 * * 7 /path/to/scripts/backup.sh

A “Atualização do Sistema” deve ser executada a cada seis horas. Isto é indicado pela entrada */6na coluna da hora. A tarefa é executada pelo script update_software.sh, cujo caminho é fornecido na última coluna.

A tarefa execute scriptsdeve ser executada todo primeiro dia do mês à meia-noite. Isto é indicado pelas entradas 0e 0nas colunas de minutos e horas e 1na coluna de dias do mês. A tarefa é executada pelo run_scripts.shscript, cujo caminho é fornecido na última coluna.

A terceira tarefa, Cleanup DB, deve ser executada todos os domingos à meia-noite. Isto é especificado pelas entradas 0e 0nas colunas de minutos e horas e 0na coluna de dias da semana. A tarefa é executada pelo clean_database.shscript, cujo caminho é fornecido na última coluna.

A quarta tarefa, backups, deve ser executada todos os domingos à meia-noite. Isto é indicado pelas entradas 0e 0nas colunas de minutos e horas e 7na coluna de dias da semana. A tarefa é executada pelo backup.shscript, cujo caminho é fornecido na última coluna.

Também é possível receber notificações quando uma tarefa é executada com ou sem sucesso. Além disso, podemos criar logs para monitorar a execução das tarefas.

## System x Cron

Systemd e Cron são ferramentas que podem ser usadas em sistemas Linux para agendar e automatizar processos. A principal diferença entre essas duas ferramentas é como elas são configuradas. Com o Systemd, você precisa criar um script de cronômetro e serviços que informe ao sistema operacional quando executar as tarefas. Por outro lado, com o Cron, você precisa criar um crontabarquivo que informe ao daemon cron quando executar as tarefas.

## Atividade

What is the type of the service of the "syslog.service"?

`$ systemctl show syslog.service`

**Answer: notify**
