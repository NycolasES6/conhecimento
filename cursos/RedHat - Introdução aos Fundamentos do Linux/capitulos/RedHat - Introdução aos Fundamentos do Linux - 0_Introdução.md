#redhat #Linux 
# RedHat - Introdução aos Fundamentos do Linux - Introdução

# Orientação para o ambiente de sala de aula

![[Pasted image 20240612135656.png]]

Neste curso, o principal sistema de computador para atividades de aprendizagem prática é o `workstation`. Os alunos também utilizam outra máquina para essas atividades: `servera`. Os dois sistemas estão no `lab.example.com`domínio DNS.

Todos os sistemas de computador dos alunos possuem uma conta de usuário padrão, `student`que usa a senha `student`. A `root`senha do usuário em todos os sistemas dos alunos é `redhat`.

## Tabela 1. Máquinas de sala de aula

|Nome da maquina|endereço de IP|Papel|
|:--|:--|:--|
|bastion.lab.example.com|172.25.250.254|Sistema gateway para conectar a rede privada do aluno ao servidor da sala de aula (deve estar sempre em execução)|
|sala de aula.exemplo.com|172.25.254.254|Servidor que hospeda os materiais de sala de aula necessários|
|estação de trabalho.lab.example.com|172.25.250.9|Estação de trabalho gráfica para uso dos alunos|
|servera.lab.example.com|172.25.250.10|Servidor gerenciado "A"|

A principal função da `bastion`máquina é atuar como um roteador entre a rede que conecta as máquinas dos alunos e a rede da sala de aula. Se a `bastion`máquina estiver inoperante, as outras máquinas dos alunos poderão acessar apenas os sistemas que estão na rede individual dos alunos.

Vários sistemas na sala de aula fornecem serviços de suporte. Dois servidores, `content.example.com`e `materials.example.com`, são fontes de software e materiais de laboratório em atividades práticas. Informações sobre como usar esses servidores são fornecidas nas instruções para essas atividades. A `workstation`máquina virtual fornece essas atividades. Ambas as máquinas `classroom`e `bastion`devem estar sempre funcionando para o uso adequado do ambiente de laboratório.

### OBSERVAÇÃO

Ao fazer login na `servera`máquina, você poderá ver uma mensagem sobre a ativação do `cockpit`console da web. Você pode ignorar a mensagem.

```sh
[aluno@estação de trabalho ~]$ssh student@servera
Aviso: ‘servera,172.25.250.09’ (ECDSA) foi adicionado permanentemente à lista de hosts conhecidos.
Ative o console web com: systemctl enable --now cockpit.socket
[aluno@servidor ~]$
```

### Controlando seus sistemas

Você recebe computadores remotos em uma sala de aula do Red Hat Online Learning (ROLE). Os cursos individualizados são acessados ​​por meio de um aplicativo da web hospedado em [rol.redhat.com](http://rol.redhat.com/) . Faça login neste site com suas credenciais de usuário do Red Hat Customer Portal.

#### Controlando as máquinas virtuais

As máquinas virtuais em seu ambiente de sala de aula são controladas por meio de controles de interface de página web. O estado de cada máquina virtual de sala de aula é exibido na guia Ambiente de Laboratório .

![[Pasted image 20240612135952.png]]

**Tabela 2. Estados da Máquina**

|Estado da máquina virtual|Descrição|
|:--|:--|
|prédio|A máquina virtual está sendo criada.|
|ativo|A máquina virtual está em execução e disponível. Se acabou de começar, ainda pode estar iniciando serviços.|
|parou|A máquina virtual está completamente desligada. Ao iniciar, a máquina virtual inicializa no mesmo estado em que estava antes do desligamento. O estado do disco é preservado.|

**Tabela 3. Ações em sala de aula**

|Botão ou ação|Descrição|
|:--|:--|
|CRIAR|Crie a sala de aula ROLE. Cria e inicia todas as máquinas virtuais necessárias para esta sala de aula. A criação pode levar vários minutos para ser concluída.|
|CRIANDO|As máquinas virtuais de sala de aula ROLE estão sendo criadas. Cria e inicia todas as máquinas virtuais necessárias para esta sala de aula. A criação pode levar vários minutos para ser concluída.|
|EXCLUIR|Exclua a sala de aula ROLE. Destrói todas as máquinas virtuais da sala de aula. **Todo o trabalho salvo nos discos desses sistemas será perdido.**|
|COMEÇAR|Inicie todas as máquinas virtuais na sala de aula.|
|INICIANDO|Todas as máquinas virtuais da sala de aula estão sendo iniciadas.|
|PARAR|Pare todas as máquinas virtuais na sala de aula.|

**Tabela 4. Ações da Máquina**

| Botão ou ação       | Descrição                                                                                                                                                                                                                                                                                                              |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ABRIR CONSOLA       | Conecte-se ao console do sistema da máquina virtual em uma nova guia do navegador. Você pode fazer login diretamente na máquina virtual e executar comandos, quando necessário. Normalmente, faça login apenas na `workstation`máquina virtual e, a partir daí, use `ssh`para conectar-se às outras máquinas virtuais. |
| AÇÃO → Iniciar      | Inicie (ligue) a máquina virtual.                                                                                                                                                                                                                                                                                      |
| AÇÃO → Desligamento | Desligue normalmente a máquina virtual, preservando o conteúdo do disco.                                                                                                                                                                                                                                               |
| AÇÃO → Desligar     | Desligue a máquina virtual à força, preservando ao mesmo tempo o conteúdo do disco. Esta ação equivale a remover a energia de uma máquina física.                                                                                                                                                                      |
| AÇÃO → Redefinir    | Desligue à força a máquina virtual e redefina o armazenamento associado ao seu estado inicial. **Todo o trabalho salvo nos discos desse sistema será perdido.**                                                                                                                                                        |

No início de um exercício, se for instruído a redefinir um único nó de máquina virtual, clique em AÇÃO → Redefinir apenas para aquela máquina virtual específica.

No início de um exercício, se for instruído a redefinir todas as máquinas virtuais, clique em AÇÃO → Redefinir em todas as máquinas virtuais da lista.

Se quiser retornar o ambiente da sala de aula ao seu estado original no início do curso, clique em EXCLUIR para remover todo o ambiente da sala de aula. Depois que o laboratório for excluído, clique em CRIAR para provisionar um novo conjunto de sistemas de sala de aula.

#### Os temporizadores de parada automática e destruição automática

A inscrição no Red Hat Online Learning lhe dá direito a uma parcela definida de tempo de uso do computador. Para ajudar a conservar o tempo alocado, a sala de aula ROLE usa temporizadores, que desligam ou excluem o ambiente da sala de aula quando o temporizador apropriado expira.

Para ajustar os cronômetros, localize os dois botões + na parte inferior da página de gerenciamento do curso. Clique no botão de parada automática  + para adicionar mais uma hora ao cronômetro de parada automática. Clique no botão + destruição automática  para adicionar outro dia ao cronômetro de destruição automática. A parada automática tem no máximo 11 horas e a destruição automática tem no máximo 14 dias. Tenha cuidado para manter os temporizadores configurados enquanto você trabalha, para que seu ambiente não seja desligado inesperadamente. Tenha cuidado para não definir os cronômetros desnecessariamente altos, o que pode desperdiçar o tempo de sua assinatura.

## Realizando exercícios de laboratório

Você poderá ver os seguintes tipos de atividades de laboratório neste curso:

- A_exercício guiado_é um exercício prático que segue uma seção de apresentação. Ele orienta você em um procedimento a ser executado, passo a passo.
    
- A_questionário_é normalmente usado para verificar a aprendizagem baseada em conhecimento ou quando uma atividade prática é impraticável por algum outro motivo.
    
- Um_laboratório de final de capítulo_é uma atividade prática avaliável para ajudá-lo a verificar seu aprendizado. Você trabalha através de um conjunto de etapas de alto nível, com base nos exercícios guiados naquele capítulo, mas as etapas não orientam você em todos os comandos. Uma solução é fornecida com um passo a passo.
    
- A_laboratório de revisão abrangente_é usado no final do curso. Também é uma atividade prática avaliável e pode abranger o conteúdo de todo o curso. Você trabalha com uma especificação do que realizar na atividade, sem receber as etapas específicas para fazê-lo. Novamente, uma solução é fornecida com um passo a passo que atende às especificações.
    

Para preparar seu ambiente de laboratório no início de cada atividade prática, execute o `lab start`comando com um nome de atividade especificado nas instruções da atividade. Da mesma forma, ao final de cada atividade prática, execute o `lab finish`comando com o mesmo nome de atividade para limpar após a atividade. Cada atividade prática tem um nome exclusivo dentro de um curso.

A sintaxe para executar um script de exercício é a seguinte:

[aluno@estação de trabalho ~]$**``lab _`action`_ _`exercise`_``**

O_Ação_é uma escolha de `start`, `grade`, ou `finish`. Todos os exercícios suportam `start`e `finish`. Somente laboratórios de final de capítulo e laboratórios de revisão abrangentes oferecem suporte `grade`.

começar

A `start`ação verifica os recursos necessários para iniciar um exercício. Pode incluir a definição de configurações, a criação de recursos, a verificação de serviços pré-requisitos e a verificação dos resultados necessários de exercícios anteriores. Você pode realizar um exercício a qualquer momento, mesmo sem realizar os exercícios anteriores.

nota

Para atividades avaliáveis, a `grade`ação direciona o `lab`comando para avaliar seu trabalho e mostra uma lista de critérios de avaliação com um status `PASS`ou `FAIL`para cada um. Para obter um `PASS`status para todos os critérios, corrija as falhas e execute novamente a `grade`ação.

terminar

A `finish`ação limpa recursos que foram configurados durante o exercício. Você pode realizar um exercício quantas vezes quiser.

O `lab`comando oferece suporte ao preenchimento de tabulação. Por exemplo, para listar todos os exercícios que você pode iniciar, digite `lab start`e pressione a tecla **Tab duas vezes**
