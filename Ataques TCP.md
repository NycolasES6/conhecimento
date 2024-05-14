#redes #cyber 

# Ataques TCP

Aplicações em Rede usam portas TCP ou UDP. Os atores de ameaças realizam varreduras de portas dos dispositivos de destino para descobrir quais serviços eles oferecem.

**Ataque de Inundação de SYN TCP**

O ataque de inundação SYN TCP explora o aperto de mãos triplo do TCP. A figura mostra um agente de ameaça enviando continuamente pacotes de solicitação de sessão TCP SYN com um endereço IP de origem falsificado aleatoriamente para um destino. O dispositivo de destino responde com um pacote TCP SYN-ACK ao endereço IP falsificado e aguarda um pacote TCP ACK. Essas respostas nunca chegam. Eventualmente, o host de destino é sobrecarregado com conexões TCP semi-abertas e os serviços TCP são negados a usuários legítimos.

**Ataque de Inundação de SYN TCP**

![[Pasted image 20240507133646.png]]

1. O agente da ameaça envia várias solicitações SYN para o servidor web.
2. O servidor web responde com SYN-ACK's para cada solicitação SYN e espera completar o handshake de três vias. O ator de tratamento não responde aos SYN-ACK's.
3. O usuário válido não pode acessar o servidor web porque o servidor web tem muitas conexões TCP semi-abertas.

**Ataque de redefinição de TCP**

Um ataque de redefinição de TCP pode ser usado para encerrar as comunicações TCP entre dois hosts. A figura mostra como o TCP usa uma troca de quatro direções para fechar a conexão TCP usando um par de segmentos FIN e ACK de cada extremidade da conexão TCP. Uma conexão TCP termina quando recebe um bit RST. Essa é uma maneira abrupta de interromper a conexão TCP e informar o host de recebimento para parar imediatamente de usar a conexão TCP. Um agente de ameaça pode fazer um ataque de redefinição de TCP e enviar um pacote falsificado contendo um TCP RST para um ou ambos os pontos de extremidade.

**Terminando uma conexão TCP**

![[Pasted image 20240507134020.png]]

O encerramento de uma sessão TCP usa o seguinte processo de troca de quatro vias:

1. Quando o cliente não tem mais dados para enviar no fluxo, ele envia um segmento com o sinalizador FIN definido.
2. O servidor envia um ACK para confirmar o recebimento do FIN para encerrar a sessão do cliente para o servidor.
3. O servidor envia o FIN ao cliente para encerrar a sessão de servidor para cliente.
4. O cliente responde com um ACK para reconhecer o FIN do servidor.

**Sequestro de sessão TCP**

Sequestro de sessão TCP é outra vulnerabilidade do TCP. Embora seja difícil de conduzir, um agente de ameaça assume um host já autenticado quando ele se comunica com o alvo. O agente de ameaça deve falsificar o endereço IP de um dos hosts, prever o próximo número de sequência e enviar um ACK para o outro host. Se for bem-sucedido, o agente da ameaça poderá enviar, mas não receber, dados do dispositivo de destino.

---






