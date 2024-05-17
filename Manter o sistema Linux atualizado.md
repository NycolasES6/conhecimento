#Linux 
# Manter o sistema Linux atualizado

Também conhecido como patches, as atualizações do sistema operacional são lançadas periodicamente por empresas de sistema operacional para resolver quaisquer vulnerabilidades conhecidas em seus sistemas operacionais. Embora as empresas tenham programações de atualização, o lançamento de atualizações não programadas do sistema operacional pode acontecer quando uma vulnerabilidade importante é encontrada no código do sistema operacional. Os sistemas operacionais modernos alertarão o usuário quando atualizações estiverem disponíveis para download e instalação, mas o usuário pode verificar as atualizações a qualquer momento.

A tabela a seguir compara os comandos de distribuição Arch Linux e Debian / Ubuntu Linux para realizar operações básicas do sistema de pacotes.

|Tarefa|Arch|Debian/Ubuntu|
|---|---|---|
|Instalar um pacote pelo nome|pacman -S|apt install|
|Remover um pacote pelo nome|pacman -Rs|apt remover|
|Atualize um pacote local|pacman -Syy|apt-get update|
|Atualizar todos os pacotes atualmente instalados|pacman -Syu|apt-get upgrade|

Uma GUI do Linux também pode ser usada para verificar e instalar atualizações manualmente. No Ubuntu, por exemplo, para instalar atualizações, clique em **Dash Search Box** , digite **Atualizador de Software** e clique no ícone **Atualizador de Software**, conforme mostrado na figura.

![[Pasted image 20240515115528.jpg]]



