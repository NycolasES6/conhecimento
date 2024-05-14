#SO #Windows 

# Modo de Usuário e Modo Kernel

Conforme identificado na figura, existem dois modos diferentes em que uma CPU opera quando o computador tem o Windows instalado: o modo de usuário e o modo kernel.

![[Pasted image 20240514100733.png]]

Os aplicativos instalados são executados no modo de usuário e o código do sistema operacional é executado no modo kernel. O código que está sendo executado no modo kernel tem acesso irrestrito ao hardware subjacente e é capaz de executar qualquer instrução de CPU. O código do modo kernel também pode referenciar qualquer endereço de memória diretamente. Geralmente reservado para as funções mais confiáveis do sistema operacional, falhas no código em execução no modo kernel param a operação de todo o computador. Por outro lado, programas como aplicativos de usuário são executados no modo de usuário e não têm acesso direto a locais de hardware ou memória. O código do modo de usuário deve passar pelo sistema operacional para acessar recursos de hardware. Devido ao isolamento fornecido pelo modo de usuário, as falhas no modo de usuário são restritas apenas ao aplicativo e são recuperáveis. A maioria dos programas no Windows são executados no modo de usuário. Drivers de dispositivo, peças de software que permitem que o sistema operacional e um dispositivo se comuniquem, podem ser executados no modo kernel ou usuário, dependendo do driver.

Todo o código que é executado no modo kernel usa o mesmo espaço de endereço. Os drivers de modo kernel não têm isolamento do sistema operacional. Se ocorrer um erro com o driver em execução no modo kernel e ele gravar no espaço de endereço errado, o sistema operacional ou outro driver de modo kernel pode ser afetado negativamente. A este respeito, o driver pode falhar, fazendo com que todo o sistema operacional falhe.

Quando o código de modo de usuário é executado, ele é concedido seu próprio espaço de endereço restrito pelo kernel, juntamente com um processo criado especificamente para o aplicativo. A razão para essa funcionalidade é principalmente para impedir que aplicativos alterem o código do sistema operacional que está sendo executado ao mesmo tempo. Ao ter seu próprio processo, esse aplicativo tem seu próprio espaço de endereço privado, tornando outros aplicativos incapazes de modificar os dados nele. Isso também ajuda a evitar que o sistema operacional e outros aplicativos falhe se esse aplicativo falhar.













