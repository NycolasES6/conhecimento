#redes #cyber 

# Ataques UDP

O UDP não está protegido por nenhuma criptografia. Você pode adicionar criptografia ao UDP, mas não está disponível por padrão. A falta de criptografia significa que qualquer pessoa pode ver o tráfego, alterá-lo e enviá-lo ao seu destino. Alterar os dados no tráfego alterará o número de checagem de 16 bits, mas o número de checagem é opcional e nem sempre é usado. Quando o número de checagem é usado, o agente de ameaça pode criar um novoo número de checagem com base na nova carga de dados e registrá-lo no cabeçalho como um novo o número de checagem. O dispositivo de destino descobrirá que o número de checagem corresponde aos dados sem saber que os dados foram alterados. Esse tipo de ataque não é amplamente utilizado.

**Ataques de inundação UDP**

É mais provável que você veja um ataque de inundação UDP. Em um ataque de inundação UDP, todos os recursos em uma rede são consumidos. O agente de ameaça deve usar uma ferramenta como UDP Unicorn ou Low Orbit Ion Cannon. Essas ferramentas enviam uma inundação de pacotes UDP, geralmente de um host falsificado, para um servidor na sub-rede. O programa varrerá todas as portas conhecidas tentando encontrar portas fechadas. Isso fará com que o servidor responda com uma mensagem inacessível da porta ICMP. Como existem muitas portas fechadas no servidor, isso cria muito tráfego no segmento, que consome a maior parte da largura de banda. O resultado é muito semelhante a um ataque de negação de serviço (DoS).




































