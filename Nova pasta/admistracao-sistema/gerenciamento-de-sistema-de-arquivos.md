## Gerenciamento de sitemas de arquivos

O gerenciamento do sistema de arquivos no Linux é um processo complexo que envolve a organização e manutenção dos dados armazenados em um disco ou outro dispositivo de armazenamento. Linux é um sistema operacional poderoso que oferece suporte a uma ampla variedade de sistemas de arquivos, incluindo ext2, ext3, ext4, XFS, Btrfs, NTFS e muito mais. Cada um desses sistemas de arquivos oferece recursos e benefícios exclusivos, e a melhor escolha para qualquer situação dependerá dos requisitos específicos do aplicativo ou usuário. Por exemplo, ext2 é adequado para tarefas básicas de gerenciamento de sistema de arquivos, enquanto Btrfs oferece integridade robusta de dados e recursos de snapshot. Além disso, o NTFS é útil quando é necessária compatibilidade com o Windows. Não importa a situação, é importante analisar adequadamente as necessidades do aplicativo ou do usuário antes de selecionar um sistema de arquivos.

O sistema de arquivos Linux é baseado no sistema de arquivos Unix, que é uma estrutura hierárquica composta por vários componentes. No topo desta estrutura está a tabela de inodes, a base de todo o sistema de arquivos. A tabela inode é uma tabela de informações associadas a cada arquivo e diretório em um sistema Linux. Os inodes contêm metadados sobre o arquivo ou diretório, como permissões, tamanho, tipo, proprietário e assim por diante. A tabela inode é como um banco de dados de informações sobre cada arquivo e diretório em um sistema Linux, permitindo que o sistema operacional acesse e gerencie arquivos rapidamente. Os arquivos podem ser armazenados no sistema de arquivos Linux de duas maneiras:

 - Arquivos normais
 - Diretórios

Arquivos regulares são o tipo de arquivo mais comum e são armazenados no diretório raiz do sistema de arquivos. Diretórios são usados ​​para armazenar coleções de arquivos. Quando um arquivo é armazenado em um diretório, o diretório é conhecido como diretório pai dos arquivos. Além de arquivos e diretórios regulares, o Linux também suporta links simbólicos, que são referências a outros arquivos ou diretórios. Links simbólicos podem ser usados ​​para acessar rapidamente arquivos localizados em diferentes partes do sistema de arquivos. Cada arquivo e diretório precisa ser gerenciado em termos de permissões. As permissões controlam quem tem acesso aos arquivos e diretórios. Cada arquivo e diretório possui um conjunto associado de permissões que determina quem pode ler, gravar e executar o arquivo. As mesmas permissões se aplicam a todos os usuários, portanto, se as permissões de um usuário forem alteradas, todos os outros usuários também serão afetados.

`$ ls -il`

## Discos e unidades

O gerenciamento de disco no linux envolve o gerenciamento de dispositivos de armazenamento físico, incluindo discos rígidos, unidades de estado sólido e dispositivos de armazenamento removíveis. A principal ferramenta para gerenciamento de disco no linux é o **fdisk**, que nos permite criar, excluir e gerenciar partições em uma unidade. Ele também pode exibir informações sobre a tabela de partições, incluindo o tamanho e o tipo de cada partição. Particionar uma unidade no linux envolve dividir o espaço de armazenamento físico em seções lógicas separadas. Cada partição pode então ser formatada com um sistema de arquivos específico,  como ext4, NTFS ou FAT32, e pode ser montada como um sistema de arquivos separado. A ferramenta de particionamento mais comum no Linux também é **fdisk**, **gpart** e **GParted**.

## fdisk

`$ sudo fdisk -l`

## mount

Cada partição ou unidade lógica precisa ser atribuída a um diretório específico no Linux. Este processo é chamado de montagem. A montagem envolve anexar uma unidade a um diretório específico, tornando-a acessível à hierarquia do sistema de arquivos. Depois que uma unidade é montada, ela pode ser acessada e manipulada como qualquer outro diretório do sistema. A ferramenta **mount** é usada para montar sistemas de arquivos no Linux e o arquivo **/etc/fstab** é usado para definir os sistemas de arquivos padrão que são montados no momento da inicialização.

### Sistemas de arquivos montados na inicialização

`$ cat /etc/fstab`

Para visualizar os sistemas de arquivos atualmente montados, podemos usar o comando "mount" sem quaisquer argumentos. A saída mostrará uma lista de todos os sistemas de arquivos montados atualmente, incluindo o nome do dispositivo, tipo de sistema de arquivos, ponto de montagem e opções.

### Listar unidades montadas

`$ mount`

Para montar uma unidade de arquivos, podemos usar o v=comando `mount` seguido do nome do dispositivo e do ponto de montagem. Por exemplo, para montar uma unidade USB com o nome do dispositivo **/dev/sdb1** no diretório **/mnt/usb**, usaríamos o seguinte comando:

### Montagem USB

`$ sudo mount /dev/sdb1 /mnt/usb`

`$ cd /mnt/usb && ls -l`

Para desmontar um sistema de arquivos no Linux, podemos usar o comando `mount` seguido do ponto de montagem do sistema de arquivos que queremos desmontar. O ponto de montagem é o local no sistema de arquivos onde o sistema de arquivos está montado e está acessível para nós. Por exemplo, para desmontar a unidade USB que foi montada anteriormente no diretório **/mnt/usb/**, usaríamos o seguinte comando:

### umount

`$ sudo umount /mnt/usb`

É importante observar que devemos ter permissões suficientes parar desmontar um sistema de arquivos. Também não podemos desmontar um sistema de arquivos que esteja em uso por um processo em execução. Para garantir que não haja processos em execução usando o sistema de arquivos, podemos usar o comando `lsof` para listar os arquivos abertos no sistema de arquivos.

`$ lsof | grep cry0l1t3`

Se encontrarmos algum processo que esteja usando o sistema de arquivos, precisaremos interrompê-lo antes de podermos desmontar o sistema de arquivos. Além disso, também podemos desmontar um sistema de arquivos automaticamente quando o sistema é desligado, adicionando uma entrada ao arquivo **/etc/fstab***. O arquivo **/etc/fstab** contém informações sobre todos os sistemas de arquivos montados no sistema, incluindo as opções para montagem automática no momento da inicialização e outras opções de montagem. Para desmontar um sistema de arquivos automaticamente no desligamento, precisamos adicionar a opção **noauto** à entrada no arquivo **/etc/fstab** desse sistema de arquivos. Isso seria parecido, por exemplo, com o seguinte:

Arquivo fstab

>/dev/sda1 / ext4 defaults 0 0 \
>/dev/sda2 /home ext4 defaults 0 0 \
>/dev/sdb1 /mnt/usb ext4 rw,noauto,user 0 0 \
>192.168.1.100:/nfs /mnt/nfs nfs defaults 0 0

## swap

O espaço swap é um aspecto crucial do gerenciamento de memória no linux e desempenha um papel importante para garantir que o sistema funcione sem problemas, mesmo quando a memória física disponível estiver esgotada. Quando o sistema fica sem memória física, o kernel transfere páginas inativas de memória para o espaço de troca, liberando memória fisíca para uso por processos ativos. Este processo é conhecido como troca.

O espaço de troca pode ser criado durante a instalação do sistema operacional ou qualquer momento depois usando os comandos `mkswap` e `swapon`. O comando `mkswap` é usado para configurar uma área de troca do Linux em um dispositivo ou arquivo, enquanto o comando `swapon` é usado para ativar uma área de troca. O tamanho do espaço de troca é uma questão de preferência pessoal e depende da quantidade de memória física instalada no sistema e do tipo de uso ao qual o sistema estará sujeito. Ao criar um espaço de troca adequado disponível quando necessário. Também é importante garantir que o espaço de troca seja criptografado, pois dados confidenciais podem ser armazenados temporariamente no espaço de troca.

Além de ser usado como uma extensão da memória física, o espaço de troca também pode ser usado para hibernação, que é um recurso de gerenciamento de energia que permite ao sistema salvar seu estado no disco e depois desligar em vez de desligar completamente. Quando o sistema for ligado posteriormente, ele poderá restaurar seu estado a partir do espaço de troca, retornando ao estado em que estava antes de ser desligado.

