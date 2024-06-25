# Cyber - Pós engajamento

Não existem dois trabalhos iguais, pelo que estas atividades podem diferir ligeiramente, mas geralmente devem ser realizadas para encerrar totalmente um trabalho.

![[0-PT-Process 1.webp]]

## Limpar

Assim que o teste for concluído, devemos realizar qualquer limpeza necessária, como excluir ferramentas/scripts carregados nos sistemas de destino, reverter quaisquer (pequenas) alterações de configuração que possamos ter feito, etc. atividades de limpeza fáceis e eficientes. 

Se não conseguirmos acessar um sistema onde um artefato precisa ser excluído ou outra alteração revertida, devemos alertar o cliente e listar esses problemas nos apêndices do relatório.

Mesmo que possamos remover quaisquer arquivos carregados e reverter alterações (como adicionar uma conta de administrador local), devemos documentar essas alterações em nossos apêndices de relatório, caso o cliente receba alertas de que precisa acompanhar e confirmar que a atividade em questão fazia parte de nossos testes sancionados.

## Documentação de relatórios


Antes de concluir a avaliação e desconectar-se da rede interna do cliente ou enviar e-mails de notificação de “parada” para sinalizar o fim do teste devemos nos certificar de ter documentação adequada para todas as descobertas que planejamos incluir em nosso relatório

Já devemos ter uma lista detalhada das descobertas que incluiremos no relatório e todos os detalhes necessários para adaptar as descobertas ao ambiente do cliente. Nosso relatório final (que é abordado detalhadamente no módulo [Documentação e Relatórios](https://academy.hackthebox.com/module/details/162) ) deve consistir no seguinte:

- Uma cadeia de ataque (no caso de comprometimento interno total ou acesso externo ao interno) detalhando as etapas tomadas para alcançar o comprometimento
- Um resumo executivo forte que um público não técnico possa entender
- Descobertas detalhadas específicas do ambiente do cliente que incluem uma classificação de risco, localização de impacto, recomendações de remediação e referências externas de alta qualidade relacionadas ao problema
- Etapas adequadas para reproduzir cada descoberta para que a equipe responsável pela correção possa entender e testar o problema enquanto implementa as correções
- Recomendações de curto, médio e longo prazo específicas para o meio ambiente
- Apêndices que incluem informações como o escopo do alvo, dados OSINT (se relevante para o trabalho), análise de quebra de senha (se relevante), portas/serviços descobertos, hosts comprometidos, contas comprometidas, arquivos transferidos para sistemas de propriedade do cliente, qualquer criação de conta /modificações do sistema, uma análise de segurança do Active Directory (se relevante), dados de verificação relevantes/documentação complementar e quaisquer outras informações necessárias para explicar melhor uma descoberta ou recomendação específica

Nesta fase, criaremos um relatório preliminar que será a primeira entrega que nosso cliente receberá. A partir daqui, poderão comentar o relatório e solicitar quaisquer esclarecimentos/modificações necessárias.

## Reunião de revisão de relatórios

Depois que o relatório preliminar for entregue e o cliente tiver tido a oportunidade de distribuí-lo internamente e revisá-lo em profundidade, é habitual realizar uma reunião de revisão do relatório para analisar os resultados da avaliação.

A reunião de revisão do relatório normalmente inclui as mesmas pessoas do cliente e da empresa que realizam a avaliação.

Freqüentemente, o cliente virá com uma lista de perguntas sobre descobertas específicas e não desejará cobrir todas as descobertas detalhadamente (como as de baixo risco)

## Aceitação de entrega

O Escopo do Trabalho deve definir claramente a aceitação de quaisquer entregas do projeto

 Nas avaliações de testes de penetração, geralmente, entregamos um relatório pontuado `DRAFT`e damos ao cliente a oportunidade de revisar e comentar.

Depois que o cliente tiver enviado feedback durante uma reunião de revisão do relatório, podemos emitir uma nova versão do relatório marcada como `FINAL`.

Algumas empresas de auditoria às quais os clientes podem estar em dívida não aceitarão um relatório de teste de penetração com uma `DRAFT`designação. Outras empresas não se importarão, mas é melhor manter uma abordagem uniforme para todos os clientes.

## Teste Pós-Remediação

Nesta fase, analisaremos qualquer documentação fornecida pelo cliente que mostre evidências de remediação ou apenas uma lista de descobertas corrigidas.

Precisaremos acessar novamente o ambiente de destino e testar cada problema para garantir que ele foi corrigido adequadamente.

Emitiremos um relatório pós-remediação que mostra claramente o estado do ambiente antes e depois dos testes pós-remediação. Por exemplo, podemos incluir uma tabela como:

| #   | Encontrando a Gravidade | Encontrando Título                  | Status        |
| --- | ----------------------- | ----------------------------------- | ------------- |
| 1   | Alto                    | Injeção SQL                         | Corrigido     |
| 2   | Alto                    | Autenticação quebrada               | Corrigido     |
| 3   | Alto                    | Upload irrestrito de arquivos       | Corrigido     |
| 4   | Alto                    | Filtragem inadequada de Web e saída | Não remediado |
| 5   | Médio                   | Assinatura SMB não habilitada       | Não remediado |
| 6   | Baixo                   | Listagem de diretório ativada       | Não remediado |

Para cada descoberta (quando possível), desejaremos mostrar evidências de que o problema não está mais presente no ambiente por meio de resultados de varredura ou provas de que as técnicas de exploração originais falharam.

## Papel do pentester na remediação

Como um teste de penetração é essencialmente uma auditoria, devemos permanecer imparciais com terceiros e não realizar correções em nossas descobertas

 Devemos manter um certo grau de independência e podemos servir como consultores de confiança, dando conselhos gerais de remediação sobre como um problema específico pode ser resolvido ou estar disponíveis para explicar melhor/demonstrar uma descoberta para que a equipe designada para remediá-la tenha uma melhor compreensão

## Retenção de dados

Após a conclusão de um teste de penetração, teremos uma quantidade considerável de dados específicos do cliente

Os requisitos de retenção e destruição de dados podem diferir de país para país e de empresa para empresa, e os procedimentos relativos a cada um devem ser claramente descritos na linguagem contratual do Escopo de Trabalho e das Regras de Compromisso.

Devemos reter as evidências por algum tempo após o teste de penetração, caso surjam dúvidas sobre descobertas específicas ou para ajudar no novo teste de descobertas "fechadas" após o cliente ter realizado atividades de correção

Quaisquer dados retidos após a avaliação devem ser armazenados em um local seguro de propriedade e controlado pela empresa e criptografados em repouso.

Todos os dados devem ser apagados dos sistemas testadores na conclusão de uma avaliação.

Uma nova máquina virtual específica para o cliente em questão deve ser criada para qualquer teste pós-remediação ou investigação de descobertas relacionadas às consultas do cliente.

## Fechar

Depois de entregar o relatório final, auxiliar o cliente com dúvidas sobre a remediação e realizar os testes pós-remediação/emitir um novo relatório, podemos finalmente encerrar o projeto.

Nesta fase, devemos garantir que quaisquer sistemas usados ​​para conectar-se aos sistemas do cliente ou processar dados foram apagados ou destruídos e que quaisquer artefatos remanescentes do trabalho sejam armazenados de forma segura (criptografados) de acordo com a política da nossa empresa e de acordo com as obrigações contratuais para com o nosso cliente.

As etapas finais seriam o faturamento do cliente e a cobrança pelos serviços prestados. Finalmente, é sempre bom fazer o acompanhamento com uma pesquisa de satisfação do cliente pós-avaliação para que a equipe e a gestão, em particular, possam ver o que deu certo durante o trabalho e o que poderia ser melhorado do ponto de vista do processo da empresa e do consultor individual designado.







