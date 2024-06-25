# Cyber - Exploração

Durante o estágio de exploração, procuramos maneiras de adaptar essas fraquezas ao nosso caso de uso para obter a função desejada (ou seja, uma posição segura, privilégios escalados, etc.). Se quisermos obter um shell reverso, precisamos modificar o PoC para executar o código, para que o sistema de destino se conecte de volta a nós por meio de (idealmente) uma conexão criptografada com um endereço IP que especificamos. Portanto, a preparação de uma exploração faz parte principalmente do `Exploitation`estágio.

![[0-PT-Process-EX.webp]]

Essas etapas não devem ser estritamente separadas umas das outras, pois estão intimamente ligadas. No entanto, ainda é importante distinguir em que fase nos encontramos e qual a sua finalidade. Porque mais tarde, com processos muito mais complexos e muito mais informações, é muito fácil perder o controle dos passos que foram dados, principalmente se o teste de penetração durar várias semanas e abranger um escopo enorme.

## Priorização de possíveis ataques

Depois de encontrarmos uma ou duas vulnerabilidades durante o `Vulnerability Assessment`estágio que podemos aplicar à nossa rede/sistema alvo, podemos priorizar esses ataques. Qual desses ataques priorizamos mais que os outros depende dos seguintes fatores:

- Probabilidade de sucesso
- Complexidade
- Probabilidade de dano

Primeiro, precisamos avaliar a `probability of successfully`execução de um ataque específico contra o alvo. [A pontuação CVSS](https://nvd.nist.gov/vuln-metrics/cvss) pode nos ajudar aqui, usando melhor a [calculadora NVD](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator) para calcular os ataques específicos e sua probabilidade de sucesso.

`Complexity`representa o esforço de explorar uma vulnerabilidade específica. Isso é usado para estimar quanto tempo, esforço e pesquisa são necessários para executar o ataque ao sistema com sucesso.

Estimar o `probability of damage`causado pela execução de uma exploração desempenha um papel crítico, pois devemos evitar qualquer dano aos sistemas alvo. Geralmente, não realizamos ataques DoS, a menos que nosso cliente solicite.

Além disso, podemos atribuir estes fatores a um sistema de pontos pessoais que permitirá calcular a avaliação com mais precisão com base nas nossas habilidades e conhecimentos:

| **Fator**                   | **Pontos** | **Inclusão remota de arquivos** | **Estouro de buffer** |
| --------------------------- | ---------- | ------------------------------- | --------------------- |
| 1. Probabilidade de sucesso | `10`       | 10                              | 8                     |
| 2. Complexidade – Fácil     | `5`        | 4                               | 0                     |
| 3. Complexidade – Média     | `3`        | 0                               | 3                     |
| 4. Complexidade – Difícil   | `1`        | 0                               | 0                     |
| 5. Probabilidade de dano    | `-5`       | 0                               | -5                    |
| **Resumo**                  | `max. 15`  | 14                              | 6                     |

Com base no exemplo acima, preferiríamos o `remote file inclusion`ataque. É fácil de preparar e executar e não deve causar nenhum dano se for abordado com cuidado.







