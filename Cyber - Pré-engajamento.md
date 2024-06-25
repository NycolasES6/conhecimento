#incomplete #htb
# Cyber - Pré-engajamento

O pré-engajamento é a fase de preparação para o teste de penetração propriamente dito. Durante esta fase, muitas perguntas são feitas e alguns acordos contratuais são feitos. O cliente nos informa o que deseja que seja testado e explicamos detalhadamente como tornar o teste o mais eficiente possível.

![[0-PT-Process-PRE.webp]]

Todo o processo de pré-engajamento consiste em três componentes essenciais:

1. Questionário de escopo
    
2. Reunião pré-engajamento
    
3. Reunião de lançamento

Antes que qualquer um deles possa ser discutido em detalhes, um `Non-Disclosure Agreement`( `NDA`) deve ser assinado por todas as partes. Existem vários tipos de NDAs:

| **Tipo**           | **Descrição**                                                                                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Unilateral NDA`   | Este tipo de NDA obriga apenas uma parte a manter a confidencialidade e permite que a outra parte compartilhe as informações recebidas com terceiros.                                                                            |
| `Bilateral NDA`    | Neste tipo, ambas as partes são obrigadas a manter confidenciais as informações resultantes e adquiridas. Este é o tipo mais comum de NDA que protege o trabalho dos testadores de penetração.                                   |
| `Multilateral NDA` | A NDA multilateral é um compromisso de confidencialidade por parte de mais de duas partes. Se realizarmos um teste de penetração para uma rede cooperativa, todos os responsáveis ​​e envolvidos deverão assinar este documento. |

Abaixo está um exemplo de lista (não exaustiva) de membros da empresa que podem estar autorizados a nos contratar para testes de penetração. Isso pode variar de empresa para empresa, com organizações maiores não envolvendo diretamente a equipe de nível C e a responsabilidade recaindo sobre a gerência sênior de TI, Auditoria ou Segurança de TI ou similares.

|                               |                        |                                             |
| ----------------------------- | ---------------------- | ------------------------------------------- |
| Chief Executive Officer (CEO) | Diretor Técnico (CTO)  | Diretor de Segurança da Informação (CISO)   |
| Diretor de Segurança (CSO)    | Diretor de Risco (CRO) | Diretor de Informações (CIO)                |
| VP de Auditoria Interna       | Gerente de auditoria   | VP ou Diretor de TI/Segurança da Informação |

Esta fase também requer a preparação de vários documentos antes da realização de um teste de penetração que devem ser assinados pelo nosso cliente e por nós para que a declaração de consentimento também possa ser apresentada por escrito, se necessário. Caso contrário, o teste de penetração poderá violar a [Lei de Uso Indevido de Computadores](https://www.legislation.gov.uk/ukpga/1990/18/contents) . Esses documentos incluem, mas não estão limitados a:

| **Documento**                                                        | **Tempo para a Criação**                             |
| -------------------------------------------------------------------- | ---------------------------------------------------- |
| `1. Non-Disclosure Agreement`( `NDA`)                                | ``Depois`` do contato inicial                        |
| `2. Scoping Questionnaire`                                           | ``Antes`` da reunião de pré-engajamento              |
| `3. Scoping Document`                                                | ``Durante`` a reunião de pré-engajamento             |
| `4. Penetration Testing Proposal`( `Contract/Scope of Work`( `SoW`)) | ``Durante`` a reunião de pré-engajamento             |
| `5. Rules of Engagement`( `RoE`)                                     | ``Antes`` da reunião de lançamento                   |
| `6. Contractors Agreement`(Avaliações Físicas)                       | ``Antes`` da reunião de lançamento                   |
| `7. Reports`                                                         | `Durante` e `depois` o teste de penetração realizado |

>**Nota importante:**
>Esses documentos deverão ser revisados ​​e adaptados por um advogado após sua preparação.

## Questionário de escopo

Após o contato inicial com o cliente, normalmente enviamos um email `Scoping Questionnaire`para entender melhor os serviços que procura. Este questionário de definição de escopo deve explicar claramente nossos serviços e normalmente pode solicitar que escolham um ou mais da lista a seguir:

|                                        |                                                |
| -------------------------------------- | ---------------------------------------------- |
| ☐ Avaliação de vulnerabilidade interna | ☐ Avaliação de vulnerabilidade externa         |
| ☐ Teste de penetração interna          | ☐ Teste de penetração externa                  |
| ☐ Avaliação de segurança sem fio       | ☐ Avaliação de segurança de aplicativos        |
| ☐ Avaliação de segurança física        | ☐ Avaliação de Engenharia Social               |
| ☐ Avaliação da Equipe Vermelha         | ☐ Avaliação de segurança de aplicativos da Web |

Eles precisam de uma avaliação de aplicativo web ou aplicativo móvel? Revisão de código segura? O Teste de Penetração Interna deve ser caixa preta e semi-evasivo? Eles querem apenas uma avaliação de phishing como parte da Avaliação de Engenharia Social ou também ligações de vishing?

Aqui explicamos a profundidade e amplitude dos nossos serviços, garantir que entendemos as necessidades e expectativas dos nossos clientes e garantir que podemos fornecer adequadamente a avaliação que eles exigem.

Além do tipo de avaliação, nome do cliente, endereço e informações principais de contato do pessoal, algumas outras informações críticas incluem:

|   |   |
|---|---|
|Quantos hosts ao vivo esperados?||
|Quantos intervalos de IPs/CIDR no escopo?||
|Quantos domínios/subdomínios estão no escopo?||
|Quantos SSIDs sem fio no escopo?||
|Quantos aplicativos web/móveis? Se o teste for autenticado, quantas funções (usuário padrão, administrador, etc.)?||
|Para uma avaliação de phishing, quantos usuários serão alvo? O cliente fornecerá uma lista ou seremos obrigados a reuni-la via OSINT?||
|Caso o cliente esteja solicitando Avaliação Física, em quantos locais? Se vários sites estiverem no escopo, eles estão geograficamente dispersos?||
|Qual é o objetivo da Avaliação da Equipe Vermelha? Alguma atividade (como phishing ou ataques à segurança física) está fora do escopo?||
|É desejada uma avaliação de segurança separada do Active Directory?||
|Os testes de rede serão conduzidos por um usuário anônimo na rede ou por um usuário de domínio padrão?||
|Precisamos ignorar o Controle de Acesso à Rede (NAC)?|

Finalmente, queremos perguntar sobre divulgação de informações e evasão (se aplicável ao tipo de avaliação):

- O teste de penetração é caixa preta (nenhuma informação fornecida), caixa cinza (somente endereço IP/intervalos CIDR/URLs fornecidos), caixa branca (informações detalhadas fornecidas)

- Eles gostariam que testássemos de um modo não evasivo, híbrido-evasivo (comecemos silencioso e gradualmente tornemos "mais alto" para avaliar em que nível o pessoal de segurança do cliente detecta nossas atividades) ou totalmente evasivo.

















































