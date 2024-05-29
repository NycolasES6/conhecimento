#redes 
# Telnet, SSH, SCP

**O Secure Shell (SSH)** é um protocolo que fornece uma conexão com um dispositivo remoto de natureza segura (criptografada) e baseada em uma linha de comando. **O Telnet** é um protocolo mais antigo que usa transmissão de texto não criptografado, não protegido, tanto para autenticação de logon (nome de usuário e senha) quanto para dados transmitidos entre os dispositivos de comunicação. O SSH deve ser usado em vez do Telnet para gerenciar conexões, pois ele oferece criptografia forte. O SSH usa a porta TCP 22. Já o Telnet usa a porta 23.

**A SCP (Secure Copy, cópia segura)** , transfere, com segurança, arquivos de computador entre dois sistemas remotos. O SCP usa o SSH para a transferência de dados (incluindo o elemento de autenticação), para que o SCP garanta a autenticidade e a confidencialidade dos dados em trânsito.
