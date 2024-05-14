#Linux #shell 
# Monitoramento de logs de serviço

Arquivos de log são os registros que um computador armazena para manter o controle de eventos importantes. Kernel, serviços e eventos de aplicativos são todos registrados em arquivos de log. É muito importante que um administrador revise periodicamente os logs de um computador para mantê-lo saudável. Ao monitorar arquivos de log do Linux, um administrador obtém uma visão clara do desempenho do computador, status de segurança e quaisquer problemas subjacentes. A análise do arquivo de log permite que um administrador proteja contra problemas futuros antes que eles ocorram.

No Linux, os arquivos de log podem ser categorizados como:

- Registros de aplicação
- Logs de eventos
- Registros de serviço
- Registros do sistema

Alguns logs contêm informações sobre daemons que estão sendo executados no sistema Linux. Um daemon é um processo em segundo plano que é executado sem a necessidade de interação do usuário. Por exemplo, o System Security Services Daemon (SSSD) gerencia o acesso remoto e a autenticação para recursos de logon único.

A tabela lista alguns arquivos de log populares do Linux e suas funções

<table class="" style="min-width: 600px">
                <!--?lit$730157786$--><!---->
                    <tr class="table-row nth-child-0 ">
                    <!--?lit$730157786$--><!---->
                                <th rowspan="1" colspan="1" class="table-data table-heading nth-child-0 ">
                                   <!--?lit$730157786$-->Arquivo de log do Linux
                                    <!--?lit$730157786$-->
                                </th>
                                <!----><!---->
                                <th rowspan="1" colspan="1" class="table-data table-heading nth-child-1 ">
                                   <!--?lit$730157786$-->Descrição
                                    <!--?lit$730157786$-->
                                </th>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-1 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/mensagens
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Este diretório contém logs genéricos de atividade do computador.</li> <li>Ele é usado principalmente para armazenar mensagens informativas e não críticas do sistema.</li> <li>Em computadores baseados em Debian, o diretório /var/log/syslog serve a mesma finalidade.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-2 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/auth.log
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Este arquivo armazena todos os eventos relacionados à autenticação em computadores Debian e Ubuntu.</li> <li>Qualquer coisa que envolva o mecanismo de autorização do usuário pode ser encontrada neste arquivo.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-3 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/secure
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Este diretório é usado por computadores RedHat e CentOS em vez de /var/log/auth.log.</li> <li>Ele também rastreia logins sudo, logins SSH e outros erros registrados pelo SSSD.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-4 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/boot.log
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Este arquivo armazena informações relacionadas à inicialização e mensagens registradas durante o processo de inicialização do computador.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-5 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/dmesg
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Este diretório contém mensagens de buffer do anel do kernel.</li> <li>Informações relacionadas a dispositivos de hardware e seus drivers são registradas aqui.</li> <li>É muito importante porque, devido à sua natureza de baixo nível, sistemas de registro como syslog não estão sendo executados quando esses eventos ocorrem e, portanto, muitas vezes não estão disponíveis para o administrador em tempo real.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-6 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/kern.log
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Este arquivo contém informações registradas pelo kernel.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-7 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/cron
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Cron é um serviço usado para agendar tarefas automatizadas no Linux e este diretório armazena seus eventos.</li> <li>Sempre que uma tarefa agendada (também chamada de trabalho cron) é executada, todas as informações relevantes, incluindo status de execução e mensagens de erro, são armazenadas aqui.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!----><!---->
                    <tr class="table-row nth-child-8 ">
                    <!--?lit$730157786$--><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-0 ">
                                <!--?lit$730157786$-->/var/log/mysqld.log ou /var/log/mysql.log
                                 <!--?lit$730157786$-->
                                </td>
                                <!----><!---->
                                <td rowspan="1" colspan="1" class="table-data nth-child-1 ">
                                <!--?lit$730157786$--><ul> <li>Este é o arquivo de log do MySQL.</li> <li>Todas as mensagens de depuração, falha e sucesso relacionadas ao processo mysqld e ao daemon mysqld_safe são registradas aqui.</li> <li>As distribuições RedHat, CentOS e Fedora Linux armazenam logs MySQL em /var/log/mysqld.log, enquanto Debian e Ubuntu mantêm o log no arquivo /var/log/mysql.log.</li> </ul>
                                 <!--?lit$730157786$-->
                                </td>
                                <!---->
                   </tr>  
                    <!---->
                </table>

A saída do comando mostra uma parte do arquivo de log **/var/log/messages**. Cada linha representa um evento registrado. Os carimbos de data/hora no início das linhas marcam o momento em que o evento ocorreu.

```txt
[analyst@secOps ~]$ sudo cat /var/log/messages

Mar 20 15:28:45 secOps kernel: Linux version 4.15.10-1-ARCH (builduser@heftig-18961) (gcc version 7.3.1

20180312 (GCC)) #1 SMP PREEMPT Thu Mar 15 12:24:34 UTC 2018

Mar 20 15:28:45 secOps kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-linux root=UUID=07c6b457-3f39-

4ddf-bfd8-c169e8a877b2 rw quiet

Mar 20 15:28:45 secOps kernel: KERNEL supported cpus:

Mar 20 15:28:45 secOps kernel:   Intel GenuineIntel

Mar 20 15:28:45 secOps kernel:   AMD AuthenticAMD

Mar 20 15:28:45 secOps kernel:   Centaur CentaurHauls

Mar 20 15:28:45 secOps kernel: x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'

Mar 20 15:28:45 secOps kernel: x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'

Mar 20 15:28:45 secOps kernel: x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'

Mar 20 15:28:45 secOps kernel: x86/fpu: xstate_offset[2]: 576, xstate_sizes[2]: 256

Mar 20 15:28:45 secOps kernel: x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using

'standard' format.

Mar 20 15:28:45 secOps kernel: e820: BIOS-provided physical RAM map:

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x0000000000100000-0x000000003ffeffff] usable

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x000000003fff0000-0x000000003fffffff] ACPI data

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved

Mar 20 15:28:45 secOps kernel: BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved

Mar 20 15:28:45 secOps kernel: NX (Execute Disable) protection: active

Mar 20 15:28:45 secOps kernel: random: fast init done

Mar 20 15:28:45 secOps kernel: SMBIOS 2.5 present.

Mar 20 15:28:45 secOps kernel: DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006

Mar 20 15:28:45 secOps kernel: Hypervisor detected: KVM

Mar 20 15:28:45 secOps kernel: e820: last_pfn = 0x3fff0 max_arch_pfn = 0x400000000

Mar 20 15:28:45 secOps kernel: MTRR: Disabled

Mar 20 15:28:45 secOps kernel: x86/PAT: MTRRs disabled, skipping PAT initialization too.

Mar 20 15:28:45 secOps kernel: CPU MTRRs all blank - virtualized system.

```
