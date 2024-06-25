# Cyber - Pós-exploração

Vamos supor que exploramos com sucesso o sistema alvo durante o `Exploitation`estágio. Tal como acontece com o estágio de Exploração, devemos novamente considerar se devemos ou não utilizar `Evasive Testing`no `Post-Exploitation`estágio. Já estamos no sistema na fase pós-exploração, tornando muito mais difícil evitar um alerta. A `Post-Exploitation`etapa visa obter informações sensíveis e relevantes para a segurança a partir de uma perspectiva local e informações relevantes para o negócio que, na maioria dos casos, requerem privilégios mais elevados do que um utilizador padrão. Esta etapa inclui os seguintes componentes:

|                          |                              |
| ------------------------ | ---------------------------- |
| Testes Evasivos          | Coleta de informações        |
| Pilhagem                 | Avaliação de vulnerabilidade |
| Escalação de privilégios | Persistência                 |
| Exfiltração de dados     |                              |

![[0-PT-Process-POEX.webp]]

## Testes evasivos

Se um administrador qualificado monitorar os sistemas, qualquer alteração ou mesmo um único comando poderá disparar um alarme que nos denunciará. Em muitos casos, somos expulsos da rede e então começa a caça às ameaças onde somos o foco. Também podemos perder o acesso a um host (que fica em quarentena) ou a uma conta de usuário (que fica temporariamente desativada ou com a senha alterada). Esse teste de penetração teria falhado, mas foi bem-sucedido em alguns aspectos porque o cliente conseguiu detectar algumas ações. Podemos agregar valor ao cliente nesta situação, ainda escrevendo toda uma cadeia de ataque e ajudando-o a identificar lacunas em seu monitoramento e processos onde eles não perceberam nossas ações. Para nós, podemos estudar como e por que o cliente nos detectou e trabalhar para melhorar nossas habilidades de evasão. Talvez não tenhamos testado completamente uma carga útil ou tenhamos sido descuidados e executado um comando como `net user`ou `whoami`que é frequentemente monitorado por sistemas EDR e sinalizado como atividade anômala.

s testes evasivos são divididos em três categorias diferentes:

| **`Evasive`** | **`Hybrid Evasive`** | **`Non-Evasive`** |
| ------------- | -------------------- | ----------------- |

## Coleta de informações

Como ganhamos uma nova perspectiva sobre o sistema e a rede do nosso sistema alvo no estágio de Exploração, estamos basicamente em um novo ambiente. Isso significa que primeiro precisamos nos familiarizar novamente com o que estamos trabalhando e quais opções estão disponíveis. Portanto, no `Post-Exploitation`estágio, passamos novamente pelos estágios `Information Gathering`e `Vulnerability Assessment`, que podemos considerar como partes do estágio atual. Isto porque a informação que tínhamos até agora foi recolhida a partir de uma perspectiva externa e não interna.

Do ponto de vista interno (local), temos muito mais possibilidades e alternativas para acessar determinadas informações que são relevantes para nós. Portanto, a etapa de coleta de informações recomeça a partir da perspectiva local. Pesquisamos e coletamos o máximo de informações que podemos. A diferença aqui é que também enumeramos a rede local e os serviços locais, como impressoras, servidores de banco de dados, serviços de virtualização, etc. Freqüentemente, encontraremos compartilhamentos destinados aos funcionários para troca e compartilhamento de dados e arquivos. A investigação destes serviços e componentes de rede é chamada `Pillaging`.

## Pilhagem

A pilhagem é a fase em que examinamos o papel do hospedeiro na rede corporativa. Analisamos as configurações de rede, incluindo, mas não limitado a:

|              |            |                 |
| ------------ | ---------- | --------------- |
| Interfaces   | Roteamento | DNS             |
| ARP          | Serviços   | VPN             |
| Sub-redes IP | Ações      | Tráfego de rede |

`Understanding the role of the system`estamos também nos dá uma excelente compreensão de como ele se comunica com outros dispositivos de rede e sua finalidade.

Por exemplo, suponhamos que descobrimos que a política de senha requer apenas oito caracteres, mas nenhum caractere especial. Nesse caso, podemos concluir que temos uma probabilidade relativamente alta de adivinhar as senhas de outros usuários neste e em outros sistemas.

Durante a fase de pilhagem, também caçaremos dados confidenciais, como senhas em compartilhamentos, máquinas locais, em scripts, arquivos de configuração, cofres de senhas, documentos (Excel, Word, arquivos .txt, etc.) e até e-mail.

## Persistência

Assim que tivermos uma visão geral do sistema, nosso próximo passo imediato é manter o acesso ao host explorado. Desta forma, caso a conexão seja interrompida, ainda poderemos acessá-la. Esta etapa é essencial e frequentemente usada como a primeira etapa antes dos estágios `Information Gathering`e `Pillaging`.

Devemos seguir sequências não padronizadas porque cada sistema é configurado individualmente por um administrador único que traz suas próprias preferências e conhecimentos.

Por exemplo, suponha que tenhamos usado um ataque de buffer overflow em um serviço que provavelmente irá travá-lo. Nesse caso, devemos estabelecer a persistência do sistema o mais rápido possível para evitar ter que atacar o serviço diversas vezes e potencialmente causar uma interrupção. Muitas vezes, se perdermos a conexão, não conseguiremos acessar o sistema da mesma forma.

## Avaliação de vulnerabilidade

Se conseguirmos manter o acesso e ter uma boa visão geral do sistema, podemos utilizar as informações sobre o sistema e seus serviços e quaisquer outros dados nele armazenados para repetir a `Vulnerability Assessment`etapa, mas desta vez de dentro do sistema.

Mais uma vez, é essencial distinguir entre explorações que podem prejudicar o sistema e ataques contra os serviços que não causam qualquer perturbação.

## Escalação de privilégios

Obter os privilégios mais altos possíveis no sistema ou domínio costuma ser crucial. Portanto, queremos obter os privilégios do `root`(nos `Linux-based`sistemas) ou do domínio `administrator`/ `local administrator`/ `SYSTEM`(nos `Windows-based`sistemas), porque isso muitas vezes nos permitirá mover-nos por toda a rede sem quaisquer restrições.

Também podemos obter credenciais armazenadas durante a fase de coleta de informações de outros usuários que sejam membros de um grupo com privilégios mais elevados.

## Exfiltração de dados

Durante a fase `Information Gathering`e `Pillaging`, muitas vezes poderemos encontrar, entre outras coisas, informações pessoais e dados de clientes consideráveis. Alguns clientes vão querer verificar se é possível exfiltrar esses tipos de dados. Isso significa que tentamos transferir essas informações do sistema de destino para o nosso. Sistemas de segurança como `Data Loss Prevention`( `DLP`) e `Endpoint Detection and Response`( `EDR`) ajudam a detectar e prevenir a exfiltração de dados.

Antes de extrair quaisquer dados reais, devemos verificar com o cliente e nosso gerente. Muitas vezes pode ser suficiente criar alguns dados falsos (como números de cartão de crédito ou números de segurança social falsos) e exfiltrá-los para o nosso sistema. Dessa forma, os mecanismos de proteção que procuram padrões nos dados que saem da rede serão testados, mas não seremos responsáveis ​​por quaisquer dados sensíveis ativos em nossa máquina de testes.

As empresas devem aderir aos regulamentos de segurança de dados, dependendo do tipo de dados envolvidos. Estes incluem, mas não estão limitados a:

|**Tipo de informação**|**Regulamento de Segurança**|
|---|---|
|Informações da conta do cartão de crédito|`Payment Card Industry`( `PCI`)|
|Informações Eletrônicas de Saúde do Paciente|`Health Insurance Portability and Accountability Act`( `HIPAA`)|
|Informações bancárias privadas dos consumidores|`Gramm-Leach-Bliley`( `GLBA`)|
|Informações Governamentais|`Federal Information Security Management Act of 2002`( `FISMA`)|

Algumas estruturas que as empresas podem seguir incluem:

| | |
|---|---|
|( `NIST`) - Instituto Nacional de Padrões e Tecnologia|( `CIS Controls`) - Centro de Controles de Segurança da Internet|
|( `ISO`) - Organização Internacional para Padronização|( `PCI-DSS`) - O padrão de segurança de dados da indústria de cartões de pagamento|
|( `GDPR`) - Regulamento Geral de Proteção de Dados|( `COBIT`) - Objetivos de Controle para Informações e Tecnologias Relacionadas|
|( `FedRAMP`) - Programa Federal de Gerenciamento de Riscos e Autorizações|( `ITAR`) - Regulamentação do Tráfico Internacional de Armas|
|( `AICPA`) - Instituto Americano de Contadores Públicos Certificados|( `NERC CIP Standards`) - Padrões de proteção de infraestrutura crítica NERC|

 Para nós, o tipo de dados não tem muita importância, mas os controles necessários em torno deles sim, e como afirmado anteriormente, podemos simular a exfiltração de dados da rede como uma prova de conceito de que isso é possível.

É um bom hábito fazer uma gravação de tela (juntamente com capturas de tela) como evidência adicional para essas etapas vitais. Se tivermos apenas acesso ao terminal, podemos exibir o nome do host, o endereço IP, o nome do usuário e o caminho correspondente para o arquivo do cliente e fazer uma captura de tela ou captura de tela. Isso nos ajuda a provar a origem dos dados e que podemos removê-los do ambiente com sucesso.










































