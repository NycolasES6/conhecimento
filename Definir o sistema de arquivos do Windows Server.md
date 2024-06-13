#Windows 
# Definir o sistema de arquivos do Windows Server

Antes de poder armazenar dados em um volume, primeiro você precisa formatá-lo. Para fazer isso, selecione o sistema de arquivos que o volume deve usar. Vários sistemas de arquivos estão disponíveis, cada um com suas vantagens e desvantagens.

## O que é um sistema de arquivos?

Um sistema de arquivos fornece uma variedade de recursos que implementam o armazenamento e a recuperação de arquivos em dispositivos de armazenamento. Ele permite que você organize arquivos em uma estrutura hierárquica e controle o formato e a convenção de nomenclatura deles. Os sistemas de arquivos dão suporte a uma ampla variedade de dispositivos de armazenamento, incluindo discos rígidos e mídia removível.

Todos os sistemas de arquivos disponíveis no sistema operacional Windows consistem nos seguintes componentes de armazenamento:

- Arquivos. Um arquivo é um agrupamento lógico de dados relacionados.
- Diretórios. Um diretório é uma coleção hierárquica de diretórios e arquivos.
- Volumes. Um volume é uma coleção de diretórios e arquivos.

## Quais são os recursos diferenciais dos tipos de sistema de arquivos do Windows Server?

Os tipos de sistema de arquivos do Windows Server incluem:

- FAT (tabela de alocação de arquivos), FAT32 e exFAT (tabela de alocação de arquivos estendida).
- O sistema de arquivos NT (NTFS).
- ReFS (Sistema de Arquivos Resiliente).

### FAT, FAT32 e exFAT

O sistema de arquivos FAT é o mais simples disponível no suporte a sistemas operacionais do Windows. Ele controla os objetos do sistema de arquivos usando uma tabela no nível do volume. O FAT mantém duas cópias da tabela para resiliência. As tabelas e o diretório raiz devem residir em um local fixo no disco formatado.

Devido à limitação de tamanho da tabela de alocação de arquivos, não é possível usar o FAT para criar volumes com mais de 4 GB (gigabytes). Para acomodar discos maiores, a Microsoft desenvolveu o FAT32, que dá suporte a partições de até 64 GB.

O exFAT é o sistema de arquivos projetado para unidades flash, com suporte para tamanhos de volume maiores do que aqueles disponíveis em FAT32. Ele funciona com dispositivos de mídia, como TVs de painel plano modernas, centros de mídia e players de mídia portáteis.

O FAT e o FAT32 não fornecem segurança no nível do sistema de arquivos. Você não deve criar volumes FAT ou FAT32 em discos anexados aos servidores que executam qualquer um dos sistemas operacionais Windows Server. No entanto, você pode considerar o uso do FAT, FAT32 ou exFAT para formatar mídias externas, como pen drives.

### NTFS

Tradicionalmente, o NTFS tem sido a opção mais comum do sistema de arquivos para os sistemas operacionais Windows Server. O NTFS oferece várias melhorias em relação ao FAT, aproveitando estruturas de dados avançadas para melhorar o desempenho, a confiabilidade e a utilização do espaço em disco. O NTFS também fornece segurança interna, com recursos de controle de acesso como ACLs (listas de controle de acesso), auditoria, diário de sistema de arquivos e criptografia. O NTFS também dá suporte à criptografia e compactação do sistema de arquivos, embora elas sejam mutuamente exclusivas para que você não possa aplicar ambas no mesmo arquivo ou pasta.

### ReFS

A Microsoft introduziu o ReFS (Sistema de Arquivos Resiliente) no Windows Server 2012 para aprimorar os recursos do NTFS. Conforme indicado por seu nome, um dos principais pontos fortes do ReFS é sua resiliência aprimorada para dados corrompidos por meio de um mecanismo de detecção mais preciso e a capacidade de corrigir problemas de integridade online. O ReFS também dá suporte para tamanhos maiores de arquivos e volumes individuais, incluindo a eliminação de duplicação.

Na maioria dos casos, o ReFS é a melhor opção de sistema de arquivos para volumes de dados no Windows Server 2022. No entanto, lembre-se de que o ReFS não oferece paridade completa de recursos com o NTFS. Por exemplo, o ReFS não dá suporte à compactação e criptografia no nível do arquivo. Ele também não é adequado para volumes de inicialização e mídia removível.

## O que são setores e unidades de alocação?

Um setor é a quantidade mínima de dados que podem ser lidos ou gravados em um disco rígido. Tradicionalmente, o tamanho do setor foi fixado em 512 bytes. As unidades modernas dão suporte a tamanhos maiores, como 1 KB, 2 KB ou 4 KB. A formatação de um volume com um sistema de arquivos combina setores em clusters lógicos, também chamados de unidades de alocação. Por exemplo, se os setores de um disco rígido forem de 512 bytes, um cluster de 4 KB terá oito setores e um cluster de 64 KB terá 128 setores. Se você iniciar o processo de formatação, terá a opção de designar o tamanho de cluster preferencial. Como alternativa, você pode contar com padrões, que determinam o tamanho do cluster com base no tamanho do volume.

O tamanho do cluster representa a menor quantidade de espaço em disco que pode ser usada para manter um arquivo, com base no formato definido pelo sistema de arquivos. Quando o tamanho do arquivo não corresponde aos tamanhos de cluster individual ou múltiplo, isso resulta em algum grau de ineficiência no uso do espaço em disco. No entanto, a escolha de um tamanho de cluster menor pode afetar negativamente o desempenho, pois a leitura ou gravação de um arquivo pode exigir um número maior de operações de disco. Além de escolher o tamanho de cluster ideal, convém garantir que os limites do cluster fiquem alinhados aos setores subjacentes.

Para melhorar o desempenho, tente deixar o tamanho da unidade de alocação o mais próximo possível ao do arquivo típico ou ao tamanho de registro gravado ou lido no disco. Por exemplo, se você tiver um banco de dados que grava registros de 8.192 bytes, o tamanho da unidade de alocação ideal será de 8 KB. Essa configuração permitiria que o sistema operacional gravasse um registro completo em uma única unidade de alocação no volume. Usando um tamanho de unidade de alocação de 4 KB, o sistema operacional teria que dividir o registro em duas unidades de alocação e gerenciar atualizações para os metadados subjacentes. Usando uma unidade de alocação de tamanho adequado, você pode reduzir a carga de trabalho no subsistema de disco do servidor.









