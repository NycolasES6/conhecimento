# Cyber - Avaliação de vulnerabilidades

Durante a `vulnerability assessment`fase, examinamos e analisamos as informações coletadas durante a fase de coleta de informações. A fase de avaliação da vulnerabilidade é um processo analítico baseado nas descobertas.

![[0-PT-Process-VA.webp]]

An analysis is a detailed examination of an event or process, describing its origin and impact, that with the help of certain precautions and actions, can be triggered to support or prevent future occurrences.

Qualquer análise pode ser muito complicada, uma vez que muitos factores diferentes e as suas interdependências desempenham um papel significativo. Além de trabalharmos com os três tempos distintos (passado, presente e futuro) em cada análise, a origem e o destino desempenham um papel significativo. Existem quatro tipos diferentes de análise:

| **Tipo de análise** | **Descrição**                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Descriptive`       | A análise descritiva é essencial em qualquer análise de dados. Por um lado, descreve um conjunto de dados baseado em características individuais. Ajuda a detectar possíveis erros na coleta de dados ou valores discrepantes no conjunto de dados.                                                                                                             |
| `Diagnostic`        | A análise diagnóstica esclarece as causas, efeitos e interações das condições. Isso fornece insights que são obtidos por meio de correlações e interpretação. Devemos adoptar uma visão retrospectiva, semelhante à análise descritiva, com a subtil diferença de que tentamos encontrar razões para acontecimentos e desenvolvimentos.                         |
| `Predictive`        | Ao avaliar dados históricos e atuais, a análise preditiva cria um modelo preditivo para probabilidades futuras. Com base nos resultados de análises descritivas e diagnósticas, este método de análise de dados permite identificar tendências, detectar precocemente desvios dos valores esperados e prever ocorrências futuras com a maior precisão possível. |
| `Prescriptive`      | A análise prescritiva visa restringir quais ações tomar para eliminar ou prevenir um problema futuro ou desencadear uma atividade ou processo específico.                                                                                                                                                                                                       |

Suponha que encontramos uma porta TCP 2121 aberta em um host durante a fase de coleta de informações.

Além do fato desta porta estar aberta, o Nmap não nos mostrou mais nada.  Porém, é essencial perguntar `questões precisas` e lembrar o que nós `sabemos` e  o que `não sabemos`. Neste ponto, devemos primeiro nos perguntar o que `vemos` e o que realmente somos `temos`, porque o que vemos não é o mesmo que temos:

- um `TCP`porto `2121`. - `TCP` já significa que este serviço é `connection-oriented`.
    
- Isto é uma porta `padrão` ? - `Não`, porque estão entre , também conhecidas como [portas](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)`0-1023` bem conhecidas ou do sistema

## Pesquisa de análise de vulnerabilidaddes

`Information Gathering`e `Vulnerability Research`pode ser considerado parte da análise descritiva. É aqui que identificamos a rede individual ou os componentes do sistema que estamos investigando. Em `Vulnerability Research`, procuramos vulnerabilidades conhecidas, explorações e falhas de segurança que já foram descobertas e relatadas. Portanto, se identificamos uma versão de um serviço ou aplicativo por meio da coleta de informações e encontramos [Vulnerabilidades e Exposições Comuns (CVE)](https://www.cve.org/ResourcesSupport/FAQs) , é muito provável que essa vulnerabilidade ainda esteja presente.

|                                                                            |                                                         |                                     |
| -------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------- |
| [Detalhes do CVE](https://www.cvedetails.com/)                             | [Explorar banco de dados](https://www.exploit-db.com/)  | [Vulneráveis](https://vulners.com/) |
| [Segurança contra tempestade de pacotes](https://packetstormsecurity.com/) | [NIST](https://nvd.nist.gov/vuln/search?execution=e2s1) |                                     |

É aqui que `Diagnostic Analysis`e `Predictive Analysis`é usado. Depois de encontrarmos uma vulnerabilidade publicada como esta, podemos diagnosticá-la para determinar o que está causando ou causou a vulnerabilidade. Aqui, devemos entender a funcionalidade do código `Proof-Of-Concept`( `POC`) ou da aplicação ou serviço em si da melhor forma possível, pois muitas configurações manuais por parte dos administradores exigirão alguma customização para o POC. Cada POC é adaptado a um caso específico que também precisaremos adaptar ao nosso na maioria dos casos.

## Avaliação de possíveis vetores de ataque

`Vulnerability Assessment`também inclui o teste real, que faz parte do `Predictive Analysis`. Ao fazê-lo, analisamos a informação histórica e combinamo-la com a informação atual que conseguimos descobrir. Quer tenhamos recebido requisitos específicos de nível de evasão de nosso cliente, testamos os serviços e aplicações encontrados `locally`ou `on the target system`. Se tivermos que testar secretamente e evitar alertas, devemos espelhar o sistema alvo localmente com a maior precisão possível. Isso significa que usamos as informações obtidas durante a fase de coleta de informações para replicar o sistema de destino e, em seguida, procurar vulnerabilidades no sistema implantado localmente.

## O retorno

Suponha que não consigamos detectar ou identificar vulnerabilidades potenciais em nossa análise. Nesse caso, voltaremos ao `Information Gathering`palco e buscaremos informações mais aprofundadas do que as que coletamos até agora.

Num CTF, o objetivo é chegar à máquina alvo e `capture the flags`com os privilégios mais elevados o mais rápido possível, em vez de expor todas as potenciais fraquezas do sistema.

|**`A (real) Penetration Test is not a CTF.`**|
|---|
Aqui o `quality` e `intensity` do nosso teste de penetração e sua análise têm a mais alta prioridade porque nada será pior se nosso cliente for hackeado com sucesso por meio de um vetor relativamente simples que deveríamos ter descoberto durante nosso teste de penetração.



























