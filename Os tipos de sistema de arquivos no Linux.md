#Linux 
# Os tipos de sistema de arquivos no Linux

Existem muitos tipos diferentes de sistemas de arquivos, variando em propriedades de velocidade, flexibilidade, segurança, tamanho, estrutura, lógica e muito mais. Cabe ao administrador decidir qual tipo de sistema de arquivos melhor se adequa ao sistema operacional e aos arquivos que ele armazenará.

### ext2 (segundo sistema de arquivos estendido)

- ext2 era o sistema de arquivos padrão em várias distribuições Linux principais até ser suplantado pelo ext3.
- Quase totalmente compatível com ext2, ext3 também suporta registro no diário (veja abaixo).
- O ext2 ainda é o sistema de arquivos escolhido para mídia de armazenamento baseada em flash porque sua falta de diário aumenta o desempenho e minimiza o número de gravações.
- Como os dispositivos de memória flash têm um número limitado de operações de gravação, a minimização das operações de gravação aumenta a vida útil do dispositivo.
- No entanto, os kernels Linux contemporâneos também suportam ext4, um sistema de arquivos ainda mais moderno, com melhor desempenho e que também pode operar em um modo sem diário.

### ext3 (terceiro sistema de arquivos estendido)

- ext3 é um sistema de arquivo registrado projetado para melhorar o sistema de arquivo ext2 existente.
- Um diário, o principal recurso adicionado a ext3, é uma técnica usada para minimizar o risco de danos ao sistema de arquivos no caso de perda repentina de energia.
- Os sistemas de arquivos mantém um registro (ou diário) de todas as alterações do sistema de arquivos prestes a ser feitas.
- Se o computador falhar antes da conclusão da alteração, o diário pode ser usado para restaurar ou corrigir quaisquer eventuais problemas criados pela falha.
- O tamanho máximo do arquivo em sistemas de arquivos ext3 é 32 TB.

### ext4 (quarto sistema de arquivos estendido)

- Projetado como um sucessor de ext3, ext4 foi criado com base em uma série de extensões para ext3.
- Enquanto as extensões melhoram o desempenho do ext3 e aumentam o tamanho dos arquivos suportados, os desenvolvedores do kernel Linux estavam preocupados com problemas de estabilidade e se opuseram a adicionar as extensões ao ext3 estável.
- O projeto ext3 foi dividido em dois; um mantido como ext3 e seu desenvolvimento normal e o outro, denominado ext4, incorporou as extensões mencionadas.

### NFS (Sistema de arquivos de rede)

- NFS é um sistema de arquivos baseado em rede, permitindo acesso a arquivos pela rede.
- Do ponto de vista do usuário, não há diferença entre acessar um arquivo armazenado localmente ou em outro computador da rede.
- O NFS é um padrão aberto, o que permite que qualquer pessoa o implemente.

### CDFS (Sistema de arquivo de disco compacto)

- O CDFS foi criado especificamente para mídia de disco óptico.

### Sistema de troca de arquivos

- O sistema de arquivos de troca é usado pelo Linux quando fica sem RAM.
- Tecnicamente, é uma partição de swap que não tem um sistema de arquivos específico, mas é relevante para a discussão do sistema de arquivos.
- Quando isso acontece, o kernel move o conteúdo inativo da RAM para a partição de troca no disco.
- Embora as partições de permuta (também conhecidas como espaço de permuta) possam ser úteis para computadores Linux com uma quantidade limitada de memória, elas não devem ser consideradas como uma solução primária.
- A partição de permuta é armazenada no disco que tem velocidades de acesso muito mais baixas do que a RAM.

### HFS Plus ou HFS+ (Sistema de Arquivos Hierárquico Plus)

- Um sistema de arquivos usado pela Apple em seus computadores Macintosh.
- O kernel Linux inclui um módulo para montar HFS+ para operações de leitura-gravação.

### APFS (Sistema de Arquivos Apple)

- Um sistema de arquivos atualizado que é usado por dispositivos Apple. Ele fornece criptografia forte e é otimizado para unidades flash e de estado sólido.

### Registro mestre de inicialização (MBR)

- Localizado no primeiro setor de um computador particionado, o MBR armazena todas as informações sobre a forma como o sistema de arquivos é organizado.
- O MBR entrega rapidamente o controle a uma função de carregamento, que carrega o sistema operacional.

---

Montagem é o termo usado para o processo de atribuição de um diretório a uma partição. Após uma operação de montagem bem-sucedida, o sistema de arquivos contido na partição é acessível através do diretório especificado. Neste contexto, o diretório é chamado de ponto de montagem para esse sistema de arquivos. Os usuários do Windows podem estar familiarizados com um conceito semelhante; a letra da unidade.

A saída do comando mostra a saída do comando **mount** emitido na VM Cisco CyberOps.

```txt
[analyst@secOps ~]$ mount

proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)

sys on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)

dev on /dev type devtmpfs (rw,nosuid,relatime,size=494944k,nr_inodes=123736,mode=755)

run on /run type tmpfs (rw,nosuid,nodev,relatime,mode=755)

/dev/sda1 on / type ext4 (rw,relatime)

securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)

tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)

devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)

tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)

cgroup2 on /sys/fs/cgroup/unified type cgroup2 (rw,nosuid,nodev,noexec,relatime,nsdelegate)

cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,name=systemd)

pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)

none on /sys/fs/bpf type bpf (rw,nosuid,nodev,noexec,relatime,mode=700)

cgroup on /sys/fs/cgroup/rdma type cgroup (rw,nosuid,nodev,noexec,relatime,rdma)

cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)

cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)

cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)

cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)

cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)

cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)

cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)

cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)

cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)

cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)

systemd-1 on /proc/sys/fs/binfmt_misc type autofs

(rw,relatime,fd=29,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=11792)

debugfs on /sys/kernel/debug type debugfs (rw,nosuid,nodev,noexec,relatime)

tracefs on /sys/kernel/tracing type tracefs (rw,nosuid,nodev,noexec,relatime)

hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime,pagesize=2M)

mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime)

tmpfs on /tmp type tmpfs (rw,nosuid,nodev)
```

Quando emitido sem opções, **mount** retorna a lista de sistemas de arquivos atualmente montados em um computador Linux. Embora muitos dos sistemas de arquivos mostrados estejam fora do escopo deste curso, observe o sistema de arquivos raiz (destacado). O sistema de arquivos raiz é representado pelo símbolo “/” e contém todos os arquivos no computador por padrão. Também é mostrado na saída que o sistema de arquivos raiz foi formatado como ext4 e ocupa a primeira partição da primeira unidade (/dev/sda1).