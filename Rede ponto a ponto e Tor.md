#cyber
# Rede ponto a ponto e Tor

Na rede ponto a ponto (P2P), mostrada na figura, os hosts podem operar em funções de cliente e servidor. Existem três tipos de aplicativos P2P: compartilhamento de arquivos, compartilhamento de processadores e mensagens instantâneas. No compartilhamento de arquivos P2P, os arquivos em uma máquina participante são compartilhados com membros da rede P2P. Exemplos disso são os outrora populares Napster e Gnutella. Bitcoin é uma operação P2P que envolve o compartilhamento de um banco de dados distribuído, ou razão, que registra saldos e transações Bitcoin. BitTorrent é uma rede de compartilhamento de arquivos P2P.

Sempre que os usuários desconhecidos recebem acesso aos recursos de rede, a segurança é uma preocupação. Aplicativos P2P de compartilhamento de arquivos não devem ser permitidos em redes corporativas. A atividade da rede P2P pode contornar as proteções de firewall e é um vetor comum para a propagação de malware. P2P é inerentemente dinâmico. Ele pode operar conectando-se a vários endereços IP de destino e também pode usar numeração dinâmica de portas. Arquivos compartilhados são frequentemente infectados com malware, e os atores de ameaças podem posicionar seu malware em clientes P2P para distribuição a outros usuários.

As redes P2P de compartilhamento de processadores doam ciclos de processador para tarefas computacionais distribuídas. Pesquisa de câncer, pesquisa de extraterrestres, e pesquisa científica usam ciclos de processador doados para distribuir tarefas computacionais.

Mensagens instantâneas (IM) também é considerado um aplicativo P2P. IM tem valor legítimo dentro de organizações que têm equipes de projeto distribuídas geograficamente. Nesse caso, aplicativos de IM especializados estão disponíveis, como a plataforma Webex Teams, que são mais seguras do que as mensagens instantâneas que usam servidores públicos.

## P2P

![[Pasted image 20240611082039.png]]

Tor é uma plataforma de software e rede de hosts P2P que funcionam como roteadores de internet na rede Tor. A rede Tor permite que os usuários naveguem na internet anonimamente. Os usuários acessam a rede Tor usando um navegador especial. Quando uma sessão de navegação é iniciada, o navegador constrói um caminho de ponta a ponta em camadas na rede do servidor Tor que é criptografado, como mostrado na figura. Cada camada criptografada é “removida” como as camadas de uma cebola (portanto, “onion routing”) à medida que o tráfego atravessa um retransmissor do Tor. As camadas contêm informações criptografadas do próximo salto que só podem ser lidas pelo roteador que precisa ler as informações. Dessa forma, nenhum dispositivo único conhece todo o caminho para o destino e as informações de roteamento só podem ser lidas pelo dispositivo que as requer. Finalmente, no final do caminho do Tor, o tráfego atinge seu destino na internet. Quando o tráfego é retornado à origem, um caminho criptografado em camadas é construído novamente.

Tor apresenta uma série de desafios aos analistas de segurança cibernética. Primeiro, o Tor é amplamente utilizado por organizações criminosas na “Dark Net”. Além disso, Tor tem sido usado como um canal de comunicação para malware CNC. Como o endereço IP de destino do tráfego Tor é ofuscado pela criptografia, com apenas o nó Tor de próximo salto conhecido, o tráfego Tor evita listas negras configuradas em dispositivos de segurança.

## Operação Tor

![[Pasted image 20240611082118.png]]



