#redes 

# HTTP e HTTPS

## Estrutura HTTP

A estrutura HTTP é composta de um **Header** e um **Body**.

O protocolo HTTP suporta vários métodos tais como GET, POST, HEAD, PUT, DELETE e OPTIONS.

Os mais utilizados são o método **GET** para requisitar recursos e o método **POST** para enviar dados como por exemplo formulários de páginas.

![[Pasted image 20240618113214.png]]



---

Os navegadores da Internet são usados por quase todos. Bloquear completamente a navegação na Web não é uma opção porque as empresas precisam de acesso à Web, sem comprometer a segurança da Web.

Para investigar ataques baseados na Web, os analistas de segurança devem ter uma boa compreensão de como funciona um ataque padrão baseado na Web. Estes são os estágios comuns de um ataque típico da web:

1. A vítima visita inconscientemente uma página web que foi comprometida por malware.
2. A página Web comprometida redireciona o usuário, muitas vezes através de muitos servidores comprometidos, para um site contendo código malicioso.
3. O usuário visita este site com código malicioso e seu computador fica infectado. Isso é conhecido como uma unidade por download. Quando o usuário visita o site, um kit de exploração verifica o software em execução no computador da vítima, incluindo o sistema operacional, Java ou Flash player que procura uma exploração no software. O kit de exploração geralmente é um script PHP e fornece ao invasor um console de gerenciamento para gerenciar o ataque.
4. Depois de identificar um pacote de software vulnerável em execução no computador da vítima, o kit de exploração entra em contato com o servidor do kit de exploração para baixar código que pode usar a vulnerabilidade para executar código mal-intencionado no computador da vítima.
5. Depois que o computador da vítima foi comprometido, ele se conecta ao servidor de malware e baixa uma carga útil. Isso pode ser malware ou um serviço de download de arquivos que baixa outro malware.
6. O último pacote de malware é executado no computador da vítima.

Independente do tipo de ataque que está sendo usado, o objetivo principal do ator da ameaça é garantir que o navegador da Web da vítima acabe na página da web do ator da ameaça, que, em seguida, serve a exploração maliciosa para a vítima.

Alguns sites mal-intencionados aproveitam plug-ins vulneráveis ou vulnerabilidades do navegador para comprometer o sistema do cliente. Redes maiores dependem de IDSs para verificar arquivos baixados em busca de malware. Se detectado, o IDS emite alertas e registra o evento em arquivos de log para análise posterior.

Os logs de conexão do servidor geralmente podem revelar informações sobre o tipo de varredura ou ataque. Os diferentes tipos de códigos de status de conexão estão listados aqui:

- **Informativo 1xx -** Esta é uma resposta provisória, consistindo apenas na Linha de Status e cabeçalhos opcionais. É encerrado por uma linha vazia. Não há cabeçalhos necessários para esta classe de código de status. Servidores NÃO DEVE enviar uma resposta 1xx para um cliente HTTP/1.0, exceto em condições experimentais.
- **Successful 2xx -** A solicitação do cliente foi recebida, compreendida e aceita com êxito.
- **Redirection 3xx -** Outras ações devem ser tomadas pelo agente do usuário para atender a solicitação. Um cliente DEVE detectar loops de redirecionamento infinitos, porque esses loops geram tráfego de rede para cada redirecionamento.
- **Client Error 4xx -** Para casos em que o cliente parece ter errado. Exceto quando responder a uma solicitação HEAD, o servidor DEVE incluir uma entidade contendo uma explicação da situação, e se ela é temporária. Agentes de usuário DEVE exibir qualquer entidade incluída para o usuário.
- **Server Error 5xx -** Para casos em que o servidor está ciente de que ele errou ou não pode executar a solicitação. Exceto quando responder a uma solicitação HEAD, o servidor DEVE incluir uma entidade contendo uma explicação da situação de erro, e se ela é temporária. Agentes de usuário DEVE exibir qualquer entidade incluída para o usuário.

Para se defender contra ataques baseados na web, as seguintes contramedidas devem ser usadas:

- Sempre atualize o sistema operacional e os navegadores com patches e atualizações atuais.
- Use um proxy da Web como o Cisco Cloud Web Security ou o Cisco Web Security Appliance para bloquear sites mal-intencionados.
- Use as melhores práticas de segurança do Open Web Application Security Project (OWASP) ao desenvolver aplicativos Web.
- Educar os usuários finais mostrando-lhes como evitar ataques baseados na Web.

O OWASP Top 10 Riscos de Segurança de Aplicativos Web foi projetado para ajudar as organizações a criar aplicativos Web seguros. É uma lista útil de potenciais vulnerabilidades que são comumente exploradas por atores de ameaças.

## Exploração de injeção iFrame de HTTP

![[Pasted image 20240604113241.png]]

Para lidar com a alteração ou interceptação de dados confidenciais, muitas organizações comerciais adotaram HTTPS ou implementaram políticas somente HTTPS para proteger os visitantes de seus sites e serviços.

HTTPS adiciona uma camada de criptografia ao protocolo HTTP usando Secure Socket Layer (SSL), como mostrado na figura. Isso torna os dados HTTP ilegíveis, pois deixam o computador de origem até chegar ao servidor. Observe que HTTPS não é um mecanismo para a segurança do servidor Web. Ele só protege o tráfego de protocolo HTTP enquanto está em trânsito.

## Diagrama de protocolo HTTPS

![[Pasted image 20240604113343.png]]

Infelizmente, o tráfego HTTPS criptografado complica o monitoramento de segurança de rede. Alguns dispositivos de segurança incluem descriptografia e inspeção SSL; no entanto, isso pode apresentar problemas de processamento e privacidade. Além disso, o HTTPS adiciona complexidade às capturas de pacotes devido às mensagens adicionais envolvidas no estabelecimento da conexão criptografada. Esse processo é resumido na figura e representa sobrecarga adicional sobre HTTP.

## Transações HTTPS

![[Pasted image 20240604113518.png]]

