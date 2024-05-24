#redes #Windows #SO 
# Acessando recursos de rede no Windows

Como outros sistemas operacionais, o Windows usa rede para muitos aplicativos diferentes, como serviços da Web, email e arquivos. Originalmente desenvolvido pela IBM, a Microsoft ajudou no desenvolvimento do protocolo SMB (Bloco de mensagem do servidor) para compartilhar recursos de rede. O SMB é usado principalmente para acessar arquivos em hosts remotos. O formato UNC (Convenção Universal de Nomenclatura) é usado para se conectar a recursos, por exemplo:

**∖∖servername∖sharename∖file**

No UNC, nome_do_servidor é o servidor que está hospedando o recurso. Pode ser um nome DNS, um nome NetBIOS ou simplesmente um endereço IP. O nome do compartilhamento é a raiz da pasta no sistema de arquivos no host remoto, enquanto o arquivo é o recurso que o host local está tentando encontrar. O arquivo pode estar mais profundo dentro do sistema de arquivos e essa hierarquia precisará ser indicada.

Ao compartilhar recursos na rede, a área do sistema de arquivos que será compartilhada precisará ser identificada. O controle de acesso pode ser aplicado às pastas e arquivos para restringir usuários e grupos a funções específicas, como ler, gravar ou negar. Há também compartilhamentos especiais que são criados automaticamente pelo Windows. Essas ações são chamadas de ações administrativas. Um compartilhamento administrativo é identificado pelo cifrão ($) que vem após o nome do compartilhamento. Cada volume de disco tem um compartilhamento administrativo, representado pela letra do volume e o $, como C$, D$ ou E\$. A pasta de instalação do Windows é compartilhada como admin\$, a pasta das impressoras é compartilhada como print\$ e há outros compartilhamentos administrativos que podem ser conectados. Somente usuários com privilégios administrativos podem acessar esses compartilhamentos.

A maneira mais fácil de se conectar a um compartilhamento é digitar o UNC do compartilhamento no Explorador de Arquivos do Windows, na caixa na parte superior da tela que mostra a listagem de rastreamento do local atual do sistema de arquivos. Quando o Windows tentar se conectar ao compartilhamento, você será solicitado a fornecer credenciais para acessar o recurso. Lembre-se de que, como o recurso está em um computador remoto, as credenciais precisam ser para o computador remoto, não para o computador local.

Além de acessar compartilhamentos em hosts remotos, você também pode fazer login em um host remoto e manipular esse computador, como se fosse local, para fazer alterações de configuração, instalar software ou solucionar um problema. No Windows, esse recurso usa o protocolo RDP (Protocolo de Área de Trabalho Remota). Ao investigar incidentes de segurança, um analista de segurança usa o RDP frequentemente para acessar computadores remotos. Para iniciar o RDP e conectar-se a um computador remoto, procure área de trabalho remota e clique no aplicativo. A janela Conexão de área de trabalho remota é mostrada na figura.

Como o RDP foi projetado para permitir que usuários remotos controlem hosts individuais, ele é um alvo natural para atores de ameaças. Deve-se ter cuidado ao ativar o RDP, especialmente em versões legado sem os patches do Windows, como aquelas que ainda são encontradas em sistemas de controle industrial. Deve-se ter cuidado para limitar a exposição do RDP à internet, e abordagens de segurança e políticas de controle de acesso, como Zero Trust, devem ser usadas para limitar o acesso a hosts internos.

![[Pasted image 20240514134415.jpg]]



































