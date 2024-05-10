#cyber #redes 
# Autenticação na Empresa

Em redes com requisitos de segurança mais rígidos, é necessária uma autenticação ou login adicional para conceder acesso a clientes sem fio. A opção de modo de segurança corporativa requer um servidor RADIUS de autenticação, autorização e contabilidade (AAA - Authentication, Authorization, and Accounting).

- **Endereço IP do servidor RADIUS -** Este é o endereço acessível do servidor RADIUS.
- **Números de porta UDP -** Portas UDP oficialmente atribuídas 1812 para autenticação RADIUS e 1813 para contabilidade RADIUS, mas também podem operar usando as portas UDP 1645 e 1646, conforme mostrado na figura.
- **Chave compartilhada -** Usada para autenticar o AP com o servidor RADIUS.

Na figura, o administrador está configurando o roteador sem fio com autenticação WPA2 Enterprise usando criptografia AES. O endereço IPv4 do servidor RADIUS também está configurado com uma senha forte para ser usada entre o roteador sem fio e o servidor RADIUS.

![[Pasted image 20240510133138.png]]

Uma chave compartilhada não é um parâmetro que deve ser configurado em um cliente sem fio. É necessário apenas um ponto de acesso para se autenticar com o servidor RADIUS. A autenticação e autorização do usuário são tratadas pelo padrão 802.1X, que fornece uma autenticação centralizada e baseada no servidor dos usuários finais.

O processo de login 802.1X usa o EAP para se comunicar com o servidor AP e RADIUS. O EAP é uma estrutura para autenticar ou acessar a rede. Ele pode fornecer um mecanismo de autenticação segura e negociar uma chave privada segura que pode ser usada para uma sessão de criptografia sem fio usando a criptografia TKIP ou AES.












