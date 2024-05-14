#SO #Windows 
# Sistemas de Arquivos do Windows

## exFAT

 - Este é um sistema de arquivos simples suportado por muitos sistemas operacionais diferentes.
- O FAT tem limitações para o número de partições, tamanhos de partições e tamanhos de arquivo que pode resolver, portanto, não é mais usado para discos rígidos (HDs) ou unidades de estado sólido (SSDs).
- Tanto o FAT16 quanto o FAT32 estão disponíveis para uso, sendo o FAT32 o mais comum porque tem muito menos restrições do que o FAT16.

## Sistema de Arquivos Hierárquico Plus (HFS+)

- Este sistema de arquivos é usado em computadores MAC OS X e permite nomes de arquivos, tamanhos de arquivo e tamanhos de partição muito mais longos do que os sistemas de arquivos anteriores.
- Embora não seja suportado pelo Windows sem software especial, o Windows é capaz de ler dados de partições HFS+.

## Sistema de arquivos estendido (EXT)

- Este sistema de arquivos é usado com computadores baseados em Linux.
- Embora não seja suportado pelo Windows, o Windows é capaz de ler dados de partições EXT com software especial.

## Novo Sistema de Tecnologia de Arquivos (NTFS)

- Este é o sistema de arquivos mais comumente usado ao instalar o Windows. Todas as versões do Windows e Linux suportam NTFS.
- Computadores Mac-OS X só podem ler uma partição NTFS. Eles são capazes de gravar em uma partição NTFS depois de instalar drivers especiais.

---

O NTFS é o sistema de arquivos mais utilizado para Windows por muitas razões. NTFS suporta arquivos e partições muito grandes e é muito compatível com outros sistemas operacionais. O NTFS também é muito confiável e oferece suporte a recursos de recuperação. Mais importante ainda, ele suporta muitos recursos de segurança. O controle de acesso a dados é alcançado através de descritores de segurança. Esses descritores de segurança contêm permissões e propriedade do arquivo até o nível do arquivo. O NTFS também controla muitos carimbos de data/hora para controlar a atividade do arquivo. Às vezes referido como MACE, os carimbos de data/hora Modificar, Access (acesso), Create (criar) e Entry Modified (entrada modificada) são frequentemente usados em investigações forenses para determinar o histórico de um arquivo ou pasta. O NTFS também suporta criptografia do sistema de arquivos para proteger toda a mídia de armazenamento.

Antes que um dispositivo de armazenamento, como um disco, possa ser usado, ele deve ser formatado com um sistema de arquivos. Por sua vez, antes que um sistema de arquivos possa ser colocado em prática em um dispositivo de armazenamento, o dispositivo precisa ser particionado. Um disco rígido é dividido em áreas denominadas partições. Cada partição é uma unidade lógica de armazenamento que pode ser formatada para armazenar informações, como arquivos de dados ou de aplicações. Durante o processo de instalação, a maioria dos sistemas operacionais particiona e formata automaticamente o espaço disponível na unidade com um sistema de arquivos como o NTFS.

A formatação NTFS cria estruturas importantes no disco para armazenamento de arquivos e tabelas para gravar os locais dos arquivos:

- **Setor de inicialização da partição -** São os primeiros 16 setores da unidade. Ele contém o local da tabela de arquivos mestre (MFT). Os últimos 16 setores contêm uma cópia do setor de inicialização.
- **Master File Table (MFT) -** Esta tabela contém os locais de todos os arquivos e diretórios na partição, incluindo atributos de arquivo, como informações de segurança e carimbos de data/hora.
- **Arquivos de sistema -** São arquivos ocultos que armazenam informações sobre outros volumes e atributos de arquivo.
- **Área do Arquivo** - A área principal da partição onde os arquivos e diretórios são armazenados.

**Nota:** Ao formatar uma partição, os dados anteriores ainda podem ser recuperados porque nem todos os dados são completamente removidos. O espaço livre pode ser examinado e os arquivos podem ser recuperados, o que pode comprometer a segurança. Recomenda-se executar um apagamento seguro em uma unidade que está sendo reutilizada. O apagamento seguro grava dados em toda a unidade várias vezes para garantir que não haja dados restantes.














