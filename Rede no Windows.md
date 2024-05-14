#redes #Windows #SO 
# Rede

Um dos recursos mais importantes de qualquer sistema operacional é a capacidade do computador se conectar a uma rede. Sem esse recurso, não há acesso aos recursos de rede ou à internet. Para configurar as propriedades de rede do Windows e testar as configurações de rede, o Centro de Rede e Compartilhamento é usado. A maneira mais fácil de executar esta ferramenta é procurá-la e clicar nela. Use o Centro de Rede e Compartilhamento para verificar ou criar conexões de rede, configurar o compartilhamento de rede e alterar as configurações do adaptador de rede.

## Central de rede e compartilhamento

![[Pasted image 20240514133229.jpg]]

 visualização inicial mostra uma visão geral da rede ativa. Essa exibição mostra se há acesso à Internet e se a rede é privada, pública ou convidada. O tipo de rede, com ou sem fio, também é mostrado. Nessa janela, você pode ver o Grupo Doméstico ao qual o computador pertence ou criar um caso ainda não faça parte de um Grupo Doméstico. Essa ferramenta também pode ser usada para alterar configurações do adaptador, alterar configurações de compartilhamento antecipado, configurar uma nova conexão ou solucionar problemas. Observe que o Grupo Doméstico foi removido do Windows 10 na versão 1803.

## Alterar as configurações do adaptador

A visualização inicial mostra uma visão geral da rede ativa. Essa exibição mostra se há acesso à Internet e se a rede é privada, pública ou convidada. O tipo de rede, com ou sem fio, também é mostrado. Nessa janela, você pode ver o Grupo Doméstico ao qual o computador pertence ou criar um caso ainda não faça parte de um Grupo Doméstico. Essa ferramenta também pode ser usada para alterar configurações do adaptador, alterar configurações de compartilhamento antecipado, configurar uma nova conexão ou solucionar problemas. Observe que o Grupo Doméstico foi removido do Windows 10 na versão 1803.

**Alterar as configurações do adaptador**

Para configurar um adaptador de rede, escolha **Alterar configurações do adaptador** no Centro de Rede e Compartilhamento para mostrar todas as conexões de rede disponíveis. Selecione o adaptador que você deseja configurar. Neste caso, alteramos um adaptador Ethernet para adquirir seu endereço IPv4 automaticamente da rede.

### Propriedades do Adaptador de Acesso

Clique com o botão direito do mouse no adaptador que deseja configurar e escolha Propriedades, conforme mostrado na figura.

![[Pasted image 20240514133403.jpg]]

### Acessar Propriedades TCP/IPV4

Esta conexão utiliza os seguintes itens: Protocolo **Internet Protocol Version 4 (TCP/IPv4)** ou **Internet Protocol Version 6 (TCP/IPv6),** dependendo da versão que pretende utilizar. Na figura, IPv4 está sendo selecionado.

![[Pasted image 20240514133423.jpg]]

### Alterar configurações

Clique em **Propriedades** para configurar o adaptador. Na caixa de diálogo **Propriedades**, mostrada na figura, você pode optar por **Obter um endereço automaticamente** se houver um servidor DHCP disponível na rede. Se desejar configurar o endereçamento manualmente, você pode preencher o endereço, a sub-rede, o gateway padrão e os servidores DNS para configurar o adaptador. Clique em **OK** para aceitar as alterações. Você também pode usar a ferramenta netsh.exe para configurar os parâmetros de rede em um prompt de comando. Este programa pode exibir e modificar a configuração de rede. Digite **netsh/?** no prompt de comando para ver uma lista de todas as opções que podem ser usadas com este comando.

![[Pasted image 20240514133447.jpg]]

## nslook e netstat

O Sistema de Nomes de Domínio (DNS) também deve ser testado porque é essencial encontrar o endereço dos hosts traduzindo-o a partir de um nome, como uma URL. Use o comando **nslookup** para testar o DNS. Digite **nslookup cisco.com** no prompt de comando para encontrar o endereço do servidor da Web Cisco. Quando o endereço é retornado, você sabe que o DNS está funcionando corretamente. Você também pode verificar quais portas estão abertas, onde elas estão conectadas e qual é seu status atual. Digite **netstat** na linha de comando para ver os detalhes das conexões de rede ativas, conforme mostrado na saída do comando. O comando **netstat** será examinado mais adiante neste módulo.

```sh
C:∖Users∖USER>netstat

Active Connections

  Proto     Local Address        Foreign Address     State

  TCP     127.0.0.1:3030        USER-VGFFA:58652   ESTABLISHED

  TCP     127.0.0.1:3030        USER-VGFFA:62114   ESTABLISHED

  TCP     &127.0.0.1:3030       USER-VGFFA:62480   TIME_WAIT

  TCP     127.0.0.1:3030        USER-VGFFA:62481   TIME_WAIT

  TCP     127.0.0.1:3030        USER-VGFFA:62484   TIME_WAIT
```
