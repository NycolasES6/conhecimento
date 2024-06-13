#Windows 
# Definir o SMB e suas considerações de segurança

Gerenciar a colaboração e o compartilhamento de dados é uma parte importante das responsabilidades de um administrador de TI. Para atender a essas responsabilidades, convém entender as tecnologias que servem como base para o compartilhamento de arquivos do Windows, como o protocolo SMB.

## O que é o protocolo SMB?

SMB é um protocolo de compartilhamento de arquivos de rede baseado em TCP/IP que permite que aplicativos em um computador leiam e gravem em arquivos e solicitem serviços de programas de servidor em uma rede de computadores. Utilizando o protocolo SMB, um aplicativo (ou o usuário de um aplicativo) pode acessar arquivos ou outros recursos em um servidor remoto. Isso permite que os aplicativos leiam, criem e atualizem arquivos no servidor remoto.

## Quais são os benefícios do SMB 3.x?

A Microsoft desenvolveu o protocolo SMB nos anos 1980. A especificação original, SMB 1, era ineficiente em termos de largura de banda e não tinha um nível de segurança suficiente. As versões do SMB subsequentes abordaram essas deficiências por meio de recursos como criptografia interna, SMB Multichannel e SMB Direct.

O SMB 2.0, que a Microsoft introduziu no Windows Server 2008, ofereceu melhorias significativas de desempenho, no entanto, não resolveu de nenhuma maneira significativa os desafios de segurança.

O SMB 3.0, que a Microsoft introduziu no Windows Server 2012, inclui os seguintes recursos:

- Failover Transparente do SMB. Esse recurso permite aos administradores realizar a manutenção de hardware ou software dos nós em um servidor de arquivos em cluster sem interromper os aplicativos do servidor que armazenam dados nos compartilhamentos de arquivos.
- Escalar horizontalmente o SMB. Em configurações clusterizadas, você pode criar compartilhamentos de arquivos que fornecem acesso simultâneo a arquivos de dados, com E/S (entrada/saída) direta, por meio de todos os nós em um cluster de servidor de arquivos.
- Criptografia de SMB. Esse recurso fornece a criptografia ponta a ponta de dados SMB em redes não confiáveis e ajuda a proteger os dados contra espionagem.
- Comandos do Windows PowerShell para gerenciar o SMB. Você pode gerenciar compartilhamentos de arquivo no servidor de arquivos, de ponta a ponta, pela linha de comando.
- SMB Multichannel. Esse recurso permite que você agregue a largura de banda da rede e a tolerância a falhas da rede caso vários caminhos estejam disponíveis entre o servidor e o cliente SMB 3.x.
- SMB Direct. Esse recurso dá suporte a adaptadores de rede que têm o recurso RDMA (Acesso Remoto Direto à Memória) e podem funcionar em velocidade total com latência muito baixa e usando muito pouco tempo de processamento da CPU (unidade de processamento central).

O SMB 3.1.1, que a Microsoft introduziu no Windows Server 2016, oferece vários aprimoramentos adicionais, incluindo:

- Integridade da pré-autenticação. A integridade da pré-autenticação fornece proteção aprimorada contra um ataque man-in-the-middle que possa interferir no estabelecimento e na autenticação de mensagens de conexão SMB.
- Aprimoramentos de criptografia do SMB. A criptografia do SMB, introduzida com o SMB 3.0, usa um algoritmo de criptografia fixo, o AES-128-CCM. No entanto, o AES-128-GCM, disponível com o SMB 3.1.1, funciona melhor com processadores mais modernos.
- Remoção da configuração **RequireSecureNegotiate**. Como algumas implementações de terceiros do SMB não executam essa negociação corretamente, a Microsoft fornece uma opção para desabilitar a Negociação Segura. No entanto, o padrão para servidores e clientes SMB 3.1.1 é usar a integridade pré-autenticação, conforme descrito anteriormente.






