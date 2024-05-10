#redes 

# Cliente sem fio e associação de AP

Para que os dispositivos sem fio se comuniquem através de uma rede, eles devem primeiro se associar a um Ponto de acesso ou roteador sem fio. Uma parte importante do processo 802.11 é descobrir uma WLAN e subsequentemente conectar-se a ela. Os dispositivos sem fio concluem o seguinte processo de três estágios, conforme mostrado na figura:

- Descobrir novo AP sem fio.
- Autenticar-se no AP
- Associar no AP

![[Pasted image 20240510111401.png]]

Para ter uma associação bem-sucedida, um cliente sem fio e um ponto de acesso devem concordar com parâmetros específicos. Os parâmetros devem ser configurados no ponto de acesso e subseqüentemente no cliente para permitir a negociação de uma associação bem-sucedida.

- **SSID -** O nome SSID aparece na lista de redes sem fio disponíveis em um cliente. Em organizações maiores que usam várias VLANs para segmentar o tráfego, cada SSID é mapeado para uma VLAN. Dependendo da configuração da rede, vários pontos de acesso em uma rede podem compartilhar um SSID comum.
- **Senha -** Isso é exigido do cliente sem fio para autenticar no AP.
- **Modo de rede -** Refere-se aos padrões WLAN 802.11a/b/g/n/ac/ad. Os pontos de acesso e roteadores sem fio podem operar no modo misto, o que significa que eles podem oferecer suporte simultâneo a clientes que se conectam por vários padrões.
- **Modo de Segurança -** Refere-se às configurações dos parâmetros de segurança, como WEP, WPA ou WPA2. Sempre habilite o nível de segurança mais alto suportado.
- **Configurações de canal -** Refere-se às bandas de frequência usadas para transmitir dados sem fio. Os roteadores sem fio e os APs podem verificar os canais de frequência de rádio e selecionar automaticamente uma configuração de canal apropriada. O canal também pode ser configurado manualmente se houver interferência com outro ponto de acesso ou dispositivo sem fio.