#redes #cyber 

# Ataques de falsificação de endereços

Os ataques de falsificação de endereço IP ocorrem quando um agente de ameaça cria pacotes com informações falsas de endereço IP de origem para ocultar a identidade do remetente ou para se passar por outro usuário legítimo. O agente de ameaças pode obter acesso a dados inacessíveis ou burlar as configurações de segurança. A falsificação é geralmente incorporada a outro ataque, como um ataque Smurf.

Os ataques de falsificação podem ser cegos ou não cegos:

- **Spoofing não cego -** O agente da ameaça pode ver o tráfego que está sendo enviado entre o host e o destino. O agente de ameaça usa a falsificação não cega para inspecionar o pacote de resposta da vítima alvo. A falsificação não cega determina o estado de um firewall e prever número de sequência. Também pode sequestrar uma sessão autorizada.
- **Spoofing cego -** O agente da ameaça não pode ver o tráfego que está sendo enviado entre o host e o destino. A falsificação cega é usada em ataques de negação de serviço.

Os ataques de falsificação de endereço MAC são usados quando os atores de ameaças têm acesso à rede interna. Os agentes de ameaças alteram o endereço MAC de seu host para corresponder a outro endereço MAC conhecido de um host de destino, conforme mostrado na figura. O host atacante envia um quadro pela rede com o endereço MAC recém configurado. Quando o switch recebe o quadro, ele examina o endereço MAC de origem.

**Threat Actor falsifica o endereço MAC de um servidor**

![[Pasted image 20240507130312.png]]

O switch substitui a entrada atual da tabela CAM e atribui o endereço MAC à nova porta, como mostrado na figura. Em seguida, encaminha os quadros destinados ao host de destino para o host atacante.

**O Switch atualiza a tabela CAM com endereço falsificado**

![[Pasted image 20240507130407.png]]

A falsificação de aplicativos ou serviços é outro exemplo de falsificação. Um agente de ameaça pode conectar um servidor DHCP não autorizado para criar uma condição MiTM.




