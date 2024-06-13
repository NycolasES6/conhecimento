#cyber 
# Protocolos e tecnologias de autenticação

Um protocolo de autenticação autentica os dados entre duas entidades para impedir o acesso não autorizado. Um protocolo descreve o tipo de informação que precisa ser compartilhada para se autenticar e se conectar.

### Protocolo de autenticação extensível (EAP)

Uma senha do cliente é enviada usando um hash para o servidor de autenticação. O servidor de autenticação tem um certificado (o cliente não precisa de um certificado).

### PAP (Password Authentication Protocol)

Um nome de usuário e uma senha são enviados para um servidor de acesso remoto em texto sem formatação. A maioria dos servidores remotos de sistema operacional de rede é compatível com PAP.

### CHAP (Challenge Handshake Authentication Protocol)

CHAP valida a identidade de clientes remotos usando uma função de hash unidirecional criada pelo cliente. O serviço também calcula o valor esperado de hash. O servidor (o autenticador) compara os dois valores. Se os valores corresponderem, a transmissão continua. CHAP também verifica periodicamente a identidade do cliente durante a transmissão.

### 802.1x

Uma empresa autentica sua identidade e autoriza o acesso à rede. Sua identidade é determinada com base em credenciais ou em um certificado confirmado por um servidor RADIUS.

### RADIUS

Quando a autenticação simples de nome de usuário/senha for necessária, use RADIUS para aceitar ou negar acesso. RADIUS criptografa apenas a senha do usuário do cliente RADIUS para o servidor RADIUS. O nome de usuário, a contabilidade e os serviços autorizados são transmitidos em texto não criptografado. Quando o RADIUS é integrado a um produto, são necessárias medidas de segurança que protegem contra ataques de repetição.

### TACACS+

TACACS + usa TCP como protocolo de transporte. TACACS + criptografa todos os dados (nome de usuário, senha, contabilidade e serviços autorizados) entre o cliente e o servidor. Como os administradores de rede podem definir ACLs, filtros e privilégios de usuário, TACACS + é a melhor escolha para redes corporativas que exigem etapas de autenticação mais sofisticadas e controle sobre atividades de autorização.

### Kerberos

Kerberos usa criptografia forte, solicitando que um cliente comprove sua identidade para um servidor, com o servidor, por sua vez, se autenticando no cliente.

O servidor Kerberos contém IDs de usuário e senhas com hash para todos os usuários que terão autorizações para serviços de região. O servidor Kerberos também tem chaves secretas compartilhadas com todos os servidores aos quais concederá tíquetes de acesso. A base para a autenticação em um ambiente Kerberos é o tíquete. Os tíquetes são usados em um processo de duas etapas com o cliente. O primeiro tíquete é um tíquete de concessão de tíquete emitido pelo serviço de autenticação para um cliente solicitante. O cliente pode então apresentar esse tíquete ao servidor Kerberos com uma solicitação de tíquete para acessar um servidor específico. 

Esse tíquete do cliente para o servidor (também conhecido como tíquete de serviço) é usado para obter acesso ao serviço de um servidor. Como toda a sessão pode ser criptografada, isso elimina a transmissão inerentemente insegura de itens (como senhas) que podem ser interceptados na rede. Os tickets têm o carimbo de hora e expiram, portanto, qualquer tentativa de reutilização de um ticket não será bem-sucedida.