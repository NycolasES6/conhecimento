# Cyber - Metodologia de enumeração

Processos complexos devem ter uma metodologia padronizada que nos ajude a nos orientar e evitar omitir algum aspecto por engano.

Sabemos que o teste de penetração e, portanto, a enumeração, é um processo dinâmico.

Consequentemente, desenvolvemos uma metodologia de enumeração estática para testes de penetração externos e internos que inclui dinâmica livre e permite uma ampla gama de mudanças e adaptações ao ambiente determinado. Esta metodologia está aninhada em 6 camadas e representa, metaforicamente falando, limites que tentamos ultrapassar com o processo de enumeração. Todo o processo de enumeração é dividido em três níveis diferentes:


| `Infrastructure-based enumeration` | `Host-based enumeration` | `OS-based enumeration` |
| ---------------------------------- | ------------------------ | ---------------------- |

![[Pasted image 20240625085655.png]]

Considere essas linhas como uma espécie de obstáculo, como uma parede, por exemplo. O que fazemos aqui é olhar em volta para descobrir onde fica a entrada, ou a abertura pela qual podemos passar, ou escalar para nos aproximarmos do nosso objetivo. Teoricamente também é possível atravessar a parede de cabeça, mas muitas vezes acontece que o local que abrimos a brecha com muito esforço e tempo com força não nos traz muito porque não há entrada neste ponto de a parede para passar para a próxima parede.

| **Camada**               | **Descrição**                                                                                              | **Categorias de informação**                                                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1. Internet Presence`   | Identificação da presença na Internet e infraestrutura acessível externamente.                             | Domínios, subdomínios, vHosts, ASN, Netblocks, endereços IP, instâncias de nuvem, medidas de segurança                                                        |
| `2. Gateway`             | Identifique as possíveis medidas de segurança para proteger a infraestrutura externa e interna da empresa. | Firewalls, DMZ, IPS/IDS, EDR, Proxies, NAC, Segmentação de Rede, VPN, Cloudflare                                                                              |
| `3. Accessible Services` | Identifique interfaces e serviços acessíveis hospedados externa ou internamente.                           | Tipo de serviço, funcionalidade, configuração, porta, versão, interface                                                                                       |
| `4. Processes`           | Identifique os processos internos, fontes e destinos associados aos serviços.                              | PID, Dados Processados, Tarefas, Origem, Destino                                                                                                              |
| `5. Privileges`          | Identificação das permissões e privilégios internos aos serviços acessíveis.                               | Grupos, usuários, permissões, restrições, ambiente                                                                                                            |
| `6. OS Setup`            | Identificação dos componentes internos e configuração dos sistemas.                                        | Tipo de sistema operacional, nível de patch, configuração de rede, ambiente de sistema operacional, arquivos de configuração, arquivos privados confidenciais |

Podemos finalmente imaginar todo o teste de penetração na forma de um labirinto onde temos que identificar as lacunas e encontrar a forma de entrar o mais rápida e eficazmente possível. Este tipo de labirinto pode ser parecido com isto:

![[Pasted image 20240625090204.png]]
Os quadrados representam as lacunas/vulnerabilidades.

## Camada N. 1: Presença na internet

A primeira camada que temos que passar é a camada “Presença na Internet”, onde nos concentramos em encontrar os alvos que podemos investigar.

Nesta camada utilizamos diversas técnicas para encontrar domínios, subdomínios, netblocks e muitos outros componentes e informações que apresentam a presença da empresa e sua infraestrutura na Internet.

`The goal of this layer is to identify all possible target systems and interfaces that can be tested.`

## Camada N. 2: Gateway

Aqui tentamos entender a interface do alvo alcançável, como ele está protegido e onde está localizado na rede.

`The goal is to understand what we are dealing with and what we have to watch out for.`

## Camada N.3: Serviços Acessíveis

No caso dos serviços acessíveis, examinamos cada destino em busca de todos os serviços que oferece.
Para trabalhar eficazmente com eles, precisamos saber como funcionam. Caso contrário, precisamos aprender a entendê-los.

`This layer aims to understand the reason and functionality of the target system and gain the necessary knowledge to communicate with it and exploit it for our purposes effectively.`

## Camada N.4: Processos

Cada vez que um comando ou função é executado, são processados ​​dados, sejam eles inseridos pelo usuário ou gerados pelo sistema.

Isto inicia um processo que deve executar tarefas específicas, e tais tarefas têm pelo menos uma origem e um destino.

`The goal here is to understand these factors and identify the dependencies between them.`

## Camada N.5: Privilégios

Cada serviço é executado por meio de um usuário específico em um grupo específico com permissões e privilégios definidos pelo administrador ou pelo sistema.

Esses privilégios geralmente nos fornecem funções que os administradores ignoram.

`It is crucial to identify these and understand what is and is not possible with these privileges.`

## Camada N. 6: Configuração

Aqui coletamos informações sobre o sistema operacional real e sua configuração usando acesso interno. Isto dá-nos uma boa visão geral da segurança interna dos sistemas e reflete as competências e capacidades das equipas administrativas da empresa.

`The goal here is to see how the administrators manage the systems and what sensitive internal information we can glean from them.`

















































