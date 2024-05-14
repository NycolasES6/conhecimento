#SO #Windows 

# Gerenciador de Tarefas e Monitor de Recursos

Existem duas ferramentas muito importantes e úteis para ajudar um administrador a compreender os vários aplicativos, serviços e processos diferentes que estão sendo executados em um computador Windows. Essas ferramentas também fornecem informações sobre o desempenho do computador, como CPU, memória e uso da rede. Essas ferramentas são especialmente úteis ao investigar um problema em que o malware é suspeito. Quando um componente não está executando da maneira que deveria ser, essas ferramentas podem ser usadas para determinar qual o problema pode ser.

## Gerenciador de Tarefas

O Gerenciador de Tarefas, que é mostrado na figura, fornece muitas informações sobre o software em execução e o desempenho geral do computador.

![[Pasted image 20240514131426.jpg]]

### Processos

- Lista todos os programas e processos que estão em execução no momento.
- Exibe a utilização da CPU, da memória, do disco e da rede de cada processo.
- As propriedades de um processo podem ser examinadas ou encerradas se ele não estiver se comportando corretamente ou tiver parado.

### Desempenho

- Uma exibição de todas as estatísticas de desempenho fornece uma visão geral útil do desempenho da CPU, memória, disco e rede.
- Clicar em cada item no painel esquerdo irá mostrar estatísticas detalhadas desse item no painel direito.

### Histórico de aplicativos

- O uso de recursos por aplicativo ao longo do tempo fornece informações sobre aplicativos que estão consumindo mais recursos do que deveriam.
- Clique em **Opções** e **Mostrar histórico de todos os processos** para ver o histórico de todos os processos executados desde que o computador foi iniciado.

### Inicializar

- Todos os aplicativos e serviços que iniciam quando o computador é inicializado são mostrados nesta guia.
- Para desativar o início de um programa na inicialização, **clique com** o botão direito do mouse no item e escolha **Desativar**.

### Usuários

- Todos os usuários que estão conectados ao computador são mostrados nesta guia.
- Também são mostrados todos os recursos que os aplicativos e processos de cada usuário estão usando.
- Nesta guia, um administrador pode desconectar um usuário do computador.

### Detalhes

- Semelhante à guia Processos, essa guia fornece opções de gerenciamento adicionais para processos, como definir uma prioridade para que o processador dedique mais ou menos tempo a um processo.
- A afinidade da CPU também pode ser definida, o que determina qual núcleo ou CPU um programa usará.
- Além disso, um recurso útil chamado Analisar cadeia de espera mostra qualquer processo para o qual outro processo está aguardando.
- Esse recurso ajuda a determinar se um processo está simplesmente aguardando ou está parado.

### Serviços

- Todos os serviços que são carregados são mostrados nesta guia.
- O ID do processo (PID) e uma breve descrição também são mostrados juntamente com o status de Executando ou Parado.
- Na parte inferior, há um botão para abrir o console Serviços que fornece gerenciamento adicional de serviços.

## Monitor de recursos

Quando forem necessárias informações mais detalhadas sobre o uso de recursos, você poderá usar o Monitor de Recursos, conforme mostrado na figura.

![[Pasted image 20240514131902.jpg]]

Ao procurar o motivo pelo qual um computador pode estar agindo de forma irregular, o Monitor de Recursos pode ajudar a encontrar a origem do problema.

### Visão geral

- A guia exibe o uso geral de cada recurso.
- Se você selecionar um único processo, ele será filtrado em todas as guias para mostrar apenas as estatísticas desse processo.

### CPU

- O PID, o número de threads, qual CPU o processo está usando e o uso médio da CPU de cada processo é mostrado.
- Informações adicionais sobre quaisquer serviços em que o processo se baseia e os identificadores e módulos associados podem ser vistas expandindo as linhas inferiores.

### Memória

- Todas as informações estatísticas sobre como cada processo usa memória são mostradas nesta guia.
- Além disso, uma visão geral do uso de toda a RAM é mostrada abaixo da linha Processos.

### Disco

Todos os processos que estão usando um disco são mostrados nesta guia, com estatísticas de leitura/gravação e uma visão geral de cada dispositivo de armazenamento.

### Rede

- Todos os processos que estão usando a rede são mostrados nesta guia, com estatísticas de leitura/gravação.
- Mais importante ainda, as conexões TCP atuais são mostradas, juntamente com todas as portas que estão escutando.
- Esta guia é muito útil ao tentar determinar quais aplicativos e processos estão se comunicando pela rede.
- Permite saber se um processo não autorizado está acessando a rede, ouvindo uma comunicação e o endereço com o qual está se comunicando.