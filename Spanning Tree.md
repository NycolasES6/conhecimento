#redes #cyber 
# Spanning Tree

A redundância aumenta a disponibilidade da infraestrutura da rede, protegendo-a de um ponto único de falha, como um cabo ou um switch com falha na rede.

Quando os designers projetam a redundância física em uma rede, pode haver loops e quadros duplicados. Os loops e quadros duplicados têm consequências graves para uma rede comutada.

O Spanning Tree Protocol (STP) soluciona esses problemas. A função básica do STP é prevenir loops em uma rede, quando os switches se interconectarem por vários caminhos. O STP garante que os links físicos redundantes estejam livres de loop e que apenas um caminho lógico seja executado entre todos os destinos na rede. O STP bloqueia intencionalmente os caminhos redundantes que poderiam provocar um loop.

Bloquear os caminhos redundantes é fundamental para evitar loops na rede. Os caminhos físicos ainda existirão para fornecer redundância, mas o STP desativa esses caminhos para evitar que ocorram loops. Se um cabo ou switch da rede falhar, o STP recalculará os caminhos e desbloqueará as portas necessárias, para permitir que o caminho redundante se torne ativo.

Esta animação mostra os estágios de STP quando ocorre uma falha.

1. O PC1 envia uma transmissão para a rede.
2. O trunk link entre S2 e S1 falha, resultando em interrupção do caminho original.
3. O S2 desbloqueia a porta anteriormente bloqueada do Tronco2 e permite que o tráfego de broadcast siga o caminho alternativo na rede, permitindo que a comunicação continue.
4. Se o link entre S2 e S1 voltar a funcionar, o STP bloqueará novamente o link entre S2 e S3.

![[Pasted image 20240604095954.png]]











