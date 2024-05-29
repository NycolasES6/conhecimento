#cyber 
# OWASP top 10

![[Pasted image 20240528102629.png]]
Bem-vindo à última edição do OWASP Top 10! O OWASP Top 10 2021 é totalmente novo, com um novo design gráfico e um infográfico disponível que você pode imprimir ou obter em nossa página inicial.

![[2017to2021.svg]]

## A01:2021-Quebra de Controle de Acesso

94% das aplicação foram testados para alguma forma de controle de acesso quebrado. O 34 CWEs mapeados para Quebra de Controle de Acesso tiveram mais ocorrências em aplicações do que qualquer outra categoria.

## A02:2021-Falhas Criptográficas

anteriormente conhecido como _Exposição de Dados Sensíveis_, que era um sintoma amplo em vez de uma causa raiz. O foco renovado aqui está nas falhas relacionadas à criptografia, que muitas vezes leva à exposição de dados confidenciais ou sistema comprometido.

## A03:2021-Injeção

94% das aplicações foram testadas para alguma forma de injeção com uma taxa de incidência máxima de 19%, uma taxa de incidência média de 3,37% e os 33 CWEs mapeados nesta categoria têm o segundo maior número de ocorrências em aplicações, com 274k ocorrências. Cross-site Scripting (Scripts Inter-site) agora faz parte desta categoria nesta edição.

## A04:2021-Design Inseguro

Um design inseguro não pode ser corrigido por uma implementação perfeita, pois, por definição, os controles de segurança necessários nunca foram criados para a defesa contra ataques específicos.

## A05:2021-Configuração Insegura

90% dos aplicativos foram testados para alguma conforma de configuração insegura, com uma taxa de incidência média de 4,5% e mais de 208 mil ocorrências de CWEs mapeados para esta categoria de risco. Com mais mudanças em software altamente configurável, não é surpreendente ver essa categoria subir.

## A06:2021-Componente Desatualizado e Vulnerável

Esta categoria subiu da 9ª posição em 2017 e é um problema conhecido que temos dificuldade em testar e avaliar o risco. É a única categoria a não ter nenhuma Vulnerabilidade e Exposições Comuns (CVEs) mapeada para os CWEs incluídos, portanto, uma exploração padrão e pesos de impacto de 5,0 são considerados em suas pontuações.

## A07:2021-Falha de Identificação e Autenticação

Era conhecida anteriormente como Falha de Autenticação e caiu da terceira posição para essa, e foram incluídas as CWEs que mais se relacionam com as falhas na identificação. Essa categoria ainda é parte integrante do Top 10, mas a maior disponibilidade de estruturas (frameworks) padronizadas parece estar ajudando a reduzir.

## A08:2021-Falha na Integridade de Dados e Software

Um dos maiores pesos dos dados nessa categoria são CVE/CVSS mapeados para os 10 CWEs nesta categoria. A categoria **A8:2017-Desserialização Insegura** agora faz parte dessa categoria.

## A09:2021-Monitoramento de Falhas e Registros de Segurança

 Anteriormente chamado de **A10:2017-Registro e Monitoramentos Insuficientes** e foi adicionado pela pesquisa da comunidade de Top 10, ficando em terceiro lugar, passando da 10° posição anterior. Essa categoria foi expandida para incluir um maior número de falhas, sendo um desafio para testar e não está bem representada nos dados de CVE/CVSS. No entanto falhas nessa categoria podem impactar diretamente a visibilidade, o alerta de incidente e a perícia.

## A10:2021-Falsificação de Solicitação do Lado do Servidor

Os dados mostram uma taxa de incidência relativamente baixa com cobertura de teste acima da média, junto com classificações acima da média para potencial de exploração e impacto. Esta categoria representa o cenário em que os membros da comunidade de segurança estão nos dizendo que isso é importante, embora não esteja ilustrado nos dados neste momento.

---

[OWASP top 10](https://owasp.org/Top10/pt_BR/)





































