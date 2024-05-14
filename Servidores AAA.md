#redes 
# Servidores AAA

### Autenticação

- Os usuários e administradores devem provar quem são.
- A autenticação pode ser estabelecida usando combinações de nome de usuário e senha, perguntas e respostas de desafio, tokens e outros métodos.
- A autenticação AAA fornece uma maneira centralizada de controlar o acesso à rede.

### Autorização

- Após a autenticação do usuário, os serviços de autorização determinam quais recursos o usuário pode acessar e quais operações ele tem permissão para executar.
- Um exemplo é “O usuário‘ aluno ’pode acessar o host serverXYZ usando apenas SSH.”

### Accounting (Contabilidade)

- O accounting registra o que o usuário faz, incluindo o que é acessado, a quantidade de tempo em que o recurso é acessado e todas as alterações efetuadas.
- O accounting rastreia como os recursos de rede são usados.
- Um exemplo é "O usuário 'aluno' acessou o servidor host XYZ usando SSH por 15 minutos".

Terminal Access Controller Access-Control System Plus (TACACS) e Remote Authentication Dial-In User Service (RADIUS) são protocolos de autenticação usados para se comunicar com servidores AAA. A seleção do TACACS+ ou RADIUS depende das necessidades da empresa.

Embora ambos os protocolos possam ser usados para comunicação entre um roteador e os servidores de AAA, o TACACS+ é considerado o protocolo mais seguro. Isto é porque todas as trocas de protocolo TACACS+ são criptografadas, enquanto o RADIUS criptografa apenas a senha do usuário. O RADIUS não criptografa nomes de usuário, informações de contabilidade ou qualquer outra informação transportada na mensagem RADIUS.

A tabela lista a diferença entre os dois protocolos.

![[Pasted image 20240513114224.png]]

































