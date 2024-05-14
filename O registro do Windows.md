#SO #Windows 
# O registro do Windows

O Windows armazena todas as informações sobre hardware, aplicativos, usuários e configurações do sistema em um banco de dados grande conhecido como o Registro. As formas como esses objetos interagem também são registradas, como quais arquivos um aplicativo abre e todos os detalhes de propriedade de pastas e aplicativos. O registro é um banco de dados hierárquico onde o nível mais alto é conhecido como um ramo, abaixo que existem chaves, seguido por subchaves. Os valores armazenam dados e são armazenados nas chaves e subchaves. Uma chave do Registro pode ter até 512 níveis de profundidade.

- HKEY_CURRENT_USER (HKCU) - Contém informações sobre o usuário conectado no momento.
- HKEY_USERS (HKU) - Contém informações relativas a todas as contas de usuário no host.
- HKEY_CLASSES_ROOT (HKCR) - Contém informações sobre registros OLE (vinculação e incorporação de objetos). OLE permite que os usuários incorporem objetos de outros aplicativos (como uma planilha) em um único documento (como um documento do Word).
- HKEY_LOCAL_MACHINE (HKLM) - Contém informações relacionadas ao sistema.
- HKEY_CURRENT_CONFIG (HKCC) - Contém informações sobre o perfil de hardware atual.

Novas seções (hives) não podem ser criadas. As chaves do Registro e os valores nas seções podem ser criados, modificados ou excluídos por uma conta com privilégios administrativos. Como mostrado na figura, a ferramenta **regedit.exe** usada para modificar o registro. Tenha muito cuidado ao usar esta ferramenta. Alterações menores no registro podem ter efeitos maciços ou mesmo catastróficos.

![[Pasted image 20240514110702.jpg]]

A navegação no registro é muito semelhante ao explorador de arquivos do Windows. Use o painel esquerdo para navegar nas seções (hives) e na estrutura abaixo dele e use o painel direito para ver o conteúdo do item realçado no painel esquerdo. Com tantas chaves e subchaves, o caminho da chave pode se tornar muito longo. O caminho é exibido na parte inferior da janela para referência. Como cada chave e subchave é essencialmente um contêiner, o caminho é representado muito parecido com uma pasta em um sistema de arquivos. A barra invertida (∖) é usada para diferenciar a hierarquia do banco de dados.

As chaves do Registro podem conter uma subchave ou um valor. Os diferentes valores que as chaves podem conter são os seguintes:

- **REG_BINARY -** Números ou valores booleanos
- **REG_DWORD -** Números maiores que 32 bits ou dados brutos
- **REG_SZ -** Valores de string

Como o registro contém quase toda infomação do sistema operacional e do usuário, é essencial garantir que ele não seja comprometido. Aplicativos potencialmente mal-intencionados podem adicionar chaves do Registro para que elas sejam iniciadas quando o computador for iniciado. Durante uma inicialização normal, o usuário não verá o programa iniciar porque a entrada está no registro e o aplicativo não exibe janelas ou indicação de início quando o computador for inicializado. Um keylogger, por exemplo, seria devastador para a segurança de um computador se ele fosse iniciado na inicialização sem o conhecimento ou consentimento do usuário. Ao executar auditorias de segurança normais ou corrigir um sistema infectado, revise os locais de inicialização do aplicativo no registro para garantir que cada item seja conhecido e seguro para ser executado.

O registro também contém a atividade que um usuário executa durante o uso diário normal do computador. Isso inclui o histórico de dispositivos de hardware, incluindo todos os dispositivos que foram conectados ao computador, incluindo o nome, o fabricante e o número de série. Outras informações, como quais documentos um usuário e um programa abriram, onde eles estão localizados e quando foram acessados, são armazenadas no registro. Isso tudo é uma informação muito útil quando uma investigação forense precisa ser realizada.

















