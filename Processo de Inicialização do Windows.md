#SO #Windows 
# Processo de Inicialização do Windows

Muitas ações ocorrem entre o momento em que o botão liga/desliga do computador é pressionado e o Windows está totalmente carregado, como mostrado na figura. Isso é conhecido como o processo de inicialização do Windows.

![[Pasted image 20240514102948.png]]

Existem dois tipos de firmware de computador:

- **Basic Input-Output System (Sistema básico de Entrada-Saída - BIOS)** - O firmware do BIOS foi criado no início dos anos 80 e funciona da mesma maneira que quando foi criado. À medida que os computadores evoluíram, tornou-se difícil para o firmware do BIOS suportar todos os novos recursos solicitados pelos usuários.
- **Unified Extensible Firmware Interface (UEFI)** - O UEFI foi projetado para substituir o BIOS e oferecer suporte aos novos recursos.

No firmware do BIOS, o processo começa com a fase de inicialização do BIOS. Isso ocorre quando os dispositivos de hardware são inicializados e um POST (Power On Self-Test) é executado para garantir que todos esses dispositivos estejam se comunicando. Quando o disco do sistema é descoberto, o POST termina. A última instrução no POST é procurar o registro mestre de inicialização (MBR).

A MBR contém um pequeno programa que é responsável por localizar e carregar o sistema operacional. O BIOS executa esse código e o sistema operacional começa a carregar.

Em contraste com o firmware do BIOS, o firmware UEFI tem muita visibilidade sobre o processo de inicialização. O UEFI inicializa carregando arquivos de programa EFI, armazenados como arquivos.efi em uma partição de disco especial, conhecida como EFI System Partition (ESP).

**Nota:** Um computador que usa UEFI armazena o código de inicialização no firmware. Isso ajuda a aumentar a segurança do computador no momento da inicialização porque o computador entra diretamente no modo protegido.

Independentemente de o firmware ser BIOS ou UEFI, depois que uma instalação válida do Windows for localizada, o arquivo **Bootmgr.exe** será executado. **Bootmgr.exe** alterna o sistema do modo real para o modo protegido para que toda a memória do sistema possa ser usada.

**Bootmgr.exe** lê o banco de dados de configuração de inicialização (BCD). O BCD contém qualquer código adicional necessário para iniciar o computador, juntamente com uma indicação de se o computador está saindo da hibernação ou se este é um arranque a frio. Se o computador estiver saindo da hibernação, o processo de inicialização continuará com o **Winresume.exe.** Isso permite que o computador leia o arquivo **Hiberfil.sys** que contém o estado do computador quando foi colocado em hibernação.

Se o computador estiver sendo inicializado a partir de uma inicialização a frio, o arquivo **Winload.exe** será carregado. O arquivo **Winload.exe** cria um registro da configuração de hardware no registro. O registro é um registro de todas as configurações, opções, hardware e software do computador. O registro será explorado em profundidade posteriormente neste capítulo.**Winload.exe** também usa Kernel Mode Code Signing (KMCS) para garantir que todos os drivers sejam assinados digitalmente. Isso garante que os drivers são seguros para carregar à medida que o computador é iniciado.

Depois que os drivers forem examinados, o **Winload.exe** executa o **Ntoskrnl.exe**, que inicia o kernel do Windows e configura o HAL. Finalmente, o Subsistema do Gestor de Sessões (SMSS) lê o registo para criar o ambiente do utilizador, iniciar o serviço Winlogon e preparar a área de trabalho de cada utilizador à medida que inicia sessão.


























