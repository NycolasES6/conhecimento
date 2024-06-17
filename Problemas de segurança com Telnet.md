#redes 
# Problemas de segurança com Telnet

Quando uma conexão Telnet é estabelecida, os usuários podem executar qualquer função autorizada no servidor, como se estivessem usando uma sessão de linha de comando no próprio servidor. Se autorizados, podem iniciar e parar processos, configurar o dispositivo e até mesmo desligar o sistema.

Embora o protocolo Telnet possa exigir o login de um usuário, ele não suporta o transporte de dados criptografados. Todos os dados trocados durante as sessões Telnet são transportados como texto simples pela rede. Isso significa que os dados podem ser facilmente interceptados e compreendidos.

O protocolo Secure Shell (SSH) oferece um método alternativo e seguro para acesso ao servidor. O SSH fornece a estrutura para proteger login remoto e outros serviços de rede segura. Ele também fornece autenticação mais forte do que o Telnet e suporta o transporte de dados de sessão usando criptografia. Como melhor prática, os profissionais de rede sempre devem utilizar o SSH em vez do Telnet, quando possível.

![[Pasted image 20240617085720.png]]