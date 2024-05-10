#redes #cyber 
# Arquiteturas comuns de segurança

O design do firewall é principalmente sobre interfaces de dispositivo que permitem ou negam tráfego com base na origem, no destino e no tipo de tráfego. Alguns designs são tão simples quanto designar uma rede externa e uma rede interna, que são determinados por duas interfaces em um firewall.

Aqui estão três designs comuns de firewall.

### Privado e público

Como mostrado na figura, a rede pública (ou rede externa) não é confiável e a rede privada (ou rede interna) é confiável.

Normalmente, um firewall com duas interfaces é configurado da seguinte forma:

- O tráfego proveniente da rede privada é permitido e inspecionado à medida que viaja em direção à rede pública. É permitido o tráfego inspecionado que retorna da rede pública e associado ao tráfego originado da rede privada.
- O tráfego originado da rede pública e que viaja para a rede privada geralmente é bloqueado.

![[Pasted image 20240510163234.png]]

### Zona Desmilitarizada

Uma zona desmilitarizada (DMZ) é um projeto de firewall onde normalmente há uma interface interna conectada à rede privada, uma interface externa conectada à rede pública e uma interface DMZ, conforme mostrado na figura.

- O tráfego proveniente da rede privada é inspecionado à medida que ele viaja para a rede pública ou DMZ. Este tráfego é permitido com pouca ou nenhuma restrição. Tráfego inspecionado que retorna da DMZ ou da rede pública para a rede privada é permitido.
- O tráfego originado da rede DMZ e que viaja para a rede privada geralmente é bloqueado.
- O tráfego originado da rede DMZ e viajando para a rede pública é permitido seletivamente com base nos requisitos de serviço.
- O tráfego proveniente da rede pública e que viaja em direção à DMZ é seletivamente permitido e inspecionado. Esse tipo de tráfego normalmente é tráfego de email, DNS, HTTP ou HTTPS. O tráfego de retorno da DMZ para a rede pública é permitido dinamicamente.
- O tráfego originado da rede pública e que viaja para a rede privada está bloqueado.

![[Pasted image 20240510163858.png]]

### Firewalls de política baseados em zona

Os firewalls de política baseados em zona (ZPFs) usam o conceito de zonas para fornecer flexibilidade adicional. Uma zona é um grupo de uma ou mais interfaces que têm funções ou recursos semelhantes. As zonas ajudam a especificar onde uma regra ou política de firewall do Cisco IOS deve ser aplicada. Na figura, as políticas de segurança para LAN 1 e LAN 2 são semelhantes e podem ser agrupadas em uma zona para configurações de firewall. Por padrão, o tráfego entre interfaces na mesma zona não está sujeito a nenhuma política e passa livremente. No entanto, todo o tráfego de zona para zona está bloqueado. Para permitir o tráfego entre as zonas, uma política que permite ou inspeciona o tráfego deve ser configurada.

A única exceção a este padrão **deny any** política é a zona própria do roteador. A zona auto é o próprio roteador e inclui todos os endereços IP da interface do roteador. As configurações de política que incluem a zona automática aplicar-se-iam ao tráfego destinado e proveniente do roteador. Por padrão, não há nenhuma política para esse tipo de tráfego. O tráfego que deve ser considerado ao projetar uma política para a auto zona inclui o tráfego de plano de gerenciamento e plano de controle, como SSH, SNMP e protocolos de roteamento.

![[Pasted image 20240510164001.png]]










