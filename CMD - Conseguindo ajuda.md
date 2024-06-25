# CMD - Conseguindo ajuda

O prompt de comando possui uma função integrada chamada `help`, que pode nos fornecer informações detalhadas sobre os comandos disponíveis em nosso sistema e como utilizar essas funções. Nesta seção, abordaremos o seguinte com mais detalhes:

- Como utilizamos a funcionalidade de ajuda no prompt de comando?
- Por que utilizar a funcionalidade de ajuda é essencial?
- Onde podemos encontrar recursos externos adicionais para ajuda?
- Como utilizar dicas e truques adicionais no prompt de comando?

## Como obter ajuda

Algumas questões iniciais podem surgir, como:

- A quais comandos tenho acesso?
- Como faço para usar esses comandos?

Sem quaisquer parâmetros adicionais, o comando `help` fornece uma lista de comandos integrados e informações básicas sobre o uso de cada comando exibido. Vamos dar uma olhada abaixo.

```cmd
C:\htb> help

For more information on a specific command, type HELP command-name
ASSOC          Displays or modifies file extension associations.
ATTRIB         Displays or changes file attributes.
BREAK          Sets or clears extended CTRL+C checking.
BCDEDIT        Sets properties in boot database to control boot loading.
CACLS          Displays or modifies access control lists (ACLs) of files.
CALL           Calls one batch program from another.
CD             Displays the name of or changes the current directory.
CHCP           Displays or sets the active code page number.
CHDIR          Displays the name of or changes the current directory.
CHKDSK         Checks a disk and displays a status report.

<snip>
```

Podemos obter ajuda de um comando específico passando como argumento para `help`, o comando ao qual queremos obter ajuda.

```cmd
C:\htb> help time

Displays or sets the system time.

TIME [/T | time]

Type TIME with no parameters to display the current time setting and a prompt
for a new one. Press ENTER to keep the same time.

If Command Extensions are enabled, the TIME command supports
the /T switch which tells the command to just output the
current time, without prompting for a new time.
```

Alguns comandos, não tem uma página de ajuda no comando `help`, mas se utilizarmos, ele redirecionara para o comando certo.

```cmd
C:\htb> help ipconfig

This command is not supported by the help utility. Try "ipconfig /?".
```

A utilização do comando sugerido `ipconfig /?` nos fornecerá as informações necessárias para utilizá-lo corretamente.

Esteja ciente de que vários comandos usam o modificador `/?` de forma intercambiável com ajuda.

- `cls`
Limpa a tela do terminal, mas mantém o histórico de comandos.

- `doskey /history`
Mostra o histórico de comandos.

| **Key/Command** | **Description**                                                                                                            |
| :-------------: | -------------------------------------------------------------------------------------------------------------------------- |
| doskey /history | doskey /history will print the session's command history to the terminal or output it to a file when specified.            |
|     page up     | Places the first command in our session history to the prompt.                                                             |
|    page down    | Places the last command in history to the prompt.                                                                          |
|        ⇧        | Allows us to scroll up through our command history to view previously run commands.                                        |
|        ⇩        | Allows us to scroll down to our most recent commands run.                                                                  |
|        ⇨        | Types the previous command to prompt one character at a time.                                                              |
|        ⇦        | N/A                                                                                                                        |
|       F3        | Will retype the entire previous entry to our prompt.                                                                       |
|       F5        | Pressing F5 multiple times will allow you to cycle through previous commands.                                              |
|       F7        | Opens an interactive list of previous commands.                                                                            |
|       F9        | Enters a command to our prompt based on the number specified. The number corresponds to the commands place in our history. |









