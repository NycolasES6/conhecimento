#redes #cyber 
# DNS

O Serviço de Nome de Domínio (DNS) é usado por milhões de pessoas diariamente. Por isso, muitas organizações têm políticas menos rigorosas para proteger contra ameaças baseadas em DNS do que precisam proteger contra outros tipos de explorações. Os invasores reconheceram isso e geralmente encapsulam diferentes protocolos de rede no DNS para evitar dispositivos de segurança. O DNS agora é usado por muitos tipos de malware. Algumas variedades de malware usam DNS para se comunicar com servidores de comando e controle (CNC) e para exfiltrar dados no tráfego disfarçados como consultas DNS normais. Vários tipos de codificação, como Base64, binário de 8 bits e Hex podem ser usados para camuflar os dados e evitar medidas básicas de prevenção de perda de dados (DLP).

Por exemplo, malware pode codificar dados roubados como a parte de subdomínio de uma pesquisa DNS para um domínio onde o servidor de nomes está sob controle de um invasor. Uma pesquisa de DNS para 'long string-of-exfiltrated-data.example.com' seria encaminhada para o servidor de nomes de example.com, que gravaria 'long string-of-exfiltrated-data' e responderia de volta ao malware com uma resposta codificada. Este uso do subdomínio DNS é mostrado na figura. Os dados exfiltrados são o texto codificado mostrado na caixa. O ator de ameaças coleta esses dados codificados, decodifica e combina e agora tem acesso a um arquivo de dados inteiro, como um banco de dados de nome de usuário/senha.

É provável que a parte do subdomínio de tais solicitações seria muito mais longa do que as solicitações usuais. Analistas cibernéticos podem usar a distribuição dos comprimentos de subdomínios dentro de solicitações DNS para construir um modelo matemático que descreva a normalidade. Eles podem então usar isso para comparar suas observações e identificar um abuso do processo de consulta DNS. Por exemplo, não seria normal ver um host em sua rede enviando uma consulta para AW4GCGXHy2UGDG8GCHJVDGVJDC.Example.com.

Consultas DNS para nomes de domínio gerados aleatoriamente, ou subdomínios com aparência aleatória extremamente longos, devem ser consideradas suspeitas, especialmente se a ocorrência deles aumentar drasticamente na rede. Os logs de proxy DNS podem ser analisados para detectar essas condições. Como alternativa, serviços como o serviço DNS passivo do Cisco Umbrella podem ser usados para bloquear solicitações para CNC suspeitos e domínios de exploração.

## Exfiltração de DNS

![[Pasted image 20240604112619.png]]