# Cyber - Information Gathering

Assim que a fase de pré-compromisso for concluída e todas as partes tiverem assinado todos os termos e condições contratuais, a fase `information gathering` começa.

 Esta é a fase em que reunimos toda a informação disponível sobre a empresa, os seus colaboradores e infraestruturas, e como estão organizados. A coleta de informações é a fase mais frequente e vital em todo o processo de teste de penetração, à qual retornaremos continuamente.

![[0-PT-Process-IG.webp]]

Podemos obter as informações necessárias e relevantes para nós de muitas maneiras diferentes. No entanto, podemos dividi-los nas seguintes categorias:

- Inteligência de código aberto
- Enumeração de infraestrutura
- Enumeração de serviço
- Enumeração de hosts

Todas as quatro categorias devem e devem ser realizadas por nós para cada teste de penetração. Isso ocorre porque a informação é o principal componente que nos leva a testes de penetração bem-sucedidos e à identificação de vulnerabilidades de segurança. Podemos obter essas informações em qualquer lugar, seja nas redes sociais, anúncios de emprego, hosts e servidores individuais ou até mesmo nos funcionários.

## Inteligência de código aberto

Vamos supor que nosso cliente queira que vejamos quais informações podemos encontrar sobre sua empresa na internet. Para tanto, utilizamos o que é conhecido como `Open Source Intelligence`( `OSINT`). OSINT é um processo para encontrar informações publicamente disponíveis sobre uma empresa ou indivíduos-alvo que permite a identificação de eventos (ou seja, reuniões públicas e privadas), dependências externas e internas e conexões.

## Enumeração e infraestrutura

Durante a enumeração da infraestrutura, procuramos ter uma visão geral da posição da empresa na internet e na intranet. Para isso, utilizamos OSINT e os primeiros scans ativos. Usamos serviços como DNS para criar um mapa dos servidores e hosts do cliente e desenvolver uma compreensão de como eles `infrastructure`estão estruturados. Isso inclui servidores de nomes, servidores de e-mail, servidores web, instâncias de nuvem e muito mais. Fazemos uma lista precisa de hosts e seus endereços IP e os comparamos com nosso escopo para ver se estão incluídos e listados.

Nesta fase, procuramos também determinar as medidas de segurança da empresa. Quanto mais precisas forem essas informações, mais fácil será disfarçar nossos ataques ( `Evasive Testing`). Mas identificar firewalls, como firewalls de aplicativos web, também nos dá uma excelente compreensão de quais técnicas podem acionar um alarme para nossos clientes e quais métodos podem ser usados ​​para evitar esse alarme.

Aqui também não importa “onde” estamos posicionados, se estamos tentando obter uma visão geral da infraestrutura de fora ( `external`) ou examinando a infraestrutura de dentro ( `internal`) da rede. A enumeração de dentro da rede nos dá uma boa visão geral dos hosts e servidores que podemos usar como alvos para um ataque  `Password Spraying`.

## Enumeração de serviço

Na enumeração de serviços, identificamos serviços que nos permitem interagir com o host ou servidor pela rede (ou localmente, de uma perspectiva interna). Portanto, é fundamental conhecer o serviço, qual a `versão`, qual `informação` nos é oferecida e por qual razão pode ser usada.

Muitos serviços possuem um histórico de versões que nos permite identificar se a versão instalada no host ou servidor está realmente atualizada ou não. Isso também nos ajudará a encontrar vulnerabilidades de segurança que permanecem em versões mais antigas na maioria dos casos.

## Enumeração de hosts

ssim que tivermos uma lista detalhada da infraestrutura do cliente, examinaremos cada host listado no documento de definição de escopo. Tentamos identificar qual `sistema operacional` está rodando no host ou servidor, qual `serviços` ele utiliza, qual a `versão` dos serviços e muito mais. Novamente, além das varreduras ativas, também podemos usar vários métodos OSINT para nos informar como esse host ou servidor pode ser configurado.

## Pilhagem

Outro passo essencial é `Pillaging`. Depois de chegar ao estágio  `Post-Exploitation`, a pilhagem é realizada para coletar informações confidenciais localmente no host já explorado, como nomes de funcionários, dados de clientes e muito mais. No entanto, essa coleta de informações só ocorre após a exploração do host alvo e a obtenção de acesso a ele.

As informações que podemos obter sobre os hosts explorados podem ser divididas em muitas categorias diferentes e variam muito. Isso depende da finalidade do host e do seu posicionamento na rede corporativa. Os administradores que tomam medidas de segurança para esses hosts também desempenham um papel significativo. No entanto, essas informações podem mostrar o `impacto` da existência de um ataque potencial ao nosso cliente e ser usadas para etapas adicionais `escalação de privilégios` ou no `movimento lateral` da rede.

A pilhagem por si só não é uma fase ou uma subcategoria como muitos descrevem frequentemente, mas uma parte integrante das fases de recolha de informações e escalonamento de privilégios que são inevitavelmente realizadas localmente nos sistemas-alvo.

















