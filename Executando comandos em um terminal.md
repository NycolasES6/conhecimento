#Linux 
# Executando comandos em um terminal

No Linux, normalmente você executa comandos para interagir com o computador. Ao executar comandos, você pode evitar navegar por diferentes ferramentas para obter informações do sistema ou para executar uma tarefa simples. Por exemplo, para visualizar o nome do computador, você pode abrir o aplicativo de configurações, navegar até a seção Sobre e revisar o rótulo Nome do dispositivo . Alternativamente, em um terminal, você usa apenas o `hostname`comando.

No exemplo a seguir, o comando retorna `mycomputer.example.com`, que é o nome completo da máquina.

```sh
[usuário@host ~]$ hostname
meucomputador.exemplo.com
```

A maioria dos comandos tem uma ação padrão quando são executados, mas o comando não está limitado a executar essa ação. Você pode adicionar um ou mais_opções_a um comando para modificar seu comportamento. Geralmente, uma opção de comando começa com um travessão ( `-`) e usa uma única letra, ou a opção começa com dois travessões ( `--`) e usa uma palavra.

Nos exemplos a seguir, você adiciona a `-d`opção de mostrar o nome de domínio e a `-s`opção de mostrar o nome abreviado da máquina.

```sh
[usuário@host ~]$ hostname -d
exemplo.com
[usuário@host ~]$ hostname -s
meucomputador
```

Um comando também aceita_argumentos_. Os argumentos são o alvo do comando, como um arquivo ou outro objeto sobre o qual o comando atua.

Por exemplo, o `id`comando imprime o ID do usuário que o sistema utiliza para identificar exclusivamente um usuário. No exemplo a seguir, você usa o `id`comando sozinho. Como você não utiliza opções, o `id`comando executa sua ação padrão, que é imprimir as informações do usuário atual.

```sh
[usuário@host ~]$ id
uid=1000(usuário) gid=1000(usuário) grupos=1000(usuário),10(roda)
_...saída omitida..._
```

No exemplo a seguir, você usa o `id`comando com uma opção, mas sem argumento. A `-u`opção especifica imprimir apenas o ID do usuário. O comando assume o usuário atual como argumento.

```sh
[usuário@host ~]$ id -u
1.000
```

No exemplo final, você usa o `id`comando com uma opção e um argumento. O `id`comando recebe `devops`como usuário alvo do comando. A `-u`opção imprime o `devops`ID do usuário, diferente do exemplo anterior.

```sh
[usuário@host ~]$ id -u devops
1001
```

Os comandos podem ter múltiplas opções e o significado das opções não é intercambiável entre os comandos. Você pode visualizar as opções de um comando usando a `--help`opção.

O `who`comando mostra os usuários que estão logados na máquina.

```
[usuário@host ~]$ who --help
Uso: quem [OPÇÃO]... [ ARQUIVO | ARG1 ARG2 ]
Imprima informações sobre usuários que estão logados no momento.
  -a, --tudo igual a -b -d --login -p -r -t -T -u
  -b, --boot hora da última inicialização do sistema
_...saída omitida..._
```

Os comandos `date`e `timedatectl`fornecem informações de tempo. A principal diferença é que por padrão o `timedatectl`comando mostra informações de fuso horário e se o relógio da máquina está sincronizado com um servidor de horário. Essas informações de sincronização são importantes porque alguns serviços dependem da hora do sistema para funcionar corretamente.

O exemplo a seguir mostra a saída dos comandos `date`e `timedatectl`:

```sh
[aluno@estação de trabalho ~]$ date
Sex, 29 de setembro 13:35:20 EDT 2023
```

```sh
[aluno@estação de trabalho ~]$ timedatectl
               Hora local: Sex. 2023-09-29 13:35:22 EDT
           Horário universal: Sex. 2023-09-29 17:35:22 UTC
                 Horário RTC: sexta-feira, 29/09/2023 17:35:22
                Fuso horário: América/Nova_Iorque (EDT, -0400)
**`System clock synchronized: yes`**
              Serviço NTP: ativo
          RTC em TZ local: não
```

O `passwd`comando atualiza as senhas dos usuários. Por padrão, ele altera a senha do usuário atual, portanto você não precisa especificar o nome da conta como argumento. O `root`usuário, porém, pode alterar a senha de qualquer usuário. Neste cenário, você deve especificar a conta de destino como argumento.















