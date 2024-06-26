 O gerenciamento do sistema de arquivos no Linux é um processo complexo que envolve a organização e manutenção dos dados armazenados em um disco ou outro dispositivo de armazenamento.
 
 Linux é um sistema operacional poderoso que oferece suporte a uma ampla variedade de sistemas de arquivos, incluindo ext2, ext3, ext4, XFS, Btrfs, NTFS e muito mais.
 
 O sistema de arquivos Linux é baseado no sistema de arquivos Unix, que é uma estrutura hierárquica composta por vários componentes.No topo desta estrutura está a tabela de inodes, a base de todo o sistema de arquivos.

Os inodes contêm metadados sobre o arquivo ou diretório, como permissões, tamanho, tipo, proprietário e assim por diante.

Os arquivos podem ser armazenados no sistema de arquivos Linux de duas maneiras:

- Arquivos regulares
- Diretórios

Arquivos regulares são o tipo de arquivo mais comum e são armazenados no diretório raiz do sistema de arquivos.

Diretórios são usados ​​para armazenar coleções de arquivos.
Cada arquivo e diretório possui um conjunto associado de permissões que determina quem pode ler, gravar e executar o arquivo.

As mesmas permissões se aplicam a todos os usuários, portanto, se as permissões de um usuário forem alteradas, todos os outros usuários também serão afetados.

```bash
ls -il

#total 0
#10678872 -rw-r--r--  1 cry0l1t3  htb  234123 Feb 14 19:30 myscript.py
#10678869 -rw-r--r--  1 cry0l1t3  htb   43230 Feb 14 11:52 notes.txt
```

## Discos e unidades

A principal ferramenta para gerenciamento de disco no Linux é o `fdisk`, que nos permite criar, excluir e gerenciar partições em uma unidade. Ele também pode exibir informações sobre a tabela de partições, incluindo o tamanho e o tipo de cada partição.

Cada partição pode então ser formatada com um sistema de arquivos específico, como ext4, NTFS ou FAT32, e pode ser montada como um sistema de arquivos separado.

A ferramenta de particionamento mais comum no Linux também é `fdisk`, `gpart` e `GParted`.

## Fdisk

```bash
sudo fdisk -l

#Disk /dev/vda: 160 GiB, 171798691840 bytes, 335544320 sectors
#Units: sectors of 1 * 512 = 512 bytes
#Sector size (logical/physical): 512 bytes / 512 bytes
#I/O size (minimum/optimal): 512 bytes / 512 bytes
#Disklabel type: dos
#Disk identifier: 0x5223435f

#Device     Boot     Start       End   Sectors  Size Id Type
#/dev/vda1  *         2048 158974027 158971980 75.8G 83 Linux
#/dev/vda2       158974028 167766794   8792767  4.2G 82 Linux swap / Solaris

#Disk /dev/vdb: 452 KiB, 462848 bytes, 904 sectors
#Units: sectors of 1 * 512 = 512 bytes
#Sector size (logical/physical): 512 bytes / 512 bytes
#I/O size (minimum/optimal): 512 bytes / 512 bytes
```

## Mount

Cada partição ou unidade lógica precisa ser atribuída a um diretório específico no Linux. Este processo é chamado de montagem.

A montagem envolve anexar uma unidade a um diretório específico, tornando-a acessível à hierarquia do sistema de arquivos. Depois que uma unidade é montada, ela pode ser acessada e manipulada como qualquer outro diretório do sistema.

A ferramenta `mount` é usada para montar sistemas de arquivos no Linux e o arquivo `/etc/fstab` é usado para definir os sistemas de arquivos padrão que são montados no momento da inicialização.

### Sistemas de arquivos montados na inicialização

```bash
cat /etc/fstab

# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a device; this may
# be used with UUID= as a more robust way to name devices that works even if
# disks are added and removed. See fstab(5).
#
# <file system>                      <mount point>  <type>  <options>  <dump>  <pass>
UUID=3d6a020d-...SNIP...-9e085e9c927a /              btrfs   subvol=@,defaults,noatime,nodiratime,nodatacow,space_cache,autodefrag 0 1
UUID=3d6a020d-...SNIP...-9e085e9c927a /home          btrfs   subvol=@home,defaults,noatime,nodiratime,nodatacow,space_cache,autodefrag 0 2
UUID=21f7eb94-...SNIP...-d4f58f94e141 swap           swap    defaults,noatime 0 0
```

Para visualizar os sistemas de arquivos atualmente montados, podemos usar o comando “mount” sem quaisquer argumentos.

A saída mostrará uma lista de todos os sistemas de arquivos montados atualmente, incluindo o nome do dispositivo, tipo de sistema de arquivos, ponto de montagem e opções.

### Listar unidades montadas

```bash
mount

#sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
#proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
#udev on /dev type devtmpfs (rw,nosuid,relatime,size=4035812k,nr_inodes=1008953,mode=755,inode64)
#devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
#tmpfs on /run type tmpfs (rw,nosuid,nodev,noexec,relatime,size=814580k,mode=755,inode64)
#/dev/vda1 on / type btrfs (rw,noatime,nodiratime,nodatasum,nodatacow,space_cache,autodefrag,subvolid=257,subvol=/@)
```

Para montar um sistema de arquivos, podemos usar o comando `mount` seguido do nome do dispositivo e do ponto de montagem. 
Por exemplo, para montar uma unidade USB com o nome do dispositivo `/dev/sdb1`no diretório `/mnt/usb`, usaríamos o seguinte comando:

### Monte uma unidade USB

```bash
sudo mount /dev/sdb1 /mnt/usb
cd /mnt/usb && ls -l

#total 32
#drwxr-xr-x 1 root root   18 Oct 14  2021 'Account Takeover'
#drwxr-xr-x 1 root root   18 Oct 14  2021 'API Key Leaks'
#drwxr-xr-x 1 root root   18 Oct 14  2021 'AWS Amazon Bucket S3'
#drwxr-xr-x 1 root root   34 Oct 14  2021 'Command Injection'
#drwxr-xr-x 1 root root   18 Oct 14  2021 'CORS Misconfiguration'
#drwxr-xr-x 1 root root   52 Oct 14  2021 'CRLF Injection'
#drwxr-xr-x 1 root root   30 Oct 14  2021 'CSRF Injection'
#drwxr-xr-x 1 root root   18 Oct 14  2021 'CSV Injection'
#drwxr-xr-x 1 root root 1166 Oct 14  2021 'CVE Exploits'
#...SNIP...
```

## Umount

Para desmontar um sistema de arquivos no Linux, podemos usar o comando `umount` seguido do ponto de montagem do sistema de arquivos que queremos desmontar. O ponto de montagem é o local no sistema de arquivos onde o sistema de arquivos está montado e está acessível para nós. Por exemplo, para desmontar a unidade USB que foi montada anteriormente no diretório `/mnt/usb`, usaríamos o seguinte comando:

```bash
sudo umount /mnt/usb
```

É importante observar que devemos ter permissões suficientes para desmontar um sistema de arquivos. Também não podemos desmontar um sistema de arquivos que esteja em uso por um processo em execução.

Para garantir que não haja processos em execução usando o sistema de arquivos, podemos usar o comando `lsof` para listar os arquivos abertos no sistema de arquivos.

```bash
lsof | grep cry0l1t3

#vncserver 6006        cry0l1t3  mem       REG      0,24       402274 /usr/bin/perl (path dev=0,26)
#vncserver 6006        cry0l1t3  mem       REG      0,24      1554101 /usr/lib/locale/aa_DJ.utf8/LC_COLLATE (path dev=0,26)
#vncserver 6006        cry0l1t3  mem       REG      0,24       402326 /usr/lib/x86_64-linux-gnu/perl-base/auto/POSIX/POSIX.so (path dev=0,26)
#vncserver 6006        cry0l1t3  mem       REG      0,24       402059 /usr/lib/x86_64-linux-gnu/perl/5.32.1/auto/Time/HiRes/HiRes.so (path dev=0,26)
#vncserver 6006        cry0l1t3  mem       REG      0,24      1444250 /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so (path dev=0,26)
#vncserver 6006        cry0l1t3  mem       REG      0,24       402327 /usr/lib/x86_64-linux-gnu/perl-base/auto/Socket/Socket.so (path dev=0,26)
#vncserver 6006        cry0l1t3  mem       REG      0,24       402324 /usr/lib/x86_64-linux-gnu/perl-base/auto/IO/IO.so (path dev=0,26)
#...SNIP...
```

Se encontrarmos algum processo que esteja usando o sistema de arquivos, precisaremos interrompê-lo antes de podermos desmontar o sistema de arquivos.

O arquivo `/etc/fstab` contém informações sobre todos os sistemas de arquivos montados no sistema, incluindo as opções para montagem automática no momento da inicialização e outras opções de montagem.

Para desmontar um sistema de arquivos automaticamente no desligamento, precisamos adicionar a opção `noauto` à entrada no arquivo `/etc/fstab` desse sistema de arquivos. Isso seria parecido, por exemplo, com o seguinte:

#### arquivo Fstab

```txt
/dev/sda1 / ext4 defaults 0 0
/dev/sda2 /home ext4 defaults 0 0
/dev/sdb1 /mnt/usb ext4 rw,noauto,user 0 0
192.168.1.100:/nfs /mnt/nfs nfs defaults 0 0
```

## SWAP

Quando o sistema fica sem memória física, o kernel transfere páginas inativas de memória para o espaço de troca, liberando memória física para uso por processos ativos. Este processo é conhecido como swap.

O espaço de troca pode ser criado durante a instalação do sistema operacional ou a qualquer momento depois usando os comandos `mkswap` e `swapon`.

O comando `mkswap` é usado para configurar uma área de troca do Linux em um dispositivo ou arquivo, enquanto o comando `swapon` é usado para ativar uma área de troca.

Além de ser usado como uma extensão da memória física, o espaço de troca também pode ser usado para hibernação, que é um recurso de gerenciamento de energia que permite ao sistema salvar seu estado no disco e depois desligar em vez de desligar completamente. Quando o sistema for ligado posteriormente, ele poderá restaurar seu estado a partir do espaço de troca, retornando ao estado em que estava antes de ser desligado.

