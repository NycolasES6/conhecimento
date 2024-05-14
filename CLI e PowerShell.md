#SO #Windows 

# CLI e PowerShell

A interface de linha de comando (CLI) do Windows pode ser usada para executar programas, navegar no sistema de arquivos e gerenciar arquivos e pastas. Além disso, arquivos chamados de batch podem ser criados para executar vários comandos sucessivamente, assim como um script básico.

Para abrir a CLI do Windows, procure **cmd.exe** e clique no programa. Lembre-se que clicar com o botão direito do mouse no programa oferece a opção de Executar como administrador, dando muito mais poder aos comandos que serão usados.

O prompt exibe o local atual dentro do sistema de arquivos. Estas são algumas coisas a serem lembradas ao usar a CLI:

- Os nomes de arquivo e caminhos não diferenciam maiúsculas de minúsculas, por padrão.
- Os dispositivos de armazenamento recebem uma letra para referência. Isto seguido por dois pontos e barra invertida (). Isso indica a raiz, ou o nível mais alto, do dispositivo. A hierarquia de pastas e arquivos no dispositivo é indicada separando-as com a barra invertida. Por exemplo, o caminho C:∖Users∖Jim∖Desktop∖file.txt se refere a um arquivo chamado file.txt que está na pasta Desktop dentro da pasta Jim dentro da pasta Users na raiz da unidade C:.
- Comandos que têm opções opcionais usam a barra (/) para delinear entre o comando e a opção switch.
- Você pode usar a tecla **Tab** para completar comandos automaticamente quando diretórios ou arquivos são referenciados.
- O Windows mantém um histórico dos comandos inseridos durante uma sessão da CLI. Acesse comandos inseridos anteriormente usando as teclas de seta para cima e para baixo.
- Para alternar entre dispositivos de armazenamento, digite a letra do dispositivo, seguida de dois pontos e pressione **Enter**.

Mesmo que a CLI tenha muitos comandos e recursos, ela não pode funcionar em conjunto com o núcleo do Windows ou a GUI. Outro ambiente, chamado Windows PowerShell, pode ser usado para criar scripts para automatizar tarefas que a CLI normal não consegue criar. O PowerShell também fornece uma CLI para iniciar comandos. O PowerShell é um programa integrado no Windows e pode ser aberto pesquisando por “powershell” e clicando no programa. Assim como a CLI, o PowerShell também pode ser executado com privilégios administrativos.

Estes são os tipos de comandos que o PowerShell pode executar:

- **cmdlets -** Esses comandos executam uma ação e retornam uma saída ou objeto para o próximo comando que será executado.
- **Scripts do PowerShell -** São arquivos com extensão **.ps1** que contêm comandos do PowerShell que são executados.
- **Funções do PowerShell -** são pedaços de código que podem ser referenciados em um script.

Para ver mais informações sobre o Windows PowerShell e começar a usá-lo, digite ajuda no PowerShell, conforme mostrado na saída do comando.

```sh
Windows PowerShell

Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:∖WINDOWS∖system32> help

TOPIC

   Windows PowerShell Help System

SHORT DESCRIPTION

   Displays help about Windows PowerShell cmdlets and concepts.

LONG DESCRIPTION

   Windows PowerShell Help describes Windows PowerShell cmdlets,

   functions, scripts, and modules, and explains concepts, including

   the elements of the Windows PowerShell language.

   Windows PowerShell does not include help files, but you can read the

   help topics online, or use the Update-Help cmdlet to download help files

   to your computer and then use the Get-Help cmdlet to display the help

   topics at the command line.

   You can also use the Update-Help cmdlet to download updated help files

   as they are released so that your local help content is never obsolete.

   Without help files, Get-Help displays auto-generated help for cmdlets,

   functions, and scripts.

ONLINE HELP

   You can find help for Windows PowerShell online in the TechNet Library

   beginning at http://go.microsoft.com/fwlink/?LinkID=108518.

   To open online help for any cmdlet or function, type:

   Get-Help -Online

UPDATE-HELP

   To download and install help files on your computer:

      1. Start Windows PowerShell with the "Run as administrator" option.

      2. Type:

         Update-Help

   After the help files are installed, you can use the Get-Help cmdlet to

   display the help topics. You can also use the Update-Help cmdlet to

   download updated help files so that your local help files are always

   up-to-date.

   For more information about the Update-Help cmdlet, type:

      Get-Help Update-Help -Online

-- More --
```

Há quatro níveis de ajuda no Windows PowerShell:

- Comando do Powershell **get-help** - Exibe ajuda básica para um comando
- Comando do Powershell **get-help** _[-examples]_ - Exibe ajuda básica para um comando com exemplos
- Comando do Powershell **get-help** _[-detailed]_ - Exibe ajuda detalhada para um comando com exemplos
- Comando do Powershell **get-help** _[-full]_ - Exibe todas as informações de ajuda para um comando com exemplos mais detalhados














