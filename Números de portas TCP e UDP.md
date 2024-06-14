#redes 
# Números de portas TCP e UDP

São muitos os serviços que acessamos pela Internet ao longo do dia. DNS, Web, E-mail, FTP, Mensagem instantânea e VoIP são apenas alguns desses serviços que são disponibilizados por sistemas cliente/servidor em todo o mundo. Eles podem ser fornecidos por um único servidor ou por vários servidores em grandes datacenters.

Quando uma mensagem é entregue usando o TCP ou o UDP, os protocolos e os serviços são identificados por um número de porta. Uma porta é um identificador numérico dentro de cada segmento que é usado para rastrear conversas específicas entre um cliente e um servidor. Cada mensagem que um host envia contém uma porta origem e destino.

![[Pasted image 20240614104933.png]]

Quando uma mensagem é recebida por um servidor, é necessário que o servidor consiga determinar qual serviço está sendo solicitado pelo cliente. Os clientes são pré-configurados para usar uma porta de destino que foi registrada na Internet para cada serviço. Um exemplo disso são os clientes de navegador da Web, que são configurados previamente para enviar solicitações para servidores da Web pela porta 80, a porta usada normalmente para serviços da Web em HTTP.

As portas são atribuídas e gerenciadas por uma organização conhecida como ICANN (Internet Corporation for Assigned Names and Numbers, Corporação da Internet para Atribuição de Nomes e Números). As portas foram divididas em três categorias e variam em número de 1 a 65.535.

- **Portas bem conhecidas** – As portas de destino que estão associadas a aplicativos de rede comuns são identificadas como portas bem conhecidas. Elas estão no intervalo de 1 a 1.023.
- **Portas registradas –** As portas 1.024 a 49.151 podem ser usadas como portas de destino ou de origem. Elas podem ser usadas por empresas para registrar aplicativos específicos, como os de mensagem instantânea.
- **Portas privadas –** As portas de 49.152 a 65.535 são geralmente utilizadas como portas de origem. Elas podem ser usadas por qualquer aplicativo.

A tabela exibe alguns números de porta conhecidos comuns e seus aplicativos associados.

| Número da Porta | Transporte | Protocolo de aplicação                                                                       |
| --------------- | ---------- | -------------------------------------------------------------------------------------------- |
| 20              | TCP        | Protocolo de Transferência de Arquivos (FTP) - Dados                                         |
| 21              | TCP        | FTP - Controle                                                                               |
| 22              | TCP        | Secure Shell(Shell seguro) - SSH                                                             |
| 23              | TCP        | Telnet                                                                                       |
| 25              | TCP        | Protocolo SMTP                                                                               |
| 53              | UDP, TCP   | Protocolo DNS                                                                                |
| 67              | UDP        | Dynamic Host Configuration Protocol (DHCP) - Servidor                                        |
| 68              | UDP        | Cliente DHCP                                                                                 |
| 69              | UDP        | Protocolo de Transferência Trivial de Arquivo (TFTP)                                         |
| 80              | TCP        | Protocolo HTTP                                                                               |
| 110             | TCP        | Protocolo POP3 (Post Office Protocol - Protocolo dos Correios)                               |
| 143             | TCP        | Protocolo IMAP                                                                               |
| 161             | UDP        | Protocolo de Gerenciamento Simples de Rede (SNMP)                                            |
| 443             | TCP        | HTTPS (Secure Hypertext Transfer Protocol - Protocolo de Transferência de Hipertexto Seguro) |

Algumas aplicações podem usar tanto TCP quanto UDP. Por exemplo, o DNS usa o protocolo UDP quando os clientes enviam requisições a um servidor DNS. Contudo, a comunicação entre dois servidores DNS sempre usa TCP.

Pesquise no site da IANA o registro de portas para visualizar a lista completa de números de portas e aplicativos associados.

