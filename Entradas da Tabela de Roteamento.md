#redes 
# Entradas da Tabela de Roteamento

Os roteadores movem informações entre redes locais e remotas. Para fazer isso, eles têm que usar tabelas de roteamento para armazenar informações. As tabelas de roteamento não estão relacionadas aos endereços de hosts individuais. Tabelas de roteamento contêm endereços de redes e o melhor caminho para acessar essas redes. As entradas podem ser feitas na tabela de roteamento de duas maneiras: atualizadas dinamicamente por informações recebidas de outros roteadores na rede ou inseridas manualmente por um administrador de rede. Os roteadores usam as tabelas de roteamento para determinar qual interface deve ser usada para encaminhar uma mensagem para o destino desejado.

Se o roteador não conseguir determinar para onde encaminhar uma mensagem, ele a descartará. Os administradores de rede podem configurar uma rota padrão que é inserida na tabela de roteamento para evitar que o pacote não seja descartado pelo fato do caminho para a rede de destino não estar na tabela de roteamento. Uma rota padrão é a interface através da qual o roteador encaminha um pacote contendo um endereço de rede IP de destino que é desconhecido. Essa rota padrão normalmente se conecta a outro roteador que pode encaminhar o pacote para a rede de destino final.

![[Pasted image 20240612100335.png]]

|Tipo|Rede|Porta|
|---|---|---|
|C|10.0.0.0/8|FastEthernet0/0|
|C|172.16.0.0/16|FastEthernet0/1|

- **Tipo -** O tipo de conexão C para diretamente conectado
- **Rede -** O endereço de rede
- **Porta -** Interface usada para encaminhar pacotes para a rede








