#redes 
# Descrição de tipos de firewall

É importante entender os diferentes tipos de firewalls e suas capacidades específicas para que o firewall correto seja usado para cada situação.

## Firewall de filtragem de pacotes (sem estado)

Os firewalls de filtragem de pacotes geralmente fazem parte de um firewall de roteador, que permite ou nega tráfego com base nas informações da Camada 3 e da Camada 4. Eles são firewalls sem estado que usam uma simples pesquisa de tabela de políticas que filtra o tráfego com base em critérios específicos.

Por exemplo, os servidores SMTP escutam a porta 25 por padrão. Um administrador pode configurar o firewall de filtragem de pacotes para bloquear a porta 25 de uma estação de trabalho específica para impedir que ele transmita um vírus de e-mail

![[Pasted image 20240510172555.png]]

## Firewalls com monitoração de estado

Firewalls com estado são as tecnologias de firewall mais versáteis e mais comuns em uso. Os firewalls stateful fornecem filtragem de pacotes stateful usando informações de conexão mantidas em uma tabela de estado. Filtragem com estado é uma arquitetura de firewall classificada na camada de rede. Ele também analisa o tráfego na camada 4 da OSI e na camada 5.

![[Pasted image 20240510172714.png]]

## Firewall de gateway de aplicativo

Um firewall de gateway de aplicação (firewall proxy), conforme mostrado na figura, filtra as informações nas camadas 3, 4, 5 e 7 do modelo de referência OSI. A maior parte do controle e filtragem do firewall é feita em software. Quando um cliente precisa acessar um servidor remoto, ele se conecta a um servidor proxy. O servidor proxy se conecta ao servidor remoto em nome do cliente. Portanto, o servidor só vê uma conexão do servidor proxy.

![[Pasted image 20240510172854.png]]

## Firewall de próxima geração

Os firewalls de última geração (NGFW) vão além dos firewalls de estado, fornecendo:

- Prevenção de intrusão integrada
- Reconhecimento e controle de aplicativos para ver e bloquear aplicativos arriscados
- Caminhos de atualização para incluir futuros feeds de informações
- Técnicas para lidar com ameaças de segurança em evolução

![[Pasted image 20240510173052.jpg]]

Outros métodos de implementação de firewalls incluem:

- **Firewalls baseados em host é** - Um PC ou servidor com software de firewall em execução nele.
- **Firewall transparente -** Filtra o tráfego IP entre um par de interfaces em ponte.
- **Firewall híbrido** - Uma combinação dos vários tipos de firewall. Por exemplo, um firewall de inspeção de aplicações combina um firewall com estado com um firewall de gateway de aplicativo.



