#Linux #SO 
# A importância dos arquivos de texto no Linux

No Linux, tudo é tratado como um arquivo. Isso inclui a memória, os discos, o monitor e os diretórios. Por exemplo, do ponto de vista do sistema operacional, mostrar informações na tela significa gravar no arquivo que representa o dispositivo de exibição. Não deve ser surpresa que o próprio computador esteja configurado através de arquivos. Conhecidos como arquivos de configuração, eles geralmente são arquivos de texto usados para armazenar ajustes e configurações para aplicativos ou serviços específicos. Praticamente tudo no Linux depende de arquivos de configuração para funcionar. Alguns serviços têm não um, mas vários arquivos de configuração.

Os usuários com níveis de permissão adequados podem usar editores de texto para alterar o conteúdo dos arquivos de configuração. Depois que as alterações são feitas, o arquivo é salvo e pode ser usado pelo serviço ou aplicativo relacionado. Os usuários podem especificar exatamente como querem que qualquer aplicativo ou serviço se comporte. Quando iniciados, serviços e aplicativos verificam o conteúdo de arquivos de configuração específicos para ajustar seu comportamento de acordo.

Na figura, o administrador abriu o arquivo de configuração do host em **nano** para edição. O arquivo host contém mapeamentos estáticos de endereços IP do host para nomes. Os nomes servem como atalhos que permitem a conexão com outros dispositivos usando um nome em vez de um endereço IP. Somente o superusuário pode alterar o arquivo host.

**Nota:** O administrador usou o comando **sudo nano /etc/hosts**para abrir o arquivo. O comando **sudo** (abreviação de “superusuário do”) invoca o privilégio de superusuário para usar o editor de texto nano para abrir o arquivo host.

![[Pasted image 20240514175548.png]]