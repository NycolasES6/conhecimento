#redes 
# VPN

Uma VPN é uma rede privada criada em uma rede pública, geralmente a Internet, conforme mostrado na figura.

**Rede Virtual Privada**

![[Pasted image 20240513114744.png]]

Em vez de usar uma conexão física dedicada, uma VPN usa conexões virtuais que são roteadas pela Internet da organização para o site remoto. As primeiras VPNs eram túneis IP restritos que não incluíam autenticação ou criptografia dos dados. Por exemplo, Generic Routing Encapsulation (GRE) é um protocolo de encapsulamento desenvolvido pela Cisco que pode encapsular uma ampla variedade de tipos de pacote de protocolo de camada de rede dentro de túneis IP. Isso cria um link ponto-a-ponto virtual com roteadores Cisco em pontos remotos sobre uma rede interconectada IP.

Uma VPN é virtual, pois carrega informações dentro de uma rede privada, mas essas informações são realmente transportadas por uma rede pública. Uma VPN é privada, pois o tráfego é criptografado para manter os dados confidenciais enquanto são transportados pela rede pública.

A VPN é um ambiente de comunicações no qual o acesso é controlado rigorosamente para permitir conexões de mesmo nível em uma comunidade com interesses definidos. A confidencialidade é alcançada criptografando o tráfego dentro da VPN. Hoje, uma implementação segura de VPN com criptografia é o que geralmente é equiparado ao conceito de rede virtual privada.

No sentido mais simples, uma VPN conecta dois endpoints, como um escritório remoto a um escritório central, através de uma rede pública, para formar uma conexão lógica. As conexões lógicas podem ser feitas na Camada 2 ou na Camada 3. Exemplos comuns de VPNs de Camada 3 são GRE, MPLS (Multiprotocol Label Switching) e IPsec. As VPNs de camada 3 podem ser conexões de site ponto a ponto, como GRE e IPsec, ou podem estabelecer qualquer conectividade para muitos sites usando MPLS.

O IPsec é um conjunto de protocolos desenvolvido com o apoio do IETF para obter serviços seguros em redes IP comutadas por pacotes.

Os serviços de IPsec permitem a autenticação, integridade, controle de acesso e confidencialidade. Com o IPsec, as informações trocadas entre sites remotos podem ser criptografadas e verificadas. As VPNs são normalmente implantadas em uma topologia site a site para conectar sites centrais com locais remotos com segurança. Eles também são implantados em uma topologia de acesso remoto para fornecer acesso remoto seguro a usuários externos que viajam ou trabalham de casa. As VPNs de acesso remoto e site-to-site podem ser implantadas usando IPsec.









