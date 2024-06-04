#cyber #redes 
# Protocolos de autenticação

O protocolo de autenticação extensível (EAP) é uma estrutura de autenticação usada em redes sem fio. Vamos descobrir como isso funciona.

1. O usuário solicita a conexão à rede sem fio através de um access point.
2. O access point solicita dados de identificação (nome de usuário) do usuário, que é então enviado para um servidor de autenticação.
3. O servidor de autenticação solicita a prova de que a ID é válida.
4. O access point solicita prova de que a ID é válida do usuário, na forma de uma senha.
5. O usuário fornece a senha ao access point. O access point envia de volta para o servidor de autenticação.
6. O servidor confirma que o nome de usuário e a senha estão corretos e passa essas informações para o access point e o usuário.
7. Conecte-se à rede sem fio.

### EAP-TLS

Solicitar certificado de cliente: Sim  
Solicitar certificado de servidor: Sim  
Implantável facilmente: Dificuldade  
de segurança: alta

### PEAP

Solicitar certificado de cliente: Não  
Solicitar certificado de servidor: Sim  
Implantável facilmente: Dificuldade  
de segurança: média

### EAP-TTLS

Solicitar certificado de cliente: Não  
Solicitar certificado de servidor: Sim  
Implantável facilmente: Dificuldade  
de segurança: média

### EAP-FAST

Solicitar certificado de cliente: Não  
Solicitar certificado de servidor: Não  
implantável facilmente: Dificuldade  
de segurança: média















