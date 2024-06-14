#cyber #Windows #SO 
# O Comando netstat

Conexões TCP desconhecidas podem representar uma grande ameaça à segurança. Elas podem indicar que algo ou alguém está conectado ao host local. Às vezes é necessário conhecer quais conexões TCP ativas estão abertas e sendo executadas em um host de rede. O netstat é um utilitário de rede importante que pode ser usado para verificar essas conexões. Como mostrado abaixo, digite o comando **netstat** para listar os protocolos em uso, o endereço local e os números de porta, o endereço externo e os números de porta e o estado da conexão.

```powershell
C:∖> netstat

Active Connections

  Proto Local Address           Foreign Address             State

  TCP   192.168.1.124:3126      192.168.0.2:netbios-ssn     ESTABLISHED

  TCP   192.168.1.124:3158      207.138.126.152:http        ESTABLISHED

  TCP   192.168.1.124:3159      207.138.126.169:http        ESTABLISHED

  TCP   192.168.1.124:3161      sc.msn.com:http             ESTABLISHED

  TCP   192.168.1.124:3166      www.cisco.com:http          ESTABLISHED

(output omitted)

C:∖> netstat
```

Por padrão, o comando **netstat** tentará resolver os endereços IP para os nomes de domínio e os números de porta para aplicações bem conhecidas. A opção **n** pode ser usada para exibir endereços IP e números de porta em sua forma numérica.

---

Quando o malware está presente em um computador, ele geralmente abre portas de comunicação no host para enviar e receber dados. O comando **netstat** pode ser usado para procurar conexões de entrada ou saída não autorizadas. Quando usado sozinho, o comando **netstat** exibirá todas as conexões TCP ativas.

Examinando essas conexões, é possível determinar quais dos programas estão escutando conexões que não estão autorizadas. Quando um programa é suspeito de ser malware, uma pequena pesquisa pode ser realizada para determinar sua legitimidade. A partir daí, o processo pode ser encerrado com o Gerenciador de Tarefas, e o software de remoção de malware pode ser usado para limpar o computador.

Para facilitar esse processo, você pode vincular as conexões aos processos em execução que as criaram no Gerenciador de Tarefas. Para fazer isso, abra um prompt de comando com privilégios administrativos e digite o comando **netstat -abno**, conforme mostrado na saída do comando.

```sh
Microsoft Windows [Version 10.0.18363.720]

(c) 2019 Microsoft Corporation. All rights reserved.

C:∖WINDOWS∖system32> **netstat -abno**

Active Connections

   Proto   Local Address         Foreign Address           State           PID

   TCP     0.0.0.0:80               0.0.0.0:0             LISTENING         4

 Can not obtain ownership information

   TCP     0.0.0.0:135              0.0.0.0:0             LISTENING        952

   RpcSs

 [svchost.exe]

   TCP     0.0.0.0:445              0.0.0.0:0             LISTENING        4

 Can not obtain ownership information

   TCP     0.0.0.0:623              0.0.0.0:0             LISTENING        14660

 [LMS.exe]

   TCP     0.0.0.0:3389             0.0.0.0:0             LISTENING        1396

   TermService

 [svchost.exe]

   TCP     0.0.0.0:5040             0.0.0.0:0             LISTENING        9792

   CDPSvc

 [svchost.exe]

   TCP     0.0.0.0:5357             0.0.0.0:0             LISTENING        4

 Can not obtain ownership information

   TCP     0.0.0.0:5593             0.0.0.0:0             LISTENING        4

 Can not obtain ownership information

   TCP     0.0.0.0:8099             0.0.0.0:0             LISTENING       5248

 [SolarWinds TFTP Server.exe]

   TCP     0.0.0.0:16992            0.0.0.0:0             LISTENING       14660
```

**Nota:** Se você não estiver no modo de administrador, aparecerá a mensagem “A operação solicitada requer elevação”. Pesquise Prompt de Comando. Clique com o botão direito do mouse em **Prompt de comando** e escolha **Executar como administrador.**

Examinando as conexões TCP ativas, um analista deve ser capaz de determinar se há algum programa suspeito que esteja escutando conexões de entrada no host. Você também pode rastrear esse processo para o Gerenciador de Tarefas do Windows e cancelar o processo. Pode haver mais de um processo listado com o mesmo nome. Se este for o caso, use o PID para encontrar o processo correto. Cada processo em execução no computador tem um PID exclusivo. Para exibir os PIDs dos processos no Gerenciador de Tarefas, abra o **Gerenciador de Tarefas**, clique com o botão direito do mouse no cabeçalho da tabela e selecione **PID**.

---















