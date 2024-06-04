#redes #cyber
# Design resiliente

Resiliência representa os métodos e configurações usados para tornarem um sistema ou rede tolerante a falhas.

**Exemplos**

Por exemplo, uma rede pode ter links redundantes entre switches que executam o STP. Embora o STP proporcione um caminho alternativo pela rede se o link falhar, a transição pode não ser imediata, se a configuração não for ideal.

Os protocolos de roteamento também proporcionam resiliência, mas o ajuste fino pode melhorar a transição, para que os usuários da rede não percebam. Os administradores devem investigar as configurações não padrão em uma rede de testes, para ver se podem melhorar os tempos de recuperação em uma rede.

Como visto nos exemplos acima, o design resiliente é mais do que apenas adicionar redundância. É fundamental entender as necessidades comerciais da empresa e, em seguida, incorporar a redundância para criar uma rede resiliente.

**Resiliência do IOS**

O IOS (Interwork Operating System, Sistema operacional Interwork) para roteadores e switches Cisco incluem um atributo resiliente de configuração. Permite recuperação mais rápida se alguém, intencionalmente ou não, reformatar a memória flash ou apagar o arquivo de configuração de inicialização. Este atributo mantém uma cópia de trabalho segura do arquivo de imagem do IOS do roteador e uma cópia do arquivo de configuração de execução. O usuário não pode remover esses arquivos seguros, também conhecidos como o bootset primário.

Os comandos mostrados na figura protegem o arquivo de imagem IOS e o arquivo de configuração em execução.

**Resiliência de aplicativo**

Resiliência de aplicativo é a capacidade do aplicativo reagir a problemas em um de seus componentes sem parar de funcionar. Um administrador precisará, eventualmente, desativar aplicativos para aplicações de patches, atualizações de versão ou para implantar novas funcionalidades.

Alcançar a resiliência da infraestrutura de aplicativos significa evitar a perda de clientes, de funcionários ou de negócios devido a uma falha de aplicativo.

A figura mostra três soluções de disponibilidade para abordar a resiliência de aplicativos. À medida que o fator de disponibilidade de cada solução aumenta, a complexidade e os custos também aumentam.

- **Hardware tolerante a falhas** (mais complexo e mais caro) é um sistema projetado com a colocação de múltiplos componentes essenciais em um mesmo computador.  
- **Arquitetura de cluster** é um grupo de servidores que funcionam como se fossem um único sistema.
- **Backup e restauração** Cópias de backup de arquivos com a finalidade de poder restaurá-los se ocorrer perda de dados (menos complexo e menos caro).














