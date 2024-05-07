#redes 

# Tunelamento DNS

Botnets se tornaram um método de ataque popular de atores ameaçadores. Na maioria das vezes, os botnets são usados para espalhar malware ou iniciar ataques de DDoS e phishing.

O DNS na empresa às vezes é negligenciado como um protocolo que pode ser usado por botnets. Por isso, quando o tráfego DNS é determinado como parte de um incidente, o ataque geralmente já acabou. É necessário que o analista de segurança cibernética seja capaz de detectar quando um invasor está usando tunelamento DNS para roubar dados e prevenir e conter o ataque. Para isso, o analista de segurança deve implementar uma solução que possa bloquear as comunicações de saída dos hosts infectados.

Os agentes de ameaças que usam o tunelamento DNS colocam tráfego que não é de DNS, dentro do tráfego DNS. Esse método geralmente contorna soluções de segurança. Para que o agente da ameaça use o túnel DNS, os diferentes tipos de registros DNS, como TXT, MX, SRV, NULL, A ou CNAME, são alterados. Por exemplo, um registro TXT pode armazenar os comandos enviados para os bots de host infectados como respostas DNS. Um ataque de tunelamento DNS usando TXT funciona assim:

1. Os dados são divididos em vários blocos codificados.
2. Cada pedaço é colocado em um rótulo de nome de domínio de nível inferior na consulta DNS.
3. Como não há resposta do DNS local ou em rede para a consulta, a solicitação é enviada aos servidores DNS recursivos do ISP.
4. O serviço DNS recursivo encaminhará a consulta para o servidor de nomes autorizado do invasor.
5. O processo é repetido até que todas as consultas contendo os chunks sejam enviadas.
6. Quando o servidor de nomes autoritativo do invasor recebe as consultas DNS dos dispositivos infectados, ele envia respostas para cada consulta DNS, que contém os comandos encapsulados e codificados.
7. O malware no host comprometido recombina os pedaços e executa os comandos ocultos.

Para poder interromper o túnel DNS, um filtro que inspecione o tráfego DNS deve ser usado. Preste atenção especial às consultas DNS que são mais longas do que a média, ou aquelas que têm um nome de domínio suspeito. Além disso, as soluções de segurança de DNS, como Cisco Umbrella (anteriormente Cisco OpenDNS), bloqueiam grande parte do tráfego de túnel DNS ao identificar domínios suspeitos. Domínios associados a serviços DNS dinâmicos devem ser considerados altamente suspeitos.

![[Pasted image 20240507161316.png]]

























