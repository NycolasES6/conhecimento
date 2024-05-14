#redes #cyber
# ACLs - recursos importantes

Dois tipos de ACLs Cisco IPv4 são padrão e estendidos. As ACLs padrão podem ser usadas para permitir ou negar tráfego somente dos endereços IPv4 origem. O destino do pacote e as portas envolvidas não são avaliados.

As ACLs estendidas filtram pacotes IPv4 com base em vários atributos que incluem:

- Tipo de protocolo
- Endereço IPv4 origem
- Endereço IPv4 destino
- Portas TCP ou UDP origem
- Portas TCP ou UDP destino
- Informações opcionais do tipo de protocolo para o melhor controle

As ACLs padrão e estendidas podem ser criadas usando-se um número ou um nome para identificar a ACL e sua lista de instruções.

Usar ACLs numeradas é um método eficaz para determinar o tipo de ACL em redes pequenas com tráfego definido de forma mais homogênea. No entanto, um número não fornece informações sobre o propósito da ACL. Portanto, um nome pode ser usado para identificar uma ACL da Cisco.

Ao configurar o registro de ACL, uma mensagem ACL pode ser gerada e registrada quando o tráfego atende aos critérios de permissão ou negação definidos na ACL.

As ACLs Cisco também podem ser configuradas para permitir apenas tráfego TCP que tenha um conjunto de bits ACK ou RST, de modo que apenas o tráfego de uma sessão TCP estabelecida seja permitido. Isso pode ser usado para negar qualquer tráfego TCP de fora da rede que está tentando estabelecer uma nova sessão TCP.



























