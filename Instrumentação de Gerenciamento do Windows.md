#SO #Windows 
# Instrumentação de Gerenciamento do Windows

A Instrumentação de Gerenciamento do Windows (WMI) é usada para gerenciar computadores remotos. Ele pode recuperar informações sobre componentes de computador, estatísticas de hardware e software e monitorar a integridade de computadores remotos. Para abrir o controle WMI no Painel de Controle, clique duas vezes em **Ferramentas Administrativas > Gerenciamento do Computador** para abrir a janela Gerenciamento do Computador, expanda a árvore **Serviços e Aplicativo**s e clique com o botão direito do mouse no ícone **Controle WMI > Propriedades**.

A janela Propriedades de Controle WMI é mostrada na figura.

![[Pasted image 20240514130257.jpg]]

Estas são as quatro guias na janela Propriedades de Controle WMI:

- **Geral -** Informações resumidas sobre o computador local e o WMI
- **Backup/Restaurar -** Permite o backup manual das estatísticas coletadas pelo WMI
- **Segurança -** Configurações para configurar quem tem acesso a diferentes estatísticas WMI
- **Avançado -** Configurações para configurar o namespace padrão para WMI

Alguns ataques hoje usam o WMI para se conectar a sistemas remotos, modificar o registro e executar comandos. O WMI ajuda-os a evitar a detecção porque é tráfego comum, na maioria das vezes confiável pelos dispositivos de segurança de rede e os comandos WMI remotos geralmente não deixam evidências no host remoto. Devido a isso, o acesso WMI deve ser estritamente limitado.




















