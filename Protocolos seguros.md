#redes #cyber 
# Protocolos seguros

Os invasores podem penetrar na infraestrutura de uma rede por meio de serviços, protocolos e portas abertas. Protocolos mais antigos deixam uma rede em uma posição vulnerável, então os profissionais de segurança digital precisam garantir que os protocolos atuais estejam sendo usados.

## Protocolo de Gerenciamento Simples de Rede (SNMP)

O SNMP coleta estatísticas de dispositivos TCP/IP para monitorar a rede e equipamentos de computador. O SNMPv3 é o padrão atual - ele usa criptografia para evitar a espionagem e garantir que os dados não tenham sido violados durante o trânsito.

## HTTP

O Hypertext Transfer Protocol (HTTP) fornece conectividade básica da Web e usa a porta 80. O HTTP contém segurança interna limitada e é aberto ao monitoramento de tráfego durante a transmissão de conteúdo, deixando o computador do usuário aberto para ataques. Vamos ver como outros protocolos fornecem uma conexão mais segura:

- A Secure Sockets Layer (SSL) gerencia a criptografia usando um handshake de SSL no início de uma sessão para fornecer confidencialidade e evitar a interceptação e a violação.
- O Transport Layer Security (TLS) é um substituto atualizado e mais seguro para SSL.
- O SSL / TLS criptografa a comunicação entre o cliente e o servidor. Onde for usado, o usuário verá HTTPS no campo de URL de um navegador em vez de HTTP.

## FTP

O File Transfer Protocol (FTP) oferece a capacidade de transferir arquivos entre um cliente e um servidor. No FTP, o cliente usa um nome de usuário e uma senha de texto sem formatação para se conectar. O File Transfer Protocol Secure (FTPS) é mais seguro - ele adiciona suporte a TLS e SSL para evitar a interceptação, a violação e a falsificação de mensagens trocadas.

## POP, IMAP e MIME

O e-mail usa Post Office Protocol (POP), IMAP (Internet Message Access Protocol) e MIME (Multipurpose Internet Mail Extensions) para anexar dados sem texto, como imagens ou vídeos, a uma mensagem de e-mail.

Para proteger o POP (porta 110) ou IMAP (porta 143), use SSL / TLS para criptografar e-mails durante a transmissão. O protocolo Secure / Multipurpose Internet Mail Extensions (S / MIME) oferece um método seguro de transmissão. Ele envia mensagens digitalmente assinadas e criptografadas que fornecem autenticação, integridade de mensagem e não-repudiação.

- **O Secure Shell (SSH)** é um protocolo que fornece uma conexão com um dispositivo remoto de natureza segura (criptografada) e baseada em uma linha de comando.
- **A SCP (Secure Copy, cópia segura)** , transfere, com segurança, arquivos de computador entre dois sistemas remotos.
- O **Transport Layer Security (TLS)** evita a interceptação e a violação.






















