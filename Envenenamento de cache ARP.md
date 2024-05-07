#redes #cyber 

# Envenenamento de cache ARP

O envenenamento do cache ARP pode ser usado para iniciar vários ataques do tipo man-in-the-middle.

## Requisição ARP

 figura mostra como o envenenamento de cache do ARP funciona. PC-A requer o endereço MAC do seu gateway padrão (R1); então, ele envia uma solicitação ARP para o endereço MAC 192.168.10.1.

![[Pasted image 20240507154733.png]]

## Resposta ARP

Nesta figura, o R1 atualiza seu cache ARP com os endereços IP e MAC do PC-A. R1 envia uma resposta ARP ao PC-A, que atualiza seu cache ARP com os endereços IP e MAC de R1.

![[Pasted image 20240507154823.png]]

## Respostas falsas gratuitas de ARP

Na figura, o agente da ameaça envia duas respostas ARP gratuitas falsificadas usando seu próprio endereço MAC para os endereços IP de destino indicados. O PC-A atualiza seu cache ARP com seu gateway padrão, que agora está apontando para o endereço MAC do host do agente da ameaça. O R1 também atualiza seu cache ARP com o endereço IP do PC-A apontando para o endereço MAC do agente da ameaça.

O host do ator de ameaça está executando um ataque de envenenamento ARP. O ataque de envenenamento ARP pode ser passivo ou ativo. O envenenamento ARP passivo é onde os atores de ameaças roubam informações confidenciais. O envenenamento ARP ativo é onde os agentes de ameaças modificam dados em trânsito ou injetam dados maliciosos.

![[Pasted image 20240507154923.png]]

**Nota:** Existem muitas ferramentas disponíveis na Internet para criar ataques ARP MITM, incluindo dsniff, Cain & Abel, ettercap, Yersinia e outros.











